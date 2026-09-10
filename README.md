# 🚀 CAIR Tactical Pipeline Engine

An AI-powered real-time object detection and tactical video processing system built using *Python, FastAPI, OpenCV, and YOLOv8*.

The CAIR Tactical Pipeline Engine processes live webcam feeds or video files, detects selected objects using a YOLOv8 model, enhances video frames using custom filters, and provides real-time video streaming through a FastAPI-based application.

---

## 📌 Project Overview

Computer vision and artificial intelligence are increasingly used for real-time monitoring and video analysis. The *CAIR Tactical Pipeline Engine* is designed to demonstrate how AI-powered object detection can be integrated with a real-time video processing pipeline.

The application captures frames from a video source, performs object detection using YOLOv8, applies tactical frame enhancement, and streams the processed output.

The project supports both:

- 📹 Live Webcam Input
- 🎥 Video File Input

---

## ✨ Features

- 🎯 Real-time object detection using YOLOv8
- 📹 Live webcam support
- 🎥 Video file processing
- ⚡ FastAPI-based backend
- 🖼️ Real-time video frame processing
- 🧠 AI-powered object detection
- 🔍 Detection of selected object classes
- 🎨 Tactical frame enhancement using custom filters
- 📡 Video streaming using FastAPI
- 🚀 Lightweight and easy-to-run application

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Core programming language |
| FastAPI | Backend API and video streaming |
| OpenCV | Video capture and frame processing |
| YOLOv8 | Object detection |
| Ultralytics | YOLOv8 implementation |
| Uvicorn | ASGI server for FastAPI |

---

## 📂 Project Structure

text
CAIR_Project/
│
├── main.py
├── filters.py
├── README.md
└── .gitignore


### File Description

- *main.py* – Main application file containing the FastAPI server, YOLO model loading, video capture, and streaming pipeline.
- *filters.py* – Contains custom functions for enhancing and processing video frames.
- *README.md* – Project documentation.
- *.gitignore* – Specifies files and folders that should not be uploaded to GitHub.

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

bash
git clone https://github.com/Arpanayadav/CAIR_PROJECT.git


### 2️⃣ Navigate to the Project Directory

bash
cd CAIR_PROJECT


### 3️⃣ Create a Virtual Environment (Recommended)

bash
python -m venv venv


### Activate the Virtual Environment

#### Windows

bash
venv\Scripts\activate


#### macOS/Linux

bash
source venv/bin/activate


### 4️⃣ Install Dependencies

bash
pip install fastapi uvicorn ultralytics opencv-python


---

## 🧠 YOLO Model Setup

This project uses the YOLOv8 Nano model.

The model is loaded using:

python
from ultralytics import YOLO

model = YOLO("yolov8n.pt")


The yolov8n.pt model file is not included in this repository.

When running the project, the Ultralytics library may automatically download the required YOLO model.

---

## 📹 Video Source Configuration

The project supports different video sources.

### 🔴 Option 1: Use Live Webcam

In main.py:

python
VIDEO_SOURCE = 0


This uses the default webcam connected to your computer.

---

### 🎥 Option 2: Use a Video File

In main.py:

python
VIDEO_SOURCE = "test_drone.mp4"


Make sure the video file is available in the project directory.

---

## 🎯 Object Detection

The application uses YOLOv8 to detect objects in each video frame.

The model processes video frames and identifies objects based on the selected target classes.

Example:

python
TACTICAL_CLASSES = [0, 2, 4, 7]


The target classes can be modified depending on the application requirements.

---

## ▶️ Running the Application

Start the FastAPI server using:

bash
uvicorn main:app --reload


After successfully starting the server, open your browser and visit:

text
http://127.0.0.1:8000


---

## 🔄 Application Workflow

The application follows the following workflow:

text
Video Source
     │
     ▼
OpenCV Video Capture
     │
     ▼
YOLOv8 Object Detection
     │
     ▼
Object Filtering
     │
     ▼
Tactical Frame Enhancement
     │
     ▼
FastAPI Streaming Response
     │
     ▼
Processed Video Output


---

## 📡 Core Working Process

1. The application receives video input from a webcam or video file.
2. OpenCV captures frames from the video source.
3. Each frame is passed to the YOLOv8 model.
4. YOLOv8 detects objects present in the frame.
5. Selected object classes are filtered.
6. Custom tactical enhancement filters are applied to the frame.
7. The processed frames are converted into a streaming format.
8. FastAPI sends the processed video stream to the client.

---

## 📦 Dependencies

Install the required Python packages:

bash
pip install fastapi
pip install uvicorn
pip install ultralytics
pip install opencv-python


Alternatively:

bash
pip install fastapi uvicorn ultralytics opencv-python


---

## 🔮 Future Improvements

The following features can be added in future versions:

- 📊 Real-time analytics dashboard
- 🎯 Advanced object tracking
- 🔔 Real-time alert system
- 🗺️ Location-based monitoring
- 📈 Detection statistics and reports
- 🧠 Support for custom-trained YOLO models
- 👥 Multi-object tracking
- 🌐 Frontend dashboard using React
- ☁️ Cloud deployment
- 🔐 User authentication
- 📱 Mobile-friendly interface
- 💾 Detection history and database integration

---

## 🎓 Learning Outcomes

Through this project, the following concepts were explored:

- Computer Vision
- Object Detection
- YOLOv8
- OpenCV
- FastAPI
- Real-Time Video Processing
- AI Model Integration
- Video Streaming
- Python Backend Development

---

## ⚠️ Important Notes

The following files are intentionally excluded from the GitHub repository:

text
*.mp4
*.pt
__pycache__/
.ipynb_checkpoints/


This is done to avoid uploading large video files, machine learning model files, and unnecessary cache files.

To run the project locally, make sure you have access to:

- A webcam, or
- A compatible video file

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

To contribute:

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Commit your changes.
5. Push the branch.
6. Create a Pull Request.

---

## 👩‍💻 Author

*Arpana Yadav*

GitHub: [Arpanayadav](https://github.com/Arpanayadav)

---

## 📄 License

This project is developed for *educational, research, and hackathon purposes*.

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

---

### 🚀 Built with Python, FastAPI, OpenCV, and YOLOv8
