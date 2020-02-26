# encoding: utf-8
# module PyQt5.QtWidgets
# from /usr/lib/python3/dist-packages/PyQt5/QtWidgets.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui


from .QWidget import QWidget

class QDockWidget(QWidget):
    """
    QDockWidget(str, parent: QWidget = None, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags())
    QDockWidget(parent: QWidget = None, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags())
    """
    def allowedAreas(self): # real signature unknown; restored from __doc__
        """ allowedAreas(self) -> Qt.DockWidgetAreas """
        pass

    def changeEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ changeEvent(self, QEvent) """
        pass

    def closeEvent(self, QCloseEvent): # real signature unknown; restored from __doc__
        """ closeEvent(self, QCloseEvent) """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def features(self): # real signature unknown; restored from __doc__
        """ features(self) -> QDockWidget.DockWidgetFeatures """
        pass

    def featuresChanged(self, Union, QDockWidget_DockWidgetFeatures=None, QDockWidget_DockWidgetFeature=None): # real signature unknown; restored from __doc__
        """ featuresChanged(self, Union[QDockWidget.DockWidgetFeatures, QDockWidget.DockWidgetFeature]) [signal] """
        pass

    def initStyleOption(self, QStyleOptionDockWidget): # real signature unknown; restored from __doc__
        """ initStyleOption(self, QStyleOptionDockWidget) """
        pass

    def isAreaAllowed(self, Qt_DockWidgetArea): # real signature unknown; restored from __doc__
        """ isAreaAllowed(self, Qt.DockWidgetArea) -> bool """
        return False

    def isFloating(self): # real signature unknown; restored from __doc__
        """ isFloating(self) -> bool """
        return False

    def paintEvent(self, QPaintEvent): # real signature unknown; restored from __doc__
        """ paintEvent(self, QPaintEvent) """
        pass

    def setAllowedAreas(self, Union, Qt_DockWidgetAreas=None, Qt_DockWidgetArea=None): # real signature unknown; restored from __doc__
        """ setAllowedAreas(self, Union[Qt.DockWidgetAreas, Qt.DockWidgetArea]) """
        pass

    def setFeatures(self, Union, QDockWidget_DockWidgetFeatures=None, QDockWidget_DockWidgetFeature=None): # real signature unknown; restored from __doc__
        """ setFeatures(self, Union[QDockWidget.DockWidgetFeatures, QDockWidget.DockWidgetFeature]) """
        pass

    def setFloating(self, bool): # real signature unknown; restored from __doc__
        """ setFloating(self, bool) """
        pass

    def setTitleBarWidget(self, QWidget): # real signature unknown; restored from __doc__
        """ setTitleBarWidget(self, QWidget) """
        pass

    def setWidget(self, QWidget): # real signature unknown; restored from __doc__
        """ setWidget(self, QWidget) """
        pass

    def titleBarWidget(self): # real signature unknown; restored from __doc__
        """ titleBarWidget(self) -> QWidget """
        return QWidget

    def toggleViewAction(self): # real signature unknown; restored from __doc__
        """ toggleViewAction(self) -> QAction """
        return QAction

    def topLevelChanged(self, bool): # real signature unknown; restored from __doc__
        """ topLevelChanged(self, bool) [signal] """
        pass

    def visibilityChanged(self, bool): # real signature unknown; restored from __doc__
        """ visibilityChanged(self, bool) [signal] """
        pass

    def widget(self): # real signature unknown; restored from __doc__
        """ widget(self) -> QWidget """
        return QWidget

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    AllDockWidgetFeatures = 7
    DockWidgetClosable = 1
    DockWidgetFloatable = 4
    DockWidgetMovable = 2
    DockWidgetVerticalTitleBar = 8
    NoDockWidgetFeatures = 0


