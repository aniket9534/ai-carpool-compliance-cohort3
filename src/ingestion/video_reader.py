#Recorded video reade
import time
import cv2
import numpy as np

from config.settings import PROCESS_EVERY_N_FRAMES

class VideoReader:
    def __init__(self,video_path):
        self.video_path = video_path
        self.cap =cv2.VideoCapture(video_path)
        self.frame_count =0
        
        #checking if video opened successfully or not
        if not self.cap.isOpened():
            raise ValueError(f"Error opening video file: {video_path}")
    
    def read_frame(self):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                return None

            self.frame_count += 1

            if self.frame_count % PROCESS_EVERY_N_FRAMES == 0:
                return {
                    "img": frame,
                    "frame_number": self.frame_count,
                    "timestamp": time.time(),
                    "source_id": self.video_path
                
                }

    def release(self):
        self.cap.release()
