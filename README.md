# pyqt-switch
PyQt Switch (O ) -> ( O)

## Requirements
PyQt5 >= 5.8

## Setup
```pip3 install git+https://github.com/yjg30737/pyqt-switch.git --upgrade```

## Feature
* Provide ```toggled(bool)``` signal

## Example
Code Sample
```python
from PyQt5.QtWidgets import QWidget, QFormLayout, QApplication, QLabel
from pyqt_switch import PyQtSwitch


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        switch = PyQtSwitch()
        switch.toggled.connect(self.__toggled)

        self.__label = QLabel()
        self.__label.setText('No')
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
```

Result

https://user-images.githubusercontent.com/55078043/149455308-50950652-a175-41c0-b716-284b7de6a12e.mp4






