# encoding: utf-8
# module PyQt5.QtWidgets
# from /usr/lib/python3/dist-packages/PyQt5/QtWidgets.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui


from .QAbstractButton import QAbstractButton

class QToolButton(QAbstractButton):
    """ QToolButton(parent: QWidget = None) """
    def actionEvent(self, QActionEvent): # real signature unknown; restored from __doc__
        """ actionEvent(self, QActionEvent) """
        pass

    def arrowType(self): # real signature unknown; restored from __doc__
        """ arrowType(self) -> Qt.ArrowType """
        pass

    def autoRaise(self): # real signature unknown; restored from __doc__
        """ autoRaise(self) -> bool """
        return False

    def changeEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ changeEvent(self, QEvent) """
        pass

    def defaultAction(self): # real signature unknown; restored from __doc__
        """ defaultAction(self) -> QAction """
        return QAction

    def enterEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ enterEvent(self, QEvent) """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def hitButton(self, QPoint): # real signature unknown; restored from __doc__
        """ hitButton(self, QPoint) -> bool """
        return False

    def initStyleOption(self, QStyleOptionToolButton): # real signature unknown; restored from __doc__
        """ initStyleOption(self, QStyleOptionToolButton) """
        pass

    def leaveEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ leaveEvent(self, QEvent) """
        pass

    def menu(self): # real signature unknown; restored from __doc__
        """ menu(self) -> QMenu """
        return QMenu

    def minimumSizeHint(self): # real signature unknown; restored from __doc__
        """ minimumSizeHint(self) -> QSize """
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

    def popupMode(self): # real signature unknown; restored from __doc__
        """ popupMode(self) -> QToolButton.ToolButtonPopupMode """
        pass

    def setArrowType(self, Qt_ArrowType): # real signature unknown; restored from __doc__
        """ setArrowType(self, Qt.ArrowType) """
        pass

    def setAutoRaise(self, bool): # real signature unknown; restored from __doc__
        """ setAutoRaise(self, bool) """
        pass

    def setDefaultAction(self, QAction): # real signature unknown; restored from __doc__
        """ setDefaultAction(self, QAction) """
        pass

    def setMenu(self, QMenu): # real signature unknown; restored from __doc__
        """ setMenu(self, QMenu) """
        pass

    def setPopupMode(self, QToolButton_ToolButtonPopupMode): # real signature unknown; restored from __doc__
        """ setPopupMode(self, QToolButton.ToolButtonPopupMode) """
        pass

    def setToolButtonStyle(self, Qt_ToolButtonStyle): # real signature unknown; restored from __doc__
        """ setToolButtonStyle(self, Qt.ToolButtonStyle) """
        pass

    def showMenu(self): # real signature unknown; restored from __doc__
        """ showMenu(self) """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> QSize """
        pass

    def timerEvent(self, QTimerEvent): # real signature unknown; restored from __doc__
        """ timerEvent(self, QTimerEvent) """
        pass

    def toolButtonStyle(self): # real signature unknown; restored from __doc__
        """ toolButtonStyle(self) -> Qt.ToolButtonStyle """
        pass

    def triggered(self, QAction): # real signature unknown; restored from __doc__
        """ triggered(self, QAction) [signal] """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass

    DelayedPopup = 0
    InstantPopup = 2
    MenuButtonPopup = 1


