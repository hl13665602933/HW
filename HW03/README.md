# 人脸识别作业系统

## 项目简介
本项目是基于 **Streamlit + OpenCV** 实现的人脸检测作业系统，无需依赖复杂的 dlib/face_recognition 库，可在 Python 3.7~3.13 环境下稳定运行。

核心功能：
- 📸 支持 JPG/PNG 格式图片上传
- 🔍 自动检测图片中的人脸位置
- 🎨 绿色框标注人脸并显示编号
- 📊 统计检测到的人脸数量

---

## 项目结构
HW03/
├── src/
│ ├── app.py # 主程序（Streamlit 界面）
│ └── face_utils.py # 人脸检测工具类
└── requirements.txt # 依赖清单
└── README.md # 项目说明文档

---

## 环境配置

### 1. Python 版本
推荐使用 Python 3.11.x（兼容性最佳），也支持 Python 3.13。

### 2. 安装依赖
打开终端，执行以下命令安装所有依赖：

pip install -r requirements.txt
若遇到编译报错，可使用预编译版本安装：

pip install --only-binary=:all: -r requirements.txt
快速启动
1. 启动应用
在项目根目录下执行：
bash
运行
python -m streamlit run src/app.py
2. 访问系统
终端会输出访问地址（默认：http://localhost:8501），在浏览器中打开即可使用。
使用说明
进入页面后，点击 「Browse files」 或拖拽上传一张包含人脸的图片（JPG/PNG 格式）
系统自动完成人脸检测，并在图片上用绿色框标注人脸
下方会显示检测结果：
标注「人脸 1」「人脸 2」...
统计检测到的人脸总数
技术实现
核心技术栈
Streamlit：快速构建 Web 界面
OpenCV：实现人脸检测（Haar 级联分类器）
Pillow/Numpy：图片处理与数组操作
算法原理
图片上传后转换为 RGB 数组
调用 OpenCV 自带的 haarcascade_frontalface_default.xml 模型检测人脸
检测结果转换为 (top, right, bottom, left) 格式
在原图上绘制绿色框和标签，展示最终结果
注意事项
仅支持正面人脸检测，侧脸 / 遮挡较多时可能识别率下降
图片大小建议不超过 200MB，过大图片会影响处理速度
若在 Python 3.13 下安装依赖报错，请使用 --only-binary=:all: 参数安装预编译版本
