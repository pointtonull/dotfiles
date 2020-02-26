# encoding: utf-8
# module PyQt5.QtNetwork
# from /usr/lib/python3/dist-packages/PyQt5/QtNetwork.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore


class QLocalServer(__PyQt5_QtCore.QObject):
    """ QLocalServer(parent: QObject = None) """
    def close(self): # real signature unknown; restored from __doc__
        """ close(self) """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def fullServerName(self): # real signature unknown; restored from __doc__
        """ fullServerName(self) -> str """
        return ""

    def hasPendingConnections(self): # real signature unknown; restored from __doc__
        """ hasPendingConnections(self) -> bool """
        return False

    def incomingConnection(self, sip_voidptr): # real signature unknown; restored from __doc__
        """ incomingConnection(self, sip.voidptr) """
        pass

    def isListening(self): # real signature unknown; restored from __doc__
        """ isListening(self) -> bool """
        return False

    def listen(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        listen(self, str) -> bool
        listen(self, sip.voidptr) -> bool
        """
        return False

    def maxPendingConnections(self): # real signature unknown; restored from __doc__
        """ maxPendingConnections(self) -> int """
        return 0

    def newConnection(self): # real signature unknown; restored from __doc__
        """ newConnection(self) [signal] """
        pass

    def nextPendingConnection(self): # real signature unknown; restored from __doc__
        """ nextPendingConnection(self) -> QLocalSocket """
        return QLocalSocket

    def removeServer(self, p_str): # real signature unknown; restored from __doc__
        """ removeServer(str) -> bool """
        return False

    def serverError(self): # real signature unknown; restored from __doc__
        """ serverError(self) -> QAbstractSocket.SocketError """
        pass

    def serverName(self): # real signature unknown; restored from __doc__
        """ serverName(self) -> str """
        return ""

    def setMaxPendingConnections(self, p_int): # real signature unknown; restored from __doc__
        """ setMaxPendingConnections(self, int) """
        pass

    def setSocketOptions(self, Union, QLocalServer_SocketOptions=None, QLocalServer_SocketOption=None): # real signature unknown; restored from __doc__
        """ setSocketOptions(self, Union[QLocalServer.SocketOptions, QLocalServer.SocketOption]) """
        pass

    def socketOptions(self): # real signature unknown; restored from __doc__
        """ socketOptions(self) -> QLocalServer.SocketOptions """
        pass

    def waitForNewConnection(self, msecs=0): # real signature unknown; restored from __doc__
        """ waitForNewConnection(self, msecs: int = 0) -> Tuple[bool, bool] """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass

    GroupAccessOption = 2
    OtherAccessOption = 4
    UserAccessOption = 1
    WorldAccessOption = 7


