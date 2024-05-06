import os

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QComboBox, QVBoxLayout, QWidget, QGroupBox, QLabel, QSlider, QDoubleSpinBox, \
    QHBoxLayout, QCheckBox


class SelectionModelDemo(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.iou_spinbox.setValue(0.45)
        self.conf_spinbox.setValue(0.25)
        self.delay_spinbox.setValue(10)  # 默认值设置为10

    def initUI(self):
        layout = QVBoxLayout()

        # 创建一个大边框
        group_box = QGroupBox()
        group_box.setStyleSheet(
            "QGroupBox { border: 2px solid white; border-radius: 20px; background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #FFB6C1, stop:1 #FF69B4); }")
        group_layout = QVBoxLayout()

        # 在大边框中添加一个QLabel来显示文本
        label = QLabel("选择模型")
        label.setAlignment(Qt.AlignCenter)  # 文本居中对齐
        label.setStyleSheet("QLabel { color: white; }")
        pt_layout = QHBoxLayout()  # pt模型 水平布局

        # 添加标准IOU值范围标签
        pt_label = QLabel("选择模型:")
        pt_label.setStyleSheet("QLabel { color: white; }")
        pt_layout.addWidget(pt_label)

        self.comboBox = QComboBox()
        self.comboBox.setStyleSheet(
            "QComboBox { border: 2px solid white; border-radius: 10px; background-color: white; }"
            "QComboBox::down-arrow { image: url(:/down_arrow.png); }"
            "QComboBox::drop-down { subcontrol-origin: padding; subcontrol-position: center right; width: 20px; border-left-width: 0px; border-radius: 10px; }"
            "QComboBox::drop-down:hover { background-color: lightgray; }"
            "QComboBox::item { color: black; font-family: SimSun; }")  # 设置下拉框样式和文本样式
        self.populateComboBox()  # Populate combo box with available model files
        self.comboBox.setFixedSize(200, 30)
        self.comboBox.currentIndexChanged.connect(self.selectionChanged)
        pt_layout.addWidget(self.comboBox)
        # 创建一个水平布局来容纳标准IOU值范围和可调整数值
        iou_layout = QHBoxLayout()

        # 添加标准IOU值范围标签
        iou_label = QLabel("标准(IOU):")
        iou_label.setStyleSheet("QLabel { color: white; }")
        iou_layout.addWidget(iou_label)

        # 添加滑动块
        self.iou_slider = QSlider(Qt.Horizontal)
        self.iou_slider.setMinimum(0)
        self.iou_slider.setMaximum(100)
        self.iou_slider.setTickInterval(1)
        self.iou_slider.setTickPosition(QSlider.TicksBelow)
        self.iou_slider.valueChanged.connect(self.iouValueChanged)
        iou_layout.addWidget(self.iou_slider)

        # 添加可调整数值输入框
        self.iou_spinbox = QDoubleSpinBox()
        self.iou_spinbox.setDecimals(2)
        self.iou_spinbox.setRange(0.0, 1.0)
        self.iou_spinbox.setSingleStep(0.01)
        self.iou_spinbox.valueChanged.connect(self.iouSpinBoxValueChanged)
        iou_layout.addWidget(self.iou_spinbox)

        # 将文本和下拉框添加到大边框布局中
        group_layout.addWidget(label)
        group_layout.addLayout(pt_layout)

        # 将水平布局添加到大边框布局中
        group_layout.addLayout(iou_layout)

        # 在大边框布局中添加 conf 滑块和标签
        conf_layout = QHBoxLayout()

        # 添加标签
        conf_label = QLabel("配置(conf):")
        conf_label.setStyleSheet("QLabel { color: white; }")
        conf_layout.addWidget(conf_label)

        # 添加滑动块
        self.conf_slider = QSlider(Qt.Horizontal)
        self.conf_slider.setMinimum(0)
        self.conf_slider.setMaximum(100)
        self.conf_slider.setTickInterval(1)
        self.conf_slider.setTickPosition(QSlider.TicksBelow)
        self.conf_slider.valueChanged.connect(self.confValueChanged)
        conf_layout.addWidget(self.conf_slider)

        # 添加可调整数值输入框
        self.conf_spinbox = QDoubleSpinBox()
        self.conf_spinbox.setDecimals(2)
        self.conf_spinbox.setRange(0.0, 1.0)
        self.conf_spinbox.setSingleStep(0.01)
        self.conf_spinbox.valueChanged.connect(self.confSpinBoxValueChanged)
        conf_layout.addWidget(self.conf_spinbox)

        # 将 conf 布局添加到大边框布局中
        group_layout.addLayout(conf_layout)

        # 在大边框布局中添加延时滑块和标签
        delay_layout = QHBoxLayout()

        # 添加标签
        delay_label = QLabel("延时(ms):")
        delay_label.setStyleSheet("QLabel { color: white; }")
        delay_layout.addWidget(delay_label)

        # 添加滑动块
        self.delay_slider = QSlider(Qt.Horizontal)
        self.delay_slider.setMinimum(1)  # 最小值为1，因为您要求默认值是10
        self.delay_slider.setMaximum(100)
        self.delay_slider.setTickInterval(1)

        self.delay_slider.setTickPosition(QSlider.TicksBelow)
        self.delay_slider.valueChanged.connect(self.delayValueChanged)
        delay_layout.addWidget(self.delay_slider)

        # 添加可调整数值输入框
        self.delay_spinbox = QDoubleSpinBox()
        self.delay_spinbox.setDecimals(0)  # 延时应该是整数，不需要小数点
        self.delay_spinbox.setRange(1, 100)
        self.delay_spinbox.setSingleStep(1)  # 步长为1

        # 配置输入框的默认步长为0.01
        self.delay_spinbox.setSingleStep(1)  # 步长为0.01

        # 配置输入框的上下箭头按一次是跳0.01
        self.delay_spinbox.setAccelerated(True)

        self.delay_spinbox.valueChanged.connect(self.delaySpinBoxValueChanged)
        delay_layout.addWidget(self.delay_spinbox)

        # 将延时布局添加到大边框布局中
        group_layout.addLayout(delay_layout)

        # 在大边框布局中添加保存格式复选框的布局
        self.save_format_layout = QHBoxLayout()
        self.save_format_label = QLabel("保存格式:")
        self.save_format_label.setStyleSheet("QLabel { color: white; }")
        self.save_format_layout.addWidget(self.save_format_label)

        # 复选框：是否保存为 mp4/jpg
        self.save_mp4_jpg_checkbox = QCheckBox("MP4/JPG")
        self.save_mp4_jpg_checkbox.setStyleSheet("QCheckBox { color: white; }")
        self.save_mp4_jpg_checkbox.stateChanged.connect(self.onSaveMp4JpgChanged)
        self.save_format_layout.addWidget(self.save_mp4_jpg_checkbox)

        # 复选框：是否保存 labels (.txt)
        self.save_labels_checkbox = QCheckBox("Labels (.txt)")
        self.save_labels_checkbox.setStyleSheet("QCheckBox { color: white; }")
        self.save_labels_checkbox.stateChanged.connect(self.onSaveLabelsChanged)
        self.save_format_layout.addWidget(self.save_labels_checkbox)

        group_layout.addLayout(self.save_format_layout)
        group_box.setLayout(group_layout)

        # 将大边框添加到主布局中
        layout.addWidget(group_box)

        self.setLayout(layout)
        self.setWindowTitle("Model Selection Demo")
        self.show()

    def populateComboBox(self):
        model_dir = "data/models"  # Directory containing model files
        model_files = os.listdir(model_dir)
        for file_name in model_files:
            if file_name.endswith(".pt"):  # Filter out only .pt files
                self.comboBox.addItem(file_name)

    def selectionChanged(self, index):
        selected_model = self.comboBox.currentText()
        print("Selected model:", selected_model)
        # Add your code here to load and use the selected model file

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


if __name__ == "__main__":
    app = QApplication([])
    demo = SelectionModelDemo()
    app.exec()
