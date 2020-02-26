# encoding: utf-8
# module PyQt5.QtCore
# from /usr/lib/python3/dist-packages/PyQt5/QtCore.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc
# no imports

class QUuid(): # skipped bases: <class 'sip.simplewrapper'>
    """
    QUuid()
    QUuid(int, int, int, int, int, int, int, int, int, int, int)
    QUuid(str)
    QUuid(Union[QByteArray, bytes, bytearray])
    QUuid(QUuid)
    """
    def createUuid(self): # real signature unknown; restored from __doc__
        """ createUuid() -> QUuid """
        return QUuid

    def createUuidV3(self, QUuid, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        createUuidV3(QUuid, Union[QByteArray, bytes, bytearray]) -> QUuid
        createUuidV3(QUuid, str) -> QUuid
        """
        return QUuid

    def createUuidV5(self, QUuid, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        createUuidV5(QUuid, Union[QByteArray, bytes, bytearray]) -> QUuid
        createUuidV5(QUuid, str) -> QUuid
        """
        return QUuid

    def fromRfc4122(self, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ fromRfc4122(Union[QByteArray, bytes, bytearray]) -> QUuid """
        return QUuid

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def toByteArray(self): # real signature unknown; restored from __doc__
        """ toByteArray(self) -> QByteArray """
        return QByteArray

    def toRfc4122(self): # real signature unknown; restored from __doc__
        """ toRfc4122(self) -> QByteArray """
        return QByteArray

    def toString(self): # real signature unknown; restored from __doc__
        """ toString(self) -> str """
        return ""

    def variant(self): # real signature unknown; restored from __doc__
        """ variant(self) -> QUuid.Variant """
        pass

    def version(self): # real signature unknown; restored from __doc__
        """ version(self) -> QUuid.Version """
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

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
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

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    DCE = 2
    EmbeddedPOSIX = 2
    Md5 = 3
    Microsoft = 6
    Name = 3
    NCS = 0
    Random = 4
    Reserved = 7
    Sha1 = 5
    Time = 1
    VarUnknown = -1
    VerUnknown = -1


