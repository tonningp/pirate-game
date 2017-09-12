#!/usr/bin/env python3
import sys
from PyQt5.QtCore import (
        Qt,
        QTime,
        QPoint,
        qsrand,
        pyqtSlot
)
from PyQt5.QtGui import (
        QPainter, 
        QColor, 
        QPen,
        QIcon,
        QBrush,
        QPixmap,
        QImage,
        QFont,
        QFontMetrics
)

from PyQt5.QtWidgets import (
        QApplication,
        QGraphicsView,
        QMainWindow,
        QAction,
        QVBoxLayout
)

from PyQt5.QtPrintSupport import QPrinter


class View(QGraphicsView):

    def __init__(self,scene,parent=None):
        super(View,self).__init__(parent)
        self.parent = parent;
        self.scene = scene
        self.setScene(scene)
        self.setRenderHint(QPainter.Antialiasing)
        self.setBackgroundBrush(QBrush(QPixmap(':/images/cheese.jpg')))
        self.setCacheMode(QGraphicsView.CacheBackground)
        self.setViewportUpdateMode(QGraphicsView.BoundingRectViewportUpdate)
        self.setDragMode(QGraphicsView.ScrollHandDrag)
        self.setMouseTracking(True) 
        self.parent.updateStatusBar("Ready")
        
    def resizeEvent(self, event):
        super(View, self).resizeEvent(event)
        self.fitInView(self.sceneRect(), Qt.KeepAspectRatio)


    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.NoButton:
            scenePos = self.mapToScene(QPoint(event.x(),event.y()))
            self.parent.updateStatusBar("({},{}) -\
 ({},{})".format(event.x(),event.y(),scenePos.x(),scenePos.y()))
        elif event.buttons() == Qt.LeftButton:
            self.parent.updateStatusBar("Left click drag")
        elif event.buttons() == Qt.RightButton:
            self.parent.updateStatusBar("Right click drag")
        super(View, self).mouseMoveEvent(event)

    @pyqtSlot()
    def onPrintPDF(self):
        import os
        printer = QPrinter(QPrinter.HighResolution)
        printer.setPaperSize(QPrinter.A4)
        printer.setOutputFormat(QPrinter.PdfFormat)
        printer.setOutputFileName("out.pdf")
        painter = QPainter(printer)
        self.render(painter)
        painter.end()
        #self.console.setText('Successfully rendered the scene')
        os.system("xpdf out.pdf")



