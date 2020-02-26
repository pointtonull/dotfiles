# encoding: utf-8
# module PyQt5.QtMultimedia
# from /usr/lib/python3/dist-packages/PyQt5/QtMultimedia.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore


class QVideoProbe(__PyQt5_QtCore.QObject):
    """ QVideoProbe(parent: QObject = None) """
    def flush(self): # real signature unknown; restored from __doc__
        """ flush(self) [signal] """
        pass

    def isActive(self): # real signature unknown; restored from __doc__
        """ isActive(self) -> bool """
        return False

    def setSource(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setSource(self, QMediaObject) -> bool
        setSource(self, QMediaRecorder) -> bool
        """
        return False

    def videoFrameProbed(self, QVideoFrame): # real signature unknown; restored from __doc__
        """ videoFrameProbed(self, QVideoFrame) [signal] """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


