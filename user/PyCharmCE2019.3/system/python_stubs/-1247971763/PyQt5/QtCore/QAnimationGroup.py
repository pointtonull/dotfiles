# encoding: utf-8
# module PyQt5.QtCore
# from /usr/lib/python3/dist-packages/PyQt5/QtCore.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc
# no imports

from .QAbstractAnimation import QAbstractAnimation

class QAnimationGroup(QAbstractAnimation):
    """ QAnimationGroup(parent: QObject = None) """
    def addAnimation(self, QAbstractAnimation): # real signature unknown; restored from __doc__
        """ addAnimation(self, QAbstractAnimation) """
        pass

    def animationAt(self, p_int): # real signature unknown; restored from __doc__
        """ animationAt(self, int) -> QAbstractAnimation """
        return QAbstractAnimation

    def animationCount(self): # real signature unknown; restored from __doc__
        """ animationCount(self) -> int """
        return 0

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def indexOfAnimation(self, QAbstractAnimation): # real signature unknown; restored from __doc__
        """ indexOfAnimation(self, QAbstractAnimation) -> int """
        return 0

    def insertAnimation(self, p_int, QAbstractAnimation): # real signature unknown; restored from __doc__
        """ insertAnimation(self, int, QAbstractAnimation) """
        pass

    def removeAnimation(self, QAbstractAnimation): # real signature unknown; restored from __doc__
        """ removeAnimation(self, QAbstractAnimation) """
        pass

    def takeAnimation(self, p_int): # real signature unknown; restored from __doc__
        """ takeAnimation(self, int) -> QAbstractAnimation """
        return QAbstractAnimation

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


