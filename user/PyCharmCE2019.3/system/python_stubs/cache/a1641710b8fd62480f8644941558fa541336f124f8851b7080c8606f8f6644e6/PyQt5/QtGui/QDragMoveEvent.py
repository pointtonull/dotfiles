# encoding: utf-8
# module PyQt5.QtGui
# from /usr/lib/python3/dist-packages/PyQt5/QtGui.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore


from .QDropEvent import QDropEvent

class QDragMoveEvent(QDropEvent):
    """
    QDragMoveEvent(QPoint, Union[Qt.DropActions, Qt.DropAction], QMimeData, Union[Qt.MouseButtons, Qt.MouseButton], Union[Qt.KeyboardModifiers, Qt.KeyboardModifier], type: QEvent.Type = QEvent.DragMove)
    QDragMoveEvent(QDragMoveEvent)
    """
    def accept(self, QRect=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        accept(self)
        accept(self, QRect)
        """
        pass

    def answerRect(self): # real signature unknown; restored from __doc__
        """ answerRect(self) -> QRect """
        pass

    def ignore(self, QRect=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        ignore(self)
        ignore(self, QRect)
        """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


