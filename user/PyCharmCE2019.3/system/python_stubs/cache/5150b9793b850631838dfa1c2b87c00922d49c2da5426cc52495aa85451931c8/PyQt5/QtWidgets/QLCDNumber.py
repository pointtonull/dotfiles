# encoding: utf-8
# module PyQt5.QtWidgets
# from /usr/lib/python3/dist-packages/PyQt5/QtWidgets.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui


from .QFrame import QFrame

class QLCDNumber(QFrame):
    """
    QLCDNumber(parent: QWidget = None)
    QLCDNumber(int, parent: QWidget = None)
    """
    def checkOverflow(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        checkOverflow(self, float) -> bool
        checkOverflow(self, int) -> bool
        """
        return False

    def digitCount(self): # real signature unknown; restored from __doc__
        """ digitCount(self) -> int """
        return 0

    def display(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        display(self, str)
        display(self, float)
        display(self, int)
        """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def intValue(self): # real signature unknown; restored from __doc__
        """ intValue(self) -> int """
        return 0

    def mode(self): # real signature unknown; restored from __doc__
        """ mode(self) -> QLCDNumber.Mode """
        pass

    def overflow(self): # real signature unknown; restored from __doc__
        """ overflow(self) [signal] """
        pass

    def paintEvent(self, QPaintEvent): # real signature unknown; restored from __doc__
        """ paintEvent(self, QPaintEvent) """
        pass

    def segmentStyle(self): # real signature unknown; restored from __doc__
        """ segmentStyle(self) -> QLCDNumber.SegmentStyle """
        pass

    def setBinMode(self): # real signature unknown; restored from __doc__
        """ setBinMode(self) """
        pass

    def setDecMode(self): # real signature unknown; restored from __doc__
        """ setDecMode(self) """
        pass

    def setDigitCount(self, p_int): # real signature unknown; restored from __doc__
        """ setDigitCount(self, int) """
        pass

    def setHexMode(self): # real signature unknown; restored from __doc__
        """ setHexMode(self) """
        pass

    def setMode(self, QLCDNumber_Mode): # real signature unknown; restored from __doc__
        """ setMode(self, QLCDNumber.Mode) """
        pass

    def setNumDigits(self, p_int): # real signature unknown; restored from __doc__
        """ setNumDigits(self, int) """
        pass

    def setOctMode(self): # real signature unknown; restored from __doc__
        """ setOctMode(self) """
        pass

    def setSegmentStyle(self, QLCDNumber_SegmentStyle): # real signature unknown; restored from __doc__
        """ setSegmentStyle(self, QLCDNumber.SegmentStyle) """
        pass

    def setSmallDecimalPoint(self, bool): # real signature unknown; restored from __doc__
        """ setSmallDecimalPoint(self, bool) """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> QSize """
        pass

    def smallDecimalPoint(self): # real signature unknown; restored from __doc__
        """ smallDecimalPoint(self) -> bool """
        return False

    def value(self): # real signature unknown; restored from __doc__
        """ value(self) -> float """
        return 0.0

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    Bin = 3
    Dec = 1
    Filled = 1
    Flat = 2
    Hex = 0
    Oct = 2
    Outline = 0


