# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from views.widgets.widget_view import Widget
from views.frame_view import AutomaticMovements

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(832, 672)
        MainWindow.setMinimumSize(QSize(832, 672))
        MainWindow.setMaximumSize(QSize(832, 672))
        MainWindow.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.actionOpen_Star_File = QAction(MainWindow)
        self.actionOpen_Star_File.setObjectName(u"actionOpen_Star_File")
        icon = QIcon()
        icon.addFile(u":/icons/icons/constellation.png", QSize(), QIcon.Normal, QIcon.On)
        self.actionOpen_Star_File.setIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget_4 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(10, 160, 451, 101))
        self.verticalLayout_8 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.verticalLayoutWidget_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_7)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self._roll_label = QLabel(self.verticalLayoutWidget_4)
        self._roll_label.setObjectName(u"_roll_label")
        self._roll_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self._roll_label)

        self._roll_spin = QDoubleSpinBox(self.verticalLayoutWidget_4)
        self._roll_spin.setObjectName(u"_roll_spin")
        self._roll_spin.setAlignment(Qt.AlignCenter)
        self._roll_spin.setKeyboardTracking(False)
        self._roll_spin.setMaximum(360.000000000000000)

        self.verticalLayout_6.addWidget(self._roll_spin)

        self._roll_scroll = QScrollBar(self.verticalLayoutWidget_4)
        self._roll_scroll.setObjectName(u"_roll_scroll")
        self._roll_scroll.setAutoFillBackground(False)
        self._roll_scroll.setMaximum(360)
        self._roll_scroll.setOrientation(Qt.Horizontal)

        self.verticalLayout_6.addWidget(self._roll_scroll)


        self.horizontalLayout_4.addLayout(self.verticalLayout_6)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self._ar_label = QLabel(self.verticalLayoutWidget_4)
        self._ar_label.setObjectName(u"_ar_label")
        self._ar_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self._ar_label)

        self._ar_spin = QDoubleSpinBox(self.verticalLayoutWidget_4)
        self._ar_spin.setObjectName(u"_ar_spin")
        self._ar_spin.setAlignment(Qt.AlignCenter)
        self._ar_spin.setKeyboardTracking(False)
        self._ar_spin.setMaximum(360.000000000000000)

        self.verticalLayout_9.addWidget(self._ar_spin)

        self._ar_scroll = QScrollBar(self.verticalLayoutWidget_4)
        self._ar_scroll.setObjectName(u"_ar_scroll")
        self._ar_scroll.setMaximum(360)
        self._ar_scroll.setOrientation(Qt.Horizontal)

        self.verticalLayout_9.addWidget(self._ar_scroll)


        self.horizontalLayout_4.addLayout(self.verticalLayout_9)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self._dec_label = QLabel(self.verticalLayoutWidget_4)
        self._dec_label.setObjectName(u"_dec_label")
        self._dec_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self._dec_label)

        self._dec_spin = QDoubleSpinBox(self.verticalLayoutWidget_4)
        self._dec_spin.setObjectName(u"_dec_spin")
        self._dec_spin.setEnabled(True)
        self._dec_spin.setAlignment(Qt.AlignCenter)
        self._dec_spin.setKeyboardTracking(False)
        self._dec_spin.setMaximum(180.000000000000000)

        self.verticalLayout_7.addWidget(self._dec_spin)

        self._dec_scroll = QScrollBar(self.verticalLayoutWidget_4)
        self._dec_scroll.setObjectName(u"_dec_scroll")
        self._dec_scroll.setOrientation(Qt.Horizontal)

        self.verticalLayout_7.addWidget(self._dec_scroll)


        self.horizontalLayout_4.addLayout(self.verticalLayout_7)


        self.verticalLayout_8.addLayout(self.horizontalLayout_4)

        self.viewPlot = Widget(self.centralwidget)
        self.viewPlot.setObjectName(u"viewPlot")
        self.viewPlot.setGeometry(QRect(0, 268, 701, 401))
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 831, 161))
        self.tabWidget.setCursor(QCursor(Qt.ArrowCursor))
        self.tabWidget.setMovable(True)
        self.File = QWidget()
        self.File.setObjectName(u"File")
        self.File.setEnabled(True)
        self.File.setCursor(QCursor(Qt.PointingHandCursor))
        self.horizontalLayoutWidget = QWidget(self.File)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 570, 124))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self._load_stars_file = QPushButton(self.horizontalLayoutWidget)
        self._load_stars_file.setObjectName(u"_load_stars_file")
        icon1 = QIcon()
        icon1.addFile(u":/icon/icons/Artboard 1.png", QSize(), QIcon.Normal, QIcon.Off)
        self._load_stars_file.setIcon(icon1)
        self._load_stars_file.setIconSize(QSize(64, 64))
        self._load_stars_file.setFlat(True)

        self.verticalLayout.addWidget(self._load_stars_file)

        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setTextFormat(Qt.AutoText)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.line = QFrame(self.horizontalLayoutWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self._load_movements_file = QPushButton(self.horizontalLayoutWidget)
        self._load_movements_file.setObjectName(u"_load_movements_file")
        icon2 = QIcon()
        icon2.addFile(u":/icon/icons/Artboard 2.png", QSize(), QIcon.Normal, QIcon.Off)
        self._load_movements_file.setIcon(icon2)
        self._load_movements_file.setIconSize(QSize(64, 64))
        self._load_movements_file.setFlat(True)

        self.verticalLayout_2.addWidget(self._load_movements_file)

        self.label_2 = QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.line_2 = QFrame(self.horizontalLayoutWidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self._load_camera_file = QPushButton(self.horizontalLayoutWidget)
        self._load_camera_file.setObjectName(u"_load_camera_file")
        icon3 = QIcon()
        icon3.addFile(u":/icon/icons/Artboard 3.png", QSize(), QIcon.Normal, QIcon.Off)
        self._load_camera_file.setIcon(icon3)
        self._load_camera_file.setIconSize(QSize(64, 64))
        self._load_camera_file.setFlat(True)

        self.verticalLayout_3.addWidget(self._load_camera_file)

        self.label_3 = QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_3)


        self.horizontalLayout.addLayout(self.verticalLayout_3)


        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.label_4 = QLabel(self.horizontalLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_4)


        self.horizontalLayout_3.addLayout(self.verticalLayout_5)

        self.line_3 = QFrame(self.horizontalLayoutWidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line_3)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self._create_stars_file = QPushButton(self.horizontalLayoutWidget)
        self._create_stars_file.setObjectName(u"_create_stars_file")
        self._create_stars_file.setIcon(icon1)
        self._create_stars_file.setIconSize(QSize(64, 64))
        self._create_stars_file.setFlat(True)

        self.verticalLayout_15.addWidget(self._create_stars_file)

        self.label_8 = QLabel(self.horizontalLayoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setTextFormat(Qt.AutoText)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_8)


        self.horizontalLayout_8.addLayout(self.verticalLayout_15)

        self.line_5 = QFrame(self.horizontalLayoutWidget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_8.addWidget(self.line_5)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self._create_movements_file = QPushButton(self.horizontalLayoutWidget)
        self._create_movements_file.setObjectName(u"_create_movements_file")
        self._create_movements_file.setIcon(icon2)
        self._create_movements_file.setIconSize(QSize(64, 64))
        self._create_movements_file.setFlat(True)

        self.verticalLayout_16.addWidget(self._create_movements_file)

        self.label_10 = QLabel(self.horizontalLayoutWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_10)


        self.horizontalLayout_8.addLayout(self.verticalLayout_16)

        self.line_7 = QFrame(self.horizontalLayoutWidget)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.VLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_8.addWidget(self.line_7)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self._create_camera_file = QPushButton(self.horizontalLayoutWidget)
        self._create_camera_file.setObjectName(u"_create_camera_file")
        self._create_camera_file.setIcon(icon3)
        self._create_camera_file.setIconSize(QSize(64, 64))
        self._create_camera_file.setFlat(True)

        self.verticalLayout_17.addWidget(self._create_camera_file)

        self.label_11 = QLabel(self.horizontalLayoutWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_11)


        self.horizontalLayout_8.addLayout(self.verticalLayout_17)


        self.verticalLayout_13.addLayout(self.horizontalLayout_8)

        self.label_12 = QLabel(self.horizontalLayoutWidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_12)


        self.horizontalLayout_3.addLayout(self.verticalLayout_13)

        self.line_8 = QFrame(self.horizontalLayoutWidget)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.VLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line_8)

        self.tabWidget.addTab(self.File, "")
        self.Help = QWidget()
        self.Help.setObjectName(u"Help")
        self.horizontalLayoutWidget_2 = QWidget(self.Help)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(0, 0, 283, 101))
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self._about_button = QPushButton(self.horizontalLayoutWidget_2)
        self._about_button.setObjectName(u"_about_button")
        icon4 = QIcon()
        icon4.addFile(u":/icon/icons/info.png", QSize(), QIcon.Normal, QIcon.Off)
        self._about_button.setIcon(icon4)
        self._about_button.setIconSize(QSize(64, 64))
        self._about_button.setFlat(True)

        self.verticalLayout_12.addWidget(self._about_button)

        self.label_6 = QLabel(self.horizontalLayoutWidget_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setTextFormat(Qt.AutoText)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_6)


        self.horizontalLayout_6.addLayout(self.verticalLayout_12)

        self.line_4 = QFrame(self.horizontalLayoutWidget_2)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_6.addWidget(self.line_4)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self._source_button = QPushButton(self.horizontalLayoutWidget_2)
        self._source_button.setObjectName(u"_source_button")
        icon5 = QIcon()
        icon5.addFile(u":/icon/icons/github.png", QSize(), QIcon.Normal, QIcon.Off)
        self._source_button.setIcon(icon5)
        self._source_button.setIconSize(QSize(64, 64))
        self._source_button.setFlat(True)

        self.verticalLayout_14.addWidget(self._source_button)

        self.label_9 = QLabel(self.horizontalLayoutWidget_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_9)


        self.horizontalLayout_6.addLayout(self.verticalLayout_14)


        self.verticalLayout_11.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_5.addLayout(self.verticalLayout_11)

        self.line_6 = QFrame(self.horizontalLayoutWidget_2)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.VLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_5.addWidget(self.line_6)

        self.tabWidget.addTab(self.Help, "")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(700, 270, 137, 190))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.view3D_text = QPushButton(self.layoutWidget)
        self.view3D_text.setObjectName(u"view3D_text")
        self.view3D_text.setCheckable(True)
        self.view3D_text.setFlat(True)

        self.verticalLayout_4.addWidget(self.view3D_text)

        self.view3D_icon = QPushButton(self.layoutWidget)
        self.view3D_icon.setObjectName(u"view3D_icon")
        self.view3D_icon.setLayoutDirection(Qt.LeftToRight)
        self.view3D_icon.setText(u"")
        icon6 = QIcon()
        icon6.addFile(u":/icon/icons/axis.png", QSize(), QIcon.Normal, QIcon.Off)
        icon6.addFile(u":/icon/icons/3d.png", QSize(), QIcon.Normal, QIcon.On)
        self.view3D_icon.setIcon(icon6)
        self.view3D_icon.setIconSize(QSize(64, 64))
        self.view3D_icon.setCheckable(True)
        self.view3D_icon.setChecked(False)
        self.view3D_icon.setAutoDefault(False)
        self.view3D_icon.setFlat(True)

        self.verticalLayout_4.addWidget(self.view3D_icon)

        self._camera_view = QCheckBox(self.layoutWidget)
        self._camera_view.setObjectName(u"_camera_view")

        self.verticalLayout_4.addWidget(self._camera_view)

        self._graticule_control = QCheckBox(self.layoutWidget)
        self._graticule_control.setObjectName(u"_graticule_control")

        self.verticalLayout_4.addWidget(self._graticule_control)

        self.checkBox_3 = QCheckBox(self.layoutWidget)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.verticalLayout_4.addWidget(self.checkBox_3)

        self._automatic_control_frame = AutomaticMovements(self.centralwidget)
        self._automatic_control_frame.setObjectName(u"_automatic_control_frame")
        self._automatic_control_frame.setGeometry(QRect(460, 160, 371, 81))
        self._automatic_control_frame.setFrameShape(QFrame.StyledPanel)
        self._automatic_control_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayoutWidget = QWidget(self._automatic_control_frame)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 371, 80))
        self.verticalLayout_10 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_5 = QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 22))
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_5)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self._file = QLabel(self.verticalLayoutWidget)
        self._file.setObjectName(u"_file")

        self.horizontalLayout_2.addWidget(self._file)

        self._play_button = QPushButton(self.verticalLayoutWidget)
        self._play_button.setObjectName(u"_play_button")
        self._play_button.setText(u"")
        icon7 = QIcon()
        icon7.addFile(u":/icon/icons/botao-play.png", QSize(), QIcon.Normal, QIcon.Off)
        icon7.addFile(u":/icon/icons/botao-play.png", QSize(), QIcon.Normal, QIcon.On)
        icon7.addFile(u":/icon/icons/stop.png", QSize(), QIcon.Active, QIcon.Off)
        icon7.addFile(u":/icon/icons/botao-play.png", QSize(), QIcon.Active, QIcon.On)
        self._play_button.setIcon(icon7)
        self._play_button.setIconSize(QSize(24, 24))
        self._play_button.setCheckable(True)
        self._play_button.setChecked(False)
        self._play_button.setFlat(True)

        self.horizontalLayout_2.addWidget(self._play_button)

        self._movement_play_progress_bar = QProgressBar(self.verticalLayoutWidget)
        self._movement_play_progress_bar.setObjectName(u"_movement_play_progress_bar")
        self._movement_play_progress_bar.setMaximumSize(QSize(200, 16777215))
        self._movement_play_progress_bar.setValue(24)

        self.horizontalLayout_2.addWidget(self._movement_play_progress_bar)


        self.verticalLayout_10.addLayout(self.horizontalLayout_2)

        self.horizontalLayoutWidget_3 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(460, 240, 371, 31))
        self.horizontalLayout_7 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.horizontalLayoutWidget_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(80, 16777215))
        self.label_13.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_13)

        self._camera_file = QLabel(self.horizontalLayoutWidget_3)
        self._camera_file.setObjectName(u"_camera_file")

        self.horizontalLayout_7.addWidget(self._camera_file)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionOpen_Star_File.setText(QCoreApplication.translate("MainWindow", u"Open Star File", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Manual Control", None))
        self._roll_label.setText(QCoreApplication.translate("MainWindow", u"Roll", None))
        self._ar_label.setText(QCoreApplication.translate("MainWindow", u"Ar", None))
        self._dec_label.setText(QCoreApplication.translate("MainWindow", u"Dec", None))
        self._load_stars_file.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Stars", None))
        self._load_movements_file.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Movements", None))
        self._load_camera_file.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Camera", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Load File", None))
        self._create_stars_file.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Stars", None))
        self._create_movements_file.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Movements", None))
        self._create_camera_file.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Camera", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Create File", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.File), QCoreApplication.translate("MainWindow", u"Files", None))
        self._about_button.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self._source_button.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Source", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Help), QCoreApplication.translate("MainWindow", u"Help", None))
        self.view3D_text.setText(QCoreApplication.translate("MainWindow", u"View Mode", None))
        self._camera_view.setText(QCoreApplication.translate("MainWindow", u"Camera View", None))
        self._graticule_control.setText(QCoreApplication.translate("MainWindow", u"Graticule", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"View Simulation", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Automatic Control ", None))
        self._file.setText(QCoreApplication.translate("MainWindow", u"No loaded file", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Camera:", None))
        self._camera_file.setText(QCoreApplication.translate("MainWindow", u"No loaded file", None))
    # retranslateUi

