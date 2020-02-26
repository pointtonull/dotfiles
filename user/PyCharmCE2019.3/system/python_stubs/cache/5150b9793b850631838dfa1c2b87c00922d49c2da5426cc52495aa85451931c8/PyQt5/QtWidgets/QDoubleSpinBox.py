# encoding: utf-8
# module PyQt5.QtWidgets
# from /usr/lib/python3/dist-packages/PyQt5/QtWidgets.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui


from .QAbstractSpinBox import QAbstractSpinBox

class QDoubleSpinBox(QAbstractSpinBox):
    """ QDoubleSpinBox(parent: QWidget = None) """
    def cleanText(self): # real signature unknown; restored from __doc__
        """ cleanText(self) -> str """
        return ""

    def decimals(self): # real signature unknown; restored from __doc__
        """ decimals(self) -> int """
        return 0

    def fixup(self, p_str): # real signature unknown; restored from __doc__
        """ fixup(self, str) -> str """
        return ""

    def maximum(self): # real signature unknown; restored from __doc__
        """ maximum(self) -> float """
        return 0.0

    def minimum(self): # real signature unknown; restored from __doc__
        """ minimum(self) -> float """
        return 0.0

    def prefix(self): # real signature unknown; restored from __doc__
        """ prefix(self) -> str """
        return ""

    def setDecimals(self, p_int): # real signature unknown; restored from __doc__
        """ setDecimals(self, int) """
        pass

    def setMaximum(self, p_float): # real signature unknown; restored from __doc__
        """ setMaximum(self, float) """
        pass

    def setMinimum(self, p_float): # real signature unknown; restored from __doc__
        """ setMinimum(self, float) """
        pass

    def setPrefix(self, p_str): # real signature unknown; restored from __doc__
        """ setPrefix(self, str) """
        pass

    def setRange(self, p_float, p_float_1): # real signature unknown; restored from __doc__
        """ setRange(self, float, float) """
        pass

    def setSingleStep(self, p_float): # real signature unknown; restored from __doc__
        """ setSingleStep(self, float) """
        pass

    def setSuffix(self, p_str): # real signature unknown; restored from __doc__
        """ setSuffix(self, str) """
        pass

    def setValue(self, p_float): # real signature unknown; restored from __doc__
        """ setValue(self, float) """
        pass

    def singleStep(self): # real signature unknown; restored from __doc__
        """ singleStep(self) -> float """
        return 0.0

    def suffix(self): # real signature unknown; restored from __doc__
        """ suffix(self) -> str """
        return ""

    def textFromValue(self, p_float): # real signature unknown; restored from __doc__
        """ textFromValue(self, float) -> str """
        return ""

    def validate(self, p_str, p_int): # real signature unknown; restored from __doc__
        """ validate(self, str, int) -> Tuple[QValidator.State, str, int] """
        pass

    def value(self): # real signature unknown; restored from __doc__
        """ value(self) -> float """
        return 0.0

    def valueChanged(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        valueChanged(self, float) [signal]
        valueChanged(self, str) [signal]
        """
        pass

    def valueFromText(self, p_str): # real signature unknown; restored from __doc__
        """ valueFromText(self, str) -> float """
        return 0.0

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


