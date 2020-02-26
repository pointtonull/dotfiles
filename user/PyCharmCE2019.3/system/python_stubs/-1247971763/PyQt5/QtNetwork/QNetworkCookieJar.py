# encoding: utf-8
# module PyQt5.QtNetwork
# from /usr/lib/python3/dist-packages/PyQt5/QtNetwork.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore


class QNetworkCookieJar(__PyQt5_QtCore.QObject):
    """ QNetworkCookieJar(parent: QObject = None) """
    def allCookies(self): # real signature unknown; restored from __doc__
        """ allCookies(self) -> List[QNetworkCookie] """
        return []

    def cookiesForUrl(self, QUrl): # real signature unknown; restored from __doc__
        """ cookiesForUrl(self, QUrl) -> List[QNetworkCookie] """
        return []

    def deleteCookie(self, QNetworkCookie): # real signature unknown; restored from __doc__
        """ deleteCookie(self, QNetworkCookie) -> bool """
        return False

    def insertCookie(self, QNetworkCookie): # real signature unknown; restored from __doc__
        """ insertCookie(self, QNetworkCookie) -> bool """
        return False

    def setAllCookies(self, Iterable, QNetworkCookie=None): # real signature unknown; restored from __doc__
        """ setAllCookies(self, Iterable[QNetworkCookie]) """
        pass

    def setCookiesFromUrl(self, Iterable, QNetworkCookie=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setCookiesFromUrl(self, Iterable[QNetworkCookie], QUrl) -> bool """
        pass

    def updateCookie(self, QNetworkCookie): # real signature unknown; restored from __doc__
        """ updateCookie(self, QNetworkCookie) -> bool """
        return False

    def validateCookie(self, QNetworkCookie, QUrl): # real signature unknown; restored from __doc__
        """ validateCookie(self, QNetworkCookie, QUrl) -> bool """
        return False

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


