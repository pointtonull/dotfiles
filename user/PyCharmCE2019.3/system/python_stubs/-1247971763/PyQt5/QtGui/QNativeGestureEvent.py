# encoding: utf-8
# module PyQt5.QtGui
# from /usr/lib/python3/dist-packages/PyQt5/QtGui.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore


from .QInputEvent import QInputEvent

class QNativeGestureEvent(QInputEvent):
    """
    QNativeGestureEvent(Qt.NativeGestureType, Union[QPointF, QPoint], Union[QPointF, QPoint], Union[QPointF, QPoint], float, int, int)
    QNativeGestureEvent(QNativeGestureEvent)
    """
    def gestureType(self): # real signature unknown; restored from __doc__
        """ gestureType(self) -> Qt.NativeGestureType """
        pass

    def globalPos(self): # real signature unknown; restored from __doc__
        """ globalPos(self) -> QPoint """
        pass

    def localPos(self): # real signature unknown; restored from __doc__
        """ localPos(self) -> QPointF """
        pass

    def pos(self): # real signature unknown; restored from __doc__
        """ pos(self) -> QPoint """
        pass

    def screenPos(self): # real signature unknown; restored from __doc__
        """ screenPos(self) -> QPointF """
        pass

    def value(self): # real signature unknown; restored from __doc__
        """ value(self) -> float """
        return 0.0

    def windowPos(self): # real signature unknown; restored from __doc__
        """ windowPos(self) -> QPointF """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


