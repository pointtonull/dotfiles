# encoding: utf-8
# module PyQt5.QtWidgets
# from /usr/lib/python3/dist-packages/PyQt5/QtWidgets.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui


from .QWidget import QWidget

class QMainWindow(QWidget):
    """ QMainWindow(parent: QWidget = None, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags()) """
    def addDockWidget(self, Qt_DockWidgetArea, QDockWidget, Qt_Orientation=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addDockWidget(self, Qt.DockWidgetArea, QDockWidget)
        addDockWidget(self, Qt.DockWidgetArea, QDockWidget, Qt.Orientation)
        """
        pass

    def addToolBar(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addToolBar(self, Qt.ToolBarArea, QToolBar)
        addToolBar(self, QToolBar)
        addToolBar(self, str) -> QToolBar
        """
        return QToolBar

    def addToolBarBreak(self, area=None): # real signature unknown; restored from __doc__
        """ addToolBarBreak(self, area: Qt.ToolBarArea = Qt.TopToolBarArea) """
        pass

    def centralWidget(self): # real signature unknown; restored from __doc__
        """ centralWidget(self) -> QWidget """
        return QWidget

    def contextMenuEvent(self, QContextMenuEvent): # real signature unknown; restored from __doc__
        """ contextMenuEvent(self, QContextMenuEvent) """
        pass

    def corner(self, Qt_Corner): # real signature unknown; restored from __doc__
        """ corner(self, Qt.Corner) -> Qt.DockWidgetArea """
        pass

    def createPopupMenu(self): # real signature unknown; restored from __doc__
        """ createPopupMenu(self) -> QMenu """
        return QMenu

    def dockOptions(self): # real signature unknown; restored from __doc__
        """ dockOptions(self) -> QMainWindow.DockOptions """
        pass

    def dockWidgetArea(self, QDockWidget): # real signature unknown; restored from __doc__
        """ dockWidgetArea(self, QDockWidget) -> Qt.DockWidgetArea """
        pass

    def documentMode(self): # real signature unknown; restored from __doc__
        """ documentMode(self) -> bool """
        return False

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def iconSize(self): # real signature unknown; restored from __doc__
        """ iconSize(self) -> QSize """
        pass

    def iconSizeChanged(self, QSize): # real signature unknown; restored from __doc__
        """ iconSizeChanged(self, QSize) [signal] """
        pass

    def insertToolBar(self, QToolBar, QToolBar_1): # real signature unknown; restored from __doc__
        """ insertToolBar(self, QToolBar, QToolBar) """
        pass

    def insertToolBarBreak(self, QToolBar): # real signature unknown; restored from __doc__
        """ insertToolBarBreak(self, QToolBar) """
        pass

    def isAnimated(self): # real signature unknown; restored from __doc__
        """ isAnimated(self) -> bool """
        return False

    def isDockNestingEnabled(self): # real signature unknown; restored from __doc__
        """ isDockNestingEnabled(self) -> bool """
        return False

    def isSeparator(self, QPoint): # real signature unknown; restored from __doc__
        """ isSeparator(self, QPoint) -> bool """
        return False

    def menuBar(self): # real signature unknown; restored from __doc__
        """ menuBar(self) -> QMenuBar """
        return QMenuBar

    def menuWidget(self): # real signature unknown; restored from __doc__
        """ menuWidget(self) -> QWidget """
        return QWidget

    def removeDockWidget(self, QDockWidget): # real signature unknown; restored from __doc__
        """ removeDockWidget(self, QDockWidget) """
        pass

    def removeToolBar(self, QToolBar): # real signature unknown; restored from __doc__
        """ removeToolBar(self, QToolBar) """
        pass

    def removeToolBarBreak(self, QToolBar): # real signature unknown; restored from __doc__
        """ removeToolBarBreak(self, QToolBar) """
        pass

    def resizeDocks(self, Iterable, QDockWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ resizeDocks(self, Iterable[QDockWidget], Iterable[int], Qt.Orientation) """
        pass

    def restoreDockWidget(self, QDockWidget): # real signature unknown; restored from __doc__
        """ restoreDockWidget(self, QDockWidget) -> bool """
        return False

    def restoreState(self, Union, QByteArray=None, bytes=None, bytearray=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ restoreState(self, Union[QByteArray, bytes, bytearray], version: int = 0) -> bool """
        pass

    def saveState(self, version=0): # real signature unknown; restored from __doc__
        """ saveState(self, version: int = 0) -> QByteArray """
        pass

    def setAnimated(self, bool): # real signature unknown; restored from __doc__
        """ setAnimated(self, bool) """
        pass

    def setCentralWidget(self, QWidget): # real signature unknown; restored from __doc__
        """ setCentralWidget(self, QWidget) """
        pass

    def setCorner(self, Qt_Corner, Qt_DockWidgetArea): # real signature unknown; restored from __doc__
        """ setCorner(self, Qt.Corner, Qt.DockWidgetArea) """
        pass

    def setDockNestingEnabled(self, bool): # real signature unknown; restored from __doc__
        """ setDockNestingEnabled(self, bool) """
        pass

    def setDockOptions(self, Union, QMainWindow_DockOptions=None, QMainWindow_DockOption=None): # real signature unknown; restored from __doc__
        """ setDockOptions(self, Union[QMainWindow.DockOptions, QMainWindow.DockOption]) """
        pass

    def setDocumentMode(self, bool): # real signature unknown; restored from __doc__
        """ setDocumentMode(self, bool) """
        pass

    def setIconSize(self, QSize): # real signature unknown; restored from __doc__
        """ setIconSize(self, QSize) """
        pass

    def setMenuBar(self, QMenuBar): # real signature unknown; restored from __doc__
        """ setMenuBar(self, QMenuBar) """
        pass

    def setMenuWidget(self, QWidget): # real signature unknown; restored from __doc__
        """ setMenuWidget(self, QWidget) """
        pass

    def setStatusBar(self, QStatusBar): # real signature unknown; restored from __doc__
        """ setStatusBar(self, QStatusBar) """
        pass

    def setTabPosition(self, Union, Qt_DockWidgetAreas=None, Qt_DockWidgetArea=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setTabPosition(self, Union[Qt.DockWidgetAreas, Qt.DockWidgetArea], QTabWidget.TabPosition) """
        pass

    def setTabShape(self, QTabWidget_TabShape): # real signature unknown; restored from __doc__
        """ setTabShape(self, QTabWidget.TabShape) """
        pass

    def setToolButtonStyle(self, Qt_ToolButtonStyle): # real signature unknown; restored from __doc__
        """ setToolButtonStyle(self, Qt.ToolButtonStyle) """
        pass

    def setUnifiedTitleAndToolBarOnMac(self, bool): # real signature unknown; restored from __doc__
        """ setUnifiedTitleAndToolBarOnMac(self, bool) """
        pass

    def splitDockWidget(self, QDockWidget, QDockWidget_1, Qt_Orientation): # real signature unknown; restored from __doc__
        """ splitDockWidget(self, QDockWidget, QDockWidget, Qt.Orientation) """
        pass

    def statusBar(self): # real signature unknown; restored from __doc__
        """ statusBar(self) -> QStatusBar """
        return QStatusBar

    def tabifiedDockWidgetActivated(self, QDockWidget): # real signature unknown; restored from __doc__
        """ tabifiedDockWidgetActivated(self, QDockWidget) [signal] """
        pass

    def tabifiedDockWidgets(self, QDockWidget): # real signature unknown; restored from __doc__
        """ tabifiedDockWidgets(self, QDockWidget) -> object """
        return object()

    def tabifyDockWidget(self, QDockWidget, QDockWidget_1): # real signature unknown; restored from __doc__
        """ tabifyDockWidget(self, QDockWidget, QDockWidget) """
        pass

    def tabPosition(self, Qt_DockWidgetArea): # real signature unknown; restored from __doc__
        """ tabPosition(self, Qt.DockWidgetArea) -> QTabWidget.TabPosition """
        pass

    def tabShape(self): # real signature unknown; restored from __doc__
        """ tabShape(self) -> QTabWidget.TabShape """
        pass

    def takeCentralWidget(self): # real signature unknown; restored from __doc__
        """ takeCentralWidget(self) -> QWidget """
        return QWidget

    def toolBarArea(self, QToolBar): # real signature unknown; restored from __doc__
        """ toolBarArea(self, QToolBar) -> Qt.ToolBarArea """
        pass

    def toolBarBreak(self, QToolBar): # real signature unknown; restored from __doc__
        """ toolBarBreak(self, QToolBar) -> bool """
        return False

    def toolButtonStyle(self): # real signature unknown; restored from __doc__
        """ toolButtonStyle(self) -> Qt.ToolButtonStyle """
        pass

    def unifiedTitleAndToolBarOnMac(self): # real signature unknown; restored from __doc__
        """ unifiedTitleAndToolBarOnMac(self) -> bool """
        return False

    def __init__(self, parent=None, flags, Qt_WindowFlags=None, Qt_WindowType=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    AllowNestedDocks = 2
    AllowTabbedDocks = 4
    AnimatedDocks = 1
    ForceTabbedDocks = 8
    GroupedDragging = 32
    VerticalTabs = 16


