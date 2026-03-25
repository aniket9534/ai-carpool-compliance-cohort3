# live camera capture 
#To capture a video, you need to create a VideoCapture object

import time

import cv2
import numpy as np
from config.settings import CAMERA_SOURCE

class CameraCapture:
    def __init__(self, camera_source=CAMERA_SOURCE):
        self.camera_source = camera_source
        self.cap = cv2.VideoCapture(camera_source)
        self.frame_count =0
        
        #checking if camera opened successfully or not
        if not self.cap.isOpened():
            raise ValueError(f"Error opening camera source: {camera_source}")
    
    def read_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            return None
        self.frame_count +=1
        
        return {
            "img": frame,
            "frame_number": self.frame_count,
            "timestamp": time.time(),
            "source_id": self.camera_source
        }
    
    def release(self):
        self.cap.release()