# 📹 EZVIZ-RTSP

A lightweight Python application for accessing EZVIZ camera streams over RTSP and performing real-time face detection using OpenCV and YuNet.

Integrates EZVIZ device discovery, cloud authentication, camera key retrieval, live video processing, and automated face extraction into a simple pipeline.

## ✨ Features  
🔍 EZVIZ device discovery  
🔐 Cloud authentication  
🔑 Automatic camera verification key retrieval  
📡 Live RTSP video streaming  
🧠 Real-time face detection with YuNet  
🖼️ Automatic face extraction and saving  
⚙️ Configuration  

## 🚀 Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Sum1t01/EZVIZ-RTSP.git
   cd EZVIZ-RTSP
2. ***Create a Virtual Environment***
    ```bash
    python -m venv venv
3. ***Install Dependencies***
    ```bash
    pip install opencv-python numpy python-dotenv pyezvizapi
4. ***Download YuNet Model***  
    Download **face_detection_yunet_2023mar.onnx** from the [OpenCV Zoo – YuNet Model](https://github.com/opencv/opencv_zoo/tree/main/models/face_detection_yunet).

    Place the model in the project root directory.

5. ***Configure Environment Variables***  
    Create a .env file in the project root:
    ```env
    # EZVIZ Account Credentials
   USERNAME=your_ezviz_email
   PASSWORD=your_ezviz_account_password

   # Camera Credentials
   CAMERA_USERNAME=admin
   CAMERA_PASSWORD=your_camera_password

   # Camera Configuration
   DEVICE_SERIAL=your_camera_serial

## ▶️ Usage

Run the application:

```bash
python main.py
```
## 🛠️ Tech Stack

Python · OpenCV · RTSP · EZVIZ API · YuNet · ONNX

