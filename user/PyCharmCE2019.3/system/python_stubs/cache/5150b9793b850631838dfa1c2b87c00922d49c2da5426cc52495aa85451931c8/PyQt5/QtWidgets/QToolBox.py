# encoding: utf-8
# module PyQt5.QtWidgets
# from /usr/lib/python3/dist-packages/PyQt5/QtWidgets.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui


from .QFrame import QFrame

class QToolBox(QFrame):
    """ QToolBox(parent: QWidget = None, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags()) """
    def addItem(self, QWidget, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addItem(self, QWidget, str) -> int
        addItem(self, QWidget, QIcon, str) -> int
        """
        return 0

    def changeEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ changeEvent(self, QEvent) """
        pass

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

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def indexOf(self, QWidget): # real signature unknown; restored from __doc__
        """ indexOf(self, QWidget) -> int """
        return 0

    def insertItem(self, p_int, QWidget, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        insertItem(self, int, QWidget, str) -> int
        insertItem(self, int, QWidget, QIcon, str) -> int
        """
        return 0

    def isItemEnabled(self, p_int): # real signature unknown; restored from __doc__
        """ isItemEnabled(self, int) -> bool """
        return False

    def itemIcon(self, p_int): # real signature unknown; restored from __doc__
        """ itemIcon(self, int) -> QIcon """
        pass

    def itemInserted(self, p_int): # real signature unknown; restored from __doc__
        """ itemInserted(self, int) """
        pass

    def itemRemoved(self, p_int): # real signature unknown; restored from __doc__
        """ itemRemoved(self, int) """
        pass

    def itemText(self, p_int): # real signature unknown; restored from __doc__
        """ itemText(self, int) -> str """
        return ""

    def itemToolTip(self, p_int): # real signature unknown; restored from __doc__
        """ itemToolTip(self, int) -> str """
        return ""

    def removeItem(self, p_int): # real signature unknown; restored from __doc__
        """ removeItem(self, int) """
        pass

    def setCurrentIndex(self, p_int): # real signature unknown; restored from __doc__
        """ setCurrentIndex(self, int) """
        pass

    def setCurrentWidget(self, QWidget): # real signature unknown; restored from __doc__
        """ setCurrentWidget(self, QWidget) """
        pass

    def setItemEnabled(self, p_int, bool): # real signature unknown; restored from __doc__
        """ setItemEnabled(self, int, bool) """
        pass

    def setItemIcon(self, p_int, QIcon): # real signature unknown; restored from __doc__
        """ setItemIcon(self, int, QIcon) """
        pass

    def setItemText(self, p_int, p_str): # real signature unknown; restored from __doc__
        """ setItemText(self, int, str) """
        pass

    def setItemToolTip(self, p_int, p_str): # real signature unknown; restored from __doc__
        """ setItemToolTip(self, int, str) """
        pass

    def showEvent(self, QShowEvent): # real signature unknown; restored from __doc__
        """ showEvent(self, QShowEvent) """
        pass

    def widget(self, p_int): # real signature unknown; restored from __doc__
        """ widget(self, int) -> QWidget """
        return QWidget

    def __init__(self, parent=None, flags, Qt_WindowFlags=None, Qt_WindowType=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass


