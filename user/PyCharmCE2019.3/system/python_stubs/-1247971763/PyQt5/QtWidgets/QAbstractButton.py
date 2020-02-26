# encoding: utf-8
# module PyQt5.QtWidgets
# from /usr/lib/python3/dist-packages/PyQt5/QtWidgets.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui


from .QWidget import QWidget

class QAbstractButton(QWidget):
    """ QAbstractButton(parent: QWidget = None) """
    def animateClick(self, msecs=100): # real signature unknown; restored from __doc__
        """ animateClick(self, msecs: int = 100) """
        pass

    def autoExclusive(self): # real signature unknown; restored from __doc__
        """ autoExclusive(self) -> bool """
        return False

    def autoRepeat(self): # real signature unknown; restored from __doc__
        """ autoRepeat(self) -> bool """
        return False

    def autoRepeatDelay(self): # real signature unknown; restored from __doc__
        """ autoRepeatDelay(self) -> int """
        return 0

    def autoRepeatInterval(self): # real signature unknown; restored from __doc__
        """ autoRepeatInterval(self) -> int """
        return 0

    def changeEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ changeEvent(self, QEvent) """
        pass

    def checkStateSet(self): # real signature unknown; restored from __doc__
        """ checkStateSet(self) """
        pass

    def click(self): # real signature unknown; restored from __doc__
        """ click(self) """
        pass

    def clicked(self, bool=False): # real signature unknown; restored from __doc__
        """ clicked(self, bool = False) [signal] """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def focusInEvent(self, QFocusEvent): # real signature unknown; restored from __doc__
        """ focusInEvent(self, QFocusEvent) """
        pass

    def focusOutEvent(self, QFocusEvent): # real signature unknown; restored from __doc__
        """ focusOutEvent(self, QFocusEvent) """
        pass

    def group(self): # real signature unknown; restored from __doc__
        """ group(self) -> QButtonGroup """
        return QButtonGroup

    def hitButton(self, QPoint): # real signature unknown; restored from __doc__
        """ hitButton(self, QPoint) -> bool """
        return False

    def icon(self): # real signature unknown; restored from __doc__
        """ icon(self) -> QIcon """
        pass

    def iconSize(self): # real signature unknown; restored from __doc__
        """ iconSize(self) -> QSize """
        pass

    def isCheckable(self): # real signature unknown; restored from __doc__
        """ isCheckable(self) -> bool """
        return False

    def isChecked(self): # real signature unknown; restored from __doc__
        """ isChecked(self) -> bool """
        return False

    def isDown(self): # real signature unknown; restored from __doc__
        """ isDown(self) -> bool """
        return False

    def keyPressEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, QKeyEvent) """
        pass

    def keyReleaseEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ keyReleaseEvent(self, QKeyEvent) """
        pass

    def mouseMoveEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ mouseMoveEvent(self, QMouseEvent) """
        pass

    def mousePressEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ mousePressEvent(self, QMouseEvent) """
        pass

    def mouseReleaseEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ mouseReleaseEvent(self, QMouseEvent) """
        pass

    def nextCheckState(self): # real signature unknown; restored from __doc__
        """ nextCheckState(self) """
        pass

    def paintEvent(self, QPaintEvent): # real signature unknown; restored from __doc__
        """ paintEvent(self, QPaintEvent) """
        pass

    def pressed(self): # real signature unknown; restored from __doc__
        """ pressed(self) [signal] """
        pass

    def released(self): # real signature unknown; restored from __doc__
        """ released(self) [signal] """
        pass

    def setAutoExclusive(self, bool): # real signature unknown; restored from __doc__
        """ setAutoExclusive(self, bool) """
        pass

    def setAutoRepeat(self, bool): # real signature unknown; restored from __doc__
        """ setAutoRepeat(self, bool) """
        pass

    def setAutoRepeatDelay(self, p_int): # real signature unknown; restored from __doc__
        """ setAutoRepeatDelay(self, int) """
        pass

    def setAutoRepeatInterval(self, p_int): # real signature unknown; restored from __doc__
        """ setAutoRepeatInterval(self, int) """
        pass

    def setCheckable(self, bool): # real signature unknown; restored from __doc__
        """ setCheckable(self, bool) """
        pass

    def setChecked(self, bool): # real signature unknown; restored from __doc__
        """ setChecked(self, bool) """
        pass

    def setDown(self, bool): # real signature unknown; restored from __doc__
        """ setDown(self, bool) """
        pass

    def setIcon(self, QIcon): # real signature unknown; restored from __doc__
        """ setIcon(self, QIcon) """
        pass

    def setIconSize(self, QSize): # real signature unknown; restored from __doc__
        """ setIconSize(self, QSize) """
        pass

    def setShortcut(self, Union, QKeySequence=None, QKeySequence_StandardKey=None, p_str=None, p_int=None): # real signature unknown; restored from __doc__
        """ setShortcut(self, Union[QKeySequence, QKeySequence.StandardKey, str, int]) """
        pass

    def setText(self, p_str): # real signature unknown; restored from __doc__
        """ setText(self, str) """
        pass

    def shortcut(self): # real signature unknown; restored from __doc__
        """ shortcut(self) -> QKeySequence """
        pass

    def text(self): # real signature unknown; restored from __doc__
        """ text(self) -> str """
        return ""

    def timerEvent(self, QTimerEvent): # real signature unknown; restored from __doc__
        """ timerEvent(self, QTimerEvent) """
        pass

    def toggle(self): # real signature unknown; restored from __doc__
        """ toggle(self) """
        pass

    def toggled(self, bool): # real signature unknown; restored from __doc__
        """ toggled(self, bool) [signal] """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


