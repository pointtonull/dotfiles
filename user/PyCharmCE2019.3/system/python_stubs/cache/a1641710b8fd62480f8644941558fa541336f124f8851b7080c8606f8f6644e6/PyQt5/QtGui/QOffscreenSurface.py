# encoding: utf-8
# module PyQt5.QtGui
# from /usr/lib/python3/dist-packages/PyQt5/QtGui.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore


from .QSurface import QSurface

class QOffscreenSurface(__PyQt5_QtCore.QObject, QSurface):
    """ QOffscreenSurface(screen: QScreen = None) """
    def create(self): # real signature unknown; restored from __doc__
        """ create(self) """
        pass

    def destroy(self): # real signature unknown; restored from __doc__
        """ destroy(self) """
        pass

    def format(self): # real signature unknown; restored from __doc__
        """ format(self) -> QSurfaceFormat """
        return QSurfaceFormat

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def nativeHandle(self): # real signature unknown; restored from __doc__
        """ nativeHandle(self) -> sip.voidptr """
        pass

    def requestedFormat(self): # real signature unknown; restored from __doc__
        """ requestedFormat(self) -> QSurfaceFormat """
        return QSurfaceFormat

    def screen(self): # real signature unknown; restored from __doc__
        """ screen(self) -> QScreen """
        return QScreen

    def screenChanged(self, QScreen): # real signature unknown; restored from __doc__
        """ screenChanged(self, QScreen) [signal] """
        pass

    def setFormat(self, QSurfaceFormat): # real signature unknown; restored from __doc__
        """ setFormat(self, QSurfaceFormat) """
        pass

    def setNativeHandle(self, sip_voidptr): # real signature unknown; restored from __doc__
        """ setNativeHandle(self, sip.voidptr) """
        pass

    def setScreen(self, QScreen): # real signature unknown; restored from __doc__
        """ setScreen(self, QScreen) """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> QSize """
        pass

    def surfaceType(self): # real signature unknown; restored from __doc__
        """ surfaceType(self) -> QSurface.SurfaceType """
        pass

    def __init__(self, screen=None): # real signature unknown; restored from __doc__
        pass


