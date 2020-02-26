# encoding: utf-8
# module PyQt5.QtGui
# from /usr/lib/python3/dist-packages/PyQt5/QtGui.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore


from .QValidator import QValidator

class QDoubleValidator(QValidator):
    """
    QDoubleValidator(parent: QObject = None)
    QDoubleValidator(float, float, int, parent: QObject = None)
    """
    def bottom(self): # real signature unknown; restored from __doc__
        """ bottom(self) -> float """
        return 0.0

    def decimals(self): # real signature unknown; restored from __doc__
        """ decimals(self) -> int """
        return 0

    def notation(self): # real signature unknown; restored from __doc__
        """ notation(self) -> QDoubleValidator.Notation """
        pass

    def setBottom(self, p_float): # real signature unknown; restored from __doc__
        """ setBottom(self, float) """
        pass

    def setDecimals(self, p_int): # real signature unknown; restored from __doc__
        """ setDecimals(self, int) """
        pass

    def setNotation(self, QDoubleValidator_Notation): # real signature unknown; restored from __doc__
        """ setNotation(self, QDoubleValidator.Notation) """
        pass

    def setRange(self, p_float, p_float_1, decimals=0): # real signature unknown; restored from __doc__
        """ setRange(self, float, float, decimals: int = 0) """
        pass

    def setTop(self, p_float): # real signature unknown; restored from __doc__
        """ setTop(self, float) """
        pass

    def top(self): # real signature unknown; restored from __doc__
        """ top(self) -> float """
        return 0.0

    def validate(self, p_str, p_int): # real signature unknown; restored from __doc__
        """ validate(self, str, int) -> Tuple[QValidator.State, str, int] """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    ScientificNotation = 1
    StandardNotation = 0


