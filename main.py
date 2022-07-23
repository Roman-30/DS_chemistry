from PyQt5 import QtWidgets

#todo образка(исклячение)
#todo пустой файл

from table import UiMainWindow

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ui = UiMainWindow()
    ui.show()
    sys.exit(app.exec_())
