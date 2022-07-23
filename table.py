import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtWidgets import QMainWindow
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from services import *


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, width=50, height=40, dpi=1100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class UiMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setObjectName("MainWindow")
        self.setMinimumSize(900, 600)
        self.central_widget = QtWidgets.QWidget(self)
        self.central_widget.setObjectName("centralwidget")

        self.gridLayout = QtWidgets.QGridLayout(self.central_widget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_33 = QtWidgets.QLabel(self.central_widget)
        self.label_33.setText("")
        self.label_33.setObjectName("label_33")
        self.gridLayout.addWidget(self.label_33, 0, 9, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.central_widget)
        self.label_32.setObjectName("label_32")
        self.gridLayout.addWidget(self.label_32, 0, 8, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.central_widget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 2, 2, 1, 5)
        self.spline_button = QtWidgets.QPushButton(self.central_widget)
        self.spline_button.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.spline_button, 4, 2, 1, 4)
        self.label_3 = QtWidgets.QLabel(self.central_widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 7, 1, 6)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.central_widget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 6, 2, 1, 5)
        spacer_item = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacer_item, 8, 1, 1, 1)
        self.calculate_button = QtWidgets.QPushButton(self.central_widget)
        self.calculate_button.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.calculate_button, 7, 2, 1, 1)
        self.line = QtWidgets.QFrame(self.central_widget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 9, 1, 1, 12)
        self.cancel_button = QtWidgets.QPushButton(self.central_widget)
        self.cancel_button.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.cancel_button, 1, 5, 1, 3)
        self.label_30 = QtWidgets.QLabel(self.central_widget)
        self.label_30.setObjectName("label_30")
        self.gridLayout.addWidget(self.label_30, 6, 7, 1, 3)
        self.label_2 = QtWidgets.QLabel(self.central_widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 7, 1, 5)
        self.label_10 = QtWidgets.QLabel(self.central_widget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 12, 9, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.central_widget)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 13, 10, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.central_widget)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 14, 9, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.central_widget)
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 15, 9, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.central_widget)
        self.label_12.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 13, 8, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.central_widget)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 14, 10, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.central_widget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 11, 10, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.central_widget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 3, 2, 1, 5)
        self.open_button = QtWidgets.QPushButton(self.central_widget)
        self.open_button.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.open_button, 0, 2, 1, 3)
        self.cut_button = QtWidgets.QPushButton(self.central_widget)
        self.cut_button.setObjectName("pushButton")
        self.gridLayout.addWidget(self.cut_button, 1, 2, 1, 3)
        self.label_21 = QtWidgets.QLabel(self.central_widget)
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 15, 10, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.central_widget)
        self.label_6.setMaximumSize(QtCore.QSize(50, 13))
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 11, 8, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.central_widget)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 12, 10, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.central_widget)
        self.label_22.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_22.setObjectName("label_22")
        self.gridLayout.addWidget(self.label_22, 16, 8, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.central_widget)
        self.label_9.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 12, 8, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.central_widget)
        self.label_23.setObjectName("label_23")
        self.gridLayout.addWidget(self.label_23, 16, 9, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.central_widget)
        self.label_14.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 14, 8, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.central_widget)
        self.label_19.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 15, 8, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.central_widget)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 13, 9, 1, 1)
        spacer_item_1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacer_item_1, 10, 9, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.central_widget)
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 16, 10, 1, 1)
        self.label = QtWidgets.QLabel(self.central_widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 5, 3, 1, 3)
        self.label_29 = QtWidgets.QLabel(self.central_widget)
        self.label_29.setObjectName("label_29")
        self.gridLayout.addWidget(self.label_29, 0, 5, 1, 2)
        self.widget_2 = QtWidgets.QWidget(self.central_widget)
        self.widget_2.setObjectName("widget_2")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.widget_2)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout.addWidget(self.widget_2, 10, 1, 10, 4)
        self.widget = QtWidgets.QWidget(self.central_widget)
        self.widget.setObjectName("widget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.widget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout.addWidget(self.widget, 0, 0, 8, 2)
        self.label_26 = QtWidgets.QLabel(self.central_widget)
        self.label_26.setObjectName("label_26")
        self.gridLayout.addWidget(self.label_26, 17, 8, 1, 1)
        self.spline_display_radio_button = QtWidgets.QRadioButton(self.central_widget)
        self.spline_display_radio_button.setObjectName("radioButton")
        self.gridLayout.addWidget(self.spline_display_radio_button, 5, 2, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.central_widget)
        self.label_28.setObjectName("label_28")
        self.gridLayout.addWidget(self.label_28, 17, 10, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.central_widget)
        self.label_27.setObjectName("label_27")
        self.gridLayout.addWidget(self.label_27, 17, 9, 1, 1)
        spacer_item_2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacer_item_2, 18, 9, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.central_widget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 11, 9, 1, 1)
        self.setCentralWidget(self.central_widget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 681, 21))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.change_button = QtWidgets.QPushButton(self.central_widget)
        self.change_button.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.change_button, 1, 8, 1, 1)

        self.flag = False
        self.points = []

        self.sc_1 = MplCanvas(width=5, height=4, dpi=80)
        toolbar_1 = NavigationToolbar(self.sc_1, self)
        layout_1 = QtWidgets.QVBoxLayout()
        layout_1.addWidget(toolbar_1)
        layout_1.addWidget(self.sc_1)
        self.sc_1.axes.set_xlabel("E")
        self.sc_1.axes.set_ylabel("I")
        self.sc_1.axes.grid()
        self.widget.setLayout(layout_1)

        self.sc_2 = MplCanvas(width=5, height=4, dpi=100)
        toolbar_2 = NavigationToolbar(self.sc_2, self)
        layout_2 = QtWidgets.QVBoxLayout()
        layout_2.addWidget(toolbar_2)
        layout_2.addWidget(self.sc_2)
        self.sc_2.axes.set_xlabel("ΔE")
        self.sc_2.axes.set_ylabel("Y = 2.3*Rp*i")
        self.sc_2.axes.grid()
        self.widget_2.setLayout(layout_2)

        self.widgets = {0: self.lineEdit,
                        1: self.lineEdit_2,
                        2: self.lineEdit_3,
                        3: self.spline_display_radio_button,
                        4: self.cut_button,
                        5: self.cancel_button,
                        6: self.open_button,
                        7: self.calculate_button,
                        8: self.spline_button,
                        9: self.change_button}

        self.ser = WindowService()
        self.md = GraphModel()
        self.butt_func()

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_32.setText(_translate("MainWindow", "Вы работаете с файлом"))
        self.lineEdit_2.setText(_translate("MainWindow", "34.54"))
        self.spline_button.setText(_translate("MainWindow", "Сделать сплайн"))
        self.label_3.setText(_translate("MainWindow", "Площадь электрода см^2  [0.01...500.0]"))
        self.lineEdit_3.setText(_translate("MainWindow", "3"))
        self.calculate_button.setText(_translate("MainWindow", "Рассчитать"))
        self.cancel_button.setText(_translate("MainWindow", "Сброс обрезки"))
        self.label_30.setText(_translate("MainWindow", "Интервал дифференцирования, mV  [1...10]"))
        self.label_2.setText(_translate("MainWindow", "Кол-во узлов сплайна  [5...100]"))
        self.label_10.setText(_translate("MainWindow", "0"))
        self.label_15.setText(_translate("MainWindow", "mV"))
        self.label_16.setText(_translate("MainWindow", "0"))
        self.label_20.setText(_translate("MainWindow", "(0)"))
        self.label_12.setText(_translate("MainWindow", "ba = "))
        self.label_17.setText(_translate("MainWindow", "mV"))
        self.label_8.setText(_translate("MainWindow", "mV"))
        self.lineEdit.setText(_translate("MainWindow", "10"))
        self.open_button.setText(_translate("MainWindow", "Открыть файл"))
        self.cut_button.setText(_translate("MainWindow", "Обрезать"))
        self.label_21.setText(_translate("MainWindow", "mv"))
        self.label_6.setText(_translate("MainWindow", "E_cor ="))
        self.label_11.setText(_translate("MainWindow", "Ω*см^2"))
        self.label_22.setText(_translate("MainWindow", "I_cor ="))
        self.label_9.setText(_translate("MainWindow", "Rp = "))
        self.label_23.setText(_translate("MainWindow", "(0)"))
        self.label_14.setText(_translate("MainWindow", "bc ="))
        self.label_19.setText(_translate("MainWindow", "B ="))
        self.label_13.setText(_translate("MainWindow", "0"))
        self.label_24.setText(_translate("MainWindow", "mkA/см^2"))
        self.label.setText(_translate("MainWindow", "OFF"))
        self.label_29.setText(_translate("MainWindow", "OFF"))
        self.label_26.setText(_translate("MainWindow", "Относ.отклонение"))
        self.spline_display_radio_button.setText(_translate("MainWindow", "Сплайн"))
        self.label_28.setText(_translate("MainWindow", "%"))
        self.label_27.setText(_translate("MainWindow", "0"))
        self.label_7.setText(_translate("MainWindow", "0"))
        self.change_button.setText(_translate("MainWindow", "Изменить площадь"))

        self.visual_controler(False, [0, 2, 3, 4, 5, 7, 8, 9])

        self.label_29.setStyleSheet("color: rgb(255, 0, 0)")
        self.label_29.setText("OFF")

        self.label.setStyleSheet("color: rgb(255, 0, 0)")
        self.label.setText("OFF")

    def butt_func(self):
        self.sc_1.figure.canvas.mpl_connect('button_press_event', self.click_for_graph)
        self.cancel_button.clicked.connect(lambda: self.ex_click())
        self.open_button.clicked.connect(lambda: self.open_file())
        self.spline_display_radio_button.clicked.connect(lambda: self.click_radio_b())
        self.spline_button.clicked.connect(lambda: self.make_spline())
        self.change_button.clicked.connect(lambda: self.change_area())
        self.calculate_button.clicked.connect(lambda: self.calculate())
        self.cut_button.clicked.connect(lambda: self.cut_graph())

    def cut_graph(self):
        self.cancel_button.setEnabled(True)

        self.sc_1.axes.clear()
        self.sc_1.axes.plot(self.md.adjusted.x, self.md.adjusted.y, label="Исходный")
        self.sc_1.axes.legend(loc='lower right')
        self.label.setStyleSheet("color: rgb(255, 0, 0)")
        self.label.setText("OFF")
        self.sc_1.axes.grid()
        self.sc_1.axes.legend(loc='lower right')
        self.sc_1.axes.set_xlabel("E")
        self.sc_1.axes.set_ylabel("I")
        self.sc_1.draw()

        self.visual_controler(False, [0, 1, 2, 3, 4, 6, 7, 8, 9])
        self.points = []
        self.flag = True

    def make_spline(self):
        try:
            num = int(self.lineEdit.text())
            if num in range(5, 101):
                self.ser.spline(self.md, num)
                self.spline_display_radio_button.setChecked(True)
                self.label.setStyleSheet("color: rgb(0, 255, 0)")
                self.label.setText("ON_")
                self.sc_1.axes.clear()
                self.sc_1.axes.plot(self.md.spline.x, self.md.spline.y, label="Сплайн")
                self.sc_1.axes.legend(loc='lower right')
                self.sc_1.axes.grid()
                self.sc_1.axes.set_xlabel("E")
                self.sc_1.axes.set_ylabel("I")
                self.sc_1.draw()

                self.visual_controler(True, [2, 3, 7])
            else:
                QMessageBox.critical(self, "Ошибка ", "Выход из дозволенных значений в разделе \"Узлы сплайна\"",
                                     QMessageBox.Ok)
        except ValueError:
            QMessageBox.critical(self, "Ошибка ", "Некорректные данные в разделе \"Узлы сплайна\"",
                                 QMessageBox.Ok)

    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_E:
            sys.exit(0)

    def change_area(self):
        try:
            self.sc_1.axes.clear()
            s = round(float(self.lineEdit_2.text()), 2)
            if s * 100 in range(1, 50001):
                self.ser.perform_area_correction(s, self.md)
                self.sc_1.axes.plot(self.md.adjusted.x, self.md.adjusted.y, label="Исходный")
                self.sc_1.axes.legend(loc='lower right')
                self.sc_1.axes.legend(loc='lower right')
                self.sc_1.axes.set_xlabel("E")
                self.sc_1.axes.set_ylabel("I")
                self.sc_1.axes.grid()
                self.sc_1.draw()
            else:
                QMessageBox.critical(self, "Ошибка ", "Выход из диапозона значений в разделе \"Площадь электрода\"",
                                     QMessageBox.Ok)
        except ValueError:
            QMessageBox.critical(self, "Ошибка ", "Некорректные данные в разделе \"Площадь электрода\"",
                                 QMessageBox.Ok)

    def calculate(self):
        try:
            self.ser.calculate_E_corrosivity(self.md)
            num = int(self.lineEdit_3.text())
            if num in range(1, 11):
                self.ser.calculate_point_derivative(self.md, num)
                self.ser.calculate_final_graph(self.md)
                self.ser.calc_d(self.md)
                self.sc_2.axes.clear()
                self.sc_2.axes.plot(self.md.expired.x, self.md.expired.y, label="Эксперимент")
                self.sc_2.draw()

                f = self.ser.new_sequence(self.md, self.md.expired.x)
                print(len(f))
                lq = self.ser.calculate_between(f, self.md)
                key = self.ser.search_min_map_num(lq)

                self.md.b_a = key[0]
                self.md.b_c = key[1]

                self.sc_2.axes.plot(self.md.expired.x, f[key], label="Подбор")
                self.sc_2.axes.legend(loc='lower right')
                self.sc_2.axes.set_xlabel("ΔE")
                self.sc_2.axes.set_ylabel("Y = 2.3*Rp*i")
                self.sc_2.axes.grid()
                self.sc_2.draw()

                self.ser.calculate_b(self.md)
                self.ser.calculate_i_cor(self.md)

                self.label_7.setText(str(round(self.md.E_cor, 1)))
                self.label_10.setText(str(round(self.md.derivative, 0)))
                self.label_13.setText(str(self.md.b_a))
                self.label_16.setText(str(self.md.b_c))
                self.label_20.setText(str(round(self.md.B, 1)))
                self.label_23.setText(str(round(self.md.I_cor, 4)))
                self.label_27.setText(str(round(self.ser.calculate_deviation(self.md), 3)))
            else:
                QMessageBox.critical(self, "Ошибка ",
                                     "Выход из диапозона значений в разделе \"Интервал дифференцирования\"",
                                     QMessageBox.Ok)
        except ValueError:
            QMessageBox.critical(self, "Ошибка ", "Некорректные данные в разделе \"Интервал дифференцирования\"",
                                 QMessageBox.Ok)

    def click_radio_b(self):
        status = False
        if len(self.md.spline.x) > 0:
            self.sc_1.axes.clear()
            if self.spline_display_radio_button.isChecked():
                self.sc_1.axes.plot(self.md.spline.x, self.md.spline.y, label="Сплайн")
                self.sc_1.axes.legend(loc='lower right')
                self.label.setStyleSheet("color: rgb(0, 255, 0)")
                self.label.setText("ON_")
            else:
                self.sc_1.axes.plot(self.md.adjusted.x, self.md.adjusted.y, label="Исходный")
                self.sc_1.axes.legend(loc='lower right')
                self.label.setStyleSheet("color: rgb(255, 0, 0)")
                self.label.setText("OFF")
            self.sc_1.axes.grid()
            self.sc_1.axes.legend(loc='lower right')
            self.sc_1.axes.set_xlabel("E")
            self.sc_1.axes.set_ylabel("I")
            self.sc_1.draw()
            status = True
        else:
            self.spline_display_radio_button.setChecked(False)
            QMessageBox.critical(self, "Ошибка ", "Сплайн не выполнен!",
                                 QMessageBox.Ok)
        return status

    def ex_click(self):
        self.flag = False
        self.cancel_button.setEnabled(False)
        self.visual_controler(True, [0, 1, 2, 3, 4, 6, 7, 8, 9])

    def click_for_graph(self, event):
        if self.flag:
            self.points.append((event.xdata, event.ydata))
        if len(self.points) == 2:
            self.flag = False
            nums = []
            for i in self.points:
                nums.append(self.ser.search_index(self.md.adjusted.x, i[0]))
            self.points.clear()
            if nums[1] - nums[0] > 0:
                x = self.md.adjusted.x[nums[0]:nums[1] + 1]
                y = self.md.adjusted.y[nums[0]:nums[1] + 1]
                if len(x) > 15:
                    self.md.adjusted.x = x
                    self.md.adjusted.y = y
                    self.sc_1.axes.clear()
                    self.sc_1.axes.plot(x, y, label="Входной")
                    self.sc_1.axes.legend(loc='lower right')
                    self.sc_1.axes.set_xlabel("E")
                    self.sc_1.axes.set_ylabel("I")
                    self.sc_1.axes.grid()
                    self.visual_controler(True)
                    self.sc_1.draw()

                    self.md.input.x = self.md.input.x[nums[0]:nums[1] + 1]
                    self.md.input.y = self.md.input.y[nums[0]:nums[1] + 1]
                else:
                    self.visual_controler(True)
                    QMessageBox.critical(self, "Ошибка ", "Выбран критически большой диапозон",
                                         QMessageBox.Ok)
            else:
                self.visual_controler(True)
                QMessageBox.critical(self, "Ошибка ", "Некорректный выбор точек",
                                     QMessageBox.Ok)

    def visual_controler(self, state, widget_nums=None):
        if widget_nums is None:
            widget_nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        for wid in widget_nums:
            self.widgets.get(wid).setEnabled(state)

    def open_file(self):
        self.visual_controler(False, [4])

        path = QFileDialog.getOpenFileName()
        if path[0] == '':
            QMessageBox.critical(self, "Ошибка", "Файл не был выбран!", QMessageBox.Ok)
        else:
            self.ser.read_file(path[0], self.md)
            if len(self.md.input.x) > 0:
                try:
                    s = round(float(self.lineEdit_2.text()), 2)
                    if s * 100 in range(1, 50001):
                        self.ser.perform_area_correction(s, self.md)
                        self.sc_1.axes.clear()
                        self.sc_1.axes.plot(self.md.adjusted.x, self.md.adjusted.y, label="Входной")
                        self.sc_1.axes.legend(loc='lower right')
                        self.sc_1.axes.set_xlabel("E")
                        self.sc_1.axes.set_ylabel("I")
                        self.sc_1.axes.grid()
                        self.sc_1.draw()

                        self.visual_controler(True, [4, 2, 0, 8, 9])

                        self.label_33.setText(self.ser.get_file_name(path[0]))
                        self.label_32.setText("Вы работаете с файлом")
                        self.label_29.setStyleSheet("color: rgb(0, 255, 0)")
                        self.label_29.setText("ON_")
                    else:
                        QMessageBox.critical(self, "Ошибка ",
                                             "Выход из диапозона значений в разделе \"Площадь электрода\"",
                                             QMessageBox.Ok)
                except ValueError:
                    QMessageBox.critical(self, "Ошибка ", "Некорректные данные в разделе \"Площадь электрода\"",
                                         QMessageBox.Ok)
            else:
                QMessageBox.critical(self, "Ошибка ", "Ошибка файла",
                                     QMessageBox.Ok)
