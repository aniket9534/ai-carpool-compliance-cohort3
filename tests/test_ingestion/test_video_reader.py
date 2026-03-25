import pytest
from src.ingestion.video_reader import VideoReader


def test_video_reader_packet():
    video_path = "data/videos/boajqbjzbh_trimmed.mp4"  # put your test video here

    reader = VideoReader(video_path)

    packet = reader.read_frame()

    # 🔍 Basic checks
    assert packet is not None, "Packet should not be None"

    assert "img" in packet
    assert "frame_number" in packet
    assert "timestamp" in packet
    assert "source_id" in packet

    # 🔍 Type checks
    assert isinstance(packet["frame_number"], int)
    assert isinstance(packet["timestamp"], float)
    assert isinstance(packet["source_id"], str)

    # 🔍 Image checks
    frame = packet["img"]
    assert frame is not None
    assert len(frame.shape) == 3  # H, W, C

    reader.release()