# encoding: utf-8
# module PyQt5.QtCore
# from /usr/lib/python3/dist-packages/PyQt5/QtCore.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc
# no imports

from .QObject import QObject

class QSignalMapper(QObject):
    """ QSignalMapper(parent: QObject = None) """
    def map(self, QObject=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        map(self)
        map(self, QObject)
        """
        pass

    def mapped(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        mapped(self, int) [signal]
        mapped(self, str) [signal]
        mapped(self, QObject) [signal]
        """
        pass

    def mapping(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        mapping(self, int) -> QObject
        mapping(self, str) -> QObject
        mapping(self, QWidget) -> QObject
        mapping(self, QObject) -> QObject
        """
        return QObject

    def removeMappings(self, QObject): # real signature unknown; restored from __doc__
        """ removeMappings(self, QObject) """
        pass

    def setMapping(self, QObject, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setMapping(self, QObject, int)
        setMapping(self, QObject, str)
        setMapping(self, QObject, QWidget)
        setMapping(self, QObject, QObject)
        """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


