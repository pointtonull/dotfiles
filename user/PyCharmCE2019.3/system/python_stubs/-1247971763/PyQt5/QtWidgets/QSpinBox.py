# encoding: utf-8
# module PyQt5.QtWidgets
# from /usr/lib/python3/dist-packages/PyQt5/QtWidgets.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui


from .QAbstractSpinBox import QAbstractSpinBox

class QSpinBox(QAbstractSpinBox):
    """ QSpinBox(parent: QWidget = None) """
    def cleanText(self): # real signature unknown; restored from __doc__
        """ cleanText(self) -> str """
        return ""

    def displayIntegerBase(self): # real signature unknown; restored from __doc__
        """ displayIntegerBase(self) -> int """
        return 0

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def fixup(self, p_str): # real signature unknown; restored from __doc__
        """ fixup(self, str) -> str """
        return ""

    def maximum(self): # real signature unknown; restored from __doc__
        """ maximum(self) -> int """
        return 0

    def minimum(self): # real signature unknown; restored from __doc__
        """ minimum(self) -> int """
        return 0

    def prefix(self): # real signature unknown; restored from __doc__
        """ prefix(self) -> str """
        return ""

    def setDisplayIntegerBase(self, p_int): # real signature unknown; restored from __doc__
        """ setDisplayIntegerBase(self, int) """
        pass

    def setMaximum(self, p_int): # real signature unknown; restored from __doc__
        """ setMaximum(self, int) """
        pass

    def setMinimum(self, p_int): # real signature unknown; restored from __doc__
        """ setMinimum(self, int) """
        pass

    def setPrefix(self, p_str): # real signature unknown; restored from __doc__
        """ setPrefix(self, str) """
        pass

    def setRange(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ setRange(self, int, int) """
        pass

    def setSingleStep(self, p_int): # real signature unknown; restored from __doc__
        """ setSingleStep(self, int) """
        pass

    def setSuffix(self, p_str): # real signature unknown; restored from __doc__
        """ setSuffix(self, str) """
        pass

    def setValue(self, p_int): # real signature unknown; restored from __doc__
        """ setValue(self, int) """
        pass

    def singleStep(self): # real signature unknown; restored from __doc__
        """ singleStep(self) -> int """
        return 0

    def suffix(self): # real signature unknown; restored from __doc__
        """ suffix(self) -> str """
        return ""

    def textFromValue(self, p_int): # real signature unknown; restored from __doc__
        """ textFromValue(self, int) -> str """
        return ""

    def validate(self, p_str, p_int): # real signature unknown; restored from __doc__
        """ validate(self, str, int) -> Tuple[QValidator.State, str, int] """
        pass

    def value(self): # real signature unknown; restored from __doc__
        """ value(self) -> int """
        return 0

    def valueChanged(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        valueChanged(self, int) [signal]
        valueChanged(self, str) [signal]
        """
        pass

    def valueFromText(self, p_str): # real signature unknown; restored from __doc__
        """ valueFromText(self, str) -> int """
        return 0

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


