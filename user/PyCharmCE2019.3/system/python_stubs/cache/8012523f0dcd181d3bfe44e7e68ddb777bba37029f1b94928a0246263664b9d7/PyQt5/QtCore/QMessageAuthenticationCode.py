# encoding: utf-8
# module PyQt5.QtCore
# from /usr/lib/python3/dist-packages/PyQt5/QtCore.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc
# no imports

class QMessageAuthenticationCode(): # skipped bases: <class 'sip.simplewrapper'>
    """ QMessageAuthenticationCode(QCryptographicHash.Algorithm, key: Union[QByteArray, bytes, bytearray] = QByteArray()) """
    def addData(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addData(self, str, int)
        addData(self, Union[QByteArray, bytes, bytearray])
        addData(self, QIODevice) -> bool
        """
        return False

    def hash(self, Union, QByteArray=None, bytes=None, bytearray=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ hash(Union[QByteArray, bytes, bytearray], Union[QByteArray, bytes, bytearray], QCryptographicHash.Algorithm) -> QByteArray """
        pass

    def reset(self): # real signature unknown; restored from __doc__
        """ reset(self) """
        pass

    def result(self): # real signature unknown; restored from __doc__
        """ result(self) -> QByteArray """
        return QByteArray

    def setKey(self, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ setKey(self, Union[QByteArray, bytes, bytearray]) """
        pass

    def __init__(self, QCryptographicHash_Algorithm, key, QByteArray=None, bytes=None, bytearray=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



