# encoding: utf-8
# module PyQt5.QtWidgets
# from /usr/lib/python3/dist-packages/PyQt5/QtWidgets.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui


from .QWidget import QWidget

class QDesktopWidget(QWidget):
    """ QDesktopWidget() """
    def availableGeometry(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        availableGeometry(self, screen: int = -1) -> QRect
        availableGeometry(self, QWidget) -> QRect
        availableGeometry(self, QPoint) -> QRect
        """
        pass

    def isVirtualDesktop(self): # real signature unknown; restored from __doc__
        """ isVirtualDesktop(self) -> bool """
        return False

    def primaryScreen(self): # real signature unknown; restored from __doc__
        """ primaryScreen(self) -> int """
        return 0

    def primaryScreenChanged(self): # real signature unknown; restored from __doc__
        """ primaryScreenChanged(self) [signal] """
        pass

    def resized(self, p_int): # real signature unknown; restored from __doc__
        """ resized(self, int) [signal] """
        pass

    def resizeEvent(self, QResizeEvent): # real signature unknown; restored from __doc__
        """ resizeEvent(self, QResizeEvent) """
        pass

    def screen(self, screen=-1): # real signature unknown; restored from __doc__
        """ screen(self, screen: int = -1) -> QWidget """
        return QWidget

    def screenCount(self): # real signature unknown; restored from __doc__
        """ screenCount(self) -> int """
        return 0

    def screenCountChanged(self, p_int): # real signature unknown; restored from __doc__
        """ screenCountChanged(self, int) [signal] """
        pass

    def screenGeometry(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        screenGeometry(self, screen: int = -1) -> QRect
        screenGeometry(self, QWidget) -> QRect
        screenGeometry(self, QPoint) -> QRect
        """
        pass

    def screenNumber(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        screenNumber(self, widget: QWidget = None) -> int
        screenNumber(self, QPoint) -> int
        """
        return 0

    def workAreaResized(self, p_int): # real signature unknown; restored from __doc__
        """ workAreaResized(self, int) [signal] """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass


