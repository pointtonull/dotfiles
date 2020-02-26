# encoding: utf-8
# module PyQt5.QtMultimedia
# from /usr/lib/python3/dist-packages/PyQt5/QtMultimedia.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore


class QAudioProbe(__PyQt5_QtCore.QObject):
    """ QAudioProbe(parent: QObject = None) """
    def audioBufferProbed(self, QAudioBuffer): # real signature unknown; restored from __doc__
        """ audioBufferProbed(self, QAudioBuffer) [signal] """
        pass

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

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


