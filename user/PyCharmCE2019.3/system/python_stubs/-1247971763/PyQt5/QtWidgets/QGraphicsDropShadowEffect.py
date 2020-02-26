# encoding: utf-8
# module PyQt5.QtWidgets
# from /usr/lib/python3/dist-packages/PyQt5/QtWidgets.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui


from .QGraphicsEffect import QGraphicsEffect

class QGraphicsDropShadowEffect(QGraphicsEffect):
    """ QGraphicsDropShadowEffect(parent: QObject = None) """
    def blurRadius(self): # real signature unknown; restored from __doc__
        """ blurRadius(self) -> float """
        return 0.0

    def blurRadiusChanged(self, p_float): # real signature unknown; restored from __doc__
        """ blurRadiusChanged(self, float) [signal] """
        pass

    def boundingRectFor(self, QRectF): # real signature unknown; restored from __doc__
        """ boundingRectFor(self, QRectF) -> QRectF """
        pass

    def color(self): # real signature unknown; restored from __doc__
        """ color(self) -> QColor """
        pass

    def colorChanged(self, Union, QColor=None, Qt_GlobalColor=None, QGradient=None): # real signature unknown; restored from __doc__
        """ colorChanged(self, Union[QColor, Qt.GlobalColor, QGradient]) [signal] """
        pass

    def draw(self, QPainter): # real signature unknown; restored from __doc__
        """ draw(self, QPainter) """
        pass

    def offset(self): # real signature unknown; restored from __doc__
        """ offset(self) -> QPointF """
        pass

    def offsetChanged(self, Union, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ offsetChanged(self, Union[QPointF, QPoint]) [signal] """
        pass

    def setBlurRadius(self, p_float): # real signature unknown; restored from __doc__
        """ setBlurRadius(self, float) """
        pass

    def setColor(self, Union, QColor=None, Qt_GlobalColor=None, QGradient=None): # real signature unknown; restored from __doc__
        """ setColor(self, Union[QColor, Qt.GlobalColor, QGradient]) """
        pass

    def setOffset(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setOffset(self, Union[QPointF, QPoint])
        setOffset(self, float, float)
        setOffset(self, float)
        """
        pass

    def setXOffset(self, p_float): # real signature unknown; restored from __doc__
        """ setXOffset(self, float) """
        pass

    def setYOffset(self, p_float): # real signature unknown; restored from __doc__
        """ setYOffset(self, float) """
        pass

    def xOffset(self): # real signature unknown; restored from __doc__
        """ xOffset(self) -> float """
        return 0.0

    def yOffset(self): # real signature unknown; restored from __doc__
        """ yOffset(self) -> float """
        return 0.0

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


