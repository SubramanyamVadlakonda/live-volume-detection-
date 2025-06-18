# Depth Volume Monitor Using MiDaS and IP Webcam

This project uses the MiDaS model to estimate depth from a live video stream (e.g., an IP Webcam) and compares the fill level of a container by analyzing depth maps.

---

## Features

- Capture a reference depth map of a full container.
- Capture a check depth map to compare current fill level.
- Alert if container is not full based on depth difference.
- Uses lightweight MiDaS_small model for faster performance.

---

## Requirements

- Python 3.7 or higher
- PyTorch
- OpenCV
- torchvision
- numpy

---

## Installation

pip install torch torchvision opencv-python numpy


1. Create and activate a virtual environment (optional but recommended):

```bash
python -m venv .venv
# On Windows
.\.venv\Scripts\activate
# On Linux/macOS
source .venv/bin/activate


How to Run:

Start your IP Webcam app on your phone or use another IP camera and get the video stream URL.
Example for DroidCam:

http://<your-phone-ip>:4747/video

Edit the VIDEO_STREAM_URL variable in the Python script to point to your video stream URL.
Run the script

Controls:

Press c to capture the full container depth (reference).
Modify the container fill (e.g., remove some rice).
Press c again to capture and compare.
Press q to quit.

Notes:

Make sure your phone and computer are on the same Wi-Fi network.
MiDaS_small is used for faster inference on low-RAM devices.
The depth comparison threshold can be adjusted in the script.

Troubleshooting:

If the video stream does not open, verify the IP address and port.
On Windows, if OpenCV fails to open the stream, try updating OpenCV or test with a USB webcam.
Ensure PyTorch is installed with the correct version matching your CUDA or CPU.


