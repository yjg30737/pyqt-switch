# pyqt-switch
PyQt Switch (O ) -> ( O)

You can choose the option to set the colorizing/moving animation.

## Requirements
PyQt5 >= 5.8

## Setup
`python -m pip install pyqt-switch`

## Feature
* Provide `toggled(bool)` signal
* Set the animation with `setAnimation(f: bool)`. Default is False.
* Set the diameter of circle-shaped switch button with `setCircleDiameter(diameter: int)`. Default is 20(px).

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

https://user-images.githubusercontent.com/55078043/169001914-0b86407a-5670-4ae4-ac28-54ec85460bc0.mp4

If you set the circle diameter to 40 with `switch.setCircleDiameter(40)`

![image](https://user-images.githubusercontent.com/55078043/169002295-8717adf8-a1e6-4126-8ef9-42ff8bb3988c.png)







