# encoding: utf-8
# module PyQt5.QtWidgets
# from /usr/lib/python3/dist-packages/PyQt5/QtWidgets.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui


from .QWidget import QWidget

class QProgressBar(QWidget):
    """ QProgressBar(parent: QWidget = None) """
    def alignment(self): # real signature unknown; restored from __doc__
        """ alignment(self) -> Qt.Alignment """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def format(self): # real signature unknown; restored from __doc__
        """ format(self) -> str """
        return ""

    def initStyleOption(self, QStyleOptionProgressBar): # real signature unknown; restored from __doc__
        """ initStyleOption(self, QStyleOptionProgressBar) """
        pass

    def isTextVisible(self): # real signature unknown; restored from __doc__
        """ isTextVisible(self) -> bool """
        return False

    def maximum(self): # real signature unknown; restored from __doc__
        """ maximum(self) -> int """
        return 0

    def minimum(self): # real signature unknown; restored from __doc__
        """ minimum(self) -> int """
        return 0

    def minimumSizeHint(self): # real signature unknown; restored from __doc__
        """ minimumSizeHint(self) -> QSize """
        pass

    def orientation(self): # real signature unknown; restored from __doc__
        """ orientation(self) -> Qt.Orientation """
        pass

    def paintEvent(self, QPaintEvent): # real signature unknown; restored from __doc__
        """ paintEvent(self, QPaintEvent) """
        pass

    def reset(self): # real signature unknown; restored from __doc__
        """ reset(self) """
        pass

    def resetFormat(self): # real signature unknown; restored from __doc__
        """ resetFormat(self) """
        pass

    def setAlignment(self, Union, Qt_Alignment=None, Qt_AlignmentFlag=None): # real signature unknown; restored from __doc__
        """ setAlignment(self, Union[Qt.Alignment, Qt.AlignmentFlag]) """
        pass

    def setFormat(self, p_str): # real signature unknown; restored from __doc__
        """ setFormat(self, str) """
        pass

    def setInvertedAppearance(self, bool): # real signature unknown; restored from __doc__
        """ setInvertedAppearance(self, bool) """
        pass

    def setMaximum(self, p_int): # real signature unknown; restored from __doc__
        """ setMaximum(self, int) """
        pass

    def setMinimum(self, p_int): # real signature unknown; restored from __doc__
        """ setMinimum(self, int) """
        pass

    def setOrientation(self, Qt_Orientation): # real signature unknown; restored from __doc__
        """ setOrientation(self, Qt.Orientation) """
        pass

    def setRange(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ setRange(self, int, int) """
        pass

    def setTextDirection(self, QProgressBar_Direction): # real signature unknown; restored from __doc__
        """ setTextDirection(self, QProgressBar.Direction) """
        pass

    def setTextVisible(self, bool): # real signature unknown; restored from __doc__
        """ setTextVisible(self, bool) """
        pass

    def setValue(self, p_int): # real signature unknown; restored from __doc__
        """ setValue(self, int) """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> QSize """
        pass

    def text(self): # real signature unknown; restored from __doc__
        """ text(self) -> str """
        return ""

    def value(self): # real signature unknown; restored from __doc__
        """ value(self) -> int """
        return 0

    def valueChanged(self, p_int): # real signature unknown; restored from __doc__
        """ valueChanged(self, int) [signal] """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass

    BottomToTop = 1
    TopToBottom = 0


