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

from PyQt5.QtPrintSupport import QPrinter

from PyQt5.QtWidgets import (
        QApplication,
        QGraphicsView,
        QMainWindow,
        QAction,
        QVBoxLayout
)


class View(QGraphicsView):

    def __init__(self,parent=None):
        super(View,self).__init__(parent)
        from sys import platform as _platform
        if _platform == "linux" or _platform == "linux2":
        # linux
            self.pdfReader = 'xpdf'
        elif _platform == "darwin":
            self.pdfReader = 'open'
        # MAC OS X
        elif _platform == "win32":
            pass
        # Windows
        self.parent = parent
        self.setRenderHint(QPainter.Antialiasing)
        self.setCursor(Qt.CrossCursor)
        self.setCacheMode(QGraphicsView.CacheBackground)
        self.setViewportUpdateMode(QGraphicsView.BoundingRectViewportUpdate)
        #self.setDragMode(QGraphicsView.ScrollHandDrag)
        self.setMouseTracking(True) 
#        self.parent.updateStatusBar("Ready")
        
    def resizeEvent(self, event):
        super(View, self).resizeEvent(event)
        self.fitInView(self.sceneRect(), Qt.KeepAspectRatio)

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
        os.system(self.pdfReader+" out.pdf")

    def showEditor(self):
        print('self.showEditor')

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.NoButton:
            scenePos = self.mapToScene(QPoint(event.x(),event.y()))
#            self.parent.updateStatusBar("({},{}) -\
# ({},{})".format(event.x(),event.y(),scenePos.x(),scenePos.y()))
        #elif event.buttons() == Qt.LeftButton:
        #    self.parent.updateStatusBar("Left click drag")
        #elif event.buttons() == Qt.RightButton:
        #    self.parent.updateStatusBar("Right click drag")
        super(View, self).mouseMoveEvent(event)



