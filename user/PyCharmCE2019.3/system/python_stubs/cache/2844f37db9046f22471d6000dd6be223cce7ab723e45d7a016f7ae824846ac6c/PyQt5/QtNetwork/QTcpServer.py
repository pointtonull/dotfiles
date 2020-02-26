# encoding: utf-8
# module PyQt5.QtNetwork
# from /usr/lib/python3/dist-packages/PyQt5/QtNetwork.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore


class QTcpServer(__PyQt5_QtCore.QObject):
    """ QTcpServer(parent: QObject = None) """
    def acceptError(self, QAbstractSocket_SocketError): # real signature unknown; restored from __doc__
        """ acceptError(self, QAbstractSocket.SocketError) [signal] """
        pass

    def addPendingConnection(self, QTcpSocket): # real signature unknown; restored from __doc__
        """ addPendingConnection(self, QTcpSocket) """
        pass

    def close(self): # real signature unknown; restored from __doc__
        """ close(self) """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
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

    def listen(self, address, QHostAddress=None, QHostAddress_SpecialAddress=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ listen(self, address: Union[QHostAddress, QHostAddress.SpecialAddress] = QHostAddress.Any, port: int = 0) -> bool """
        pass

    def maxPendingConnections(self): # real signature unknown; restored from __doc__
        """ maxPendingConnections(self) -> int """
        return 0

    def newConnection(self): # real signature unknown; restored from __doc__
        """ newConnection(self) [signal] """
        pass

    def nextPendingConnection(self): # real signature unknown; restored from __doc__
        """ nextPendingConnection(self) -> QTcpSocket """
        return QTcpSocket

    def pauseAccepting(self): # real signature unknown; restored from __doc__
        """ pauseAccepting(self) """
        pass

    def proxy(self): # real signature unknown; restored from __doc__
        """ proxy(self) -> QNetworkProxy """
        return QNetworkProxy

    def resumeAccepting(self): # real signature unknown; restored from __doc__
        """ resumeAccepting(self) """
        pass

    def serverAddress(self): # real signature unknown; restored from __doc__
        """ serverAddress(self) -> QHostAddress """
        return QHostAddress

    def serverError(self): # real signature unknown; restored from __doc__
        """ serverError(self) -> QAbstractSocket.SocketError """
        pass

    def serverPort(self): # real signature unknown; restored from __doc__
        """ serverPort(self) -> int """
        return 0

    def setMaxPendingConnections(self, p_int): # real signature unknown; restored from __doc__
        """ setMaxPendingConnections(self, int) """
        pass

    def setProxy(self, QNetworkProxy): # real signature unknown; restored from __doc__
        """ setProxy(self, QNetworkProxy) """
        pass

    def setSocketDescriptor(self, sip_voidptr): # real signature unknown; restored from __doc__
        """ setSocketDescriptor(self, sip.voidptr) -> bool """
        return False

    def socketDescriptor(self): # real signature unknown; restored from __doc__
        """ socketDescriptor(self) -> sip.voidptr """
        pass

    def waitForNewConnection(self, msecs=0): # real signature unknown; restored from __doc__
        """ waitForNewConnection(self, msecs: int = 0) -> Tuple[bool, bool] """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


