#!/usr/bin/env python3
from PyQt5.QtSvg import QGraphicsSvgItem,QSvgRenderer
from PyQt5.QtCore import pyqtSlot

from PyQt5.QtWidgets import (
    QGraphicsTextItem,QGraphicsItem,QGraphicsObject,QGraphicsPixmapItem,
    QGraphicsProxyWidget )

class Item(QGraphicsSvgItem):
    def __init__(self,file,scale=1.0,parent=None):
        super(Item, self).__init__(parent)
        self.scale = scale
        self.renderer = QSvgRenderer(file)
        self.setSharedRenderer(self.renderer)
        self.setScale(self.scale)

    def movable(self,m=True):
        self.setFlag(QGraphicsItem.ItemIsMovable,m)
        return self

    def onLeftClick(self,f):
    	if not hasattr(self,'leftClickF'):
    		self.leftClickF = []
    	self.leftClickF.append(f)
    	return self

    def mousePressEvent(self,event):
    	if hasattr(self,'leftClickF'):
    		for f in self.leftClickF:
    			f(event)
    	super().mousePressEvent(event)