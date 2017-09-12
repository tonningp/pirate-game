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

class Scene(QGraphicsScene):
    defaultRect = QRectF(-600,-600,600,600)
    def __init__(self,SceneRect=QRectF(-600,-600,600,600)):
        super(Scene,self).__init__()
        self.setSceneRect(SceneRect)

    def setOrigin(self,origin):
        self.grid.setOrigin(origin)
        self.update()

