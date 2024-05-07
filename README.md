# 这个是我的开源 pyside6 + yolov5+active-learning项目，欢迎 star![395494A6.png](https://cdn.nlark.com/yuque/0/2024/png/34454554/1714980244561-4f46267d-25f0-4a03-9b8a-2bf4de7d3b58.png#averageHue=%2354472a&clientId=u04ab15bb-705b-4&from=paste&height=48&id=u2733e641&originHeight=48&originWidth=48&originalType=binary&ratio=1&rotation=0&showTitle=false&size=2823&status=done&style=none&taskId=u243c43ab-fa0c-4a3d-99b2-db8ba5a2e5f&title=&width=48) and follow!
# 项目介绍
我把一些文件给删掉了 例如segement 什么的 <br />可以在原生的yolov5 7.0重新安装<br />最主要的就是两个文件<br />分别是ui.py
MainQt.py<br />直接运行MainQt.py即可<br />最主要的pt文件就是data/models/biology.pt<br />
这是用yolov5框架+主动学习跑出来的外周血细胞的模型<br />目前精度0.8 精度较高<br />并且支持切换模型 切换到原生的yolov5m.pt
支持对其他目标进行识别<br />但是biology.pt是用商业数据跑出来的模型 暂未考虑对外开放<br />对于一般的课设作业 可以将run
label train export
停止进程按钮删掉<br />![](https://github.com/huange888/yolov5_7.0_pyside6_active_learning/assets/118048444/165a5c67-7a64-4cd3-8ed2-0292cab780e9#id=UtZd0&originHeight=823&originWidth=1376&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=)

# 运行环境
```python
pip install -r requirements.txt
```

# 运行方法
```python
python MainQt.py
```
# 项目截图
![](https://github.com/huange888/yolov5_7.0_pyside6_active_learning/assets/118048444/2cbce1b7-c8b5-4495-9183-bd05800b9d43#id=DI5yH&originHeight=823&originWidth=1376&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=)
# 运行介绍

该项目是使用PySide6库开发的一个基于YOLOv5的图像识别应用程序。<br />
用户可以通过该应用程序选择图像文件或摄像头实时检测目标物体，并显示检测结果。<br />
同时，该应用程序还支持主动学习功能，用户可以手动标记一些错误的检测结果，以帮助模型进行优化。<br />不过目前摄像头还没开发好
只能识别图片 同时对于视频识别可以用原生代码进行检测 在qt中实现运行较慢  <br />暂未考虑实现视频识别模块

# 项目结构
# 功能区
## 启动按钮 (Start Button)

- **按钮名称**: `start_button`
- **功能**: 用于启动某个过程或程序。
## 图片上传按钮 (Upload Image Button)

- **按钮名称**: `upload_image_button`
- **功能**: 允许用户上传图片文件。
## 模型上传按钮 (Upload PT Button)

- **按钮名称**: `upload_pt_button`
- **功能**: 用于上传模型文件，通常指的是PyTorch模型文件。
## 运行标签按钮 (Label Run Button)

- **按钮名称**: `Labelrun_button`
- **功能**: 用于启动一个标记或分类过程。
## 主动学习运行按钮 (Active Run Button)

- **按钮名称**: `activeRun_button`
- **功能**: 用于激活或开始一个实时运行的过程。
## 主动学习训练按钮 (Active Train Button)

- **按钮名称**: `activeTrain_button`
- **功能**: 用于启动模型的活跃训练阶段。
## 导出模型按钮 (Export Button)

- **按钮名称**: `export_button`
- **功能**: 用于导出数据或模型到文件。
## 停止进程按钮 (Stop Button)

- **按钮名称**: `stop_button`
- **功能**: 用于停止当前运行的过程。
## 关闭窗口按钮 (Close Button)

- **按钮名称**: `close_button`
- **功能**: 用于关闭应用程序或当前窗口。
