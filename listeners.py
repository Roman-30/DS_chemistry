from PyQt5.QtWidgets import QFileDialog, QMessageBox

from Thread import CustomThread
from services import *


class ButtonListeners:

    def __init__(self, mw):
        self.mw = mw

    def butt_func(self):
        self.mw.sc_1.figure.canvas.mpl_connect('button_press_event', self.click_for_graph)
        self.mw.cancel_button.clicked.connect(self.ex_click)
        self.mw.open_button.clicked.connect(self.open_file)
        self.mw.spline_display_radio_button.clicked.connect(self.click_radio_b)
        self.mw.spline_button.clicked.connect(self.make_spline)
        self.mw.change_button.clicked.connect(self.change_area)
        self.mw.calculate_button.clicked.connect(self.calculate)
        self.mw.cut_button.clicked.connect(self.cut_graph)

    def cut_graph(self):
        self.mw.cancel_button.setEnabled(True)
        self.mw.label.setText("OFF")
        self.mw.label.setStyleSheet("color: rgb(255, 0, 0)")

        draw_graph(self.mw.sc_1, self.mw.md.adjusted.x, self.mw.md.adjusted.y, "Исходный", "E", "I")

        self.visual_controler(False, [0, 1, 2, 3, 4, 6, 7, 8, 9])
        self.mw.points = []
        self.mw.flag = True

    def make_spline(self):
        try:
            num = int(self.mw.lineEdit.text())
            if num in range(5, 101):
                self.mw.md.spline = spline(self.mw.md, num)
                self.mw.spline_display_radio_button.setChecked(True)
                self.mw.label.setStyleSheet("color: rgb(0, 255, 0)")
                self.mw.label.setText("ON ")

                draw_graph(self.mw.sc_1, self.mw.md.spline.x, self.mw.md.spline.y, "Сплайн", "E", "I")

                self.visual_controler(True, [2, 3, 7])
            else:
                QMessageBox.critical(self.mw, "Ошибка ", "Выход из дозволенных значений в разделе \"Узлы сплайна\"",
                                     QMessageBox.Ok)
        except ValueError:
            QMessageBox.critical(self.mw, "Ошибка ", "Некорректные данные в разделе \"Узлы сплайна\"",
                                 QMessageBox.Ok)

    def change_area(self):
        try:
            self.mw.sc_1.axes.clear()
            s = round(float(self.mw.lineEdit_2.text()), 2)
            if s * 100 in range(1, 50001):
                self.mw.md.adjusted = perform_area_correction(s, self.mw.md)

                draw_graph(self.mw.sc_1, self.mw.md.adjusted.x, self.mw.md.adjusted.y, "Исходный", "E", "I")

            else:
                QMessageBox.critical(self.mw, "Ошибка ", "Выход из диапозона значений в разделе \"Площадь электрода\"",
                                     QMessageBox.Ok)
        except ValueError:
            QMessageBox.critical(self.mw, "Ошибка ", "Некорректные данные в разделе \"Площадь электрода\"",
                                 QMessageBox.Ok)

    def calculate(self):
        try:
            self.mw.md.E_cor = calculate_E_corrosivity(self.mw.md)
            num = int(self.mw.lineEdit_3.text())
            if num in range(1, 11):
                self.mw.calculate_button.setEnabled(False)
                self.mw.md.derivative = calculate_point_derivative(self.mw.md, num)
                self.mw.md.expired = calculate_final_graph(self.mw.md)
                self.mw.label_7.setText(str(round(self.mw.md.E_cor, 1)))
                self.mw.label_10.setText(str(round(self.mw.md.derivative, 0)))
                x = self.mw.md.expired.x
                y = self.mw.md.expired.y
                arr1 = []
                arr2 = []

                fault = 1

                try:
                    fault = int(self.mw.fault.text())
                    if fault <= 0 or fault >= 100:
                        QMessageBox.critical(self.mw, "Ошибка ",
                                             "Выход из диапозона значений погрешности расчета",
                                             QMessageBox.Ok)
                        fault = 1
                except:
                    QMessageBox.critical(self.mw, "Ошибка ",
                                         "Некорректные данные погрешности расчета",
                                         QMessageBox.Ok)

                th1 = CustomThread(4, 500, arr1, x, y, fault)
                th2 = CustomThread(500, 1001, arr2, x, y, fault)

                th1.run()
                th1.setDaemon(True)
                th2.run()
                th2.setDaemon(True)

                self.mw.md.b = arr1 + arr2
                if len(self.mw.md.b) > 0:

                    f = new_sequence(self.mw.md, self.mw.md.expired.x)
                    lq = calculate_between(f, self.mw.md)
                    map_key = search_min_map_num(lq)

                    self.mw.md.b_c = map_key[1]
                    self.mw.md.b_a = map_key[0]

                    self.mw.md.selection = Graph(self.mw.md.expired.x, f[map_key])

                    self.mw.sc_2.axes.clear()
                    self.mw.sc_2.axes.plot(self.mw.md.expired.x, self.mw.md.expired.y, label="Эксперимент")
                    self.mw.sc_2.draw()

                    self.mw.sc_2.axes.plot(self.mw.md.selection.x, self.mw.md.selection.y, label="Подбор")
                    self.mw.sc_2.axes.legend(loc='lower right')
                    self.mw.sc_2.axes.set_xlabel("ΔE")
                    self.mw.sc_2.axes.set_ylabel("Y = 2.3*Rp*i")
                    self.mw.sc_2.axes.grid()
                    self.mw.sc_2.draw()
                    self.mw.sc_2.fig.tight_layout()

                    self.mw.md.B = calculate_b(self.mw.md)
                    self.mw.md.I_cor = calculate_i_cor(self.mw.md)

                    self.mw.label_13.setText(str(self.mw.md.b_a))
                    self.mw.label_16.setText(str(self.mw.md.b_c))
                    self.mw.label_20.setText(str(round(self.mw.md.B, 1)))
                    self.mw.label_23.setText(str(round(self.mw.md.I_cor, 4)))
                    self.mw.label_27.setText(str(round(calculate_deviation(self.mw.md), 3)))

                    self.mw.calculate_button.setEnabled(True)
                else:
                    QMessageBox.information(self.mw, "Информация", "Для данного промежутка подбор не был найдет")
                    self.mw.fault.setEnabled(True)
                    self.mw.calculate_button.setEnabled(True)
            else:
                QMessageBox.critical(self.mw, "Ошибка ",
                                     "Выход из диапозона значений в разделе \"Интервал дифференцирования\"",
                                     QMessageBox.Ok)
        except ValueError:
            QMessageBox.critical(self.mw, "Ошибка ", "Некорректные данные в разделе \"Интервал дифференцирования\"",
                                 QMessageBox.Ok)

    def click_radio_b(self):
        status = False
        if len(self.mw.md.spline.x) > 0:
            if self.mw.spline_display_radio_button.isChecked():
                draw_graph(self.mw.sc_1, self.mw.md.spline.x, self.mw.md.spline.y, "Сплайн", "E", "I")
                self.mw.label.setStyleSheet("color: rgb(0, 255, 0)")
                self.mw.label.setText("ON ")
            else:
                draw_graph(self.mw.sc_1, self.mw.md.adjusted.x, self.mw.md.adjusted.y, "Исходный", "E", "I")
                self.mw.label.setStyleSheet("color: rgb(255, 0, 0)")
                self.mw.label.setText("OFF")
            status = True
        else:
            self.mw.spline_display_radio_button.setChecked(False)
            QMessageBox.critical(self.mw, "Ошибка ", "Сплайн не выполнен!",
                                 QMessageBox.Ok)
        return status

    def ex_click(self):
        self.mw.flag = False
        self.mw.cancel_button.setEnabled(False)
        self.visual_controler(True, [0, 1, 2, 3, 4, 6, 7, 8, 9])

    def click_for_graph(self, event):
        if self.mw.flag:
            self.mw.points.append((event.xdata, event.ydata))
        if len(self.mw.points) == 2:
            self.mw.flag = False
            nums = []
            for i in self.mw.points:
                nums.append(search_index(self.mw.md.adjusted.x, i[0]))
            self.mw.points.clear()
            if nums[1] - nums[0] > 0:
                x = self.mw.md.adjusted.x[nums[0]:nums[1] + 1]
                y = self.mw.md.adjusted.y[nums[0]:nums[1] + 1]
                if len(x) > 30:
                    self.mw.md.adjusted.x = x
                    self.mw.md.adjusted.y = y

                    draw_graph(self.mw.sc_1, x, y, "Входной", "E", "I")

                    self.visual_controler(True)
                    self.mw.md.input.x = self.mw.md.input.x[nums[0]:nums[1] + 1]
                    self.mw.md.input.y = self.mw.md.input.y[nums[0]:nums[1] + 1]

                    self.visual_controler(False, [2, 3, 5, 7])
                else:
                    QMessageBox.critical(self.mw, "Ошибка ", "Выбран критически большой диапозон",
                                         QMessageBox.Ok)
                    self.visual_controler(True, [0, 1, 4, 8, 9])
                    self.mw.cancel_button.setEnabled(False)
            else:
                self.visual_controler(True)
                QMessageBox.critical(self.mw, "Ошибка ", "Некорректный выбор точек",
                                     QMessageBox.Ok)

    def visual_controler(self, state, widget_nums=None):
        if widget_nums is None:
            widget_nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        for wid in widget_nums:
            self.mw.widgets.get(wid).setEnabled(state)

    def open_file(self):
        file_path = QFileDialog.getOpenFileName()
        file_name = get_file_name(file_path[0])
        file_type = get_file_type(file_name)

        self.visual_controler(False, [4])
        self.mw.fault.setText("1")
        self.mw.fault.setEnabled(False)

        if file_path[0] == '' or not (file_type in ['dat', 'txt']):
            QMessageBox.critical(self.mw, "Ошибка", "Файл не был выбран!", QMessageBox.Ok)
        else:
            self.mw.md.input = read_file(file_path[0])
            if len(self.mw.md.input.x) > 0:
                try:
                    s = round(float(self.mw.lineEdit_2.text()), 2)
                    if s * 100 in range(1, 50001):
                        self.mw.md.adjusted = perform_area_correction(s, self.mw.md)

                        draw_graph(self.mw.sc_1, self.mw.md.adjusted.x, self.mw.md.adjusted.y, "Входной", "E", "I")

                        self.visual_controler(True, [4, 2, 0, 8, 9])

                        self.mw.label_33.setText(get_file_name(file_path[0]))
                        self.mw.label_32.setText("Вы работаете с файлом")
                        self.mw.label_29.setStyleSheet("color: rgb(0, 255, 0)")
                        self.mw.label_29.setText("ON ")
                    else:
                        QMessageBox.critical(self.mw, "Ошибка ",
                                             "Выход из диапозона значений в разделе \"Площадь электрода\"",
                                             QMessageBox.Ok)
                except ValueError:
                    QMessageBox.critical(self.mw, "Ошибка ", "Некорректные данные в разделе \"Площадь электрода\"",
                                         QMessageBox.Ok)
            else:
                QMessageBox.critical(self.mw, "Ошибка ", "Ошибка файла",
                                     QMessageBox.Ok)
