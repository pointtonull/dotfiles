# encoding: utf-8
# module PyQt5.QtMultimediaWidgets
# from /usr/lib/python3/dist-packages/PyQt5/QtMultimediaWidgets.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtMultimedia as __PyQt5_QtMultimedia
import PyQt5.QtWidgets as __PyQt5_QtWidgets


# no functions
# classes

class QVideoWidget(__PyQt5_QtWidgets.QWidget, __PyQt5_QtMultimedia.QMediaBindableInterface):
    """ QVideoWidget(parent: QWidget = None) """
    def aspectRatioMode(self): # real signature unknown; restored from __doc__
        """ aspectRatioMode(self) -> Qt.AspectRatioMode """
        pass

    def brightness(self): # real signature unknown; restored from __doc__
        """ brightness(self) -> int """
        return 0

    def brightnessChanged(self, p_int): # real signature unknown; restored from __doc__
        """ brightnessChanged(self, int) [signal] """
        pass

    def contrast(self): # real signature unknown; restored from __doc__
        """ contrast(self) -> int """
        return 0

    def contrastChanged(self, p_int): # real signature unknown; restored from __doc__
        """ contrastChanged(self, int) [signal] """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def fullScreenChanged(self, bool): # real signature unknown; restored from __doc__
        """ fullScreenChanged(self, bool) [signal] """
        pass

    def hideEvent(self, QHideEvent): # real signature unknown; restored from __doc__
        """ hideEvent(self, QHideEvent) """
        pass

    def hue(self): # real signature unknown; restored from __doc__
        """ hue(self) -> int """
        return 0

    def hueChanged(self, p_int): # real signature unknown; restored from __doc__
        """ hueChanged(self, int) [signal] """
        pass

    def mediaObject(self): # real signature unknown; restored from __doc__
        """ mediaObject(self) -> QMediaObject """
        pass

    def moveEvent(self, QMoveEvent): # real signature unknown; restored from __doc__
        """ moveEvent(self, QMoveEvent) """
        pass

    def paintEvent(self, QPaintEvent): # real signature unknown; restored from __doc__
        """ paintEvent(self, QPaintEvent) """
        pass

    def resizeEvent(self, QResizeEvent): # real signature unknown; restored from __doc__
        """ resizeEvent(self, QResizeEvent) """
        pass

    def saturation(self): # real signature unknown; restored from __doc__
        """ saturation(self) -> int """
        return 0

    def saturationChanged(self, p_int): # real signature unknown; restored from __doc__
        """ saturationChanged(self, int) [signal] """
        pass

    def setAspectRatioMode(self, Qt_AspectRatioMode): # real signature unknown; restored from __doc__
        """ setAspectRatioMode(self, Qt.AspectRatioMode) """
        pass

    def setBrightness(self, p_int): # real signature unknown; restored from __doc__
        """ setBrightness(self, int) """
        pass

    def setContrast(self, p_int): # real signature unknown; restored from __doc__
        """ setContrast(self, int) """
        pass

    def setFullScreen(self, bool): # real signature unknown; restored from __doc__
        """ setFullScreen(self, bool) """
        pass

    def setHue(self, p_int): # real signature unknown; restored from __doc__
        """ setHue(self, int) """
        pass

    def setMediaObject(self, QMediaObject): # real signature unknown; restored from __doc__
        """ setMediaObject(self, QMediaObject) -> bool """
        return False

    def setSaturation(self, p_int): # real signature unknown; restored from __doc__
        """ setSaturation(self, int) """
        pass

    def showEvent(self, QShowEvent): # real signature unknown; restored from __doc__
        """ showEvent(self, QShowEvent) """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> QSize """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


class QCameraViewfinder(QVideoWidget):
    """ QCameraViewfinder(parent: QWidget = None) """
    def mediaObject(self): # real signature unknown; restored from __doc__
        """ mediaObject(self) -> QMediaObject """
        pass

    def setMediaObject(self, QMediaObject): # real signature unknown; restored from __doc__
        """ setMediaObject(self, QMediaObject) -> bool """
        return False

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


class QGraphicsVideoItem(__PyQt5_QtWidgets.QGraphicsObject, __PyQt5_QtMultimedia.QMediaBindableInterface):
    """ QGraphicsVideoItem(parent: QGraphicsItem = None) """
    def aspectRatioMode(self): # real signature unknown; restored from __doc__
        """ aspectRatioMode(self) -> Qt.AspectRatioMode """
        pass

    def boundingRect(self): # real signature unknown; restored from __doc__
        """ boundingRect(self) -> QRectF """
        pass

    def itemChange(self, QGraphicsItem_GraphicsItemChange, Any): # real signature unknown; restored from __doc__
        """ itemChange(self, QGraphicsItem.GraphicsItemChange, Any) -> Any """
        pass

    def mediaObject(self): # real signature unknown; restored from __doc__
        """ mediaObject(self) -> QMediaObject """
        pass

    def nativeSize(self): # real signature unknown; restored from __doc__
        """ nativeSize(self) -> QSizeF """
        pass

    def nativeSizeChanged(self, QSizeF): # real signature unknown; restored from __doc__
        """ nativeSizeChanged(self, QSizeF) [signal] """
        pass

    def offset(self): # real signature unknown; restored from __doc__
        """ offset(self) -> QPointF """
        pass

    def paint(self, QPainter, QStyleOptionGraphicsItem, widget=None): # real signature unknown; restored from __doc__
        """ paint(self, QPainter, QStyleOptionGraphicsItem, widget: QWidget = None) """
        pass

    def setAspectRatioMode(self, Qt_AspectRatioMode): # real signature unknown; restored from __doc__
        """ setAspectRatioMode(self, Qt.AspectRatioMode) """
        pass

    def setMediaObject(self, QMediaObject): # real signature unknown; restored from __doc__
        """ setMediaObject(self, QMediaObject) -> bool """
        return False

    def setOffset(self, Union, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ setOffset(self, Union[QPointF, QPoint]) """
        pass

    def setSize(self, QSizeF): # real signature unknown; restored from __doc__
        """ setSize(self, QSizeF) """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> QSizeF """
        pass

    def timerEvent(self, QTimerEvent): # real signature unknown; restored from __doc__
        """ timerEvent(self, QTimerEvent) """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


# variables with complex values



