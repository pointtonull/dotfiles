# encoding: utf-8
# module PyQt5.QtGui
# from /usr/lib/python3/dist-packages/PyQt5/QtGui.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore


class QBackingStore(): # skipped bases: <class 'sip.simplewrapper'>
    """ QBackingStore(QWindow) """
    def beginPaint(self, QRegion): # real signature unknown; restored from __doc__
        """ beginPaint(self, QRegion) """
        pass

    def endPaint(self): # real signature unknown; restored from __doc__
        """ endPaint(self) """
        pass

    def flush(self, QRegion, window=None, offset=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ flush(self, QRegion, window: QWindow = None, offset: QPoint = QPoint()) """
        pass

    def hasStaticContents(self): # real signature unknown; restored from __doc__
        """ hasStaticContents(self) -> bool """
        return False

    def paintDevice(self): # real signature unknown; restored from __doc__
        """ paintDevice(self) -> QPaintDevice """
        return QPaintDevice

    def resize(self, QSize): # real signature unknown; restored from __doc__
        """ resize(self, QSize) """
        pass

    def scroll(self, QRegion, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ scroll(self, QRegion, int, int) -> bool """
        return False

    def setStaticContents(self, QRegion): # real signature unknown; restored from __doc__
        """ setStaticContents(self, QRegion) """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> QSize """
        pass

    def staticContents(self): # real signature unknown; restored from __doc__
        """ staticContents(self) -> QRegion """
        return QRegion

    def window(self): # real signature unknown; restored from __doc__
        """ window(self) -> QWindow """
        return QWindow

    def __init__(self, QWindow): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



