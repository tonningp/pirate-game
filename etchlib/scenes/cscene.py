#!/usr/bin/env python3
import math

from PyQt5.QtCore import *
from PyQt5.QtGui import (
    QPainter, 
    QColor, 
    QPen,
    QIcon,
    QBrush,
    QPixmap,
    QPainterPath,
    QImage,
    QFont,
    QFontMetrics
)
from PyQt5.QtWidgets import (
    QWidget,
    QFrame,
    QMainWindow,
    QLCDNumber, 
    QSlider,
    QPushButton,
    QGridLayout,
    QVBoxLayout, 
    QLabel,
    QSizePolicy,
    QGraphicsScene,
    QGraphicsView,
    QGraphicsTextItem,
    QGraphicsItem,
    QGraphicsObject,
    QGraphicsPixmapItem,
    QGraphicsProxyWidget,
    QMessageBox,
    QLineEdit,
    QFormLayout,
    QGroupBox,
    QRadioButton,
    QButtonGroup,
    QComboBox,
    QSizePolicy,
    QDialog
)

from PyQt5.QtSvg import QGraphicsSvgItem,QSvgRenderer
from etchlib.widgets.editor import Widget as EditorWidget

class CScene(QGraphicsScene):
    def __init__(self):
        super(CScene,self).__init__()

    @pyqtSlot()
    def showEditor(self):
        self.editor.show();

    @pyqtSlot()
    def hideEditor(self):
        self.editor.hide();

