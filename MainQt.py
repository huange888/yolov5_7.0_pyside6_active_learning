# MainQt.py
import os
import shutil
import subprocess
import sys
import threading
import time
from datetime import datetime
from queue import Queue

from PySide6.QtGui import QPixmap, Qt, QIcon
from PySide6.QtWidgets import QApplication, \
    QFileDialog, QMainWindow, QMessageBox

from ui import UiMainWindow


# !/usr/bin/env python
# coding=utf-8

class MainWindow(QMainWindow, UiMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('data/winIco.png'))
        self.setupUi(self)  # 使用UiMainWindow中的setupUi方法来设置UI

        self.populateComboBox()  # Populate combo box with available model files

        # 将按钮点击事件连接到逻辑类的槽函数
        self.start_button.clicked.connect(self.detectObjects)
        self.upload_image_button.clicked.connect(self.uploadImage)
        self.upload_pt_button.clicked.connect(self.uploadPTFile)
        self.Labelrun_button.clicked.connect(self.runAnylabel)
        self.activeRun_button.clicked.connect(self.runActiveLearn_run)
        self.activeTrain_button.clicked.connect(self.runActiveLearn_train)
        self.export_button.clicked.connect(self.exportFormat)
        self.export_image_button.clicked.connect(self.exportImage)
        self.close_button.clicked.connect(self.deleteImage)
        self.stop_button.clicked.connect(self.stopActiveProcess)

        # #setting
        self.comboBox.currentIndexChanged.connect(self.selectionChanged)
        self.iou_slider.valueChanged.connect(self.iouValueChanged)
        self.iou_spinbox.valueChanged.connect(self.iouSpinBoxValueChanged)
        self.conf_slider.valueChanged.connect(self.confValueChanged)
        self.conf_spinbox.valueChanged.connect(self.confSpinBoxValueChanged)
        self.delay_slider.valueChanged.connect(self.delayValueChanged)
        self.delay_spinbox.valueChanged.connect(self.delaySpinBoxValueChanged)
        self.save_mp4_jpg_checkbox.stateChanged.connect(self.onSaveMp4JpgChanged)
        self.save_labels_checkbox.stateChanged.connect(self.onSaveLabelsChanged)
        self.delete_content_checkbox.stateChanged.connect(self.onDeleteContentChanged)

        # 连接逻辑类的信号到MainWindow的槽函数

    # 展示结果
    def showResults(self, result_str):
        self.textbox.append(result_str)  # 使用append方法追加文本，而不是覆盖原有的内容

    def runAnylabel(self):
        print("点击Anylabel按钮")
        label_path = r"anylabeling/app.py"
        if os.path.exists(label_path):
            subprocess.Popen(["python", label_path])
            self.showResults("成功运行 AnyLabeling")
        else:
            self.showResults("未找到 AnyLabeling 可执行文件")

    def runActiveLearn_run(self):
        print("点击ActiveLearn_run按钮")
        label_path = r"D:/PythonFiles/Active_learning/AL_run.py"
        if os.path.exists(label_path):
            process = subprocess.Popen(["python", label_path])
            output, success = process.communicate()
            self.active_process = process
            self.showResults("成功打开 ActiveLearn_run")
            self.showResults(output.decode('utf-8'))
            self.showResults("运行结果：" + str(success))

        else:
            self.showResults("未找到 ActiveLearn_run 可执行文件")

    def runActiveLearn_train(self):
        print("点击ActiveLearn_train按钮")
        label_path = r"D:/PythonFiles/Active_learning/AL_train.py"
        if os.path.exists(label_path):
            subprocess.Popen(["python", label_path])
            self.showResults("成功打开 ActiveLearn_train")
        else:
            self.showResults("未找到 ActiveLearn_train 可执行文件")

    def exportFormat(self):
        print("点击exportFormat按钮")
        label_path = r"export.py"
        if os.path.exists(label_path):
            subprocess.Popen(["python", label_path])
            self.showResults("成功运行 export.py")
        else:
            self.showResults("未找到 export.py 可执行文件")

    def uploadImage(self):
        # 弹出文件选择对话框
        print("点击uploadImage按钮")
        file_path, _ = QFileDialog.getOpenFileName(self, "选择图片", "", "Images (*.png *.jpg *.jpeg)")
        if file_path:
            # 复制图片到 data/images 目录下
            os.makedirs("data/images", exist_ok=True)
            self.current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename = os.path.basename(file_path)
            dest_path = os.path.join("data/images", f"{self.current_time}_{filename}")
            self.imageName = os.path.basename(dest_path)
            shutil.copy(file_path, dest_path)
            self.showResults(f"成功上传图片：{dest_path}")
            # 显示上传的图片
            pixmap = QPixmap(dest_path).scaled(550, 550)
            self.left_frame.setPixmap(pixmap)
            # 保存上传图片的路径
            self.img_path = dest_path

    def uploadPTFile(self):
        # 弹出文件选择对话框
        print("点击uploadPTFile按钮")
        file_path, _ = QFileDialog.getOpenFileName(self, "选择.pt文件", "", "PT Files (*.pt)")
        if file_path:
            # 复制.pt文件到 data/models 目录下
            os.makedirs("data/models", exist_ok=True)
            dest_path = os.path.join("data/models", os.path.basename(file_path))
            self.pt_path = dest_path
            shutil.copy(file_path, dest_path)
            self.showResults(f"成功上传.pt文件：{dest_path}")

    def runScript(self, script_path, project_dir):
        # self.active_process = subprocess.Popen(["python", script_path], cwd=project_dir,
        #                                        stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

        output_queue = Queue()  # 创建一个队列用于传递输出数据
        thread = threading.Thread(target=self.process_output, args=(self.active_process.stdout, output_queue))
        thread.start()

        while True:
            line = output_queue.get()  # 从队列中获取一行输出
            if line is None:
                break  # 输出结束，跳出循环

            self.showResults(line.decode('utf-8'))  # 将输出行显示在QTextEdit中
            print(line.decode('utf-8'), end='')  # 将输出行打印到终端

        thread.join()  # 等待处理输出的线程结束

    def process_output(self, stream, output_queue):
        for line in iter(stream.readline, b''):
            output_queue.put(line)  # 将输出行放入队列

        stream.close()
        output_queue.put(None)  # 标记输出结束

    def stopActiveProcess(self):
        print("点击进程按钮")
        if self.active_process:
            self.active_process.terminate()  # 终止进程
            self.showResults("已停止活动学习进程")
        else:
            self.showResults("没有活动学习进程在运行")

    def detectObjects(self):
        print("点击目标检测按钮")
        add_label = ""
        add_jpg = ""
        command = "python detect.py --source " + self.img_path
        add_iou = " --iou-thres " + str(self.iou_spinbox.value())
        add_conf = " --conf-thres " + str(self.conf_spinbox.value())
        add_pt = " --weight data/models/" + str(self.comboBox.currentText())
        time.sleep(self.delay_spinbox.value() / 1000)
        if self.save_labels_checkbox.checkState() == Qt.CheckState.Checked:
            add_label = " --save-txt "
        if self.save_mp4_jpg_checkbox.checkState() == Qt.CheckState.Unchecked:
            add_jpg = " --nosave "
        command = command + add_jpg + add_label + add_iou + add_conf + add_pt
        print(command)
        with open('logs.txt', 'a') as log_file:
            log_file.write("current_time: " + self.current_time + '  ' + command + '\n')
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, success = process.communicate()

        if success:
            self.showResults("运行成功: \n" + success.decode('utf-8'))
            image_path = os.path.join("runs/detect/exp", f"{self.imageName}")

            if os.path.exists(image_path):
                pixmap = QPixmap(image_path).scaled(550, 550)
                self.right_frame.setPixmap(pixmap)
        else:
            pass

    def exportImage(self):
        print("点击导出图片按钮")
        # 获取图片的当前路径（假设你已经有了这个路径）
        current_image_path = "runs/detect/exp/" + os.path.basename(self.img_path)
        # 获取用户输入的目标地址
        new_address = self.address_line.text().strip("\"")

        # 检查目标地址是否有效
        if not new_address:
            QMessageBox.warning(self, "错误", "目标地址不能为空。")
            return
        # 确保目标地址是完整的文件路径
        new_address = os.path.join(new_address, os.path.basename(current_image_path))
        # 确保目标地址的目录存在
        os.makedirs(os.path.dirname(new_address), exist_ok=True)
        try:
            # 复制图片到目标地址
            shutil.copy(current_image_path, new_address)
            QMessageBox.information(self, "成功", f"图片已成功复制到：\n{new_address}")
        except Exception as e:
            QMessageBox.critical(self, "错误", f"复制图片时发生错误：\n{e}")

    def deleteImage(self):
        # 根据是否选中清空复选框来删除内容
        if self.delete_content_checkbox.checkState() == Qt.CheckState.Checked:
            # 用户选择删除，执行删除图片操作
            output_directory = "runs/detect/exp"
            input_directory = "data/images"
            label_directory = "runs/detect/exp/labels"
            success = True
            for file in os.listdir(output_directory):
                if file.endswith((".jpeg", ".gif", ".bmp")):
                    os.remove(os.path.join(output_directory, file))
                elif file.endswith((".jpg", ".png")):
                    os.remove(os.path.join(output_directory, file))
            for file in os.listdir(input_directory):
                if file.endswith((".jpeg", ".gif", ".bmp")):
                    os.remove(os.path.join(input_directory, file))
                elif file.endswith((".jpg", ".png")):
                    os.remove(os.path.join(input_directory, file))
            for file in os.listdir(label_directory):
                if file.endswith(".txt"):
                    os.remove(os.path.join(label_directory, file))  # 删除labels里面的标记文件
            with open("logs.txt", "w+") as log_file:
                log_file.truncate()  # 删除文件中的所有内容
            if success:
                QMessageBox.information(self, "成功", f"图片和文本已经全部删除,并且日志内容全部清空")
                self.close()
        else:
            # 用户选择不删除，不执行任何操作
            self.close()

    # setting
    def populateComboBox(self):
        model_dir = "data/models"  # Directory containing model files
        model_files = os.listdir(model_dir)
        for file_name in model_files:
            if file_name.endswith(".pt"):  # Filter out only .pt files
                self.comboBox.addItem(file_name)

    def selectionChanged(self, index):
        selected_model = self.comboBox.currentText()
        print("Selected model:", selected_model)

    def iouValueChanged(self, value):
        iou = value / 100.0
        self.iou_spinbox.setValue(iou)

    def iouSpinBoxValueChanged(self, value):
        iou = value * 100.0
        self.iou_slider.setValue(iou)
        print("iou_value = ", value)

    # 设置conf 和延时

    def confValueChanged(self, value):
        """
        当置信度滑块值变化时调用的函数。
        """
        # 更新数值输入框的值
        self.conf_spinbox.setValue(value / 100.0)

    def confSpinBoxValueChanged(self, value):
        """
        当置信度输入框值变化时调用的函数。
        """
        # 更新滑块的值
        self.conf_slider.setValue(int(value * 100.0))
        print("conf_value = ", value)

    def delayValueChanged(self, value):
        """
        当延时滑块值变化时调用的函数。
        """
        # 更新数值输入框的值
        self.delay_spinbox.setValue(value)

    def delaySpinBoxValueChanged(self, value):
        """
        当延时输入框值变化时调用的函数。
        """
        # 更新滑块的值
        self.delay_slider.setValue(int(value))
        print("delay_value = ", value)

    # 处理保存为 mp4/jpg 复选框变化的槽函数
    def onSaveMp4JpgChanged(self):
        if self.save_mp4_jpg_checkbox.checkState() == Qt.CheckState.Checked:
            print("保存为 MP4/JPG 选项已被选中。")
            # 在这里添加当复选框被选中时的逻辑
        elif self.save_mp4_jpg_checkbox.checkState() == Qt.CheckState.Unchecked:
            print("保存为 MP4/JPG 选项已被取消选中。")
            # 在这里添加当复选框被取消选中时的逻辑

    # 处理保存 labels (.txt) 复选框变化的槽函数
    def onSaveLabelsChanged(self):
        if self.save_labels_checkbox.checkState() == Qt.CheckState.Checked:
            print("保存 Labels (.txt) 选项已被选中。")
            # 在这里添加当复选框被选中时的逻辑
        elif self.save_labels_checkbox.checkState() == Qt.CheckState.Unchecked:
            print("保存 Labels (.txt) 选项已被取消选中。")
            # 在这里添加当复选框被取消选中时的逻辑

    def onDeleteContentChanged(self):
        if self.delete_content_checkbox.checkState() == Qt.CheckState.Checked:
            print("删除内容选项已被选中。")
        elif self.delete_content_checkbox.checkState() == Qt.CheckState.Unchecked:
            print("删除内容选项已被取消选中。")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
