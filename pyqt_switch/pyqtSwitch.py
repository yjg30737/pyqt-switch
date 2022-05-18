from PyQt5.QtCore import Qt, pyqtSignal, QPropertyAnimation, QPoint, QAbstractAnimation

from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout, QHBoxLayout


class PyQtSwitch(QWidget):
    toggled = pyqtSignal(bool)

    def __init__(self):
        super().__init__()
        self.__initVal()
        self.__initUi()

    def __initVal(self):
        self.__btn_width = 20
        self.__btn_height = 20
        self.__animationEnabledFlag = False
        self.__pointAnimation = ''
        self.__colorAnimation = ''

    def __initUi(self):
        self.__btn = QPushButton()
        self.__btn.setCheckable(True)
        self.__btn.setFixedSize(self.__btn_width, self.__btn_height)
        self.__btn.toggled.connect(self.__toggled)

        self.__layForBtnAlign = QHBoxLayout()
        self.__layForBtnAlign.setAlignment(Qt.AlignLeft)
        self.__layForBtnAlign.addWidget(self.__btn)
        self.__layForBtnAlign.setContentsMargins(0, 0, 0, 0)

        innerWidgetForStyle = QWidget()
        innerWidgetForStyle.setLayout(self.__layForBtnAlign)
        self.setStyleSheet(f'QWidget {{ border: 1px solid #AAAAAA; border-radius: {self.__btn_height // 2}px; }}')

        lay = QGridLayout()
        lay.addWidget(innerWidgetForStyle)
        lay.setContentsMargins(0, 0, 0, 0)

        self.setLayout(lay)
        self.setFixedSize(self.__btn_width * 2, self.__btn_height)

    def setAnimation(self, f: bool):
        self.__animationEnabledFlag = f
        if self.__animationEnabledFlag:
            self.__colorAnimation = QPropertyAnimation(self, b'point')
            self.__colorAnimation.valueChanged.connect(self.__btn.move)
            self.__colorAnimation.setDuration(100)
            self.__colorAnimation.setStartValue(QPoint(0, 0))
            self.__colorAnimation.setEndValue(QPoint(self.__btn_width, 0))

            self.__pointAnimation = QPropertyAnimation(self, b'color')
            self.__pointAnimation.valueChanged.connect(self.__styleInit)
            self.__pointAnimation.setDuration(100)
            self.__pointAnimation.setStartValue(255)
            self.__pointAnimation.setEndValue(200)

    def mousePressEvent(self, e):
        self.__btn.toggle()
        return super().mousePressEvent(e)

    def __toggled(self, f):
        if self.__animationEnabledFlag:
            if f:
                self.__colorAnimation.setDirection(QAbstractAnimation.Forward)
                self.__colorAnimation.start()
                self.__pointAnimation.setDirection(QAbstractAnimation.Forward)
                self.__pointAnimation.start()
            else:
                self.__colorAnimation.setDirection(QAbstractAnimation.Backward)
                self.__colorAnimation.start()
                self.__pointAnimation.setDirection(QAbstractAnimation.Backward)
                self.__pointAnimation.start()
        else:
            if f:
                self.__btn.move(self.__btn_width, 0)
                self.__layForBtnAlign.setAlignment(Qt.AlignRight)
                self.__styleInit(200)
            else:
                self.__btn.move(0, 0)
                self.__layForBtnAlign.setAlignment(Qt.AlignLeft)
                self.__styleInit(255)
        self.toggled.emit(f)

    def __styleInit(self, f: int):
        self.__btn.setStyleSheet(f'QPushButton {{ background-color: rgb({f}, {f}, 255); }}')