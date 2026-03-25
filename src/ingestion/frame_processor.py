#Resize, normalize frame for model input

import cv2
import numpy as np
import time

from config.settings import FRAME_WIDTH,FRAME_HEIGHT

class FrameProcessor:
    def __init__(self):
        self.prev_time =time.time()
        
    def preprocess(self,frame):
        frame =cv2.resize(frame,(FRAME_WIDTH,FRAME_HEIGHT))
        #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)keep bgr for opencv
        return frame
    
    def draw_fps(self,frame):
        curr_time =time.time()
        fps =1/(curr_time - self.prev_time) if curr_time != self.prev_time else 0
        self.prev_time =curr_time
        
        cv2.putText(
            frame,
            f"FPS: {int(fps)}",
            (10,30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,(0,255,0),
            2
        )
        return frame
        