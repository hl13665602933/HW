# 调试记录

## 问题1：ModuleNotFoundError: No module named 'torch'
- 解决方法：运行`pip install torch torchvision`安装PyTorch库

## 问题2：Matplotlib中文显示乱码
- 解决方法：添加`matplotlib.rcParams['font.family'] = 'SimHei'`配置

## 问题3：LeNet-5全连接层输入维度错误
- 原因：未正确计算池化后的特征图尺寸
- 解决方法：根据输入尺寸重新计算全连接层输入维度为16*4*4
