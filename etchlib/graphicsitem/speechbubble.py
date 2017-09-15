#!/usr/bin/env python3

import math
import random
from etchlib.graphicsitem import svg
from PyQt5.QtCore import(
    Qt,
    QRectF,
    QPointF,
    pyqtSignal
)
from PyQt5.QtGui import(
    QFont
)
from PyQt5.QtWidgets import (
    QWidget,
    QGraphicsObject,
    QGraphicsProxyWidget,
    QGraphicsTextItem
    )

class Bubble(QGraphicsObject):

    def __init__(self,questions,scale=1.0,parent=None):
        super(Bubble, self).__init__()
        self.bubble = svg.Item(":/images/speech_bubble2.svg",scale,self)
        self.bubble.setPos(QPointF(self.boundingRect().left(),self.boundingRect().top()))
        self.questions = questions
        self.text = QGraphicsTextItem(self)
        displayText = "Arrr!!!<br>On September 19th,<br>we be pirates.<br>Talk Like a Pi-Rate"
        self.text.setHtml('<div style="font-family:Comic Sans MS;">'+displayText+'</div>')
        self.text.setPos(-75,-80)
        #self.button = QPushButton('Button', super(Bubble,self))
        #self.button.setToolTip('This is an example button')
        #self.button.move(100,70)



    def boundingRect(self):
        r = self.bubble.boundingRect()
        return QRectF(-r.width()/2,-r.height()/2,r.width()*(self.bubble.scale),r.height()*(self.bubble.scale))

    def movable(self,m=True):
        self.setFlag(QGraphicsObject.ItemIsMovable,m)
        return self

    def paint(self, painter, option, widget):
        painter.setBrush(Qt.blue)
