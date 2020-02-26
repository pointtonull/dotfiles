# encoding: utf-8
# module PyQt5.QtSvg
# from /usr/lib/python3/dist-packages/PyQt5/QtSvg.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import PyQt5.QtWidgets as __PyQt5_QtWidgets


# no functions
# classes

class QGraphicsSvgItem(__PyQt5_QtWidgets.QGraphicsObject):
    """
    QGraphicsSvgItem(parent: QGraphicsItem = None)
    QGraphicsSvgItem(str, parent: QGraphicsItem = None)
    """
    def boundingRect(self): # real signature unknown; restored from __doc__
        """ boundingRect(self) -> QRectF """
        pass

    def elementId(self): # real signature unknown; restored from __doc__
        """ elementId(self) -> str """
        return ""

    def maximumCacheSize(self): # real signature unknown; restored from __doc__
        """ maximumCacheSize(self) -> QSize """
        pass

    def paint(self, QPainter, QStyleOptionGraphicsItem, widget=None): # real signature unknown; restored from __doc__
        """ paint(self, QPainter, QStyleOptionGraphicsItem, widget: QWidget = None) """
        pass

    def renderer(self): # real signature unknown; restored from __doc__
        """ renderer(self) -> QSvgRenderer """
        return QSvgRenderer

    def setElementId(self, p_str): # real signature unknown; restored from __doc__
        """ setElementId(self, str) """
        pass

    def setMaximumCacheSize(self, QSize): # real signature unknown; restored from __doc__
        """ setMaximumCacheSize(self, QSize) """
        pass

    def setSharedRenderer(self, QSvgRenderer): # real signature unknown; restored from __doc__
        """ setSharedRenderer(self, QSvgRenderer) """
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> int """
        return 0

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


class QSvgGenerator(__PyQt5_QtGui.QPaintDevice):
    """ QSvgGenerator() """
    def description(self): # real signature unknown; restored from __doc__
        """ description(self) -> str """
        return ""

    def fileName(self): # real signature unknown; restored from __doc__
        """ fileName(self) -> str """
        return ""

    def metric(self, QPaintDevice_PaintDeviceMetric): # real signature unknown; restored from __doc__
        """ metric(self, QPaintDevice.PaintDeviceMetric) -> int """
        return 0

    def outputDevice(self): # real signature unknown; restored from __doc__
        """ outputDevice(self) -> QIODevice """
        pass

    def paintEngine(self): # real signature unknown; restored from __doc__
        """ paintEngine(self) -> QPaintEngine """
        pass

    def resolution(self): # real signature unknown; restored from __doc__
        """ resolution(self) -> int """
        return 0

    def setDescription(self, p_str): # real signature unknown; restored from __doc__
        """ setDescription(self, str) """
        pass

    def setFileName(self, p_str): # real signature unknown; restored from __doc__
        """ setFileName(self, str) """
        pass

    def setOutputDevice(self, QIODevice): # real signature unknown; restored from __doc__
        """ setOutputDevice(self, QIODevice) """
        pass

    def setResolution(self, p_int): # real signature unknown; restored from __doc__
        """ setResolution(self, int) """
        pass

    def setSize(self, QSize): # real signature unknown; restored from __doc__
        """ setSize(self, QSize) """
        pass

    def setTitle(self, p_str): # real signature unknown; restored from __doc__
        """ setTitle(self, str) """
        pass

    def setViewBox(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setViewBox(self, QRect)
        setViewBox(self, QRectF)
        """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> QSize """
        pass

    def title(self): # real signature unknown; restored from __doc__
        """ title(self) -> str """
        return ""

    def viewBox(self): # real signature unknown; restored from __doc__
        """ viewBox(self) -> QRect """
        pass

    def viewBoxF(self): # real signature unknown; restored from __doc__
        """ viewBoxF(self) -> QRectF """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass


class QSvgRenderer(__PyQt5_QtCore.QObject):
    """
    QSvgRenderer(parent: QObject = None)
    QSvgRenderer(str, parent: QObject = None)
    QSvgRenderer(Union[QByteArray, bytes, bytearray], parent: QObject = None)
    QSvgRenderer(QXmlStreamReader, parent: QObject = None)
    """
    def animated(self): # real signature unknown; restored from __doc__
        """ animated(self) -> bool """
        return False

    def animationDuration(self): # real signature unknown; restored from __doc__
        """ animationDuration(self) -> int """
        return 0

    def boundsOnElement(self, p_str): # real signature unknown; restored from __doc__
        """ boundsOnElement(self, str) -> QRectF """
        pass

    def currentFrame(self): # real signature unknown; restored from __doc__
        """ currentFrame(self) -> int """
        return 0

    def defaultSize(self): # real signature unknown; restored from __doc__
        """ defaultSize(self) -> QSize """
        pass

    def elementExists(self, p_str): # real signature unknown; restored from __doc__
        """ elementExists(self, str) -> bool """
        return False

    def framesPerSecond(self): # real signature unknown; restored from __doc__
        """ framesPerSecond(self) -> int """
        return 0

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def load(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        load(self, str) -> bool
        load(self, Union[QByteArray, bytes, bytearray]) -> bool
        load(self, QXmlStreamReader) -> bool
        """
        return False

    def render(self, QPainter, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        render(self, QPainter)
        render(self, QPainter, QRectF)
        render(self, QPainter, str, bounds: QRectF = QRectF())
        """
        pass

    def repaintNeeded(self): # real signature unknown; restored from __doc__
        """ repaintNeeded(self) [signal] """
        pass

    def setCurrentFrame(self, p_int): # real signature unknown; restored from __doc__
        """ setCurrentFrame(self, int) """
        pass

    def setFramesPerSecond(self, p_int): # real signature unknown; restored from __doc__
        """ setFramesPerSecond(self, int) """
        pass

    def setViewBox(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setViewBox(self, QRect)
        setViewBox(self, QRectF)
        """
        pass

    def viewBox(self): # real signature unknown; restored from __doc__
        """ viewBox(self) -> QRect """
        pass

    def viewBoxF(self): # real signature unknown; restored from __doc__
        """ viewBoxF(self) -> QRectF """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


class QSvgWidget(__PyQt5_QtWidgets.QWidget):
    """
    QSvgWidget(parent: QWidget = None)
    QSvgWidget(str, parent: QWidget = None)
    """
    def load(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        load(self, str)
        load(self, Union[QByteArray, bytes, bytearray])
        """
        pass

    def paintEvent(self, QPaintEvent): # real signature unknown; restored from __doc__
        """ paintEvent(self, QPaintEvent) """
        pass

    def renderer(self): # real signature unknown; restored from __doc__
        """ renderer(self) -> QSvgRenderer """
        return QSvgRenderer

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> QSize """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


# variables with complex values



