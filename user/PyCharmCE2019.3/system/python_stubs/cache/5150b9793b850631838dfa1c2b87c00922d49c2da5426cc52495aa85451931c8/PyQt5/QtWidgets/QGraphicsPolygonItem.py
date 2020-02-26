# encoding: utf-8
# module PyQt5.QtWidgets
# from /usr/lib/python3/dist-packages/PyQt5/QtWidgets.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui


from .QAbstractGraphicsShapeItem import QAbstractGraphicsShapeItem

class QGraphicsPolygonItem(QAbstractGraphicsShapeItem):
    """
    QGraphicsPolygonItem(parent: QGraphicsItem = None)
    QGraphicsPolygonItem(QPolygonF, parent: QGraphicsItem = None)
    """
    def boundingRect(self): # real signature unknown; restored from __doc__
        """ boundingRect(self) -> QRectF """
        pass

    def contains(self, Union, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ contains(self, Union[QPointF, QPoint]) -> bool """
        return False

    def fillRule(self): # real signature unknown; restored from __doc__
        """ fillRule(self) -> Qt.FillRule """
        pass

    def isObscuredBy(self, QGraphicsItem): # real signature unknown; restored from __doc__
        """ isObscuredBy(self, QGraphicsItem) -> bool """
        return False

    def opaqueArea(self): # real signature unknown; restored from __doc__
        """ opaqueArea(self) -> QPainterPath """
        pass

    def paint(self, QPainter, QStyleOptionGraphicsItem, widget=None): # real signature unknown; restored from __doc__
        """ paint(self, QPainter, QStyleOptionGraphicsItem, widget: QWidget = None) """
        pass

    def polygon(self): # real signature unknown; restored from __doc__
        """ polygon(self) -> QPolygonF """
        pass

    def setFillRule(self, Qt_FillRule): # real signature unknown; restored from __doc__
        """ setFillRule(self, Qt.FillRule) """
        pass

    def setPolygon(self, QPolygonF): # real signature unknown; restored from __doc__
        """ setPolygon(self, QPolygonF) """
        pass

    def shape(self): # real signature unknown; restored from __doc__
        """ shape(self) -> QPainterPath """
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> int """
        return 0

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


