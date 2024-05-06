import os

from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QPushButton, QVBoxLayout, QLabel, QApplication, QWidget


class ImageViewer(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.image_paths = []
        self.current_image_index = 0

    def initUI(self):
        # ... 其他UI初始化代码 ...

        # 添加图片显示的 QLabel
        self.left_frame = QLabel()
        self.left_frame.setFixedSize(550, 500)
        self.left_frame.setStyleSheet("border: 1px solid black;")

        # 添加按钮的垂直布局
        buttons_layout = QVBoxLayout()

        # 创建“上一组”按钮
        self.prev_button = QPushButton("上一张")
        self.prev_button.clicked.connect(self.showPreviousImage)

        # 创建“下一组”按钮
        self.next_button = QPushButton("下一张")
        self.next_button.clicked.connect(self.showNextImage)

        # 将按钮添加到布局中
        buttons_layout.addWidget(self.prev_button)
        buttons_layout.addWidget(self.next_button)

        # 创建主布局并添加组件
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.left_frame)
        main_layout.addLayout(buttons_layout)

        self.setLayout(main_layout)

    def showPreviousImage(self):
        if self.current_image_index > 0:
            self.current_image_index -= 1
            self.showImageInLeftFrame(self.image_paths[self.current_image_index])

    def showNextImage(self):
        if self.current_image_index < len(self.image_paths) - 1:
            self.current_image_index += 1
            self.showImageInLeftFrame(self.image_paths[self.current_image_index])

    def showImageInLeftFrame(self, image_path):
        pixmap = QPixmap(image_path).scaled(550, 500)
        self.left_frame.setPixmap(pixmap)

    def loadImages(self):
        # 清空之前的图片路径列表
        self.image_paths.clear()
        # 添加新的图片路径到列表中
        for img_file in os.listdir("data/images"):
            if img_file.endswith(('.png', '.jpg', '.jpeg')):
                img_path = os.path.join("data/images", img_file)
                self.image_paths.append(img_path)
        # 设置当前图片索引为0
        self.current_image_index = 0
        # 显示第一张图片
        if self.image_paths:
            self.showImageInLeftFrame(self.image_paths[self.current_image_index])


# 主程序
if __name__ == "__main__":
    app = QApplication([])
    viewer = ImageViewer()
    viewer.loadImages()  # 加载图片并显示第一张
    viewer.show()
    app.exec()
