import cv2
import time
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from ultralytics import YOLO
from filters import enhance_tactical_frame

app = FastAPI(title="CAIR Tactical Pipeline Engine")

# Load the local offline AI brain
model = YOLO("yolov8n.pt")
TACTICAL_CLASSES = [0,2,4,7] # Focus on targets

#  TIP: Set to 0 to use your laptop WEBCAM live! 
# Change to "test_drone.mp4" if you want to use a video file instead.
VIDEO_SOURCE = 0

def generate_tactical_stream():
    cap = cv2.VideoCapture(VIDEO_SOURCE)
    
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break

        # 1. Performance clock starts
        start_time = time.perf_counter()

        # 2. Apply your custom weather filter
        processed_frame = enhance_tactical_frame(frame)

        # 3. AI searches for targets
        results = model(processed_frame, classes=TACTICAL_CLASSES, verbose=False)
        annotated_frame = results[0].plot()

        # 4. Calculate real-time speed
        end_time = time.perf_counter()
        fps = 1.0 / (end_time - start_time)
        
        # Burn telemetry text onto the live output stream
        cv2.putText(annotated_frame, f"FPS: {fps:.1f}", (20, 40), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        cv2.putText(annotated_frame, "MODE: LIVE EDGE EMULATION", (20, 70), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1)

        # 5. Compress the image into web-friendly JPEG bytes
        _, buffer = cv2.imencode('.jpg', annotated_frame)
        frame_bytes = buffer.tobytes()
        
        # Yield the image block to the web page server
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')
               
    cap.release()

@app.get("/")
def home():
    return {"message": "CAIR Tactical Video Pipeline Server is Active. Go to /video_feed to watch live stream."}

@app.get("/video_feed")
def video_feed():
    """This route serves the live video feed directly to your web browser"""
    return StreamingResponse(generate_tactical_stream(), 
                             media_type="multipart/x-mixed-replace; boundary=frame")
