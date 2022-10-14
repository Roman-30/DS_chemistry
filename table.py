from PyQt5 import QtWidgets
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

from Canvas import *
from listeners import ButtonListeners
from services import *


class UiMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('project_chemistry.ui', self)
        self.setMinimumSize(900, 600)
        self.flag = False
        self.points = []
        self.sc_1 = MplCanvas(dpi=80)
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
                        4: self.cut_button,  #
                        5: self.cancel_button,
                        6: self.open_button,
                        7: self.calculate_button,
                        8: self.spline_button,
                        9: self.change_button}

        self.md = GraphModel()

        self.listener = ButtonListeners(self)
        self.listener.butt_func()
        self.listener.visual_controler(False, [0, 2, 3, 4, 5, 7, 8, 9])

        self.label_29.setStyleSheet("color: rgb(255, 0, 0)")
        self.label_29.setText("OFF")

        self.label.setStyleSheet("color: rgb(255, 0, 0)")
        self.label.setText("OFF")
