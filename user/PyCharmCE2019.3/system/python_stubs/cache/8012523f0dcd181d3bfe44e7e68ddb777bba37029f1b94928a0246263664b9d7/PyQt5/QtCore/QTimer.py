# encoding: utf-8
# module PyQt5.QtCore
# from /usr/lib/python3/dist-packages/PyQt5/QtCore.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc
# no imports

from .QObject import QObject

class QTimer(QObject):
    """ QTimer(parent: QObject = None) """
    def interval(self): # real signature unknown; restored from __doc__
        """ interval(self) -> int """
        return 0

    def isActive(self): # real signature unknown; restored from __doc__
        """ isActive(self) -> bool """
        return False

    def isSingleShot(self): # real signature unknown; restored from __doc__
        """ isSingleShot(self) -> bool """
        return False

    def remainingTime(self): # real signature unknown; restored from __doc__
        """ remainingTime(self) -> int """
        return 0

    def setInterval(self, p_int): # real signature unknown; restored from __doc__
        """ setInterval(self, int) """
        pass

    def setSingleShot(self, bool): # real signature unknown; restored from __doc__
        """ setSingleShot(self, bool) """
        pass

    def setTimerType(self, Qt_TimerType): # real signature unknown; restored from __doc__
        """ setTimerType(self, Qt.TimerType) """
        pass

    def singleShot(self, p_int, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        singleShot(int, PYQT_SLOT)
        singleShot(int, Qt.TimerType, PYQT_SLOT)
        """
        pass

    def start(self, p_int=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        start(self, int)
        start(self)
        """
        pass

    def stop(self): # real signature unknown; restored from __doc__
        """ stop(self) """
        pass

    def timeout(self): # real signature unknown; restored from __doc__
        """ timeout(self) [signal] """
        pass

    def timerEvent(self, QTimerEvent): # real signature unknown; restored from __doc__
        """ timerEvent(self, QTimerEvent) """
        pass

    def timerId(self): # real signature unknown; restored from __doc__
        """ timerId(self) -> int """
        return 0

    def timerType(self): # real signature unknown; restored from __doc__
        """ timerType(self) -> Qt.TimerType """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


