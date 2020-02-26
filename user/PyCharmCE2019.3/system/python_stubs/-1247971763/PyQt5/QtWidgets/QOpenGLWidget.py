# encoding: utf-8
# module PyQt5.QtWidgets
# from /usr/lib/python3/dist-packages/PyQt5/QtWidgets.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui


from .QWidget import QWidget

class QOpenGLWidget(QWidget):
    """ QOpenGLWidget(parent: QWidget = None, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags()) """
    def aboutToCompose(self): # real signature unknown; restored from __doc__
        """ aboutToCompose(self) [signal] """
        pass

    def aboutToResize(self): # real signature unknown; restored from __doc__
        """ aboutToResize(self) [signal] """
        pass

    def context(self): # real signature unknown; restored from __doc__
        """ context(self) -> QOpenGLContext """
        pass

    def defaultFramebufferObject(self): # real signature unknown; restored from __doc__
        """ defaultFramebufferObject(self) -> int """
        return 0

    def doneCurrent(self): # real signature unknown; restored from __doc__
        """ doneCurrent(self) """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def format(self): # real signature unknown; restored from __doc__
        """ format(self) -> QSurfaceFormat """
        pass

    def frameSwapped(self): # real signature unknown; restored from __doc__
        """ frameSwapped(self) [signal] """
        pass

    def grabFramebuffer(self): # real signature unknown; restored from __doc__
        """ grabFramebuffer(self) -> QImage """
        pass

    def initializeGL(self): # real signature unknown; restored from __doc__
        """ initializeGL(self) """
        pass

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def makeCurrent(self): # real signature unknown; restored from __doc__
        """ makeCurrent(self) """
        pass

    def metric(self, QPaintDevice_PaintDeviceMetric): # real signature unknown; restored from __doc__
        """ metric(self, QPaintDevice.PaintDeviceMetric) -> int """
        return 0

    def paintEngine(self): # real signature unknown; restored from __doc__
        """ paintEngine(self) -> QPaintEngine """
        pass

    def paintEvent(self, QPaintEvent): # real signature unknown; restored from __doc__
        """ paintEvent(self, QPaintEvent) """
        pass

    def paintGL(self): # real signature unknown; restored from __doc__
        """ paintGL(self) """
        pass

    def resized(self): # real signature unknown; restored from __doc__
        """ resized(self) [signal] """
        pass

    def resizeEvent(self, QResizeEvent): # real signature unknown; restored from __doc__
        """ resizeEvent(self, QResizeEvent) """
        pass

    def resizeGL(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ resizeGL(self, int, int) """
        pass

    def setFormat(self, QSurfaceFormat): # real signature unknown; restored from __doc__
        """ setFormat(self, QSurfaceFormat) """
        pass

    def setUpdateBehavior(self, QOpenGLWidget_UpdateBehavior): # real signature unknown; restored from __doc__
        """ setUpdateBehavior(self, QOpenGLWidget.UpdateBehavior) """
        pass

    def updateBehavior(self): # real signature unknown; restored from __doc__
        """ updateBehavior(self) -> QOpenGLWidget.UpdateBehavior """
        pass

    def __init__(self, parent=None, flags, Qt_WindowFlags=None, Qt_WindowType=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    NoPartialUpdate = 0
    PartialUpdate = 1


