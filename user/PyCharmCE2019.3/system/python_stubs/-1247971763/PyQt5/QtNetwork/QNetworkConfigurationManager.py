# encoding: utf-8
# module PyQt5.QtNetwork
# from /usr/lib/python3/dist-packages/PyQt5/QtNetwork.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore


class QNetworkConfigurationManager(__PyQt5_QtCore.QObject):
    """ QNetworkConfigurationManager(parent: QObject = None) """
    def allConfigurations(self, flags, QNetworkConfiguration_StateFlags=None, QNetworkConfiguration_StateFlag=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ allConfigurations(self, flags: Union[QNetworkConfiguration.StateFlags, QNetworkConfiguration.StateFlag] = QNetworkConfiguration.StateFlags()) -> object """
        pass

    def capabilities(self): # real signature unknown; restored from __doc__
        """ capabilities(self) -> QNetworkConfigurationManager.Capabilities """
        pass

    def configurationAdded(self, QNetworkConfiguration): # real signature unknown; restored from __doc__
        """ configurationAdded(self, QNetworkConfiguration) [signal] """
        pass

    def configurationChanged(self, QNetworkConfiguration): # real signature unknown; restored from __doc__
        """ configurationChanged(self, QNetworkConfiguration) [signal] """
        pass

    def configurationFromIdentifier(self, p_str): # real signature unknown; restored from __doc__
        """ configurationFromIdentifier(self, str) -> QNetworkConfiguration """
        return QNetworkConfiguration

    def configurationRemoved(self, QNetworkConfiguration): # real signature unknown; restored from __doc__
        """ configurationRemoved(self, QNetworkConfiguration) [signal] """
        pass

    def defaultConfiguration(self): # real signature unknown; restored from __doc__
        """ defaultConfiguration(self) -> QNetworkConfiguration """
        return QNetworkConfiguration

    def isOnline(self): # real signature unknown; restored from __doc__
        """ isOnline(self) -> bool """
        return False

    def onlineStateChanged(self, bool): # real signature unknown; restored from __doc__
        """ onlineStateChanged(self, bool) [signal] """
        pass

    def updateCompleted(self): # real signature unknown; restored from __doc__
        """ updateCompleted(self) [signal] """
        pass

    def updateConfigurations(self): # real signature unknown; restored from __doc__
        """ updateConfigurations(self) """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass

    ApplicationLevelRoaming = 8
    CanStartAndStopInterfaces = 1
    DataStatistics = 32
    DirectConnectionRouting = 2
    ForcedRoaming = 16
    NetworkSessionRequired = 64
    SystemSessionSupport = 4


