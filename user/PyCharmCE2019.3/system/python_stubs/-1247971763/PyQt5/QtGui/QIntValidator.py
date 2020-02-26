# encoding: utf-8
# module PyQt5.QtGui
# from /usr/lib/python3/dist-packages/PyQt5/QtGui.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore


from .QValidator import QValidator

class QIntValidator(QValidator):
    """
    QIntValidator(parent: QObject = None)
    QIntValidator(int, int, parent: QObject = None)
    """
    def bottom(self): # real signature unknown; restored from __doc__
        """ bottom(self) -> int """
        return 0

    def fixup(self, p_str): # real signature unknown; restored from __doc__
        """ fixup(self, str) -> str """
        return ""

    def setBottom(self, p_int): # real signature unknown; restored from __doc__
        """ setBottom(self, int) """
        pass

    def setRange(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ setRange(self, int, int) """
        pass

    def setTop(self, p_int): # real signature unknown; restored from __doc__
        """ setTop(self, int) """
        pass

    def top(self): # real signature unknown; restored from __doc__
        """ top(self) -> int """
        return 0

    def validate(self, p_str, p_int): # real signature unknown; restored from __doc__
        """ validate(self, str, int) -> Tuple[QValidator.State, str, int] """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


