import streamlit as st
import cv2
import numpy as np
from PIL import Image
from face_utils import detect_faces, draw_boxes

# 页面标题
st.title("🤖 人脸识别作业系统")
st.subheader("支持：人脸检测 + 框选标注")

# 上传图片
uploaded_file = st.file_uploader("请上传一张图片（JPG/PNG）", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # 打开图片
    image = Image.open(uploaded_file)
    img_array = np.array(image)

    # 人脸检测
    face_locations = detect_faces(img_array)
    face_names = [f"人脸{i+1}" for i in range(len(face_locations))]

    # 绘制框
    result_img = draw_boxes(img_array.copy(), face_locations, face_names)

    # 展示结果
    st.image(result_img, caption="检测完成", use_column_width=True)

    # 输出统计
    st.subheader("📊 检测结果")
    st.write(f"✅ 共检测到 {len(face_locations)} 张人脸")
    for i, (top, right, bottom, left) in enumerate(face_locations):
        st.write(f"人脸 {i+1} 位置：x={left}, y={top}")

else:
    st.info("👆 请上传图片开始使用")