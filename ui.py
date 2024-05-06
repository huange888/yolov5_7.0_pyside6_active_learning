# ui.py

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QComboBox, QVBoxLayout, QWidget, QGroupBox, QLabel, QSlider, QDoubleSpinBox, QHBoxLayout
from PySide6.QtWidgets import QPushButton, QLineEdit, \
    QTextEdit, QFrame, QCheckBox


class UiMainWindow:

    def setupUi(self, main_window):
        central_widget = QWidget(main_window)
        main_window.setCentralWidget(central_widget)

        # 创建水平布局
        main_layout = QHBoxLayout(central_widget)
        # 创建菜单布局
        # 创建一个QFrame作为按钮的容器，并设置渐变色背景
        """  background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
            stop:0 #DAD299,
            stop:1 #B0DAB9);"""
        self.menu_frame = QFrame()
        self.menu_frame.setFixedSize(230, 450)
        self.menu_frame.setStyleSheet("""
            background-color: ;
            background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
            stop:0 #DAD299,
            stop:1 #B0DAB9);
            border: 2px solid white;
             border-radius: 20px;
            """)

        # 创建图像左侧布局
        left_layout = QVBoxLayout()
        # background-color: #FFFFE0; /* 设置背景颜色为淡黄色 */
        """ background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
            stop:0 #EDE574,
            stop:1 #E1F5C4);"""
        self.left_frame = QLabel()
        self.left_frame.setFixedSize(550, 550)
        self.left_frame.setStyleSheet("""
            QLabel {
                background-color: #FFFFE0; /* 设置背景颜色为淡黄色 */
                border: 1px solid white; /* 设置边框颜色为黑色 */
                border-radius : 5px;
            }
        """)

        # 创建图像右侧布局
        right_layout = QVBoxLayout()
        self.right_frame = QLabel()
        self.right_frame.setFixedSize(550, 550)
        self.right_frame.setStyleSheet(("""
            QLabel {
            background-color: #FFFFE0; /* 设置背景颜色为淡黄色 */
                border: 1px solid white; /* 设置边框颜色为黑色 */
                                border-radius : 5px;

            }
        """))

        # 创建文本框
        self.textbox = QTextEdit("运行结果将显示在这里")
        self.textbox.setFixedSize(1100, 150)
        self.textbox.setReadOnly(True)  # 设置文本框为只读

        # 设置文本框的CSS样式
        self.textbox.setStyleSheet("""
            QTextEdit {
                background-color: white; /* 浅蓝色 */
                border: 1px solid white; /* 设置边框颜色为白色 */
                border-radius: 10px; /* 设置边框圆角 */
                padding: 5px; /* 添加内边距 */
                font-size: 16px; /* 设置字体大小 */
                color : gray
            }
        """)

        # 创建导出图片地址输入框
        # background-color: rgb(204,225,227); /* 设置背景颜色为浅青色 */
        """ background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                stop:0 #076585,
                stop:1 #fff);"""
        self.address_line = QLineEdit()
        self.address_line.setPlaceholderText("请输入导出检测结果的地址")
        self.address_line.setFixedSize(950, 50)
        self.address_line.setStyleSheet("""
            QLineEdit {
               background-color: rgb(204,225,227); /* 设置背景颜色为浅青色 */
                border: 1px solid white; /* 设置边框颜色为白色 */
                border-radius: 10px; /* 设置边框圆角 */
                padding: 5px; /* 可以添加一些内边距 */
                color: black; /* 输入文本的颜色 */
                font-size: 16px; /* 设置字体大小 */
            }
        """)

        # 创建导出按钮
        self.export_image_button = QPushButton("导出图片")
        self.export_image_button.setFixedSize(150, 40)
        self.export_image_button.setStyleSheet(u"QPushButton{\n"
                                               "background-repeat: no-repeat;\n"
                                               "background-position: left center;\n"
                                               "background-color:   rgba(200, 100, 214, 100);\n"
                                               " border: 2px solid white; border-radius: 20px;\n"
                                               "text-align: center;\n"
                                               "padding-left: 0px;\n"
                                               "color: white;\n"
                                               "font: 700 12pt \"Nirmala UI\";\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton:hover{\n"
                                               "background-color: rgba(150, 140, 214, 199);\n"
                                               "}\n"
                                               )

        ## 创建按钮
        # 开始检测按钮
        self.start_button = QPushButton("开始检测")
        self.start_button.setFixedSize(200, 40)  # 设置按钮的大小
        self.start_button.setStyleSheet(u"QPushButton{\n"
                                        "background-repeat: no-repeat;\n"
                                        "background-position: left center;\n"
                                        "background-color:  rgba(200, 100, 214, 100);\n"
                                        "border: 1px black solid;\n"
                                        "text-align: center;\n"
                                        "padding-left: 0px;\n"
                                        "font: 700 12pt \"Nirmala UI\";\n"
                                        "color: white;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover{\n"
                                        "background-color: rgba(150, 140, 214, 199);\n"
                                        "}\n"
                                        )

        # 上传图片按钮
        self.upload_image_button = QPushButton("上传图片")
        self.upload_image_button.setFixedSize(200, 40)
        self.upload_image_button.setStyleSheet(u"QPushButton{\n"
                                               "background-repeat: no-repeat;\n"
                                               "background-position: left center;\n"
                                               "background-color:  rgba(200, 100, 214, 100);\n"
                                               "border: 1px black solid;\n"
                                               "text-align: center;\n"
                                               "padding-left: 0px;\n"
                                               "font: 700 12pt \"Nirmala UI\";\n"
                                               "color: white;\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton:hover{\n"
                                               "background-color: rgba(150, 140, 214, 199);\n"
                                               "}\n"
                                               )

        # 选择模型按钮
        self.upload_pt_button = QPushButton("上传模型")
        self.upload_pt_button.setFixedSize(200, 40)
        self.upload_pt_button.setStyleSheet(u"QPushButton{\n"
                                            "background-repeat: no-repeat;\n"
                                            "background-position: left center;\n"
                                            "background-color:  rgba(200, 100, 214, 100);\n"
                                            "border: 1px black solid;\n"
                                            "text-align: center;\n"
                                            "padding-left: 0px;\n"
                                            "font: 700 12pt \"Nirmala UI\";\n"
                                            "color: white;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:hover{\n"
                                            "background-color: rgba(150, 140, 214, 199);\n"
                                            "}\n"
                                            )

        # 运行AnyLabeling按钮
        self.Labelrun_button = QPushButton("运行label")
        self.Labelrun_button.setFixedSize(200, 40)
        self.Labelrun_button.setStyleSheet(u"QPushButton{\n"
                                           "background-repeat: no-repeat;\n"
                                           "background-position: left center;\n"
                                           "background-color:  rgba(200, 100, 214, 100);\n"
                                           "border: 1px black solid;\n"
                                           "text-align: center;\n"
                                           "padding-left: 0px;\n"
                                           "font: 700 12pt \"Nirmala UI\";\n"
                                           "color: white;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:hover{\n"
                                           "background-color: rgba(150, 140, 214, 199);\n"
                                           "}\n"
                                           )

        # 运行ActiveLearnRun按钮
        self.activeRun_button = QPushButton("运行run")
        self.activeRun_button.setFixedSize(200, 40)
        self.activeRun_button.setStyleSheet(u"QPushButton{\n"
                                            "background-repeat: no-repeat;\n"
                                            "background-position: left center;\n"
                                            "background-color:  rgba(200, 100, 214, 100);\n"
                                            "border: 1px black solid;\n"
                                            "text-align: center;\n"
                                            "padding-left: 0px;\n"
                                            "font: 700 12pt \"Nirmala UI\";\n"
                                            "color: white;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:hover{\n"
                                            "background-color: rgba(150, 140, 214, 199);\n"
                                            "}\n"
                                            )

        # 运行ActiveLearnTrain按钮
        self.activeTrain_button = QPushButton("运行train")
        self.activeTrain_button.setFixedSize(200, 40)
        self.activeTrain_button.setStyleSheet(u"QPushButton{\n"
                                              "background-repeat: no-repeat;\n"
                                              "background-position: left center;\n"
                                              "background-color:  rgba(200, 100, 214, 100);\n"
                                              "border: 1px black solid;\n"
                                              "text-align: center;\n"
                                              "padding-left: 0px;\n"
                                              "font: 700 12pt \"Nirmala UI\";\n"
                                              "color: white;\n"
                                              "}\n"
                                              "\n"
                                              "QPushButton:hover{\n"
                                              "background-color: rgba(150, 140, 214, 199);\n"
                                              "}\n"
                                              )

        # export格式转换按钮
        self.export_button = QPushButton("运行export")
        self.export_button.setFixedSize(200, 40)
        self.export_button.setStyleSheet(u"QPushButton{\n"
                                         "background-repeat: no-repeat;\n"
                                         "background-position: left center;\n"
                                         "background-color:  rgba(200, 100, 214, 100);\n"
                                         "border: 1px black solid;\n"
                                         "text-align: center;\n"
                                         "padding-left: 0px;\n"
                                         "font: 700 12pt \"Nirmala UI\";\n"
                                         "color: white;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover{\n"
                                         "background-color: rgba(150, 140, 214, 199);\n"
                                         "}\n"
                                         )

        # 停止进程按钮
        self.stop_button = QPushButton("停止进程")
        self.stop_button.setFixedSize(200, 40)
        self.stop_button.setStyleSheet(u"QPushButton{\n"
                                       "background-repeat: no-repeat;\n"
                                       "background-position: left center;\n"
                                       "background-color:  rgba(200, 100, 214, 100);\n"
                                       "border: 1px black solid;\n"
                                       "text-align: center;\n"
                                       "padding-left: 0px;\n"
                                       "font: 700 12pt \"Nirmala UI\";\n"
                                       "color: white;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover{\n"
                                       "background-color: rgba(150, 140, 214, 199);\n"
                                       "}\n"
                                       )

        # 关闭按钮
        self.close_button = QPushButton("关闭应用")
        self.close_button.setFixedSize(200, 40)
        self.close_button.setStyleSheet(u"QPushButton{\n"
                                        "background-repeat: no-repeat;\n"
                                        "background-position: left center;\n"
                                        "background-color:  rgba(200, 100, 214, 100);\n"
                                        "border: 1px black solid;\n"
                                        "text-align: center;\n"
                                        "padding-left: 0px;\n"
                                        "font: 700 12pt \"Nirmala UI\";\n"
                                        "color: white;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover{\n"
                                        "background-color: rgba(150, 140, 214, 199);\n"
                                        "}\n"
                                        )

        # 创建垂直按钮布局
        button_layout = QVBoxLayout()
        button_layout.setSpacing(9)  # 设置布局中部件之间的间距为 5 像素
        button_layout.addWidget(self.start_button)
        button_layout.addWidget(self.upload_image_button)
        button_layout.addWidget(self.upload_pt_button)
        button_layout.addWidget(self.Labelrun_button)
        button_layout.addWidget(self.activeRun_button)
        button_layout.addWidget(self.activeTrain_button)
        button_layout.addWidget(self.export_button)
        button_layout.addWidget(self.stop_button)
        button_layout.addWidget(self.close_button)
        button_layout.addStretch(5)  # 添加伸缩项，将按钮推到顶部

        setting_layout = QVBoxLayout()

        """ "qlineargradient(x1:0, y1:0, x2:1, y2:1, "
            "stop:0 #FFB6C1,"
            " stop:1 #FF69B4);"""  # 线性粉色渐变 #青色rgb(0,126,126)
        # rgb(204,225,227) 浅青色
        """"background: qlineargradient(x1:0, y1:0, x2:1, y2:1, "
            "stop:0 #76b852,"
            "stop:1 #8DC26F);"""
        # 创建一个大边框
        group_box = QGroupBox()
        group_box.setFixedSize(230, 310)
        group_box.setStyleSheet(
            "QGroupBox {"
            " border: 2px solid white; "
            "border-radius: 20px;"
            " background-color: ;"
            "background: qlineargradient(x1:0, y1:0, x2:1, y2:1, "
            "stop:0 #76b852,"
            "stop:1 #8DC26F);}")
        group_layout = QVBoxLayout()

        # 在大边框中添加一个QLabel来显示文本
        label = QLabel("设置参数")
        label.setAlignment(Qt.AlignCenter)  # 文本居中对齐
        label.setFixedSize(200, 30)
        label.setStyleSheet("QLabel { color: white; font : 20px }")

        pt_layout = QHBoxLayout()  # pt模型 水平布局

        # 添加标准IOU值范围标签
        pt_label = QLabel("选择模型:")
        pt_label.setStyleSheet("QLabel { color: white; }")
        pt_layout.addWidget(pt_label)
        self.comboBox = QComboBox()
        self.comboBox.setStyleSheet(
            "QComboBox { border: 2px solid white; border-radius: 10px; background-color: white; }"
            "QComboBox::down-arrow { image: url(:/box_down.png); }"
            "QComboBox::drop-down { subcontrol-origin: padding; subcontrol-position: center right; width: 20px; border-left-width: 0px; border-radius: 10px; }"
            "QComboBox::drop-down:hover { background-color: lightgray; }"
            "QComboBox::item { color: black; font-family: SimSun; }")  # 设置下拉框样式和文本样式
        self.comboBox.setFixedSize(150, 30)
        pt_layout.addWidget(self.comboBox)
        # 创建一个水平布局来容纳标准IOU值范围和可调整数值
        iou_layout = QHBoxLayout()

        # 添加标准IOU值范围标签
        iou_label = QLabel("标准(iou):")
        iou_label.setStyleSheet("QLabel { color: white; }")
        iou_layout.addWidget(iou_label)

        # 添加滑动块
        self.iou_slider = QSlider(Qt.Horizontal)
        self.iou_slider.setMinimum(0)
        self.iou_slider.setMaximum(100)
        self.iou_slider.setTickInterval(1)
        iou_layout.addWidget(self.iou_slider)

        # 添加可调整数值输入框
        self.iou_spinbox = QDoubleSpinBox()
        self.iou_spinbox.setDecimals(2)
        self.iou_spinbox.setRange(0.0, 1.0)
        self.iou_spinbox.setSingleStep(0.01)  # 设置步长为0.01
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
        conf_layout.addWidget(self.conf_slider)

        # 添加可调整数值输入框
        self.conf_spinbox = QDoubleSpinBox()
        self.conf_spinbox.setDecimals(2)
        self.conf_spinbox.setRange(0.0, 1.0)
        self.conf_spinbox.setSingleStep(0.01)  # 设置步长为0.01
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

        delay_layout.addWidget(self.delay_spinbox)
        # 设置默认值
        self.iou_spinbox.setValue(0.45)
        self.conf_spinbox.setValue(0.25)
        self.delay_spinbox.setValue(10)  # 默认值设置为10

        # 设置组件数值
        self.iou_spinbox.setValue(0.45)
        self.conf_spinbox.setValue(0.25)
        self.delay_spinbox.setValue(10)  # 默认值设置为10

        self.iou_slider.setValue(45)
        self.conf_slider.setValue(25)
        self.delay_slider.setValue(10)

        # 将延时布局添加到大边框布局中
        group_layout.addLayout(delay_layout)
        group_box.setLayout(group_layout)

        # 将大边框添加到主布局中
        setting_layout.addWidget(group_box)
        # 在大边框布局中添加保存格式复选框的布局
        self.save_format_layout = QHBoxLayout()
        self.save_format_label = QLabel("保存格式:")
        self.save_format_label.setStyleSheet("QLabel { color: white; }")
        self.save_format_layout.addWidget(self.save_format_label)

        # 复选框：是否保存为 mp4/jpg
        self.save_mp4_jpg_checkbox = QCheckBox("MP4/JPG")
        self.save_mp4_jpg_checkbox.setStyleSheet("QCheckBox { color: white; }")
        self.save_format_layout.addWidget(self.save_mp4_jpg_checkbox)
        self.save_mp4_jpg_checkbox.setCheckState(Qt.CheckState.Checked)

        # 复选框：是否保存 labels (.txt)
        self.save_labels_checkbox = QCheckBox("Labels")
        self.save_labels_checkbox.setStyleSheet("QCheckBox { color: white; }")
        self.save_format_layout.addWidget(self.save_labels_checkbox)
        self.save_labels_checkbox.setCheckState(Qt.CheckState.Unchecked)

        # 在大边框布局中添加运行后删除文件复选框的布局
        self.delete_after_run_layout = QHBoxLayout()
        self.delete_after_run_label = QLabel("清空日志/图片/标记:")
        self.delete_after_run_label.setStyleSheet("QLabel { color: white; }")
        self.delete_after_run_layout.addWidget(self.delete_after_run_label)

        # 复选框: 是否删除所有内容
        self.delete_content_checkbox = QCheckBox("是/否")
        self.delete_content_checkbox.setStyleSheet("QCheckBox { color: white; }")
        self.delete_after_run_layout.addWidget(self.delete_content_checkbox)
        self.delete_content_checkbox.setCheckState(Qt.CheckState.Unchecked)

        group_layout.addLayout(self.save_format_layout)
        group_layout.addLayout(self.delete_after_run_layout)
        group_box.setLayout(group_layout)

        # 将button_layout添加到self.left_frame中
        self.menu_frame.setLayout(button_layout)

        # 将self.left_frame添加到left_layout中
        left_layout.addWidget(self.menu_frame)
        left_layout.addLayout(setting_layout)

        # 添加组件到右侧布局
        address_line_layout = QHBoxLayout()
        address_line_layout.addWidget(self.address_line)
        address_line_layout.addWidget(self.export_image_button)

        # 添加命令行输入框到右侧布局
        frames_layout = QHBoxLayout()  # H是水平布局，V是垂直布局
        frames_layout.addWidget(self.left_frame)
        frames_layout.addWidget(self.right_frame)

        # 右侧布局
        right_layout.addLayout(address_line_layout)
        right_layout.addLayout(frames_layout)
        right_layout.addWidget(self.textbox)

        # 添加布局到主布局
        main_layout.addLayout(left_layout, 1)
        main_layout.addLayout(right_layout, 2)

        # 设置窗口标题和大小
        main_window.setWindowTitle("YOLOv5 目标检测")
        main_window.setGeometry(500, 500, 1100, 500)

        return main_window
