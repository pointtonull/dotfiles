# encoding: utf-8
# module PyQt5.QtNetwork
# from /usr/lib/python3/dist-packages/PyQt5/QtNetwork.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore


class QAbstractNetworkCache(__PyQt5_QtCore.QObject):
    """ QAbstractNetworkCache(parent: QObject = None) """
    def cacheSize(self): # real signature unknown; restored from __doc__
        """ cacheSize(self) -> int """
        return 0

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def data(self, QUrl): # real signature unknown; restored from __doc__
        """ data(self, QUrl) -> QIODevice """
        pass

    def insert(self, QIODevice): # real signature unknown; restored from __doc__
        """ insert(self, QIODevice) """
        pass

    def metaData(self, QUrl): # real signature unknown; restored from __doc__
        """ metaData(self, QUrl) -> QNetworkCacheMetaData """
        return QNetworkCacheMetaData

    def prepare(self, QNetworkCacheMetaData): # real signature unknown; restored from __doc__
        """ prepare(self, QNetworkCacheMetaData) -> QIODevice """
        pass

    def remove(self, QUrl): # real signature unknown; restored from __doc__
        """ remove(self, QUrl) -> bool """
        return False

    def updateMetaData(self, QNetworkCacheMetaData): # real signature unknown; restored from __doc__
        """ updateMetaData(self, QNetworkCacheMetaData) """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


