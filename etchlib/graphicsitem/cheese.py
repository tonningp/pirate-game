#!/usr/bin/env python3
import math
from PyQt5.QtCore import *
from PyQt5.QtGui import (QPainter, QColor,
QPen,QIcon,QBrush,QPixmap,QPainterPath,QImage,QFont,QFontMetrics)
from PyQt5.QtWidgets import (QWidget,QAction, QLCDNumber, QSlider, 
    QApplication,QMainWindow,QPushButton,QFrame,
    QGridLayout,QVBoxLayout, 
    QLabel,QSizePolicy,QGraphicsScene,QGraphicsView,
    QGraphicsTextItem,QGraphicsItem,QGraphicsObject,QGraphicsPixmapItem,
    QGraphicsProxyWidget,
    QMessageBox,
    QLineEdit,QFormLayout,QGroupBox,
    QRadioButton,QButtonGroup,QComboBox,QSizePolicy,
    QDialog)
from PyQt5.QtSvg import QGraphicsSvgItem,QSvgRenderer

from etchlib.dialogs import QuestionDialog



class Item(QGraphicsPixmapItem):

    mouseCollision = False
    questionAnswered = False
    correct_label = ''

    def __init__(self,view=None,question=None,position=None):
        super(Item, self).__init__()
        self.view = view
        self.question = question
        if position:
            self.setPos(position)
        self.setPixmap(QPixmap(':/images/cheeseImage.png'))
        self.setScale(0.10)
        self.final = False
        #self.setFlag(QGraphicsItem.ItemIsMovable,True)
        #self.setFlag(QGraphicsItem.ItemIsSelectable,True)
    
    def setView(self,view):
        self.view = view

    def hasEntered(self):
        return self.entered

    def sceneEvent(self,event):
        return super(Item,self).sceneEvent(event)

    def paint(self, painter, option, widget):
        super(Item,self).paint(painter,option,widget)
        if self.mouseCollision:
            pen = QPen(Qt.blue,20,Qt.SolidLine,Qt.RoundCap,Qt.RoundJoin)
            painter.setPen(pen)
            painter.drawRect(self.boundingRect())

    def checkCollision(self,obj):
        if obj in self.scene().collidingItems(self):
            if not self.mouseCollision:
                self.dialog = QuestionDialog(self.question,self.view)
                self.dialog.hide()
                self.mouseCollision = True
                self.entered = True
                self.dialog.exec_()
                if self.dialog.correct and not self.final:
                    self.setPos(-350,-400)
                    self.hide()
                if self.final:
                    self.correctlabel = self.dialog.correctlabel
                self.dialog.reset()
        else:
            self.mouseCollision = False
            self.entered = False

        self.update()

