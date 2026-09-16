import os
import cv2
import time

from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from ultralytics import YOLO

from filters import enhance_tactical_frame


app = FastAPI(
    title="CAIR Tactical Pipeline Engine",
    description="AI-powered tactical video processing using YOLOv8",
    version="1.0.0"
)


# Load YOLOv8 model
model = YOLO("yolov8n.pt")


# COCO target classes
TACTICAL_CLASSES = [0, 2, 4, 7]


# Video source
# Set VIDEO_SOURCE=0 locally for webcam
# Set VIDEO_SOURCE=demo.mp4 for a video file
VIDEO_SOURCE = os.getenv("VIDEO_SOURCE", "demo.mp4")


def generate_tactical_stream():

    source = VIDEO_SOURCE

    # Convert "0" string into webcam index
    if source == "0":
        source = 0

    cap = cv2.VideoCapture(source)

    if not cap.isOpened():
        print(f"Unable to open video source: {source}")
        return

    while cap.isOpened():

        success, frame = cap.read()

        # Restart video when it ends
        if not success:

            if isinstance(source, str):
                cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                continue

            break


        start_time = time.perf_counter()


        # Enhance frame
        processed_frame = enhance_tactical_frame(frame)


        # AI object detection
        results = model(
            processed_frame,
            classes=TACTICAL_CLASSES,
            verbose=False
        )


        # Draw detection results
        annotated_frame = results[0].plot()


        # Calculate FPS
        end_time = time.perf_counter()

        processing_time = end_time - start_time

        fps = 1.0 / processing_time if processing_time > 0 else 0


        # Display telemetry
        cv2.putText(
            annotated_frame,
            f"FPS: {fps:.1f}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )


        cv2.putText(
            annotated_frame,
            "MODE: AI TACTICAL ANALYSIS",
            (20, 70),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 255),
            2
        )


        # Convert to JPEG
        success, buffer = cv2.imencode(
            ".jpg",
            annotated_frame
        )

        if not success:
            continue


        frame_bytes = buffer.tobytes()


        yield (
            b"--frame\r\n"
            b"Content-Type: image/jpeg\r\n\r\n"
            + frame_bytes
            + b"\r\n"
        )


    cap.release()


@app.get("/")
def home():

    return {
        "status": "active",
        "project": "CAIR Tactical Pipeline Engine",
        "video_feed": "/video_feed"
    }


@app.get("/health")
def health():

    return {
        "status": "healthy"
    }


@app.get("/video_feed")
def video_feed():

    return StreamingResponse(
        generate_tactical_stream(),
        media_type="multipart/x-mixed-replace; boundary=frame"
    )