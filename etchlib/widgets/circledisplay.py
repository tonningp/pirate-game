#radian.py
import math
from random import randint
from PyQt5.QtCore import(
    Qt,
    QRectF,
    QPointF,
    QPoint,
    pyqtSignal,
    pyqtSlot
)
from PyQt5.QtGui import(
    QFont,
    QPen,
    QBrush,
    QFontMetrics,
    QColor
)
from PyQt5.QtWidgets import (
    QGraphicsObject,
    QGraphicsTextItem
    )

data = [
{   
    'text':'Find the <span style="font-weight:bold;">circumference</span>. Use 3.14 as an approximation for π.<br> A correct answer would look like 4.78 in.',
    'type' : 'circum-approx',
    'measure' : 'circumference',
    'precision' : 'approximation',
    'diameter' : False,
    'units' : 'in',
    'radius' : 0,
    'answer' : 0
},
{   
    'text':'Find the <span style="font-weight:bold;">circumference</span> in terms of π and the unit of measurement.<br>Type "pi" in for π so that "7.00π m" would look like "7.00pi m".',
    'type' : 'circum-exact',
    'measure' : 'circumference',
    'precision' : 'exact',
    'diameter' : False,
    'units' : 'in',
    'radius' : 0,
    'answer' : 0
},
{   
    'text':'Find the <span style="font-weight:bold;">area</span> in terms of π and the unit of measurement.<br>Type "pi" in for π so that "56.25π m<sup>2</sup>" would look like "56.25pi m^2".',
    'type' : 'area-exact',
    'measure' : 'area',
    'precision' : 'exact',
    'diameter' : False,
    'units' : 'in',
    'radius' : 0,
    'answer' : 0
},
{   
    'text':'Find the <span style="font-weight:bold;">area</span>. Use 3.14 as an approximation for π.<br> A correct answer would look like 314.00 in^2.',
    'type' : 'area-approx',
    'measure' : 'area',
    'precision' : 'approximation',
    'diameter' : False,
    'units' : 'in',
    'radius' : 0,
    'answer' : 0
}
]

units = ['in', 'ft','cubits','yards','furlongs','leagues','m','cm','km','mi','mm','parsecs']

