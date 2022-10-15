from PyQt5 import QtWidgets

from table import UiMainWindow

#todo Динамическое изменение экрана
#todo Дотрисовщик графиков
#todo лайаут графиков
#todo панель загрузки


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ui = UiMainWindow()
    ui.show()
    sys.exit(app.exec_())
