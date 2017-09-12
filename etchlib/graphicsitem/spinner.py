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
    QGraphicsObject,
    QGraphicsTextItem
    )

class Spinner(QGraphicsObject):
    tickSignal = pyqtSignal(int)
    def __init__(self,file,scale=1.0,parent=None):
        super(Spinner, self).__init__()
        self.s = svg.Item(file,scale,self)
        self.s.setPos(self.s.pos().x(),-self.boundingRect().width()/4)
        self.rect = self.boundingRect()
        self.center = self.rect.center()
        self.radius = self.rect.width()/2
        self.numbers = []
        self.spinCount = 48
        self.currentSpin = 0
        div = 15
        for a in range(self.spinCount//2):
            angle = a*div + 5
            theta = angle*math.pi/180
            textPoint = QPointF(self.center.x() + self.radius*math.cos(theta)-20,self.center.y() + self.radius*math.sin(theta)-10)
            item = QGraphicsTextItem("{0}".format(angle),self)
            #item = QGraphicsTextItem("{0}".format(random.randint(0,500)),self)
            #item.setHtml('<span style="color:black;size:24px;font-weight:bold;">{0}</span>'.format(random.randint(0,100)))
            item.setFont(QFont("Helvetica [Cronyx]", 36))
            item.setDefaultTextColor(Qt.yellow)
            self.numbers.append(item)
            item.setPos(textPoint)
        for i in range(9):
            self.spin()
        self.currentSpin = 1

    def connectFunc(self,fn):
        self.tickSignal.connect(fn)

    def spin(self):
        for i in self.numbers:
            i.setDefaultTextColor(Qt.black)
        obj = self.s
        scale = obj.scale
        r = obj.boundingRect() 
        transform = obj.transform() \
                        .translate(scale*r.width()/2,scale*r.height()/2) \
                        .rotate(obj.rotation()+15) \
                        .translate(-scale*r.width()/2,-scale*r.height()/2)
        obj.setTransform(transform)
        self.tickSignal.emit(self.currentSpin)
        self.numbers[self.currentSpin%(self.spinCount//2)].setDefaultTextColor(Qt.yellow)
        self.currentSpin += 1
        if self.currentSpin > self.spinCount-1:
            self.currentSpin = 0


    def boundingRect(self):
        r = self.s.boundingRect()
        return QRectF(r.left(),r.top(),r.width()*(self.s.scale),r.width()*(self.s.scale))

    def movable(self,m=True):
        self.setFlag(QGraphicsObject.ItemIsMovable,m)
        return self

    def paint(self, painter, option, widget):
        painter.setBrush(Qt.blue)
        painter.drawEllipse(self.rect)
        div = 15
        for a in range(self.spinCount):
            angle = a*div
            theta = angle*math.pi/180
            startAngle = angle * 16
            spanAngle = div*16
            if a % 2:
                painter.setBrush(Qt.red)
                painter.setPen(Qt.red)
            else:
               painter.setBrush(Qt.blue)
               painter.setPen(Qt.blue)
            painter.drawPie(self.rect, startAngle, spanAngle);
        painter.drawEllipse(QRectF(self.rect.width()/2-50,self.rect.height()/2-50,100,100))
