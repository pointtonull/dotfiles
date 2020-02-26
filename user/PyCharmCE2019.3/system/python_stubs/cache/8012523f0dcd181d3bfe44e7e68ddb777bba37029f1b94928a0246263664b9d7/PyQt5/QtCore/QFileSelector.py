# encoding: utf-8
# module PyQt5.QtCore
# from /usr/lib/python3/dist-packages/PyQt5/QtCore.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc
# no imports

from .QObject import QObject

class QFileSelector(QObject):
    """ QFileSelector(parent: QObject = None) """
    def allSelectors(self): # real signature unknown; restored from __doc__
        """ allSelectors(self) -> List[str] """
        return []

    def extraSelectors(self): # real signature unknown; restored from __doc__
        """ extraSelectors(self) -> List[str] """
        return []

    def select(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        select(self, str) -> str
        select(self, QUrl) -> QUrl
        """
        return "" or QUrl

    def setExtraSelectors(self, Iterable, p_str=None): # real signature unknown; restored from __doc__
        """ setExtraSelectors(self, Iterable[str]) """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


