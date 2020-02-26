# encoding: utf-8
# module PyQt5.QtWidgets
# from /usr/lib/python3/dist-packages/PyQt5/QtWidgets.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui


from .QWidget import QWidget

class QRubberBand(QWidget):
    """ QRubberBand(QRubberBand.Shape, parent: QWidget = None) """
    def changeEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ changeEvent(self, QEvent) """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def initStyleOption(self, QStyleOptionRubberBand): # real signature unknown; restored from __doc__
        """ initStyleOption(self, QStyleOptionRubberBand) """
        pass

    def move(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        move(self, QPoint)
        move(self, int, int)
        """
        pass

    def moveEvent(self, QMoveEvent): # real signature unknown; restored from __doc__
        """ moveEvent(self, QMoveEvent) """
        pass

    def paintEvent(self, QPaintEvent): # real signature unknown; restored from __doc__
        """ paintEvent(self, QPaintEvent) """
        pass

    def resize(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        resize(self, int, int)
        resize(self, QSize)
        """
        pass

    def resizeEvent(self, QResizeEvent): # real signature unknown; restored from __doc__
        """ resizeEvent(self, QResizeEvent) """
        pass

    def setGeometry(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setGeometry(self, QRect)
        setGeometry(self, int, int, int, int)
        """
        pass

    def shape(self): # real signature unknown; restored from __doc__
        """ shape(self) -> QRubberBand.Shape """
        pass

    def showEvent(self, QShowEvent): # real signature unknown; restored from __doc__
        """ showEvent(self, QShowEvent) """
        pass

    def __init__(self, QRubberBand_Shape, parent=None): # real signature unknown; restored from __doc__
        pass

    Line = 0
    Rectangle = 1


