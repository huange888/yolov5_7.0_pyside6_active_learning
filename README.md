# 这个是我的开源 pyside6 + yolov5项目，欢迎 star

# 项目介绍

我把一些文件给删掉了 例如segement 什么的 可以在原生的yolov5 7.0重新安装
最主要的就是两个文件
分别是ui.py MainQt.py
直接运行MainQt.py即可
最主要的pt文件就是data/models/biology.pt
这是用yolov5框架+主动学习跑出来的外周血细胞的模型
目前精度0.8
并且支持切换模型 切换到原生的yolov5m.pt
![image](https://github.com/huange888/yolov5_7.0_pyside6_active_learning/assets/118048444/165a5c67-7a64-4cd3-8ed2-0292cab780e9)

# 运行环境

pip install -r requirements.txt

# 运行方法

python MainQt.py

# 项目截图
![image](https://github.com/huange888/yolov5_7.0_pyside6_active_learning/assets/118048444/2cbce1b7-c8b5-4495-9183-bd05800b9d43)

# 运行介绍

该项目是使用PySide6库开发的一个基于YOLOv5的图像识别应用程序。
用户可以通过该应用程序选择图像文件或摄像头实时检测目标物体，并显示检测结果。
同时，该应用程序还支持主动学习功能，用户可以手动标记一些错误的检测结果，以帮助模型进行优化。
不过目前摄像头还没开发好 只能识别图片。

# 项目结构
