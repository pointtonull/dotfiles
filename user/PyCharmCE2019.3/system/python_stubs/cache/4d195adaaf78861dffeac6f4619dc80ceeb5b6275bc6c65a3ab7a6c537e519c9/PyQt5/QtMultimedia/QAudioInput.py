# encoding: utf-8
# module PyQt5.QtMultimedia
# from /usr/lib/python3/dist-packages/PyQt5/QtMultimedia.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore


class QAudioInput(__PyQt5_QtCore.QObject):
    """
    QAudioInput(format: QAudioFormat = QAudioFormat(), parent: QObject = None)
    QAudioInput(QAudioDeviceInfo, format: QAudioFormat = QAudioFormat(), parent: QObject = None)
    """
    def bufferSize(self): # real signature unknown; restored from __doc__
        """ bufferSize(self) -> int """
        return 0

    def bytesReady(self): # real signature unknown; restored from __doc__
        """ bytesReady(self) -> int """
        return 0

    def elapsedUSecs(self): # real signature unknown; restored from __doc__
        """ elapsedUSecs(self) -> int """
        return 0

    def error(self): # real signature unknown; restored from __doc__
        """ error(self) -> QAudio.Error """
        pass

    def format(self): # real signature unknown; restored from __doc__
        """ format(self) -> QAudioFormat """
        return QAudioFormat

    def notify(self): # real signature unknown; restored from __doc__
        """ notify(self) [signal] """
        pass

    def notifyInterval(self): # real signature unknown; restored from __doc__
        """ notifyInterval(self) -> int """
        return 0

    def periodSize(self): # real signature unknown; restored from __doc__
        """ periodSize(self) -> int """
        return 0

    def processedUSecs(self): # real signature unknown; restored from __doc__
        """ processedUSecs(self) -> int """
        return 0

    def reset(self): # real signature unknown; restored from __doc__
        """ reset(self) """
        pass

    def resume(self): # real signature unknown; restored from __doc__
        """ resume(self) """
        pass

    def setBufferSize(self, p_int): # real signature unknown; restored from __doc__
        """ setBufferSize(self, int) """
        pass

    def setNotifyInterval(self, p_int): # real signature unknown; restored from __doc__
        """ setNotifyInterval(self, int) """
        pass

    def setVolume(self, p_float): # real signature unknown; restored from __doc__
        """ setVolume(self, float) """
        pass

    def start(self, QIODevice=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        start(self, QIODevice)
        start(self) -> QIODevice
        """
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ state(self) -> QAudio.State """
        pass

    def stop(self): # real signature unknown; restored from __doc__
        """ stop(self) """
        pass

    def suspend(self): # real signature unknown; restored from __doc__
        """ suspend(self) """
        pass

    def volume(self): # real signature unknown; restored from __doc__
        """ volume(self) -> float """
        return 0.0

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


