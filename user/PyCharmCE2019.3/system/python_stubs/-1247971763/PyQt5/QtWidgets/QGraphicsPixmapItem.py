# encoding: utf-8
# module PyQt5.QtWidgets
# from /usr/lib/python3/dist-packages/PyQt5/QtWidgets.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui


from .QGraphicsItem import QGraphicsItem

class QGraphicsPixmapItem(QGraphicsItem):
    """
    QGraphicsPixmapItem(parent: QGraphicsItem = None)
    QGraphicsPixmapItem(QPixmap, parent: QGraphicsItem = None)
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

    def offset(self): # real signature unknown; restored from __doc__
        """ offset(self) -> QPointF """
        pass

    def opaqueArea(self): # real signature unknown; restored from __doc__
        """ opaqueArea(self) -> QPainterPath """
        pass

    def paint(self, QPainter, QStyleOptionGraphicsItem, QWidget): # real signature unknown; restored from __doc__
        """ paint(self, QPainter, QStyleOptionGraphicsItem, QWidget) """
        pass

    def pixmap(self): # real signature unknown; restored from __doc__
        """ pixmap(self) -> QPixmap """
        pass

    def setOffset(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setOffset(self, Union[QPointF, QPoint])
        setOffset(self, float, float)
        """
        pass

    def setPixmap(self, QPixmap): # real signature unknown; restored from __doc__
        """ setPixmap(self, QPixmap) """
        pass

    def setShapeMode(self, QGraphicsPixmapItem_ShapeMode): # real signature unknown; restored from __doc__
        """ setShapeMode(self, QGraphicsPixmapItem.ShapeMode) """
        pass

    def setTransformationMode(self, Qt_TransformationMode): # real signature unknown; restored from __doc__
        """ setTransformationMode(self, Qt.TransformationMode) """
        pass

    def shape(self): # real signature unknown; restored from __doc__
        """ shape(self) -> QPainterPath """
        pass

    def shapeMode(self): # real signature unknown; restored from __doc__
        """ shapeMode(self) -> QGraphicsPixmapItem.ShapeMode """
        pass

    def transformationMode(self): # real signature unknown; restored from __doc__
        """ transformationMode(self) -> Qt.TransformationMode """
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> int """
        return 0

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    BoundingRectShape = 1
    HeuristicMaskShape = 2
    MaskShape = 0


