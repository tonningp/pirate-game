#!/usr/bin/env python3
import sip

from PyQt5.QtCore import *
from PyQt5.QtGui import QFont,QFontMetrics,QColor
from PyQt5.QtWidgets import (
        QWidget,
        QPushButton,
        QVBoxLayout, 
        QLabel, 
        QGraphicsItem, 
        QGraphicsProxyWidget, 
        QMessageBox, 
        QSizePolicy)
from PyQt5.Qsci import QsciScintilla, QsciLexerPython




class Editor(QsciScintilla):
    ARROW_MARKER_NUM = 8

    def __init__(self, parent=None):
        super(Editor, self).__init__(parent)

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
        self.setMinimumSize(600, 450)

    def on_margin_clicked(self, nmargin, nline, modifiers):
        # Toggle marker for the line the margin was clicked on
        if self.markersAtLine(nline) != 0:
            self.markerDelete(nline, self.ARROW_MARKER_NUM)
        else:
            self.markerAdd(nline, self.ARROW_MARKER_NUM)

class Widget(QGraphicsProxyWidget):
    def __init__(self):
        super(Widget,self).__init__()
        w = QWidget()
        self.editor = Editor()
        button = QPushButton("Run")
        button.clicked.connect(self.on_run)
        vbox = QVBoxLayout()
        vbox.addWidget(self.editor)
        vbox.addWidget(button)
        w.setLayout(vbox)
        self.setWidget(w)
        self.setFlag(QGraphicsItem.ItemIsMovable,True)
        self.setFlag(QGraphicsItem.ItemIsSelectable,True)

    def on_run(self):
        text = self.scene().addText(self.editor.text())
        text.setFlag(QGraphicsItem.ItemIsMovable,True)
        text.setFlag(QGraphicsItem.ItemIsSelectable,True)
        text.setPos(-300,-300)
