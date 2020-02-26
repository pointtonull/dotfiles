# encoding: utf-8
# module PyQt5.QtWidgets
# from /usr/lib/python3/dist-packages/PyQt5/QtWidgets.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui


from .QListView import QListView

class QUndoView(QListView):
    """
    QUndoView(parent: QWidget = None)
    QUndoView(QUndoStack, parent: QWidget = None)
    QUndoView(QUndoGroup, parent: QWidget = None)
    """
    def cleanIcon(self): # real signature unknown; restored from __doc__
        """ cleanIcon(self) -> QIcon """
        pass

    def emptyLabel(self): # real signature unknown; restored from __doc__
        """ emptyLabel(self) -> str """
        return ""

    def group(self): # real signature unknown; restored from __doc__
        """ group(self) -> QUndoGroup """
        return QUndoGroup

    def setCleanIcon(self, QIcon): # real signature unknown; restored from __doc__
        """ setCleanIcon(self, QIcon) """
        pass

    def setEmptyLabel(self, p_str): # real signature unknown; restored from __doc__
        """ setEmptyLabel(self, str) """
        pass

    def setGroup(self, QUndoGroup): # real signature unknown; restored from __doc__
        """ setGroup(self, QUndoGroup) """
        pass

    def setStack(self, QUndoStack): # real signature unknown; restored from __doc__
        """ setStack(self, QUndoStack) """
        pass

    def stack(self): # real signature unknown; restored from __doc__
        """ stack(self) -> QUndoStack """
        return QUndoStack

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


