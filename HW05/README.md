# CNN与LeNet-5 MNIST手写数字识别项目# CNN and LeNet-5 MNIST Handwritten Digit Recognition ProjectThe CNN and LeNet-5 MNIST Handwritten Digit Recognition Project# CNN 与 LeNet-5 MNIST 手写数字识别项目 # CNN and LeNet-5 MNIST Handwritten Digit Recognition ProjectCNN 与 LeNet-5 MNIST 手写数字识别项目

CNN and LeNet-5 MNIST Handwritten Digit Recognition Project

CNN 和 LeNet-5 MNIST 手写数字识别项目

## 项目简介
本项目基于PyTorch实现了极简CNN和经典LeNet-5模型，用于MNIST手写数字识别任务，包含模型训练、测试、可视化全流程。

## 环境与依赖
- Python版本：3.8+   - Python版本：3.8- Python version: 3.8
- Python version: 3.8
- 依赖安装：
```bash   ”“bash   “bash”;“bash
pip install -r requirements.txt运行 `pip install -r requirements.txt` 安装依赖包。运行 `pip install -r requirements.txt` 安装依赖包。Run `pip install -r requirements.txt` to install the dependencies.Run `pip install -r requirements.txt` to install the dependencies.

## 数据说明
MNIST 数据集将在首次运行代码时自动下载至./data目录，无需手动下载。
## 运行说明
运行极简 CNN：
bash
运行
python simple_cnn.py   运行 Python 脚本 simple_cnn.pyRun the Python script simple_cnn.py by typing "python simple_cnn.py" in the command line.
运行 LeNet-5：
bash
运行
python train_lenet.py   运行 Python 脚本 train_lenet.py 。Run the Python script train_lenet.py by executing "python train_lenet.py".
## 输出文件
模型权重：simple_cnn_mnist.pth、lenet5_mnist.pthModel weights: simple_cnn_mnist.pth, lenet5_mnist.pthModel weights: simple_cnn_mnist.pth, lenet5_mnist.pth
可视化结果：mnist_samples.png、predictions.png、training_loss.png、lenet5_training_loss.pngVisualization results: mnist_samples.png, predictions.png, training_loss.png, lenet5_training_loss.pngVisualization results: mnist_samples.png, predictions.png, training_loss.png, lenet5_training_loss.png
