# encoding: utf-8
# module PyQt5.QtGui
# from /usr/lib/python3/dist-packages/PyQt5/QtGui.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore


from .QPaintDeviceWindow import QPaintDeviceWindow

class QOpenGLWindow(QPaintDeviceWindow):
    """
    QOpenGLWindow(updateBehavior: QOpenGLWindow.UpdateBehavior = QOpenGLWindow.NoPartialUpdate, parent: QWindow = None)
    QOpenGLWindow(QOpenGLContext, updateBehavior: QOpenGLWindow.UpdateBehavior = QOpenGLWindow.NoPartialUpdate, parent: QWindow = None)
    """
    def context(self): # real signature unknown; restored from __doc__
        """ context(self) -> QOpenGLContext """
        return QOpenGLContext

    def defaultFramebufferObject(self): # real signature unknown; restored from __doc__
        """ defaultFramebufferObject(self) -> int """
        return 0

    def doneCurrent(self): # real signature unknown; restored from __doc__
        """ doneCurrent(self) """
        pass

    def frameSwapped(self): # real signature unknown; restored from __doc__
        """ frameSwapped(self) [signal] """
        pass

    def grabFramebuffer(self): # real signature unknown; restored from __doc__
        """ grabFramebuffer(self) -> QImage """
        return QImage

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

    def paintEvent(self, QPaintEvent): # real signature unknown; restored from __doc__
        """ paintEvent(self, QPaintEvent) """
        pass

    def paintGL(self): # real signature unknown; restored from __doc__
        """ paintGL(self) """
        pass

    def paintOverGL(self): # real signature unknown; restored from __doc__
        """ paintOverGL(self) """
        pass

    def paintUnderGL(self): # real signature unknown; restored from __doc__
        """ paintUnderGL(self) """
        pass

    def resizeEvent(self, QResizeEvent): # real signature unknown; restored from __doc__
        """ resizeEvent(self, QResizeEvent) """
        pass

    def resizeGL(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ resizeGL(self, int, int) """
        pass

    def shareContext(self): # real signature unknown; restored from __doc__
        """ shareContext(self) -> QOpenGLContext """
        return QOpenGLContext

    def updateBehavior(self): # real signature unknown; restored from __doc__
        """ updateBehavior(self) -> QOpenGLWindow.UpdateBehavior """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    NoPartialUpdate = 0
    PartialUpdateBlend = 2
    PartialUpdateBlit = 1


