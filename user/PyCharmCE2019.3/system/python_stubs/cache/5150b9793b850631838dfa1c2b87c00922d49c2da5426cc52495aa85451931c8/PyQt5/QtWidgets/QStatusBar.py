# encoding: utf-8
# module PyQt5.QtWidgets
# from /usr/lib/python3/dist-packages/PyQt5/QtWidgets.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui


from .QWidget import QWidget

class QStatusBar(QWidget):
    """ QStatusBar(parent: QWidget = None) """
    def addPermanentWidget(self, QWidget, stretch=0): # real signature unknown; restored from __doc__
        """ addPermanentWidget(self, QWidget, stretch: int = 0) """
        pass

    def addWidget(self, QWidget, stretch=0): # real signature unknown; restored from __doc__
        """ addWidget(self, QWidget, stretch: int = 0) """
        pass

    def clearMessage(self): # real signature unknown; restored from __doc__
        """ clearMessage(self) """
        pass

    def currentMessage(self): # real signature unknown; restored from __doc__
        """ currentMessage(self) -> str """
        return ""

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def hideOrShow(self): # real signature unknown; restored from __doc__
        """ hideOrShow(self) """
        pass

    def insertPermanentWidget(self, p_int, QWidget, stretch=0): # real signature unknown; restored from __doc__
        """ insertPermanentWidget(self, int, QWidget, stretch: int = 0) -> int """
        return 0

    def insertWidget(self, p_int, QWidget, stretch=0): # real signature unknown; restored from __doc__
        """ insertWidget(self, int, QWidget, stretch: int = 0) -> int """
        return 0

    def isSizeGripEnabled(self): # real signature unknown; restored from __doc__
        """ isSizeGripEnabled(self) -> bool """
        return False

    def messageChanged(self, p_str): # real signature unknown; restored from __doc__
        """ messageChanged(self, str) [signal] """
        pass

    def paintEvent(self, QPaintEvent): # real signature unknown; restored from __doc__
        """ paintEvent(self, QPaintEvent) """
        pass

    def reformat(self): # real signature unknown; restored from __doc__
        """ reformat(self) """
        pass

    def removeWidget(self, QWidget): # real signature unknown; restored from __doc__
        """ removeWidget(self, QWidget) """
        pass

    def resizeEvent(self, QResizeEvent): # real signature unknown; restored from __doc__
        """ resizeEvent(self, QResizeEvent) """
        pass

    def setSizeGripEnabled(self, bool): # real signature unknown; restored from __doc__
        """ setSizeGripEnabled(self, bool) """
        pass

    def showEvent(self, QShowEvent): # real signature unknown; restored from __doc__
        """ showEvent(self, QShowEvent) """
        pass

    def showMessage(self, p_str, msecs=0): # real signature unknown; restored from __doc__
        """ showMessage(self, str, msecs: int = 0) """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


