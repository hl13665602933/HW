import cv2
import numpy as np

def detect_faces(image: np.ndarray):
    """
    人脸检测（使用 OpenCV 自带模型）
    返回：[(top, right, bottom, left), ...]
    """
    # 加载人脸检测器
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )
    
    # 转灰度
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    
    # 检测
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )
    
    # 格式转换
    face_locations = []
    for (x, y, w, h) in faces:
        top = y
        right = x + w
        bottom = y + h
        left = x
        face_locations.append((top, right, bottom, left))
    
    return face_locations

def draw_boxes(image: np.ndarray, face_locations: list, names: list):
    """在图片上画框和名字"""
    for (top, right, bottom, left), name in zip(face_locations, names):
        # 画框
        cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
        # 画标签背景
        cv2.rectangle(image, (left, bottom - 25), (right, bottom), (0, 255, 0), cv2.FILLED)
        # 写文字
        cv2.putText(
            image, name,
            (left + 6, bottom - 6),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (255, 255, 255),
            1
        )
    return image