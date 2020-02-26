# encoding: utf-8
# module PyQt5.QtCore
# from /usr/lib/python3/dist-packages/PyQt5/QtCore.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc
# no imports

from .QAbstractState import QAbstractState

class QHistoryState(QAbstractState):
    """
    QHistoryState(parent: QState = None)
    QHistoryState(QHistoryState.HistoryType, parent: QState = None)
    """
    def defaultState(self): # real signature unknown; restored from __doc__
        """ defaultState(self) -> QAbstractState """
        return QAbstractState

    def defaultStateChanged(self): # real signature unknown; restored from __doc__
        """ defaultStateChanged(self) [signal] """
        pass

    def defaultTransition(self): # real signature unknown; restored from __doc__
        """ defaultTransition(self) -> QAbstractTransition """
        return QAbstractTransition

    def defaultTransitionChanged(self): # real signature unknown; restored from __doc__
        """ defaultTransitionChanged(self) [signal] """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def historyType(self): # real signature unknown; restored from __doc__
        """ historyType(self) -> QHistoryState.HistoryType """
        pass

    def historyTypeChanged(self): # real signature unknown; restored from __doc__
        """ historyTypeChanged(self) [signal] """
        pass

    def onEntry(self, QEvent): # real signature unknown; restored from __doc__
        """ onEntry(self, QEvent) """
        pass

    def onExit(self, QEvent): # real signature unknown; restored from __doc__
        """ onExit(self, QEvent) """
        pass

    def setDefaultState(self, QAbstractState): # real signature unknown; restored from __doc__
        """ setDefaultState(self, QAbstractState) """
        pass

    def setDefaultTransition(self, QAbstractTransition): # real signature unknown; restored from __doc__
        """ setDefaultTransition(self, QAbstractTransition) """
        pass

    def setHistoryType(self, QHistoryState_HistoryType): # real signature unknown; restored from __doc__
        """ setHistoryType(self, QHistoryState.HistoryType) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    DeepHistory = 1
    ShallowHistory = 0


