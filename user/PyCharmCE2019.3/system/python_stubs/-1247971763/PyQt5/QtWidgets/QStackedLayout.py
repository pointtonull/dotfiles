# encoding: utf-8
# module PyQt5.QtWidgets
# from /usr/lib/python3/dist-packages/PyQt5/QtWidgets.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui


from .QLayout import QLayout

class QStackedLayout(QLayout):
    """
    QStackedLayout()
    QStackedLayout(QWidget)
    QStackedLayout(QLayout)
    """
    def addItem(self, QLayoutItem): # real signature unknown; restored from __doc__
        """ addItem(self, QLayoutItem) """
        pass

    def addWidget(self, QWidget): # real signature unknown; restored from __doc__
        """ addWidget(self, QWidget) -> int """
        return 0

    def count(self): # real signature unknown; restored from __doc__
        """ count(self) -> int """
        return 0

    def currentChanged(self, p_int): # real signature unknown; restored from __doc__
        """ currentChanged(self, int) [signal] """
        pass

    def currentIndex(self): # real signature unknown; restored from __doc__
        """ currentIndex(self) -> int """
        return 0

    def currentWidget(self): # real signature unknown; restored from __doc__
        """ currentWidget(self) -> QWidget """
        return QWidget

    def hasHeightForWidth(self): # real signature unknown; restored from __doc__
        """ hasHeightForWidth(self) -> bool """
        return False

    def heightForWidth(self, p_int): # real signature unknown; restored from __doc__
        """ heightForWidth(self, int) -> int """
        return 0

    def insertWidget(self, p_int, QWidget): # real signature unknown; restored from __doc__
        """ insertWidget(self, int, QWidget) -> int """
        return 0

    def itemAt(self, p_int): # real signature unknown; restored from __doc__
        """ itemAt(self, int) -> QLayoutItem """
        return QLayoutItem

    def minimumSize(self): # real signature unknown; restored from __doc__
        """ minimumSize(self) -> QSize """
        pass

    def setCurrentIndex(self, p_int): # real signature unknown; restored from __doc__
        """ setCurrentIndex(self, int) """
        pass

    def setCurrentWidget(self, QWidget): # real signature unknown; restored from __doc__
        """ setCurrentWidget(self, QWidget) """
        pass

    def setGeometry(self, QRect): # real signature unknown; restored from __doc__
        """ setGeometry(self, QRect) """
        pass

    def setStackingMode(self, QStackedLayout_StackingMode): # real signature unknown; restored from __doc__
        """ setStackingMode(self, QStackedLayout.StackingMode) """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> QSize """
        pass

    def stackingMode(self): # real signature unknown; restored from __doc__
        """ stackingMode(self) -> QStackedLayout.StackingMode """
        pass

    def takeAt(self, p_int): # real signature unknown; restored from __doc__
        """ takeAt(self, int) -> QLayoutItem """
        return QLayoutItem

    def widget(self, p_int=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        widget(self, int) -> QWidget
        widget(self) -> QWidget
        """
        return QWidget

    def widgetRemoved(self, p_int): # real signature unknown; restored from __doc__
        """ widgetRemoved(self, int) [signal] """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    StackAll = 1
    StackOne = 0


