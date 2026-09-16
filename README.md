# CAIR — Computer Vision & AI Recognition Pipeline

> AI-powered video analysis pipeline using YOLOv8, OpenCV, CLAHE, and FastAPI for object detection and real-time video streaming.

## 🚀 Features

- YOLOv8-based object detection
- OpenCV video processing
- CLAHE-based image enhancement
- Target-class filtering
- Frame skipping for CPU optimization
- Real-time FPS monitoring
- FastAPI backend
- MJPEG video streaming
- Render deployment

## 🛠️ Tech Stack

- *Language:* Python 3.11
- *Backend:* FastAPI, Uvicorn
- *Computer Vision:* OpenCV, NumPy, CLAHE
- *AI/ML:* Ultralytics YOLOv8
- *Deployment:* Render
- *Tools:* Git, GitHub, VS Code

## 🧠 Architecture

text
Video Input
    ↓
OpenCV
    ↓
CLAHE Enhancement
    ↓
YOLOv8 Detection
    ↓
Class Filtering
    ↓
Frame Annotation
    ↓
MJPEG Stream
    ↓
FastAPI


## 🎯 Detection Classes

The current model is configured to detect:

| Class | Object |
|---|---|
| 0 | Person |
| 2 | Car |
| 4 | Airplane |
| 7 | Truck |

## ⚡ Performance Optimization

To improve performance on CPU-based deployment:

- YOLO inference size: 320
- YOLO inference runs on every 3rd frame
- Detection is limited to selected classes

## 📁 Project Structure

text
CAIR_PROJECT/
├── main.py
├── filters.py
├── requirements.txt
├── .python-version
├── .gitignore
├── demo.mp4
└── README.md


## ⚙️ Installation

### 1. Clone Repository

bash
git clone https://github.com/Arpanayadav/CAIR_PROJECT.git
cd CAIR_PROJECT


### 2. Create Virtual Environment

bash
python -m venv venv


Activate on Windows:

bash
venv\Scripts\activate


### 3. Install Dependencies

bash
pip install -r requirements.txt


### 4. Run Locally

bash
uvicorn main:app --reload


Open:

text
http://127.0.0.1:8000


Video stream:

text
http://127.0.0.1:8000/video_feed


## 🔗 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | / | API status |
| GET | /video_feed | Processed video stream |

## ☁️ Deployment

Deployed using *Render*.

*Build Command*

bash
pip install -r requirements.txt


*Start Command*

bash
uvicorn main:app --host 0.0.0.0 --port $PORT


## 🌐 Live Demo

*API:*  
https://cair-project.onrender.com/

*Video Stream:*  
https://cair-project.onrender.com/video_feed

> Note: Cloud free-tier resources may cause higher inference latency.

## 🔮 Future Improvements

- Browser camera integration
- Dedicated frontend
- WebSocket/WebRTC streaming
- Custom-trained YOLO model
- GPU acceleration
- Multi-user support

## 👨‍💻 Author

*Arpan Yadav*  
B.Tech — Computer Science & Engineering (AI & ML)

### Skills Demonstrated

Python FastAPI OpenCV YOLOv8 Computer Vision Machine Learning Git GitHub Cloud Deployment

## 📄 License

This project is intended for educational and portfolio purposes.