class Circle(QGraphicsObject):
    tickSignal = pyqtSignal(int)
    clickSignal = pyqtSignal(int)

    #BoundingRect = QRectF(-width/2,-height/2,width,height)
    def __init__(self,w=1000,scale=1.0,parent=None):
        super(Circle, self).__init__()
        self.w = w
        self.rect = self.boundingRect()
        self.center = self.rect.center()
        self.radius = self.rect.width()/2
        self.currentValue = 0
        self.setAcceptHoverEvents(True)
        self.random_question()

    def random_question(self,signal=None):
        index = randint(0,len(data)-1)
        data[index]['radius'] = randint(1,50)
        data[index]['diameter']  = randint(0,1)
        data[index]['units'] = units[randint(0,len(units)-1)]
        if data[index]['type'] == 'circum-approx':
            data[index]['answer'] = '{0:.2f} {1}'.format(data[index]['radius'] /(data[index]['diameter']+1) * 6.28,data[index]['units'])
        elif data[index]['type'] == 'circum-exact':
            data[index]['answer'] = '{0:.2f}pi {1}'.format(float(data[index]['radius']/(data[index]['diameter']+1) * 2) ,data[index]['units'])
        elif data[index]['type'] == 'area-exact':
            data[index]['answer'] = '{0:.2f}pi {1}'.format(float((data[index]['radius']/(data[index]['diameter']+1))**2),'{0}^2'.format(data[index]['units']))
        elif data[index]['type'] == 'area-approx':
            data[index]['answer'] = '{0:.2f} {1}'.format((data[index]['radius'] /(data[index]['diameter']+1)) ** 2*3.14,'{0}^2'.format(data[index]['units']))
        self.question_index = index
        self.update()
        if signal:
            signal.emit(data[index])
        return data[index]

    def produce(self):
        return self.random_question()

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
        self.random_question()

    def hoverMoveEvent(self,event):
        self.currentHoverPosition = event.pos()
        super(Circle,self).hoverMoveEvent(event)
        self.update()

    def mouseMoveEvent(self,event):
        self.currentMovePosition = event.pos()
        super(Circle,self).mouseMoveEvent(event)
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
        super(Circle,self).mousePressEvent(event)
        self.update()

    def valueChanged(self,value):
        self.currentValue = value
        self.update()

    def toRad(self,deg):
        return deg*math.pi/180
        
    def boundingRect(self):
        return QRectF(-self.w/2,-self.w/2,self.w,self.w)

    def movable(self,m=True):
        self.setFlag(QGraphicsObject.ItemIsMovable,m)
        return self

    def selectable(self,m=True):
        self.setFlag(QGraphicsObject.ItemIsSelectable,m)
        return self

    # def drawText(self,painter, x, y,flags,text,boundingRect = 0):
    #     size = 32767.0
    #     corner = QPointF(x, y - size)
    #     if flags & Qt.AlignHCenter: 
    #         corner -= QPointF(size/2.0,0)
    #     elif flags & Qt.AlignRight:
    #         corner -= QPointF(size,0)
    #     if flags & Qt.AlignVCenter:
    #         corner += QPointF(0,size/2.0)
    #     elif flags & Qt.AlignTop:
    #         corner += QPointF(0,size)
    #     else:
    #         flags |= Qt.AlignBottom
    #     rect = QRectF(corner.x(), corner.y(), size, size)
    #     #painter.drawText(rect, text, flags, boundingRect)
    #     painter.drawText(rect, text)
    def drawText(self,painter,point,font,flags,text):
        fm = QFontMetrics(font)
        boundingRect = self.boundingRect()
        boundingRect.setHeight(boundingRect.height()/3)
        painter.setFont(font)
        painter.drawText(boundingRect,flags,text)

    def paint(self, painter, option, widget):
        painter.setBrush(QColor('AliceBlue'))
        painter.drawEllipse(self.rect)
        painter.setPen(QPen(QColor('Indigo'), 3))
        self.drawText(painter,self.center,QFont('Helvetica',48),Qt.AlignHCenter+Qt.AlignVCenter+Qt.AlignBottom,
                         '{0}\n{1}'.format(data[self.question_index]['measure'].title(),data[self.question_index]['precision'].title()))
        painter.setFont(QFont('Helvetica',48))
        painter.drawText(self.center-QPointF(10,30),
                         '{0:.2f} {1}'.format(data[self.question_index]['radius'],data[self.question_index]['units']))
        painter.setPen(QPen(QColor('Navy'), 2))
        painter.drawLine(self.center.x(),
                    self.center.y(),
                    self.center.x()+(math.cos(0)*self.radius),
                    self.center.y()-(math.sin(0)*self.radius)) 
        if data[self.question_index]['diameter'] == 1:
            painter.drawLine(self.center.x(),
                         self.center.y(),
                         self.center.x()+(math.cos(math.pi)*self.radius),
                         self.center.y()-(math.sin(math.pi)*self.radius))

        

        # if hasattr(self,'currentHoverPosition'):
        #     size = self.radius * .05
        #     painter.setBrush(Qt.blue)
        #     origin_x = -self.w/2
        #     origin_y = -self.w/2
        #     print(self.currentHoverPosition)
        #     painter.drawEllipse(QRectF(math.cos(self.currentHoverPosition.x()-origin_x)*self.radius,
        #                                math.sin(self.currentHoverPosition.y()-origin_y)*self.radius,size,size))
        #if hasattr(self,'currentClickPosition'):
        #    size = self.radius * .05
        #    painter.setBrush(Qt.red)
        #    painter.drawEllipse(QRectF(self.currentClickPosition.x()-size/2,
        #                                self.currentClickPosition.y()-size/2,size,size))
