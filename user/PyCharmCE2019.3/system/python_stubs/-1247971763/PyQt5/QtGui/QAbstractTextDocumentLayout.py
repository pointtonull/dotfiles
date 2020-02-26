# encoding: utf-8
# module PyQt5.QtGui
# from /usr/lib/python3/dist-packages/PyQt5/QtGui.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore


class QAbstractTextDocumentLayout(__PyQt5_QtCore.QObject):
    """ QAbstractTextDocumentLayout(QTextDocument) """
    def anchorAt(self, Union, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ anchorAt(self, Union[QPointF, QPoint]) -> str """
        return ""

    def blockBoundingRect(self, QTextBlock): # real signature unknown; restored from __doc__
        """ blockBoundingRect(self, QTextBlock) -> QRectF """
        pass

    def document(self): # real signature unknown; restored from __doc__
        """ document(self) -> QTextDocument """
        return QTextDocument

    def documentChanged(self, p_int, p_int_1, p_int_2): # real signature unknown; restored from __doc__
        """ documentChanged(self, int, int, int) """
        pass

    def documentSize(self): # real signature unknown; restored from __doc__
        """ documentSize(self) -> QSizeF """
        pass

    def documentSizeChanged(self, QSizeF): # real signature unknown; restored from __doc__
        """ documentSizeChanged(self, QSizeF) [signal] """
        pass

    def draw(self, QPainter, QAbstractTextDocumentLayout_PaintContext): # real signature unknown; restored from __doc__
        """ draw(self, QPainter, QAbstractTextDocumentLayout.PaintContext) """
        pass

    def drawInlineObject(self, QPainter, QRectF, QTextInlineObject, p_int, QTextFormat): # real signature unknown; restored from __doc__
        """ drawInlineObject(self, QPainter, QRectF, QTextInlineObject, int, QTextFormat) """
        pass

    def format(self, p_int): # real signature unknown; restored from __doc__
        """ format(self, int) -> QTextCharFormat """
        return QTextCharFormat

    def formatAt(self, Union, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ formatAt(self, Union[QPointF, QPoint]) -> QTextFormat """
        return QTextFormat

    def frameBoundingRect(self, QTextFrame): # real signature unknown; restored from __doc__
        """ frameBoundingRect(self, QTextFrame) -> QRectF """
        pass

    def handlerForObject(self, p_int): # real signature unknown; restored from __doc__
        """ handlerForObject(self, int) -> QTextObjectInterface """
        return QTextObjectInterface

    def hitTest(self, Union, QPointF=None, QPoint=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ hitTest(self, Union[QPointF, QPoint], Qt.HitTestAccuracy) -> int """
        pass

    def imageAt(self, Union, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ imageAt(self, Union[QPointF, QPoint]) -> str """
        return ""

    def pageCount(self): # real signature unknown; restored from __doc__
        """ pageCount(self) -> int """
        return 0

    def pageCountChanged(self, p_int): # real signature unknown; restored from __doc__
        """ pageCountChanged(self, int) [signal] """
        pass

    def paintDevice(self): # real signature unknown; restored from __doc__
        """ paintDevice(self) -> QPaintDevice """
        return QPaintDevice

    def positionInlineObject(self, QTextInlineObject, p_int, QTextFormat): # real signature unknown; restored from __doc__
        """ positionInlineObject(self, QTextInlineObject, int, QTextFormat) """
        pass

    def registerHandler(self, p_int, QObject): # real signature unknown; restored from __doc__
        """ registerHandler(self, int, QObject) """
        pass

    def resizeInlineObject(self, QTextInlineObject, p_int, QTextFormat): # real signature unknown; restored from __doc__
        """ resizeInlineObject(self, QTextInlineObject, int, QTextFormat) """
        pass

    def setPaintDevice(self, QPaintDevice): # real signature unknown; restored from __doc__
        """ setPaintDevice(self, QPaintDevice) """
        pass

    def unregisterHandler(self, p_int, component=None): # real signature unknown; restored from __doc__
        """ unregisterHandler(self, int, component: QObject = None) """
        pass

    def update(self, QRectF=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ update(self, QRectF = QRectF(0,0,1e+09,1e+09)) [signal] """
        pass

    def updateBlock(self, QTextBlock): # real signature unknown; restored from __doc__
        """ updateBlock(self, QTextBlock) [signal] """
        pass

    def __init__(self, QTextDocument): # real signature unknown; restored from __doc__
        pass



