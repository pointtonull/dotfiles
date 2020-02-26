# encoding: utf-8
# module PyQt5.QtMultimedia
# from /usr/lib/python3/dist-packages/PyQt5/QtMultimedia.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore


class QSound(__PyQt5_QtCore.QObject):
    """ QSound(str, parent: QObject = None) """
    def fileName(self): # real signature unknown; restored from __doc__
        """ fileName(self) -> str """
        return ""

    def isFinished(self): # real signature unknown; restored from __doc__
        """ isFinished(self) -> bool """
        return False

    def loops(self): # real signature unknown; restored from __doc__
        """ loops(self) -> int """
        return 0

    def loopsRemaining(self): # real signature unknown; restored from __doc__
        """ loopsRemaining(self) -> int """
        return 0

    def play(self, p_str=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        play(str)
        play(self)
        """
        pass

    def setLoops(self, p_int): # real signature unknown; restored from __doc__
        """ setLoops(self, int) """
        pass

    def stop(self): # real signature unknown; restored from __doc__
        """ stop(self) """
        pass

    def __init__(self, p_str, parent=None): # real signature unknown; restored from __doc__
        pass

    Infinite = -1


