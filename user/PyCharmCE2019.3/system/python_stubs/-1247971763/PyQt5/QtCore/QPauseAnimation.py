# encoding: utf-8
# module PyQt5.QtCore
# from /usr/lib/python3/dist-packages/PyQt5/QtCore.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc
# no imports

from .QAbstractAnimation import QAbstractAnimation

class QPauseAnimation(QAbstractAnimation):
    """
    QPauseAnimation(parent: QObject = None)
    QPauseAnimation(int, parent: QObject = None)
    """
    def duration(self): # real signature unknown; restored from __doc__
        """ duration(self) -> int """
        return 0

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def setDuration(self, p_int): # real signature unknown; restored from __doc__
        """ setDuration(self, int) """
        pass

    def updateCurrentTime(self, p_int): # real signature unknown; restored from __doc__
        """ updateCurrentTime(self, int) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


