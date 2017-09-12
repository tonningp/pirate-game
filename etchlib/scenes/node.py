#!/usr/bin/env python3

from etchlib.widgets.editor import Widget as EditorWidget
from etchlib.graphicsitems import *

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

class Scene(QGraphicsScene):

    def __init__(self):
        super(Scene,self).__init__()
        self.maintext = QGraphicsTextItem("Node Map")
        self.addItem(self.maintext)

