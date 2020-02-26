# encoding: utf-8
# module PyQt5.QtWidgets
# from /usr/lib/python3/dist-packages/PyQt5/QtWidgets.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui


class QGraphicsEffect(__PyQt5_QtCore.QObject):
    """ QGraphicsEffect(parent: QObject = None) """
    def boundingRect(self): # real signature unknown; restored from __doc__
        """ boundingRect(self) -> QRectF """
        pass

    def boundingRectFor(self, QRectF): # real signature unknown; restored from __doc__
        """ boundingRectFor(self, QRectF) -> QRectF """
        pass

    def draw(self, QPainter): # real signature unknown; restored from __doc__
        """ draw(self, QPainter) """
        pass

    def drawSource(self, QPainter): # real signature unknown; restored from __doc__
        """ drawSource(self, QPainter) """
        pass

    def enabledChanged(self, bool): # real signature unknown; restored from __doc__
        """ enabledChanged(self, bool) [signal] """
        pass

    def isEnabled(self): # real signature unknown; restored from __doc__
        """ isEnabled(self) -> bool """
        return False

    def setEnabled(self, bool): # real signature unknown; restored from __doc__
        """ setEnabled(self, bool) """
        pass

    def sourceBoundingRect(self, system=None): # real signature unknown; restored from __doc__
        """ sourceBoundingRect(self, system: Qt.CoordinateSystem = Qt.LogicalCoordinates) -> QRectF """
        pass

    def sourceChanged(self, Union, QGraphicsEffect_ChangeFlags=None, QGraphicsEffect_ChangeFlag=None): # real signature unknown; restored from __doc__
        """ sourceChanged(self, Union[QGraphicsEffect.ChangeFlags, QGraphicsEffect.ChangeFlag]) """
        pass

    def sourceIsPixmap(self): # real signature unknown; restored from __doc__
        """ sourceIsPixmap(self) -> bool """
        return False

    def sourcePixmap(self, system=None, mode=None): # real signature unknown; restored from __doc__
        """ sourcePixmap(self, system: Qt.CoordinateSystem = Qt.LogicalCoordinates, mode: QGraphicsEffect.PixmapPadMode = QGraphicsEffect.PadToEffectiveBoundingRect) -> Tuple[QPixmap, QPoint] """
        pass

    def update(self): # real signature unknown; restored from __doc__
        """ update(self) """
        pass

    def updateBoundingRect(self): # real signature unknown; restored from __doc__
        """ updateBoundingRect(self) """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass

    NoPad = 0
    PadToEffectiveBoundingRect = 2
    PadToTransparentBorder = 1
    SourceAttached = 1
    SourceBoundingRectChanged = 4
    SourceDetached = 2
    SourceInvalidated = 8


