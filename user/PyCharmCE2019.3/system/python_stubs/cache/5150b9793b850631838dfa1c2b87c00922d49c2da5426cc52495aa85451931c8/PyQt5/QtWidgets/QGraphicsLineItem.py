# encoding: utf-8
# module PyQt5.QtWidgets
# from /usr/lib/python3/dist-packages/PyQt5/QtWidgets.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui


from .QGraphicsItem import QGraphicsItem

class QGraphicsLineItem(QGraphicsItem):
    """
    QGraphicsLineItem(parent: QGraphicsItem = None)
    QGraphicsLineItem(QLineF, parent: QGraphicsItem = None)
    QGraphicsLineItem(float, float, float, float, parent: QGraphicsItem = None)
    """
    def boundingRect(self): # real signature unknown; restored from __doc__
        """ boundingRect(self) -> QRectF """
        pass

    def contains(self, Union, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ contains(self, Union[QPointF, QPoint]) -> bool """
        return False

    def isObscuredBy(self, QGraphicsItem): # real signature unknown; restored from __doc__
        """ isObscuredBy(self, QGraphicsItem) -> bool """
        return False

    def line(self): # real signature unknown; restored from __doc__
        """ line(self) -> QLineF """
        pass

    def opaqueArea(self): # real signature unknown; restored from __doc__
        """ opaqueArea(self) -> QPainterPath """
        pass

    def paint(self, QPainter, QStyleOptionGraphicsItem, widget=None): # real signature unknown; restored from __doc__
        """ paint(self, QPainter, QStyleOptionGraphicsItem, widget: QWidget = None) """
        pass

    def pen(self): # real signature unknown; restored from __doc__
        """ pen(self) -> QPen """
        pass

    def setLine(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setLine(self, QLineF)
        setLine(self, float, float, float, float)
        """
        pass

    def setPen(self, Union, QPen=None, QColor=None, Qt_GlobalColor=None, QGradient=None): # real signature unknown; restored from __doc__
        """ setPen(self, Union[QPen, QColor, Qt.GlobalColor, QGradient]) """
        pass

    def shape(self): # real signature unknown; restored from __doc__
        """ shape(self) -> QPainterPath """
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> int """
        return 0

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


