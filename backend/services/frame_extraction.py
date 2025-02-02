import cv2
import os
import numpy as np
from config import Config

FRAME_FOLDER = "extracted_frames"
os.makedirs(FRAME_FOLDER, exist_ok=True)

def extract_frames(video_path, interval=5):
    """
    Extracts frames from the video every 'interval' seconds and saves them.
    Returns a list of extracted frame file paths.
    """
    cap = cv2.VideoCapture(video_path)
    fps = int(cap.get(cv2.CAP_PROP_FPS))  # Frames per second
    frame_count = 0
    extracted_frames = []

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break

        # Save frame every 'interval' seconds
        if frame_count % (fps * interval) == 0:
            frame_filename = os.path.join(FRAME_FOLDER, f"frame_{frame_count}.jpg")
            cv2.imwrite(frame_filename, frame)
            extracted_frames.append(frame_filename)

        frame_count += 1

    cap.release()
    return extracted_frames
