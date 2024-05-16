from PyQt5.QtWidgets import QWidget, QFormLayout, QApplication, QLabel
from pyqt_switch import PyQtSwitch


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        self.__label = QLabel()
        self.__label.setText('No')

        switch = PyQtSwitch()
        switch.toggled.connect(self.__toggled)
        switch.setAnimation(True)
        # switch.setChecked(True)
        # switch.setCircleDiameter(40)

        # if switch.isChecked():
        #     print('Yes')
        # else:
        #     print('No')

        lay = QFormLayout()
        lay.addRow(self.__label, switch)
        self.setLayout(lay)

    def __toggled(self, f):
        if f:
            self.__label.setText('Yes')
        else:
            self.__label.setText('No')


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    example = Widget()
    example.show()
    app.exec_()