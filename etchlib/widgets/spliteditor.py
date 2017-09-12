#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import sip

from PyQt5.QtCore import (
        Qt,
        QRectF,
        QObject,
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
        QWidget,
        QGraphicsView,
        QPushButton,
        QVBoxLayout, 
        QHBoxLayout, 
        QFrame, 
        QSplitter, 
        QLabel, 
        QGraphicsItem, 
        QGraphicsProxyWidget, 
        QMessageBox, 
        QTabWidget,
        QSizePolicy
)

from PyQt5.Qsci import QsciScintilla, QsciLexerPython, QsciLexerCPP

class Editor(QsciScintilla):
    """
http://pyqt.sourceforge.net/Docs/QScintilla2/classQsciScintilla.html

    """
    ARROW_MARKER_NUM = 8

    def __init__(self, parent=None):
        super(Editor, self).__init__(parent)
        self.parent = parent
        self.setFrameShape(QFrame.StyledPanel)
        self.initUI()

    def initUI(self):
        # Set the default font
        font = QFont()
        font.setFamily('Courier')
        font.setFixedPitch(True)
        font.setPointSize(10)
        self.setFont(font)
        self.setMarginsFont(font)

        # Margin 0 is used for line numbers
        fontmetrics = QFontMetrics(font)
        self.setMarginsFont(font)
        self.setMarginWidth(0, fontmetrics.width("00000") + 6)
        self.setMarginLineNumbers(0, True)
        self.setMarginsBackgroundColor(QColor("#cccccc"))

        # Clickable margin 1 for showing markers
        self.setMarginSensitivity(1, True)
#        self.connect(self,
#            SIGNAL('marginClicked(int, int, Qt::KeyboardModifiers)'),
#            self.on_margin_clicked)
        self.markerDefine(QsciScintilla.RightArrow,
            self.ARROW_MARKER_NUM)
        self.setMarkerBackgroundColor(QColor("#ee1111"),
            self.ARROW_MARKER_NUM)

        # Brace matching: enable for a brace immediately before or after
        # the current position
        #
        self.setBraceMatching(QsciScintilla.SloppyBraceMatch)

        # Current line visible with special background color
        self.setCaretLineVisible(True)
        self.setCaretLineBackgroundColor(QColor("#ffe4e4"))

        # Set Python lexer
        # Set style for Python comments (style number 1) to a fixed-width
        # courier.
        #

        lexer = QsciLexerPython()
        #lexer = QsciLexerCPP()
        lexer.setDefaultFont(font)
        self.setLexer(lexer)

        text = bytearray(str.encode("Arial"))
# 32, "Courier New"         
        self.SendScintilla(QsciScintilla.SCI_STYLESETFONT, 1, text)

        # Don't want to see the horizontal scrollbar at all
        # Use raw message to Scintilla here (all messages are documented
        # here: http://www.scintilla.org/ScintillaDoc.html)
        self.SendScintilla(QsciScintilla.SCI_SETHSCROLLBAR, 0)

        # not too small
        #self.setMinimumSize(600, 450)


        sampleText = """# taken from : http://www.python-course.eu/k_nearest_neighbor_classifier.php 
import numpy as np
from sklearn import datasets
iris = datasets.load_iris()
iris_data = iris.data
iris_labels = iris.target
print(iris_data[0], iris_data[79], iris_data[100])
print(iris_labels[0], iris_labels[79], iris_labels[100])
np.random.seed(42)
indices = np.random.permutation(len(iris_data))
n_training_samples = 12
learnset_data = iris_data[indices[:-n_training_samples]]
learnset_labels = iris_labels[indices[:-n_training_samples]]
testset_data = iris_data[indices[-n_training_samples:]]
testset_labels = iris_labels[indices[-n_training_samples:]]
print(learnset_data[:4], learnset_labels[:4])
print(testset_data[:4], testset_labels[:4])

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
colors = ("r", "b")
X = []
for iclass in range(3):
    X.append([[], [], []])
    for i in range(len(learnset_data)):
        if learnset_labels[i] == iclass:
            X[iclass][0].append(learnset_data[i][0])
            X[iclass][1].append(learnset_data[i][1])
            X[iclass][2].append(sum(learnset_data[i][2:]))
colors = ("r", "g", "y")
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for iclass in range(3):
       ax.scatter(X[iclass][0], X[iclass][1], X[iclass][2], c=colors[iclass])
plt.show() 

"""
        self.setText(sampleText)






    def on_margin_clicked(self, nmargin, nline, modifiers):
        # Toggle marker for the line the margin was clicked on
        if self.markersAtLine(nline) != 0:
            self.markerDelete(nline, self.ARROW_MARKER_NUM)
        else:
            self.markerAdd(nline, self.ARROW_MARKER_NUM)

    def fixup(self,code):
        codeT = "from sandbox.python.mouse import Item\n"
        codeT += "mouse = Item()\n"
        codeT += code
        return codeT

    def runcode(self):
        import sys
        from io import StringIO
        import contextlib

        @contextlib.contextmanager
        def stdoutIO(stdout=None,stderr=None):
            oldStdout = sys.stdout
            oldStderr = sys.stderr
            #oldStderr = sys.stderr
            if stdout is None:
                stdout = StringIO()
                sys.stdout = stdout
                #sys.stderr = stdout
                yield stdout
            sys.stdout = oldStdout
            #sys.stderr = oldStderr

        code = self.text()
        with stdoutIO() as s:
            s.err = ''
            try:
                """
                import pipes
                import os
                currentdir = os.getcwd()
                os.chdir(currentdir+'/sandbox')
                infile = open('main.cpp','w')
                infile.write(code)
                infile.close()
                t = pipes.Template()
                #t.append('tr a-z A-Z','--')
                t.append('make run 2>&1','--')
                f = t.open('pipe','w')
                f.close()
                print('<strong>'+open('pipe').read().replace("\n",'<br>')+'</strong>')
                print('<div \
                        style="color:red;">'+open('errors.out','r').read().replace("\n",'<br>')+'</div>')
                os.chdir(currentdir)
                """
                codeText = self.fixup(self.text())
                code = compile(codeText,'<string>','exec')
                exec(code,globals())
                #mouse.move(-400,-400)
            except (
                    NameError,
                    SyntaxError,
                    AttributeError,
                    ImportError
                   ) as err:
                s.err = err

        return s

