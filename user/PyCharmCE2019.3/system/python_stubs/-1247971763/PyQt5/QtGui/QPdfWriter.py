# encoding: utf-8
# module PyQt5.QtGui
# from /usr/lib/python3/dist-packages/PyQt5/QtGui.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore


from .QPagedPaintDevice import QPagedPaintDevice

class QPdfWriter(__PyQt5_QtCore.QObject, QPagedPaintDevice):
    """
    QPdfWriter(str)
    QPdfWriter(QIODevice)
    """
    def creator(self): # real signature unknown; restored from __doc__
        """ creator(self) -> str """
        return ""

    def metric(self, QPaintDevice_PaintDeviceMetric): # real signature unknown; restored from __doc__
        """ metric(self, QPaintDevice.PaintDeviceMetric) -> int """
        return 0

    def newPage(self): # real signature unknown; restored from __doc__
        """ newPage(self) -> bool """
        return False

    def paintEngine(self): # real signature unknown; restored from __doc__
        """ paintEngine(self) -> QPaintEngine """
        return QPaintEngine

    def resolution(self): # real signature unknown; restored from __doc__
        """ resolution(self) -> int """
        return 0

    def setCreator(self, p_str): # real signature unknown; restored from __doc__
        """ setCreator(self, str) """
        pass

    def setMargins(self, QPagedPaintDevice_Margins): # real signature unknown; restored from __doc__
        """ setMargins(self, QPagedPaintDevice.Margins) """
        pass

    def setPageSize(self, QPagedPaintDevice_PageSize): # real signature unknown; restored from __doc__
        """ setPageSize(self, QPagedPaintDevice.PageSize) """
        pass

    def setPageSizeMM(self, QSizeF): # real signature unknown; restored from __doc__
        """ setPageSizeMM(self, QSizeF) """
        pass

    def setResolution(self, p_int): # real signature unknown; restored from __doc__
        """ setResolution(self, int) """
        pass

    def setTitle(self, p_str): # real signature unknown; restored from __doc__
        """ setTitle(self, str) """
        pass

    def title(self): # real signature unknown; restored from __doc__
        """ title(self) -> str """
        return ""

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


