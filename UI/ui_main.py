# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'maintzuTjX.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QDateTimeEdit,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QProgressBar,
    QPushButton, QSizePolicy, QSpinBox, QStackedWidget,
    QTimeEdit, QVBoxLayout, QWidget)

from custom_ui import CheckableComboBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(414, 580)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.verticalLayout = QVBoxLayout(self.home)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_3 = QFrame(self.home)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pushButton_setting = QPushButton(self.frame_3)
        self.pushButton_setting.setObjectName(u"pushButton_setting")

        self.verticalLayout_4.addWidget(self.pushButton_setting, 0, Qt.AlignmentFlag.AlignRight)

        self.frame_7 = QFrame(self.frame_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_7)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.groupBox = QGroupBox(self.frame_7)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_9 = QVBoxLayout(self.groupBox)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_8 = QFrame(self.groupBox)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_7 = QLabel(self.frame_8)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_3.addWidget(self.label_7)

        self.comboBox_vehicle_type = CheckableComboBox(self.frame_8)
        self.comboBox_vehicle_type.setObjectName(u"comboBox_vehicle_type")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.comboBox_vehicle_type.sizePolicy().hasHeightForWidth())
        self.comboBox_vehicle_type.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.comboBox_vehicle_type)


        self.verticalLayout_9.addWidget(self.frame_8)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.spinBox_in_out_keep = QSpinBox(self.groupBox)
        self.spinBox_in_out_keep.setObjectName(u"spinBox_in_out_keep")
        sizePolicy1.setHeightForWidth(self.spinBox_in_out_keep.sizePolicy().hasHeightForWidth())
        self.spinBox_in_out_keep.setSizePolicy(sizePolicy1)
        self.spinBox_in_out_keep.setMinimum(1)
        self.spinBox_in_out_keep.setMaximum(9999999)

        self.gridLayout_2.addWidget(self.spinBox_in_out_keep, 0, 1, 1, 1)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 1)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 0, 2, 1, 1)


        self.verticalLayout_9.addLayout(self.gridLayout_2)

        self.checkBox_delete_data_in_out = QCheckBox(self.groupBox)
        self.checkBox_delete_data_in_out.setObjectName(u"checkBox_delete_data_in_out")

        self.verticalLayout_9.addWidget(self.checkBox_delete_data_in_out)

        self.checkBox_delete_image_in_out = QCheckBox(self.groupBox)
        self.checkBox_delete_image_in_out.setObjectName(u"checkBox_delete_image_in_out")

        self.verticalLayout_9.addWidget(self.checkBox_delete_image_in_out)

        self.frame = QFrame(self.groupBox)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.checkBox_start_time_in_out = QCheckBox(self.frame)
        self.checkBox_start_time_in_out.setObjectName(u"checkBox_start_time_in_out")

        self.horizontalLayout_6.addWidget(self.checkBox_start_time_in_out)

        self.dateTimeEdit_in_out = QDateTimeEdit(self.frame)
        self.dateTimeEdit_in_out.setObjectName(u"dateTimeEdit_in_out")

        self.horizontalLayout_6.addWidget(self.dateTimeEdit_in_out)


        self.verticalLayout_9.addWidget(self.frame)


        self.verticalLayout_8.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.frame_7)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_10 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.spinBox_exception_keep = QSpinBox(self.groupBox_2)
        self.spinBox_exception_keep.setObjectName(u"spinBox_exception_keep")
        sizePolicy1.setHeightForWidth(self.spinBox_exception_keep.sizePolicy().hasHeightForWidth())
        self.spinBox_exception_keep.setSizePolicy(sizePolicy1)
        self.spinBox_exception_keep.setMinimum(1)
        self.spinBox_exception_keep.setMaximum(9999999)

        self.gridLayout_3.addWidget(self.spinBox_exception_keep, 0, 1, 1, 1)

        self.label_12 = QLabel(self.groupBox_2)
        self.label_12.setObjectName(u"label_12")
        sizePolicy2.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.label_12, 0, 0, 1, 1)

        self.label_13 = QLabel(self.groupBox_2)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_3.addWidget(self.label_13, 0, 2, 1, 1)


        self.verticalLayout_10.addLayout(self.gridLayout_3)

        self.checkBox_delete_data_exception = QCheckBox(self.groupBox_2)
        self.checkBox_delete_data_exception.setObjectName(u"checkBox_delete_data_exception")

        self.verticalLayout_10.addWidget(self.checkBox_delete_data_exception)

        self.checkBox_delete_image_exception = QCheckBox(self.groupBox_2)
        self.checkBox_delete_image_exception.setObjectName(u"checkBox_delete_image_exception")

        self.verticalLayout_10.addWidget(self.checkBox_delete_image_exception)

        self.frame_11 = QFrame(self.groupBox_2)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.checkBox_start_time_exception = QCheckBox(self.frame_11)
        self.checkBox_start_time_exception.setObjectName(u"checkBox_start_time_exception")

        self.horizontalLayout_7.addWidget(self.checkBox_start_time_exception)

        self.dateTimeEdit_exception = QDateTimeEdit(self.frame_11)
        self.dateTimeEdit_exception.setObjectName(u"dateTimeEdit_exception")

        self.horizontalLayout_7.addWidget(self.dateTimeEdit_exception)


        self.verticalLayout_10.addWidget(self.frame_11)


        self.verticalLayout_8.addWidget(self.groupBox_2)

        self.frame_9 = QFrame(self.frame_7)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.checkBox_auto = QCheckBox(self.frame_9)
        self.checkBox_auto.setObjectName(u"checkBox_auto")
        sizePolicy1.setHeightForWidth(self.checkBox_auto.sizePolicy().hasHeightForWidth())
        self.checkBox_auto.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.checkBox_auto)

        self.label_16 = QLabel(self.frame_9)
        self.label_16.setObjectName(u"label_16")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy3)

        self.horizontalLayout_4.addWidget(self.label_16)

        self.timeEdit_auto = QTimeEdit(self.frame_9)
        self.timeEdit_auto.setObjectName(u"timeEdit_auto")
        self.timeEdit_auto.setMinimumSize(QSize(60, 0))
        self.timeEdit_auto.setMinimumTime(QTime(0, 0, 0))
        self.timeEdit_auto.setCurrentSection(QDateTimeEdit.Section.HourSection)
        self.timeEdit_auto.setTime(QTime(1, 0, 0))

        self.horizontalLayout_4.addWidget(self.timeEdit_auto)

        self.label_10 = QLabel(self.frame_9)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_4.addWidget(self.label_10)


        self.verticalLayout_8.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.frame_7)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton_delete = QPushButton(self.frame_10)
        self.pushButton_delete.setObjectName(u"pushButton_delete")

        self.horizontalLayout_5.addWidget(self.pushButton_delete)

        self.pushButton_save = QPushButton(self.frame_10)
        self.pushButton_save.setObjectName(u"pushButton_save")

        self.horizontalLayout_5.addWidget(self.pushButton_save)


        self.verticalLayout_8.addWidget(self.frame_10)


        self.verticalLayout_4.addWidget(self.frame_7)

        self.progressBar = QProgressBar(self.frame_3)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setEnabled(True)
        self.progressBar.setMaximum(0)
        self.progressBar.setValue(-1)
        self.progressBar.setTextVisible(False)

        self.verticalLayout_4.addWidget(self.progressBar)

        self.label_log = QLabel(self.frame_3)
        self.label_log.setObjectName(u"label_log")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_log.sizePolicy().hasHeightForWidth())
        self.label_log.setSizePolicy(sizePolicy4)

        self.verticalLayout_4.addWidget(self.label_log)


        self.verticalLayout.addWidget(self.frame_3, 0, Qt.AlignmentFlag.AlignTop)

        self.label_version = QLabel(self.home)
        self.label_version.setObjectName(u"label_version")

        self.verticalLayout.addWidget(self.label_version, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignBottom)

        self.stackedWidget.addWidget(self.home)
        self.Setting = QWidget()
        self.Setting.setObjectName(u"Setting")
        self.verticalLayout_2 = QVBoxLayout(self.Setting)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_2 = QFrame(self.Setting)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 150))
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_6)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.lineEdit_postgresql_bin = QLineEdit(self.frame_6)
        self.lineEdit_postgresql_bin.setObjectName(u"lineEdit_postgresql_bin")

        self.horizontalLayout_2.addWidget(self.lineEdit_postgresql_bin)

        self.pushButton_postgresql_bin_select = QPushButton(self.frame_6)
        self.pushButton_postgresql_bin_select.setObjectName(u"pushButton_postgresql_bin_select")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.pushButton_postgresql_bin_select.sizePolicy().hasHeightForWidth())
        self.pushButton_postgresql_bin_select.setSizePolicy(sizePolicy5)
        self.pushButton_postgresql_bin_select.setMaximumSize(QSize(25, 16777215))

        self.horizontalLayout_2.addWidget(self.pushButton_postgresql_bin_select)


        self.verticalLayout_6.addWidget(self.frame_6)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 2, 1, 1)

        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.lineEdit_db_host = QLineEdit(self.frame_4)
        self.lineEdit_db_host.setObjectName(u"lineEdit_db_host")

        self.gridLayout.addWidget(self.lineEdit_db_host, 2, 1, 1, 1)

        self.label_6 = QLabel(self.frame_4)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 3, 2, 1, 1)

        self.lineEdit_db_user = QLineEdit(self.frame_4)
        self.lineEdit_db_user.setObjectName(u"lineEdit_db_user")

        self.gridLayout.addWidget(self.lineEdit_db_user, 3, 1, 1, 1)

        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)

        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.lineEdit_db_name = QLineEdit(self.frame_4)
        self.lineEdit_db_name.setObjectName(u"lineEdit_db_name")

        self.gridLayout.addWidget(self.lineEdit_db_name, 0, 1, 1, 1)

        self.lineEdit_db_password = QLineEdit(self.frame_4)
        self.lineEdit_db_password.setObjectName(u"lineEdit_db_password")
        self.lineEdit_db_password.setMaxLength(32767)
        self.lineEdit_db_password.setFrame(True)
        self.lineEdit_db_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.lineEdit_db_password.setClearButtonEnabled(False)

        self.gridLayout.addWidget(self.lineEdit_db_password, 3, 3, 1, 1)

        self.spinBox_db_port = QSpinBox(self.frame_4)
        self.spinBox_db_port.setObjectName(u"spinBox_db_port")
        self.spinBox_db_port.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.spinBox_db_port.setMinimum(1)
        self.spinBox_db_port.setMaximum(99999)
        self.spinBox_db_port.setValue(5432)

        self.gridLayout.addWidget(self.spinBox_db_port, 2, 3, 1, 1)


        self.verticalLayout_6.addLayout(self.gridLayout)


        self.verticalLayout_5.addWidget(self.frame_4, 0, Qt.AlignmentFlag.AlignTop)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_save_setting = QPushButton(self.frame_5)
        self.pushButton_save_setting.setObjectName(u"pushButton_save_setting")

        self.horizontalLayout.addWidget(self.pushButton_save_setting, 0, Qt.AlignmentFlag.AlignRight)

        self.pushButton_cancel_setting = QPushButton(self.frame_5)
        self.pushButton_cancel_setting.setObjectName(u"pushButton_cancel_setting")

        self.horizontalLayout.addWidget(self.pushButton_cancel_setting, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_5.addWidget(self.frame_5, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.stackedWidget.addWidget(self.Setting)

        self.verticalLayout_3.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_setting.setText(QCoreApplication.translate("MainWindow", u"More Setting", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"X\u00f3a d\u1eef li\u1ec7u v\u00e0o ra", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Lo\u1ea1i \u0111\u1ed1i t\u01b0\u1ee3ng", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"X\u00f3a d\u1eef li\u1ec7u sau", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"ng\u00e0y", None))
        self.checkBox_delete_data_in_out.setText(QCoreApplication.translate("MainWindow", u"X\u00f3a data", None))
        self.checkBox_delete_image_in_out.setText(QCoreApplication.translate("MainWindow", u"X\u00f3a h\u00ecnh \u1ea3nh", None))
        self.checkBox_start_time_in_out.setText(QCoreApplication.translate("MainWindow", u"X\u00f3a t\u1eeb th\u1eddi \u0111i\u1ec3m", None))
        self.dateTimeEdit_in_out.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dd/MM/yyyy hh:mm", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"X\u00f3a d\u1eef li\u1ec7u ngo\u1ea1i l\u1ec7", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"X\u00f3a d\u1eef li\u1ec7u sau", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"ng\u00e0y", None))
        self.checkBox_delete_data_exception.setText(QCoreApplication.translate("MainWindow", u"X\u00f3a data", None))
        self.checkBox_delete_image_exception.setText(QCoreApplication.translate("MainWindow", u"X\u00f3a h\u00ecnh \u1ea3nh", None))
        self.checkBox_start_time_exception.setText(QCoreApplication.translate("MainWindow", u"X\u00f3a t\u1eeb th\u1eddi \u0111i\u1ec3m", None))
        self.dateTimeEdit_exception.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dd/MM/yyyy hh:mm", None))
        self.checkBox_auto.setText(QCoreApplication.translate("MainWindow", u"T\u1ef1 \u0111\u1ed9ng x\u00f3a h\u1eb1ng ng\u00e0y", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"l\u00fac", None))
        self.timeEdit_auto.setDisplayFormat(QCoreApplication.translate("MainWindow", u"hh:mm", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"gi\u1edd", None))
        self.pushButton_delete.setText(QCoreApplication.translate("MainWindow", u"X\u00d3A D\u1eee LI\u1ec6U", None))
        self.pushButton_save.setText(QCoreApplication.translate("MainWindow", u"L\u01afU", None))
        self.label_version.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"PostgreSQL bin ", None))
        self.lineEdit_postgresql_bin.setText(QCoreApplication.translate("MainWindow", u"C:/Program Files/PostgreSQL/11/bin", None))
        self.pushButton_postgresql_bin_select.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Port", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Host", None))
        self.lineEdit_db_host.setText(QCoreApplication.translate("MainWindow", u"localhost", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.lineEdit_db_user.setText(QCoreApplication.translate("MainWindow", u"lparking", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"User name", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Database name", None))
        self.lineEdit_db_name.setText(QCoreApplication.translate("MainWindow", u"lparkingdb", None))
        self.lineEdit_db_password.setText(QCoreApplication.translate("MainWindow", u"Lovadvn.2014", None))
        self.pushButton_save_setting.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.pushButton_cancel_setting.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
    # retranslateUi

