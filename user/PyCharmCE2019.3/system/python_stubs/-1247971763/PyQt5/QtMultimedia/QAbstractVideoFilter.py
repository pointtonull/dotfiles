# encoding: utf-8
# module PyQt5.QtMultimedia
# from /usr/lib/python3/dist-packages/PyQt5/QtMultimedia.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore


class QAbstractVideoFilter(__PyQt5_QtCore.QObject):
    """ QAbstractVideoFilter(parent: QObject = None) """
    def activeChanged(self): # real signature unknown; restored from __doc__
        """ activeChanged(self) [signal] """
        pass

    def createFilterRunnable(self): # real signature unknown; restored from __doc__
        """ createFilterRunnable(self) -> QVideoFilterRunnable """
        return QVideoFilterRunnable

    def isActive(self): # real signature unknown; restored from __doc__
        """ isActive(self) -> bool """
        return False

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


