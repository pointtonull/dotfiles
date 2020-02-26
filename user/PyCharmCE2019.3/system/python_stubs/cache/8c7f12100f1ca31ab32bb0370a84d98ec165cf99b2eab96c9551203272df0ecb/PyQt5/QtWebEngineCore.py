# encoding: utf-8
# module PyQt5.QtWebEngineCore
# from /usr/lib/python3/dist-packages/PyQt5/QtWebEngineCore.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore


# no functions
# classes

class QWebEngineCookieStore(__PyQt5_QtCore.QObject):
    # no doc
    def cookieAdded(self, QNetworkCookie): # real signature unknown; restored from __doc__
        """ cookieAdded(self, QNetworkCookie) [signal] """
        pass

    def cookieRemoved(self, QNetworkCookie): # real signature unknown; restored from __doc__
        """ cookieRemoved(self, QNetworkCookie) [signal] """
        pass

    def deleteAllCookies(self): # real signature unknown; restored from __doc__
        """ deleteAllCookies(self) """
        pass

    def deleteCookie(self, QNetworkCookie, origin=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ deleteCookie(self, QNetworkCookie, origin: QUrl = QUrl()) """
        pass

    def deleteSessionCookies(self): # real signature unknown; restored from __doc__
        """ deleteSessionCookies(self) """
        pass

    def loadAllCookies(self): # real signature unknown; restored from __doc__
        """ loadAllCookies(self) """
        pass

    def setCookie(self, QNetworkCookie, origin=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setCookie(self, QNetworkCookie, origin: QUrl = QUrl()) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class QWebEngineHttpRequest(): # skipped bases: <class 'sip.simplewrapper'>
    """
    QWebEngineHttpRequest(url: QUrl = QUrl(), method: QWebEngineHttpRequest.Method = QWebEngineHttpRequest.Method.Get)
    QWebEngineHttpRequest(QWebEngineHttpRequest)
    """
    def hasHeader(self, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ hasHeader(self, Union[QByteArray, bytes, bytearray]) -> bool """
        return False

    def header(self, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ header(self, Union[QByteArray, bytes, bytearray]) -> QByteArray """
        pass

    def headers(self): # real signature unknown; restored from __doc__
        """ headers(self) -> object """
        return object()

    def method(self): # real signature unknown; restored from __doc__
        """ method(self) -> QWebEngineHttpRequest.Method """
        pass

    def postData(self): # real signature unknown; restored from __doc__
        """ postData(self) -> QByteArray """
        pass

    def postRequest(self, QUrl, p_object): # real signature unknown; restored from __doc__
        """ postRequest(QUrl, object) -> QWebEngineHttpRequest """
        return QWebEngineHttpRequest

    def setHeader(self, Union, QByteArray=None, bytes=None, bytearray=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setHeader(self, Union[QByteArray, bytes, bytearray], Union[QByteArray, bytes, bytearray]) """
        pass

    def setMethod(self, QWebEngineHttpRequest_Method): # real signature unknown; restored from __doc__
        """ setMethod(self, QWebEngineHttpRequest.Method) """
        pass

    def setPostData(self, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ setPostData(self, Union[QByteArray, bytes, bytearray]) """
        pass

    def setUrl(self, QUrl): # real signature unknown; restored from __doc__
        """ setUrl(self, QUrl) """
        pass

    def swap(self, QWebEngineHttpRequest): # real signature unknown; restored from __doc__
        """ swap(self, QWebEngineHttpRequest) """
        pass

    def unsetHeader(self, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ unsetHeader(self, Union[QByteArray, bytes, bytearray]) """
        pass

    def url(self): # real signature unknown; restored from __doc__
        """ url(self) -> QUrl """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    Get = 0
    Post = 1
    __hash__ = None


class QWebEngineUrlRequestInfo(): # skipped bases: <class 'sip.simplewrapper'>
    # no doc
    def block(self, bool): # real signature unknown; restored from __doc__
        """ block(self, bool) """
        pass

    def firstPartyUrl(self): # real signature unknown; restored from __doc__
        """ firstPartyUrl(self) -> QUrl """
        pass

    def navigationType(self): # real signature unknown; restored from __doc__
        """ navigationType(self) -> QWebEngineUrlRequestInfo.NavigationType """
        pass

    def redirect(self, QUrl): # real signature unknown; restored from __doc__
        """ redirect(self, QUrl) """
        pass

    def requestMethod(self): # real signature unknown; restored from __doc__
        """ requestMethod(self) -> QByteArray """
        pass

    def requestUrl(self): # real signature unknown; restored from __doc__
        """ requestUrl(self) -> QUrl """
        pass

    def resourceType(self): # real signature unknown; restored from __doc__
        """ resourceType(self) -> QWebEngineUrlRequestInfo.ResourceType """
        pass

    def setHttpHeader(self, Union, QByteArray=None, bytes=None, bytearray=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setHttpHeader(self, Union[QByteArray, bytes, bytearray], Union[QByteArray, bytes, bytearray]) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    NavigationTypeBackForward = 3
    NavigationTypeFormSubmitted = 2
    NavigationTypeLink = 0
    NavigationTypeOther = 5
    NavigationTypeReload = 4
    NavigationTypeTyped = 1
    ResourceTypeCspReport = 16
    ResourceTypeFavicon = 12
    ResourceTypeFontResource = 5
    ResourceTypeImage = 4
    ResourceTypeMainFrame = 0
    ResourceTypeMedia = 8
    ResourceTypeObject = 7
    ResourceTypePing = 14
    ResourceTypePluginResource = 17
    ResourceTypePrefetch = 11
    ResourceTypeScript = 3
    ResourceTypeServiceWorker = 15
    ResourceTypeSharedWorker = 10
    ResourceTypeStylesheet = 2
    ResourceTypeSubFrame = 1
    ResourceTypeSubResource = 6
    ResourceTypeUnknown = 255
    ResourceTypeWorker = 9
    ResourceTypeXhr = 13


class QWebEngineUrlRequestInterceptor(__PyQt5_QtCore.QObject):
    """ QWebEngineUrlRequestInterceptor(parent: QObject = None) """
    def interceptRequest(self, QWebEngineUrlRequestInfo): # real signature unknown; restored from __doc__
        """ interceptRequest(self, QWebEngineUrlRequestInfo) """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


class QWebEngineUrlRequestJob(__PyQt5_QtCore.QObject):
    # no doc
    def fail(self, QWebEngineUrlRequestJob_Error): # real signature unknown; restored from __doc__
        """ fail(self, QWebEngineUrlRequestJob.Error) """
        pass

    def redirect(self, QUrl): # real signature unknown; restored from __doc__
        """ redirect(self, QUrl) """
        pass

    def reply(self, Union, QByteArray=None, bytes=None, bytearray=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ reply(self, Union[QByteArray, bytes, bytearray], QIODevice) """
        pass

    def requestMethod(self): # real signature unknown; restored from __doc__
        """ requestMethod(self) -> QByteArray """
        pass

    def requestUrl(self): # real signature unknown; restored from __doc__
        """ requestUrl(self) -> QUrl """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    NoError = 0
    RequestAborted = 3
    RequestDenied = 4
    RequestFailed = 5
    UrlInvalid = 2
    UrlNotFound = 1


class QWebEngineUrlSchemeHandler(__PyQt5_QtCore.QObject):
    """ QWebEngineUrlSchemeHandler(parent: QObject = None) """
    def requestStarted(self, QWebEngineUrlRequestJob): # real signature unknown; restored from __doc__
        """ requestStarted(self, QWebEngineUrlRequestJob) """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


# variables with complex values



