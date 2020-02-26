# encoding: utf-8
# module PyQt5.QtWidgets
# from /usr/lib/python3/dist-packages/PyQt5/QtWidgets.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui


from .QAbstractSlider import QAbstractSlider

class QSlider(QAbstractSlider):
    """
    QSlider(parent: QWidget = None)
    QSlider(Qt.Orientation, parent: QWidget = None)
    """
    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def initStyleOption(self, QStyleOptionSlider): # real signature unknown; restored from __doc__
        """ initStyleOption(self, QStyleOptionSlider) """
        pass

    def minimumSizeHint(self): # real signature unknown; restored from __doc__
        """ minimumSizeHint(self) -> QSize """
        pass

    def mouseMoveEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ mouseMoveEvent(self, QMouseEvent) """
        pass

    def mousePressEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ mousePressEvent(self, QMouseEvent) """
        pass

    def mouseReleaseEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ mouseReleaseEvent(self, QMouseEvent) """
        pass

    def paintEvent(self, QPaintEvent): # real signature unknown; restored from __doc__
        """ paintEvent(self, QPaintEvent) """
        pass

    def setTickInterval(self, p_int): # real signature unknown; restored from __doc__
        """ setTickInterval(self, int) """
        pass

    def setTickPosition(self, QSlider_TickPosition): # real signature unknown; restored from __doc__
        """ setTickPosition(self, QSlider.TickPosition) """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> QSize """
        pass

    def tickInterval(self): # real signature unknown; restored from __doc__
        """ tickInterval(self) -> int """
        return 0

    def tickPosition(self): # real signature unknown; restored from __doc__
        """ tickPosition(self) -> QSlider.TickPosition """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    NoTicks = 0
    TicksAbove = 1
    TicksBelow = 2
    TicksBothSides = 3
    TicksLeft = 1
    TicksRight = 2


