#linewidget.py
'''
Option 1: Derive from QGraphicsProxyWidget and in the mouse functions (mouseMove, ...) you can call 
QGraphicsItem::mouseMove() again, this should bring back again the functionality of moving the Widget.
Option 2: This is more like a workaround, but in most cases the better solution, because it prevents 
you from managing the events as it would be necessary by option 1. Just create a GraphicsRectItem R, i
which is larger than your Widget W. Set R movable etc. Add W to your scene, you will receive a 
QGraphicsProxyWidget P. Call P->setParentItem(R) and finally scene->AddItem(R);
Now your Widget can be moved by moving the parent rectangle. You can also add additional 
GraphicsRectIrems r which have R as parent, e.g. to implement a resizing function. 
You would just have to install an EventFilter for r and react on the mouseMove event in the 
filter function.
'''

import math
import random
from PyQt5.QtCore import(
    Qt,
    QRectF,
    QPointF,
    QPoint,
    pyqtSignal
)
from PyQt5.QtGui import(
    QFont,
    QPainter
)
from PyQt5.QtWidgets import (
    QWidget,
    QGraphicsObject,
    QGraphicsProxyWidget,
    QLCDNumber,
    QPushButton,
    QVBoxLayout, 
    QLabel,
    QSlider,
    QGraphicsTextItem
    )

class Line(QWidget):
    tickSignal = pyqtSignal(float)

    #BoundingRect = QRectF(-width/2,-height/2,width,height)
    def __init__(self,w=1000,scale=1.0,parent=None):
        super(Line, self).__init__()
        self.w = w 
        #self.setAcceptHoverEvents(True)
        vbox = QVBoxLayout()
        self.lcdRadians = QLCDNumber(self)
        vbox.addWidget(self.lcdRadians)
        self.lcdDegrees = QLCDNumber(self)
        vbox.addWidget(self.lcdDegrees)
        slider = QSlider(Qt.Horizontal,self)
        slider.setRange(0,self.w)
        slider.setMaximumWidth(self.w*2*math.pi)

        #slider.valueChanged.connect(lcd.display)
        slider.valueChanged.connect(self.valueChanged)
        slider.setTickInterval(self.w/16)
        slider.setTickPosition(QSlider.TicksBelow)
        slider.setPageStep(self.w/16)
        vbox.addWidget(slider)
        self.setLayout(vbox)
        #self.resize(self.w,self.height())
        #self.setWidget(widget)

    def connectFunc(self,fn):
        self.tickSignal.connect(fn)

    def valueChanged(self,value):
        self.lcdRadians.display((2*math.pi*value)/self.w)
        self.lcdDegrees.display((180*self.lcdRadians.value()/math.pi))
        self.tickSignal.emit(2*math.pi*value/self.w)

    def onLeftClick(self,f):
        if not hasattr(self,'leftClickF'):
            self.leftClickF = []
        self.leftClickF.append(f)
        return self

    def onRightClick(self,f):
        if not hasattr(self,'rightClickF'):
            self.rightClickF = []
        self.rightClickF.append(f)
        return self

    def leftClick(self,event):
        self.currentClickPosition = event.pos()

    def rightClick(self,event):
        #self.currentClickPosition = QPointF(event.pos().x(),-event.pos().y())
        self.currentClickPosition = event.pos()

    def hoverMoveEvent(self,event):
        self.currentHoverPosition = event.pos()
        self.update()
        super(Line,self).hoverMoveEvent(event)

    def mouseMoveEvent(self,event):
        self.currentMovePosition = event.pos()
        super(Line,self).mouseMoveEvent(event)
        self.update()

    def mousePressEvent(self,event):
        if event.button() == Qt.LeftButton:
            self.leftClick(event)
            if hasattr(self,'leftClickF'):
                for f in self.leftClickF:
                    f(event)
        if event.button() == Qt.RightButton:
            self.rightClick(event)
            if hasattr(self,'rightClickF'):
                for f in self.rightClickF:
                    f(event)
        super(Line,self).mousePressEvent(event)
        self.update()

    def movable(self,m=True):
        self.setFlag(QGraphicsObject.ItemIsMovable,m)
        return self

    def selectable(self,m=True):
        self.setFlag(QGraphicsObject.ItemIsSelectable,m)
        return self

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(Qt.white)
        painter.setPen(Qt.blue)
        painter.drawRect(self.rect())
        painter.setPen(Qt.red)
        painter.drawLine(self.rect().left(),
                        self.rect().bottom(),
                        self.rect().right(),
                        self.rect().bottom()
                        )
#        super(Line,self).paintEvent(event)
