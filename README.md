# Volume Detection using MiDaS and IP Webcam

This project utilizes the MiDaS depth estimation model, combined with a smartphone's IP Webcam stream, to monitor the fill level of a container.

---

## Setup and Installation

1. Ensure you have Python 3.7 or later installed.
2. (Optional but recommended) Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # On Windows use: .venv\Scripts\activate


pip install torch torchvision opencv-python numpy


Notes
- Make sure your smartphone and computer are on the same Wi-Fi network for the IP Webcam stream to work.

- Avoid having the stream open simultaneously in a browser and the Python script.

- This code uses the MiDaS small model for depth estimation, which is lightweight and suitable for low-RAM devices.

  ## Step-by-step Procedure:

1. Install the **IPWebCam** app on your phone.
2. Start the server in the IPWebCam app on your phone.
3. You will get a URL link for the video stream.
4. Open that URL in a browser on your laptop or mobile device.
5. If the video appears, it means the stream is working — then close that browser tab because the code won't work if the stream is open in a browser.
6. Paste the URL in the Python code (`VIDEO_STREAM_URL` variable).
7. Run the Python script.
8. A window showing the webcam video stream will open. Press the **`c`** key (just press the key, no Enter needed).
9. Switch back to the VSCode terminal and check for the message confirming the frame was captured.
10. Go back to the webcam video window.
11. Press the **`c`** key again to capture the second frame, then switch back to the terminal to see the comparison output.
12. When finished, press **`q`** in the webcam window to exit the program. (Remember: only press the key, do **NOT** press Enter.)


volume_detection_2/
│
├── live_depth_monitor.py       # Your main Python script with the MiDaS code
├── README.md                   # Project README with instructions
├── requirements.txt            # (Optional) List of pip packages for easy install
├── .venv/                      # (Optional) Virtual environment folder
└── assets/                     # (Optional) Any images, configs, or helper files


