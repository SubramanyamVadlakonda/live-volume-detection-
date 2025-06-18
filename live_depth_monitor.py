import cv2
import torch
import numpy as np
import time

# Load MiDaS model (small version)
midas = torch.hub.load("intel-isl/MiDaS", "MiDaS_small")
midas.eval()
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
midas.to(device)

# Load transforms
midas_transforms = torch.hub.load("intel-isl/MiDaS", "transforms")
transform = midas_transforms.small_transform

# Replace with IP shown by IP Webcam app
VIDEO_STREAM_URL = "http://192.168.31.3:8080/video"  # Change this

# Function to estimate depth
def estimate_depth(frame):
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    input_batch = transform(img).to(device)  # already batched
    with torch.no_grad():
        prediction = midas(input_batch)
        prediction = torch.nn.functional.interpolate(
            prediction.unsqueeze(1),
            size=img.shape[:2],
            mode="bicubic",
            align_corners=False
        ).squeeze()

    depth_map = prediction.cpu().numpy()
    depth_map = cv2.normalize(depth_map, None, 0, 255, cv2.NORM_MINMAX)
    depth_map = depth_map.astype(np.uint8)
    return depth_map


# Compare reference and new depth map
def compare_depths(ref, new, threshold=15):
    diff = cv2.absdiff(ref, new)
    mean_diff = np.mean(diff)
    print(f"\n📏 Mean depth difference: {mean_diff:.2f}")
    if mean_diff > threshold:
        print("🚨 Alert: Container is NOT full!")
    else:
        print("✅ Status: Container appears full.")

# Initialize video capture
cap = cv2.VideoCapture(VIDEO_STREAM_URL)
if not cap.isOpened():
    print("❌ Could not open video stream.")
    exit()

print("📷 Press 'c' to capture (1st = full, 2nd = check)")
print("❌ Press 'q' to quit")

frame_count = 0
full_depth = None

while True:
    for _ in range(3):  # Try multiple reads
        ret, frame = cap.read()
        if ret and frame is not None and frame.size > 0:
            break
        time.sleep(0.5)
    else:
        print("❌ Failed to read a valid frame.")
        break

    cv2.imshow("Live Feed", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('c'):
        frame_count += 1
        print(f"\n📸 Capturing frame {frame_count}...")
        depth = estimate_depth(frame)

        if frame_count == 1:
            full_depth = depth
            print("📌 Full box reference depth captured.")
        elif frame_count == 2:
            compare_depths(full_depth, depth)

    elif key == ord('q'):
        print("👋 Exiting...")
        break

cap.release()
cv2.destroyAllWindows()
