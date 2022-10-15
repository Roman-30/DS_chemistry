# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'project_chemistryGTYULU.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(796, 502)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 3, 2, 1, 1)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayoutWidget_2 = QWidget(self.widget_2)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(0, 0, 2, 2))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)

        self.gridLayout.addWidget(self.widget_2, 9, 0, 10, 9)

        self.spline_display_radio_button = QRadioButton(self.centralwidget)
        self.spline_display_radio_button.setObjectName(u"spline_display_radio_button")
        self.spline_display_radio_button.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout.addWidget(self.spline_display_radio_button, 5, 4, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 17, 11, 1, 1)

        self.label_28 = QLabel(self.centralwidget)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout.addWidget(self.label_28, 16, 12, 1, 1)

        self.label_26 = QLabel(self.centralwidget)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout.addWidget(self.label_26, 16, 10, 1, 1)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 10, 11, 1, 1)

        self.label_27 = QLabel(self.centralwidget)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout.addWidget(self.label_27, 16, 11, 1, 1)

        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout.addWidget(self.label_13, 12, 11, 1, 1)

        self.label_29 = QLabel(self.centralwidget)
        self.label_29.setObjectName(u"label_29")
        sizePolicy.setHeightForWidth(self.label_29.sizePolicy().hasHeightForWidth())
        self.label_29.setSizePolicy(sizePolicy)
        self.label_29.setLayoutDirection(Qt.LeftToRight)
        self.label_29.setAutoFillBackground(False)

        self.gridLayout.addWidget(self.label_29, 0, 7, 1, 2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 9, 11, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout.addWidget(self.label, 5, 5, 1, 3)

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(50, 16777215))

        self.gridLayout.addWidget(self.label_9, 11, 10, 1, 1)

        self.label_22 = QLabel(self.centralwidget)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMaximumSize(QSize(50, 16777215))

        self.gridLayout.addWidget(self.label_22, 15, 10, 1, 1)

        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 11, 12, 1, 1)

        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMaximumSize(QSize(142, 20))
        self.lineEdit_2.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout.addWidget(self.lineEdit_2, 2, 4, 1, 5)

        self.cancel_button = QPushButton(self.centralwidget)
        self.cancel_button.setObjectName(u"cancel_button")
        sizePolicy.setHeightForWidth(self.cancel_button.sizePolicy().hasHeightForWidth())
        self.cancel_button.setSizePolicy(sizePolicy)
        self.cancel_button.setMaximumSize(QSize(100, 23))
        self.cancel_button.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout.addWidget(self.cancel_button, 1, 7, 1, 3)

        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 11, 11, 1, 1)

        self.label_33 = QLabel(self.centralwidget)
        self.label_33.setObjectName(u"label_33")
        sizePolicy.setHeightForWidth(self.label_33.sizePolicy().hasHeightForWidth())
        self.label_33.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.label_33, 0, 11, 1, 1)

        self.label_32 = QLabel(self.centralwidget)
        self.label_32.setObjectName(u"label_32")
        sizePolicy.setHeightForWidth(self.label_32.sizePolicy().hasHeightForWidth())
        self.label_32.setSizePolicy(sizePolicy)
        self.label_32.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout.addWidget(self.label_32, 0, 10, 1, 1)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaximumSize(QSize(142, 20))
        self.lineEdit.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout.addWidget(self.lineEdit, 3, 4, 1, 5)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout.addWidget(self.label_2, 3, 9, 1, 5)

        self.label_30 = QLabel(self.centralwidget)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout.addWidget(self.label_30, 6, 9, 1, 3)

        self.label_19 = QLabel(self.centralwidget)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMaximumSize(QSize(50, 16777215))

        self.gridLayout.addWidget(self.label_19, 14, 10, 1, 1)

        self.calculate_button = QPushButton(self.centralwidget)
        self.calculate_button.setObjectName(u"calculate_button")
        self.calculate_button.setMaximumSize(QSize(75, 23))
        self.calculate_button.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout.addWidget(self.calculate_button, 7, 4, 1, 1)

        self.spline_button = QPushButton(self.centralwidget)
        self.spline_button.setObjectName(u"spline_button")
        sizePolicy.setHeightForWidth(self.spline_button.sizePolicy().hasHeightForWidth())
        self.spline_button.setSizePolicy(sizePolicy)
        self.spline_button.setMaximumSize(QSize(115, 23))
        self.spline_button.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout.addWidget(self.spline_button, 4, 4, 1, 4)

        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMaximumSize(QSize(142, 20))
        self.lineEdit_3.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout.addWidget(self.lineEdit_3, 6, 4, 1, 5)

        self.label_23 = QLabel(self.centralwidget)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout.addWidget(self.label_23, 15, 11, 1, 1)

        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(50, 16777215))

        self.gridLayout.addWidget(self.label_14, 13, 10, 1, 1)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 10, 12, 1, 1)

        self.label_17 = QLabel(self.centralwidget)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout.addWidget(self.label_17, 13, 12, 1, 1)

        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(50, 16777215))

        self.gridLayout.addWidget(self.label_12, 12, 10, 1, 1)

        self.open_button = QPushButton(self.centralwidget)
        self.open_button.setObjectName(u"open_button")
        sizePolicy.setHeightForWidth(self.open_button.sizePolicy().hasHeightForWidth())
        self.open_button.setSizePolicy(sizePolicy)
        self.open_button.setMaximumSize(QSize(88, 23))
        self.open_button.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout.addWidget(self.open_button, 0, 4, 1, 3)

        self.label_21 = QLabel(self.centralwidget)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout.addWidget(self.label_21, 14, 12, 1, 1)

        self.cut_button = QPushButton(self.centralwidget)
        self.cut_button.setObjectName(u"cut_button")
        sizePolicy.setHeightForWidth(self.cut_button.sizePolicy().hasHeightForWidth())
        self.cut_button.setSizePolicy(sizePolicy)
        self.cut_button.setMaximumSize(QSize(88, 23))
        self.cut_button.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout.addWidget(self.cut_button, 1, 4, 1, 3)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(50, 13))

        self.gridLayout.addWidget(self.label_6, 10, 10, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(210, 16777215))
        self.label_3.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout.addWidget(self.label_3, 2, 9, 1, 5)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy1)
        self.widget.setMinimumSize(QSize(225, 200))
        self.widget.setLayoutDirection(Qt.RightToLeft)
        self.gridLayoutWidget = QWidget(self.widget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 2, 2))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)

        self.gridLayout.addWidget(self.widget, 0, 0, 8, 2)

        self.label_24 = QLabel(self.centralwidget)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout.addWidget(self.label_24, 15, 12, 1, 1)

        self.label_16 = QLabel(self.centralwidget)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout.addWidget(self.label_16, 13, 11, 1, 1)

        self.label_20 = QLabel(self.centralwidget)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout.addWidget(self.label_20, 14, 11, 1, 1)

        self.label_15 = QLabel(self.centralwidget)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout.addWidget(self.label_15, 12, 12, 1, 1)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 8, 0, 1, 15)

        self.change_button = QPushButton(self.centralwidget)
        self.change_button.setObjectName(u"change_button")
        sizePolicy.setHeightForWidth(self.change_button.sizePolicy().hasHeightForWidth())
        self.change_button.setSizePolicy(sizePolicy)
        self.change_button.setMaximumSize(QSize(113, 23))
        self.change_button.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout.addWidget(self.change_button, 1, 10, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 3, 3, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 796, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.spline_display_radio_button.setText(
            QCoreApplication.translate("MainWindow", u"\u0421\u043f\u043b\u0430\u0439\u043d", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow",
                                                         u"\u041e\u0442\u043d\u043e\u0441.\u043e\u0442\u043a\u043b\u043e\u043d\u0435\u043d\u0438\u0435",
                                                         None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Rp = ", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"icor =", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u03a9*\u0441\u043c^2", None))
        self.lineEdit_2.setText(QCoreApplication.translate("MainWindow", u"34.54", None))
        self.cancel_button.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0431\u0440\u043e\u0441", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_33.setText("")
        self.label_32.setText(QCoreApplication.translate("MainWindow",
                                                         u"\u0412\u044b \u0440\u0430\u0431\u043e\u0442\u0430\u0435\u0442\u0435 \u0441 \u0444\u0430\u0439\u043b\u043e\u043c",
                                                         None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow",
                                                        u"\u041a\u043e\u043b\u0432\u043e \u0443\u0437\u043b\u043e\u0432 \u0441\u043f\u043b\u0430\u0439\u043d\u0430  [5...100]]",
                                                        None))
        self.label_30.setText(QCoreApplication.translate("MainWindow",
                                                         u"\u0418\u043d\u0442\u0435\u0440\u0432\u0430\u043b \u0434\u0438\u0444\u0444\u0435\u0440\u0435\u043d\u0446\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f, mV  [1...10]",
                                                         None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"B =", None))
        self.calculate_button.setText(
            QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0447\u0435\u0442", None))
        self.spline_button.setText(QCoreApplication.translate("MainWindow",
                                                              u"\u0421\u0434\u0435\u043b\u0430\u0442\u044c \u0441\u043f\u043b\u0430\u0439\u043d",
                                                              None))
        self.lineEdit_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"(0)", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"bc =", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"mV", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"mV", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"ba = ", None))
        self.open_button.setText(QCoreApplication.translate("MainWindow",
                                                            u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0444\u0430\u0439\u043b",
                                                            None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"mv", None))
        self.cut_button.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u043e\u0440", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Ecor =", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow",
                                                        u"\u041f\u043b\u043e\u0449\u0430\u0434\u044c \u044d\u043b\u0435\u043a\u0442\u0440\u043e\u0434\u0430 \u0441\u043c^2  [0.01...500.0]",
                                                        None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"mkA/\u0441\u043c^2", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"(0)", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"mV", None))
        self.change_button.setText(QCoreApplication.translate("MainWindow",
                                                              u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u043f\u043b\u043e\u0449\u0430\u0434\u044c",
                                                              None))
    # retranslateUi
