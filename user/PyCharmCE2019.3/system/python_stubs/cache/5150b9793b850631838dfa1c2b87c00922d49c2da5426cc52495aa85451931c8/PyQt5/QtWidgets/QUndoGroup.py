# encoding: utf-8
# module PyQt5.QtWidgets
# from /usr/lib/python3/dist-packages/PyQt5/QtWidgets.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui


class QUndoGroup(__PyQt5_QtCore.QObject):
    """ QUndoGroup(parent: QObject = None) """
    def activeStack(self): # real signature unknown; restored from __doc__
        """ activeStack(self) -> QUndoStack """
        return QUndoStack

    def activeStackChanged(self, QUndoStack): # real signature unknown; restored from __doc__
        """ activeStackChanged(self, QUndoStack) [signal] """
        pass

    def addStack(self, QUndoStack): # real signature unknown; restored from __doc__
        """ addStack(self, QUndoStack) """
        pass

    def canRedo(self): # real signature unknown; restored from __doc__
        """ canRedo(self) -> bool """
        return False

    def canRedoChanged(self, bool): # real signature unknown; restored from __doc__
        """ canRedoChanged(self, bool) [signal] """
        pass

    def canUndo(self): # real signature unknown; restored from __doc__
        """ canUndo(self) -> bool """
        return False

    def canUndoChanged(self, bool): # real signature unknown; restored from __doc__
        """ canUndoChanged(self, bool) [signal] """
        pass

    def cleanChanged(self, bool): # real signature unknown; restored from __doc__
        """ cleanChanged(self, bool) [signal] """
        pass

    def createRedoAction(self, QObject, prefix=''): # real signature unknown; restored from __doc__
        """ createRedoAction(self, QObject, prefix: str = '') -> QAction """
        return QAction

    def createUndoAction(self, QObject, prefix=''): # real signature unknown; restored from __doc__
        """ createUndoAction(self, QObject, prefix: str = '') -> QAction """
        return QAction

    def indexChanged(self, p_int): # real signature unknown; restored from __doc__
        """ indexChanged(self, int) [signal] """
        pass

    def isClean(self): # real signature unknown; restored from __doc__
        """ isClean(self) -> bool """
        return False

    def redo(self): # real signature unknown; restored from __doc__
        """ redo(self) """
        pass

    def redoText(self): # real signature unknown; restored from __doc__
        """ redoText(self) -> str """
        return ""

    def redoTextChanged(self, p_str): # real signature unknown; restored from __doc__
        """ redoTextChanged(self, str) [signal] """
        pass

    def removeStack(self, QUndoStack): # real signature unknown; restored from __doc__
        """ removeStack(self, QUndoStack) """
        pass

    def setActiveStack(self, QUndoStack): # real signature unknown; restored from __doc__
        """ setActiveStack(self, QUndoStack) """
        pass

    def stacks(self): # real signature unknown; restored from __doc__
        """ stacks(self) -> object """
        return object()

    def undo(self): # real signature unknown; restored from __doc__
        """ undo(self) """
        pass

    def undoText(self): # real signature unknown; restored from __doc__
        """ undoText(self) -> str """
        return ""

    def undoTextChanged(self, p_str): # real signature unknown; restored from __doc__
        """ undoTextChanged(self, str) [signal] """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