class View(QGraphicsView):

    def __init__(self,parent=None):
        super(View,self).__init__(parent)
        self.setFrameShape(QFrame.StyledPanel)
        self.parent = parent
        self.setRenderHint(QPainter.Antialiasing)
        self.setCursor(Qt.CrossCursor)
        self.setCacheMode(QGraphicsView.CacheBackground)
        self.setViewportUpdateMode(QGraphicsView.BoundingRectViewportUpdate)
        #self.setDragMode(QGraphicsView.ScrollHandDrag)
        self.setMouseTracking(True) 

    def mouseMoveEvent(self, event):
        super(View, self).mouseMoveEvent(event)

from PyQt5.QtWidgets import (
    QGraphicsScene
)

class Scene(QGraphicsScene):
    def __init__(self,SceneRect=QRectF(-50,-50,50,50)):
        super(Scene,self).__init__()
        self.setSceneRect(SceneRect)
        
class Console(QLabel):
    def __init__(self,parent=None):
        super(Console,self).__init__(parent)

    def setError(self,error):
        self.setTextFormat(Qt.RichText)
        template = '<span\
        style="font-size:24px;font-weight:600;color:#aa0000;">'
        template += "An exception of type {0} occurred. <br>\
        Arguments:<br>{1!r}</span>"
        message = template.format(type(error).__name__, error.args)
        self.setText(message)


class Main(QWidget):
    
    def __init__(self):
        super(Main,self).__init__()
        
        self.initUI()
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
        
    def initUI(self):      

        hbox = QHBoxLayout(self)
        self.tabs = QTabWidget(self)
        self.tabcollection = []
        self.tabs.resize(300,200)
        self.editor = Editor()
        self.tabcollection.append(self.editor)
        self.tabcollection.append(QWidget())
        self.tabs.addTab(self.tabcollection[0],"main.py")
        self.tabs.addTab(self.tabcollection[1],"+")
        self.view = View(self)
        self.scene = Scene()
        #dt = self.scene.addPixmap(QPixmap(':/images/desktop.png'))
        #dt.setPos(-450,-325)
        self.view.setScene(self.scene)

        self.console = Console(self)
        self.console.setFrameShape(QFrame.StyledPanel)

        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(self.tabs)
        splitter1.addWidget(self.view)
        splitter1.setSizes([100,200])

        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(self.console)
        splitter2.setSizes([500,50])
        hbox.addWidget(splitter2)
        self.setLayout(hbox)
        self.show()
        
    @pyqtSlot()
    def onRunCode(self):
        code = self.editor.runcode()
        text = self.scene.addText('')
        self.console.setText('')
        if code.err:
            self.console.setError(code.err)
        else:
            text.setHtml(code.getvalue())
        text.setFlag(QGraphicsItem.ItemIsMovable,True)
        text.setFlag(QGraphicsItem.ItemIsSelectable,True)
        text.setPos(-300,-300)

    @pyqtSlot()
    def onPrintPDF(self):
        import os
        printer = QPrinter(QPrinter.HighResolution)
        printer.setPaperSize(QPrinter.A4)
        printer.setOutputFormat(QPrinter.PdfFormat)
        printer.setOutputFileName("out.pdf")
        painter = QPainter(printer)
        self.view.render(painter)
        painter.end()
        os.system(self.pdfReader+" out.pdf")
        self.console.setText('Successfully rendered the scene')

    def onChanged(self, text):
        
        self.lbl.setText(text)
        self.lbl.adjustSize()        
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Editor()
    ex.setWindowTitle('QSplitter')
    sys.exit(app.exec_()) 

