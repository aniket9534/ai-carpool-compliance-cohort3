'''

from src.ingestion.camera import CameraCapture
from src.ingestion.video_reader import VideoReader
from src.ingestion.frame_processor import FrameProcessor
import cv2

video =VideoReader("data/videos/boajqbjzbh_trimmed.mp4")
#   video =CameraCapture()
processed=FrameProcessor()
while True:
    packet =video.read_frame()
    if packet is None:
        break
    frame =packet["img"]
    frame =processed.preprocess(frame)
    frame =processed.draw_fps(frame)
    
    cv2.imshow("output",frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break
    
video.release()
cv2.destroyAllWindows()

'''
import cv2

from src.ingestion.video_reader import VideoReader
from src.ingestion.frame_processor import FrameProcessor
from src.pipeline.detection.detector import VehicleDetector


def main():
    video_path = "data/videos/boajqbjzbh_trimmed.mp4"

    # Initialize components
    reader = VideoReader(video_path)
    processor = FrameProcessor()
    detector = VehicleDetector()

    while True:
        packet = reader.read_frame()

        if packet is None:
            print("End of video")
            break

        frame = packet["img"]

        # Step 1: preprocess
        frame =processor.preprocess(frame)
        

        # Step 2: detect
        detections = detector.detect(frame)

        # Step 3: draw detections
        for det in detections:
            x1, y1, x2, y2 = det["bbox"]

            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

            cv2.putText(
                frame,
                f"Car {det['confidence']:.2f}",
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2
            )

        # Show frame
        cv2.imshow("Detection Output", frame)

        if cv2.waitKey(1) & 0xFF == 27:  # ESC to exit
            break

    reader.cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()