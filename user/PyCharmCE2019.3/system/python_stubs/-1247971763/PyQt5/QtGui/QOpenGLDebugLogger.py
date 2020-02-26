# encoding: utf-8
# module PyQt5.QtGui
# from /usr/lib/python3/dist-packages/PyQt5/QtGui.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore


class QOpenGLDebugLogger(__PyQt5_QtCore.QObject):
    """ QOpenGLDebugLogger(parent: QObject = None) """
    def disableMessages(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        disableMessages(self, sources: Union[QOpenGLDebugMessage.Sources, QOpenGLDebugMessage.Source] = QOpenGLDebugMessage.AnySource, types: Union[QOpenGLDebugMessage.Types, QOpenGLDebugMessage.Type] = QOpenGLDebugMessage.AnyType, severities: Union[QOpenGLDebugMessage.Severities, QOpenGLDebugMessage.Severity] = QOpenGLDebugMessage.AnySeverity)
        disableMessages(self, Iterable[int], sources: Union[QOpenGLDebugMessage.Sources, QOpenGLDebugMessage.Source] = QOpenGLDebugMessage.AnySource, types: Union[QOpenGLDebugMessage.Types, QOpenGLDebugMessage.Type] = QOpenGLDebugMessage.AnyType)
        """
        pass

    def enableMessages(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        enableMessages(self, sources: Union[QOpenGLDebugMessage.Sources, QOpenGLDebugMessage.Source] = QOpenGLDebugMessage.AnySource, types: Union[QOpenGLDebugMessage.Types, QOpenGLDebugMessage.Type] = QOpenGLDebugMessage.AnyType, severities: Union[QOpenGLDebugMessage.Severities, QOpenGLDebugMessage.Severity] = QOpenGLDebugMessage.AnySeverity)
        enableMessages(self, Iterable[int], sources: Union[QOpenGLDebugMessage.Sources, QOpenGLDebugMessage.Source] = QOpenGLDebugMessage.AnySource, types: Union[QOpenGLDebugMessage.Types, QOpenGLDebugMessage.Type] = QOpenGLDebugMessage.AnyType)
        """
        pass

    def initialize(self): # real signature unknown; restored from __doc__
        """ initialize(self) -> bool """
        return False

    def isLogging(self): # real signature unknown; restored from __doc__
        """ isLogging(self) -> bool """
        return False

    def loggedMessages(self): # real signature unknown; restored from __doc__
        """ loggedMessages(self) -> object """
        return object()

    def loggingMode(self): # real signature unknown; restored from __doc__
        """ loggingMode(self) -> QOpenGLDebugLogger.LoggingMode """
        pass

    def logMessage(self, QOpenGLDebugMessage): # real signature unknown; restored from __doc__
        """ logMessage(self, QOpenGLDebugMessage) """
        pass

    def maximumMessageLength(self): # real signature unknown; restored from __doc__
        """ maximumMessageLength(self) -> int """
        return 0

    def messageLogged(self, QOpenGLDebugMessage): # real signature unknown; restored from __doc__
        """ messageLogged(self, QOpenGLDebugMessage) [signal] """
        pass

    def popGroup(self): # real signature unknown; restored from __doc__
        """ popGroup(self) """
        pass

    def pushGroup(self, p_str, id=0, source=None): # real signature unknown; restored from __doc__
        """ pushGroup(self, str, id: int = 0, source: QOpenGLDebugMessage.Source = QOpenGLDebugMessage.ApplicationSource) """
        pass

    def startLogging(self, loggingMode=None): # real signature unknown; restored from __doc__
        """ startLogging(self, loggingMode: QOpenGLDebugLogger.LoggingMode = QOpenGLDebugLogger.AsynchronousLogging) """
        pass

    def stopLogging(self): # real signature unknown; restored from __doc__
        """ stopLogging(self) """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass

    AsynchronousLogging = 0
    SynchronousLogging = 1


