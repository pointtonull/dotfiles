# encoding: utf-8
# module PyQt5.QtWidgets
# from /usr/lib/python3/dist-packages/PyQt5/QtWidgets.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui


from .QAbstractGraphicsShapeItem import QAbstractGraphicsShapeItem

class QGraphicsSimpleTextItem(QAbstractGraphicsShapeItem):
    """
    QGraphicsSimpleTextItem(parent: QGraphicsItem = None)
    QGraphicsSimpleTextItem(str, parent: QGraphicsItem = None)
    """
    def boundingRect(self): # real signature unknown; restored from __doc__
        """ boundingRect(self) -> QRectF """
        pass

    def contains(self, Union, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ contains(self, Union[QPointF, QPoint]) -> bool """
        return False

    def font(self): # real signature unknown; restored from __doc__
        """ font(self) -> QFont """
        pass

    def isObscuredBy(self, QGraphicsItem): # real signature unknown; restored from __doc__
        """ isObscuredBy(self, QGraphicsItem) -> bool """
        return False

    def opaqueArea(self): # real signature unknown; restored from __doc__
        """ opaqueArea(self) -> QPainterPath """
        pass

    def paint(self, QPainter, QStyleOptionGraphicsItem, QWidget): # real signature unknown; restored from __doc__
        """ paint(self, QPainter, QStyleOptionGraphicsItem, QWidget) """
        pass

    def setFont(self, QFont): # real signature unknown; restored from __doc__
        """ setFont(self, QFont) """
        pass

    def setText(self, p_str): # real signature unknown; restored from __doc__
        """ setText(self, str) """
        pass

    def shape(self): # real signature unknown; restored from __doc__
        """ shape(self) -> QPainterPath """
        pass

    def text(self): # real signature unknown; restored from __doc__
        """ text(self) -> str """
        return ""

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> int """
        return 0

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


