# encoding: utf-8
# module PyQt5.QtGui
# from /usr/lib/python3/dist-packages/PyQt5/QtGui.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore


class QFocusEvent(__PyQt5_QtCore.QEvent):
    """
    QFocusEvent(QEvent.Type, reason: Qt.FocusReason = Qt.OtherFocusReason)
    QFocusEvent(QFocusEvent)
    """
    def gotFocus(self): # real signature unknown; restored from __doc__
        """ gotFocus(self) -> bool """
        return False

    def lostFocus(self): # real signature unknown; restored from __doc__
        """ lostFocus(self) -> bool """
        return False

    def reason(self): # real signature unknown; restored from __doc__
        """ reason(self) -> Qt.FocusReason """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


