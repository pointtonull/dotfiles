# encoding: utf-8
# module PyQt5.QtWidgets
# from /usr/lib/python3/dist-packages/PyQt5/QtWidgets.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui


from .QWidget import QWidget

class QToolBar(QWidget):
    """
    QToolBar(str, parent: QWidget = None)
    QToolBar(parent: QWidget = None)
    """
    def actionAt(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        actionAt(self, QPoint) -> QAction
        actionAt(self, int, int) -> QAction
        """
        return QAction

    def actionEvent(self, QActionEvent): # real signature unknown; restored from __doc__
        """ actionEvent(self, QActionEvent) """
        pass

    def actionGeometry(self, QAction): # real signature unknown; restored from __doc__
        """ actionGeometry(self, QAction) -> QRect """
        pass

    def actionTriggered(self, QAction): # real signature unknown; restored from __doc__
        """ actionTriggered(self, QAction) [signal] """
        pass

    def addAction(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addAction(self, QAction)
        addAction(self, str) -> QAction
        addAction(self, QIcon, str) -> QAction
        addAction(self, str, PYQT_SLOT) -> QAction
        addAction(self, QIcon, str, PYQT_SLOT) -> QAction
        """
        return QAction

    def addSeparator(self): # real signature unknown; restored from __doc__
        """ addSeparator(self) -> QAction """
        return QAction

    def addWidget(self, QWidget): # real signature unknown; restored from __doc__
        """ addWidget(self, QWidget) -> QAction """
        return QAction

    def allowedAreas(self): # real signature unknown; restored from __doc__
        """ allowedAreas(self) -> Qt.ToolBarAreas """
        pass

    def changeEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ changeEvent(self, QEvent) """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def iconSize(self): # real signature unknown; restored from __doc__
        """ iconSize(self) -> QSize """
        pass

    def iconSizeChanged(self, QSize): # real signature unknown; restored from __doc__
        """ iconSizeChanged(self, QSize) [signal] """
        pass

    def initStyleOption(self, QStyleOptionToolBar): # real signature unknown; restored from __doc__
        """ initStyleOption(self, QStyleOptionToolBar) """
        pass

    def insertSeparator(self, QAction): # real signature unknown; restored from __doc__
        """ insertSeparator(self, QAction) -> QAction """
        return QAction

    def insertWidget(self, QAction, QWidget): # real signature unknown; restored from __doc__
        """ insertWidget(self, QAction, QWidget) -> QAction """
        return QAction

    def isAreaAllowed(self, Qt_ToolBarArea): # real signature unknown; restored from __doc__
        """ isAreaAllowed(self, Qt.ToolBarArea) -> bool """
        return False

    def isFloatable(self): # real signature unknown; restored from __doc__
        """ isFloatable(self) -> bool """
        return False

    def isFloating(self): # real signature unknown; restored from __doc__
        """ isFloating(self) -> bool """
        return False

    def isMovable(self): # real signature unknown; restored from __doc__
        """ isMovable(self) -> bool """
        return False

    def movableChanged(self, bool): # real signature unknown; restored from __doc__
        """ movableChanged(self, bool) [signal] """
        pass

    def orientation(self): # real signature unknown; restored from __doc__
        """ orientation(self) -> Qt.Orientation """
        pass

    def paintEvent(self, QPaintEvent): # real signature unknown; restored from __doc__
        """ paintEvent(self, QPaintEvent) """
        pass

    def setAllowedAreas(self, Union, Qt_ToolBarAreas=None, Qt_ToolBarArea=None): # real signature unknown; restored from __doc__
        """ setAllowedAreas(self, Union[Qt.ToolBarAreas, Qt.ToolBarArea]) """
        pass

    def setFloatable(self, bool): # real signature unknown; restored from __doc__
        """ setFloatable(self, bool) """
        pass

    def setIconSize(self, QSize): # real signature unknown; restored from __doc__
        """ setIconSize(self, QSize) """
        pass

    def setMovable(self, bool): # real signature unknown; restored from __doc__
        """ setMovable(self, bool) """
        pass

    def setOrientation(self, Qt_Orientation): # real signature unknown; restored from __doc__
        """ setOrientation(self, Qt.Orientation) """
        pass

    def setToolButtonStyle(self, Qt_ToolButtonStyle): # real signature unknown; restored from __doc__
        """ setToolButtonStyle(self, Qt.ToolButtonStyle) """
        pass

    def toggleViewAction(self): # real signature unknown; restored from __doc__
        """ toggleViewAction(self) -> QAction """
        return QAction

    def toolButtonStyle(self): # real signature unknown; restored from __doc__
        """ toolButtonStyle(self) -> Qt.ToolButtonStyle """
        pass

    def topLevelChanged(self, bool): # real signature unknown; restored from __doc__
        """ topLevelChanged(self, bool) [signal] """
        pass

    def visibilityChanged(self, bool): # real signature unknown; restored from __doc__
        """ visibilityChanged(self, bool) [signal] """
        pass

    def widgetForAction(self, QAction): # real signature unknown; restored from __doc__
        """ widgetForAction(self, QAction) -> QWidget """
        return QWidget

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


