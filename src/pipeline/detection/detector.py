#model logic for yolo inference


from ultralytics import YOLO
from config.settings import (
    YOLO_MODEL_PATH,
    YOLO_CONFIDENCE,
    YOLO_IOU_THRESHOLD,
    VEHICLE_CLASS_IDS
)

from src.pipeline.detection.utils import is_vehicle, format_detections


class VehicleDetector:
    def __init__(self):
        self.model = YOLO(YOLO_MODEL_PATH)
        print("YOLO model loaded successfully")

    def detect(self, frame):
        results = self.model(
            frame,
            conf=YOLO_CONFIDENCE,
            iou=YOLO_IOU_THRESHOLD,
            verbose=False
        )

        detections = []

        for r in results:
            if r.boxes is None:
                continue

            for box in r.boxes:
                clss_id = int(box.cls[0])
                conf = float(box.conf[0])

                if not is_vehicle(clss_id, VEHICLE_CLASS_IDS):
                    continue

                x1, y1, x2, y2 = map(int, box.xyxy[0])

                detection = format_detections(
                    x1, y1, x2, y2, conf, clss_id
                )

                detections.append(detection)

        return detections