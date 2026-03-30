import pytest
from src.face_utils import detect_faces, encode_face, compare_faces

def test_detect_faces():
    img = face_recognition.load_image_file("data/test_img.jpg")
    locs = detect_faces(img)
    assert len(locs) > 0