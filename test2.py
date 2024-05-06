import os

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Window")
        self.setGeometry(100, 100, 500, 300)

        # 创建删除按钮
        self.delete_button = QPushButton("删除图片", self)
        self.delete_button.setGeometry(200, 150, 150, 30)

        # 连接删除按钮的点击事件到删除图片方法
        self.delete_button.clicked.connect(self.deleteImage)

    def deleteImage(self):
        # 提示用户是否删除除了jpg和png之外的所有图片文件
        reply = QMessageBox.question(self, '删除图片',
                                     "你想删除所有检测结果的图片吗?",
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.Yes)

        if reply == QMessageBox.Yes:
            # 用户选择删除，执行删除图片操作
            directory = "runs/detect/exp"
            success = True
            for file in os.listdir(directory):
                if file.endswith((".jpeg", ".gif", ".bmp")):
                    os.remove(os.path.join(directory, file))
                elif file.endswith((".jpg", ".png")):
                    os.remove(os.path.join(directory, file))
                else:
                    success = False

            if success:
                QMessageBox.information(self, "成功", "所有图片删除成功！")
        else:
            # 用户选择不删除，不执行任何操作
            pass


if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
