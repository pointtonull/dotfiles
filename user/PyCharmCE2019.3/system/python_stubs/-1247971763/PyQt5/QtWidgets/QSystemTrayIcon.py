# encoding: utf-8
# module PyQt5.QtWidgets
# from /usr/lib/python3/dist-packages/PyQt5/QtWidgets.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui


class QSystemTrayIcon(__PyQt5_QtCore.QObject):
    """
    QSystemTrayIcon(parent: QObject = None)
    QSystemTrayIcon(QIcon, parent: QObject = None)
    """
    def activated(self, QSystemTrayIcon_ActivationReason): # real signature unknown; restored from __doc__
        """ activated(self, QSystemTrayIcon.ActivationReason) [signal] """
        pass

    def contextMenu(self): # real signature unknown; restored from __doc__
        """ contextMenu(self) -> QMenu """
        return QMenu

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def geometry(self): # real signature unknown; restored from __doc__
        """ geometry(self) -> QRect """
        pass

    def hide(self): # real signature unknown; restored from __doc__
        """ hide(self) """
        pass

    def icon(self): # real signature unknown; restored from __doc__
        """ icon(self) -> QIcon """
        pass

    def isSystemTrayAvailable(self): # real signature unknown; restored from __doc__
        """ isSystemTrayAvailable() -> bool """
        return False

    def isVisible(self): # real signature unknown; restored from __doc__
        """ isVisible(self) -> bool """
        return False

    def messageClicked(self): # real signature unknown; restored from __doc__
        """ messageClicked(self) [signal] """
        pass

    def setContextMenu(self, QMenu): # real signature unknown; restored from __doc__
        """ setContextMenu(self, QMenu) """
        pass

    def setIcon(self, QIcon): # real signature unknown; restored from __doc__
        """ setIcon(self, QIcon) """
        pass

    def setToolTip(self, p_str): # real signature unknown; restored from __doc__
        """ setToolTip(self, str) """
        pass

    def setVisible(self, bool): # real signature unknown; restored from __doc__
        """ setVisible(self, bool) """
        pass

    def show(self): # real signature unknown; restored from __doc__
        """ show(self) """
        pass

    def showMessage(self, p_str, p_str_1, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        showMessage(self, str, str, icon: QSystemTrayIcon.MessageIcon = QSystemTrayIcon.Information, msecs: int = 10000)
        showMessage(self, str, str, QIcon, msecs: int = 10000)
        """
        pass

    def supportsMessages(self): # real signature unknown; restored from __doc__
        """ supportsMessages() -> bool """
        return False

    def toolTip(self): # real signature unknown; restored from __doc__
        """ toolTip(self) -> str """
        return ""

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    Context = 1
    Critical = 3
    DoubleClick = 2
    Information = 1
    MiddleClick = 4
    NoIcon = 0
    Trigger = 3
    Unknown = 0
    Warning = 2


