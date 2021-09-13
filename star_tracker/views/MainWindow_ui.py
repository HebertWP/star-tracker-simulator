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

from views.widgets.viewPlot import ViewPlot

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
        self.verticalLayoutWidget_4.setGeometry(QRect(10, 210, 451, 101))
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
        self.label_5 = QLabel(self.verticalLayoutWidget_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_5)

        self.doubleSpinBox = QDoubleSpinBox(self.verticalLayoutWidget_4)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setAlignment(Qt.AlignCenter)
        self.doubleSpinBox.setMaximum(360.000000000000000)

        self.verticalLayout_6.addWidget(self.doubleSpinBox)

        self.horizontalScrollBar = QScrollBar(self.verticalLayoutWidget_4)
        self.horizontalScrollBar.setObjectName(u"horizontalScrollBar")
        self.horizontalScrollBar.setMaximum(360)
        self.horizontalScrollBar.setOrientation(Qt.Horizontal)

        self.verticalLayout_6.addWidget(self.horizontalScrollBar)


        self.horizontalLayout_4.addLayout(self.verticalLayout_6)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_8 = QLabel(self.verticalLayoutWidget_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_8)

        self.doubleSpinBox_3 = QDoubleSpinBox(self.verticalLayoutWidget_4)
        self.doubleSpinBox_3.setObjectName(u"doubleSpinBox_3")
        self.doubleSpinBox_3.setAlignment(Qt.AlignCenter)
        self.doubleSpinBox_3.setMaximum(360.000000000000000)

        self.verticalLayout_9.addWidget(self.doubleSpinBox_3)

        self.horizontalScrollBar_3 = QScrollBar(self.verticalLayoutWidget_4)
        self.horizontalScrollBar_3.setObjectName(u"horizontalScrollBar_3")
        self.horizontalScrollBar_3.setMaximum(360)
        self.horizontalScrollBar_3.setOrientation(Qt.Horizontal)

        self.verticalLayout_9.addWidget(self.horizontalScrollBar_3)


        self.horizontalLayout_4.addLayout(self.verticalLayout_9)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_6 = QLabel(self.verticalLayoutWidget_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_6)

        self.doubleSpinBox_2 = QDoubleSpinBox(self.verticalLayoutWidget_4)
        self.doubleSpinBox_2.setObjectName(u"doubleSpinBox_2")
        self.doubleSpinBox_2.setAlignment(Qt.AlignCenter)
        self.doubleSpinBox_2.setMaximum(180.000000000000000)

        self.verticalLayout_7.addWidget(self.doubleSpinBox_2)

        self.horizontalScrollBar_2 = QScrollBar(self.verticalLayoutWidget_4)
        self.horizontalScrollBar_2.setObjectName(u"horizontalScrollBar_2")
        self.horizontalScrollBar_2.setOrientation(Qt.Horizontal)

        self.verticalLayout_7.addWidget(self.horizontalScrollBar_2)


        self.horizontalLayout_4.addLayout(self.verticalLayout_7)


        self.verticalLayout_8.addLayout(self.horizontalLayout_4)

        self.horizontalLayoutWidget_2 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(460, 210, 376, 41))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_4 = QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_2.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout_2.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.horizontalLayout_2.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.horizontalLayout_2.addWidget(self.pushButton_7)

        self.viewPlot = ViewPlot(self.centralwidget)
        self.viewPlot.setObjectName(u"viewPlot")
        self.viewPlot.setGeometry(QRect(0, 310, 711, 329))
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
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 279, 124))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.loadStarsFile = QPushButton(self.horizontalLayoutWidget)
        self.loadStarsFile.setObjectName(u"loadStarsFile")
        icon1 = QIcon()
        icon1.addFile(u":/icon/icons/Artboard 1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.loadStarsFile.setIcon(icon1)
        self.loadStarsFile.setIconSize(QSize(64, 64))
        self.loadStarsFile.setFlat(True)

        self.verticalLayout.addWidget(self.loadStarsFile)

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
        self.LoadMovmentsFile = QPushButton(self.horizontalLayoutWidget)
        self.LoadMovmentsFile.setObjectName(u"LoadMovmentsFile")
        icon2 = QIcon()
        icon2.addFile(u":/icon/icons/Artboard 2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.LoadMovmentsFile.setIcon(icon2)
        self.LoadMovmentsFile.setIconSize(QSize(64, 64))
        self.LoadMovmentsFile.setFlat(True)

        self.verticalLayout_2.addWidget(self.LoadMovmentsFile)

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
        self.loadCameraFile = QPushButton(self.horizontalLayoutWidget)
        self.loadCameraFile.setObjectName(u"loadCameraFile")
        icon3 = QIcon()
        icon3.addFile(u":/icon/icons/Artboard 3.png", QSize(), QIcon.Normal, QIcon.Off)
        self.loadCameraFile.setIcon(icon3)
        self.loadCameraFile.setIconSize(QSize(64, 64))
        self.loadCameraFile.setFlat(True)

        self.verticalLayout_3.addWidget(self.loadCameraFile)

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

        self.tabWidget.addTab(self.File, "")
        self.Edit = QWidget()
        self.Edit.setObjectName(u"Edit")
        self.tabWidget.addTab(self.Edit, "")
        self.Help = QWidget()
        self.Help.setObjectName(u"Help")
        self.tabWidget.addTab(self.Help, "")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(710, 310, 138, 161))
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
        icon4 = QIcon()
        icon4.addFile(u":/icon/icons/axis.png", QSize(), QIcon.Normal, QIcon.Off)
        icon4.addFile(u":/icon/icons/3d.png", QSize(), QIcon.Normal, QIcon.On)
        self.view3D_icon.setIcon(icon4)
        self.view3D_icon.setIconSize(QSize(64, 64))
        self.view3D_icon.setCheckable(True)
        self.view3D_icon.setChecked(False)
        self.view3D_icon.setAutoDefault(False)
        self.view3D_icon.setFlat(True)

        self.verticalLayout_4.addWidget(self.view3D_icon)

        self.checkBox = QCheckBox(self.layoutWidget)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout_4.addWidget(self.checkBox)

        self.checkBox_2 = QCheckBox(self.layoutWidget)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.verticalLayout_4.addWidget(self.checkBox_2)

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
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Roll", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Pitch", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Yaw", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.loadStarsFile.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Stars", None))
        self.LoadMovmentsFile.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Moviments", None))
        self.loadCameraFile.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Controls", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Load File", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.File), QCoreApplication.translate("MainWindow", u"File", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Edit), QCoreApplication.translate("MainWindow", u"Edit", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Help), QCoreApplication.translate("MainWindow", u"Help", None))
        self.view3D_text.setText(QCoreApplication.translate("MainWindow", u"View Mode", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Camera View", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"Graticule", None))
    # retranslateUi

