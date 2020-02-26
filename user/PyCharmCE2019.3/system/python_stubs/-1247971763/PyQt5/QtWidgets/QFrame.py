# encoding: utf-8
# module PyQt5.QtWidgets
# from /usr/lib/python3/dist-packages/PyQt5/QtWidgets.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui


from .QWidget import QWidget

class QFrame(QWidget):
    """ QFrame(parent: QWidget = None, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags()) """
    def changeEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ changeEvent(self, QEvent) """
        pass

    def drawFrame(self, QPainter): # real signature unknown; restored from __doc__
        """ drawFrame(self, QPainter) """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def frameRect(self): # real signature unknown; restored from __doc__
        """ frameRect(self) -> QRect """
        pass

    def frameShadow(self): # real signature unknown; restored from __doc__
        """ frameShadow(self) -> QFrame.Shadow """
        pass

    def frameShape(self): # real signature unknown; restored from __doc__
        """ frameShape(self) -> QFrame.Shape """
        pass

    def frameStyle(self): # real signature unknown; restored from __doc__
        """ frameStyle(self) -> int """
        return 0

    def frameWidth(self): # real signature unknown; restored from __doc__
        """ frameWidth(self) -> int """
        return 0

    def initStyleOption(self, QStyleOptionFrame): # real signature unknown; restored from __doc__
        """ initStyleOption(self, QStyleOptionFrame) """
        pass

    def lineWidth(self): # real signature unknown; restored from __doc__
        """ lineWidth(self) -> int """
        return 0

    def midLineWidth(self): # real signature unknown; restored from __doc__
        """ midLineWidth(self) -> int """
        return 0

    def paintEvent(self, QPaintEvent): # real signature unknown; restored from __doc__
        """ paintEvent(self, QPaintEvent) """
        pass

    def setFrameRect(self, QRect): # real signature unknown; restored from __doc__
        """ setFrameRect(self, QRect) """
        pass

    def setFrameShadow(self, QFrame_Shadow): # real signature unknown; restored from __doc__
        """ setFrameShadow(self, QFrame.Shadow) """
        pass

    def setFrameShape(self, QFrame_Shape): # real signature unknown; restored from __doc__
        """ setFrameShape(self, QFrame.Shape) """
        pass

    def setFrameStyle(self, p_int): # real signature unknown; restored from __doc__
        """ setFrameStyle(self, int) """
        pass

    def setLineWidth(self, p_int): # real signature unknown; restored from __doc__
        """ setLineWidth(self, int) """
        pass

    def setMidLineWidth(self, p_int): # real signature unknown; restored from __doc__
        """ setMidLineWidth(self, int) """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> QSize """
        pass

    def __init__(self, parent=None, flags, Qt_WindowFlags=None, Qt_WindowType=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    Box = 1
    HLine = 4
    NoFrame = 0
    Panel = 2
    Plain = 16
    Raised = 32
    Shadow_Mask = 240
    Shape_Mask = 15
    StyledPanel = 6
    Sunken = 48
    VLine = 5
    WinPanel = 3


