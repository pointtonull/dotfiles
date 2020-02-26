# encoding: utf-8
# module PyQt5.QtMultimedia
# from /usr/lib/python3/dist-packages/PyQt5/QtMultimedia.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore


class QMediaContent(): # skipped bases: <class 'sip.simplewrapper'>
    """
    QMediaContent()
    QMediaContent(QUrl)
    QMediaContent(QNetworkRequest)
    QMediaContent(QMediaResource)
    QMediaContent(object)
    QMediaContent(QMediaContent)
    QMediaContent(QMediaPlaylist, contentUrl: QUrl = QUrl())
    """
    def canonicalRequest(self): # real signature unknown; restored from __doc__
        """ canonicalRequest(self) -> QNetworkRequest """
        pass

    def canonicalResource(self): # real signature unknown; restored from __doc__
        """ canonicalResource(self) -> QMediaResource """
        return QMediaResource

    def canonicalUrl(self): # real signature unknown; restored from __doc__
        """ canonicalUrl(self) -> QUrl """
        pass

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def playlist(self): # real signature unknown; restored from __doc__
        """ playlist(self) -> QMediaPlaylist """
        return QMediaPlaylist

    def resources(self): # real signature unknown; restored from __doc__
        """ resources(self) -> object """
        return object()

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


    __hash__ = None


