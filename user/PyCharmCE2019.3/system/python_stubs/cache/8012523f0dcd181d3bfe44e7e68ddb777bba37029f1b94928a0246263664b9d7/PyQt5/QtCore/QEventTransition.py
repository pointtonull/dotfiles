# encoding: utf-8
# module PyQt5.QtCore
# from /usr/lib/python3/dist-packages/PyQt5/QtCore.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc
# no imports

from .QAbstractTransition import QAbstractTransition

class QEventTransition(QAbstractTransition):
    """
    QEventTransition(sourceState: QState = None)
    QEventTransition(QObject, QEvent.Type, sourceState: QState = None)
    """
    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def eventSource(self): # real signature unknown; restored from __doc__
        """ eventSource(self) -> QObject """
        return QObject

    def eventTest(self, QEvent): # real signature unknown; restored from __doc__
        """ eventTest(self, QEvent) -> bool """
        return False

    def eventType(self): # real signature unknown; restored from __doc__
        """ eventType(self) -> QEvent.Type """
        pass

    def onTransition(self, QEvent): # real signature unknown; restored from __doc__
        """ onTransition(self, QEvent) """
        pass

    def setEventSource(self, QObject): # real signature unknown; restored from __doc__
        """ setEventSource(self, QObject) """
        pass

    def setEventType(self, QEvent_Type): # real signature unknown; restored from __doc__
        """ setEventType(self, QEvent.Type) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


