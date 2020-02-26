# encoding: utf-8
# module PyQt5.QtWidgets
# from /usr/lib/python3/dist-packages/PyQt5/QtWidgets.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui


from .QWidget import QWidget

class QMdiSubWindow(QWidget):
    """ QMdiSubWindow(parent: QWidget = None, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags()) """
    def aboutToActivate(self): # real signature unknown; restored from __doc__
        """ aboutToActivate(self) [signal] """
        pass

    def changeEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ changeEvent(self, QEvent) """
        pass

    def childEvent(self, QChildEvent): # real signature unknown; restored from __doc__
        """ childEvent(self, QChildEvent) """
        pass

    def closeEvent(self, QCloseEvent): # real signature unknown; restored from __doc__
        """ closeEvent(self, QCloseEvent) """
        pass

    def contextMenuEvent(self, QContextMenuEvent): # real signature unknown; restored from __doc__
        """ contextMenuEvent(self, QContextMenuEvent) """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def eventFilter(self, QObject, QEvent): # real signature unknown; restored from __doc__
        """ eventFilter(self, QObject, QEvent) -> bool """
        return False

    def focusInEvent(self, QFocusEvent): # real signature unknown; restored from __doc__
        """ focusInEvent(self, QFocusEvent) """
        pass

    def focusOutEvent(self, QFocusEvent): # real signature unknown; restored from __doc__
        """ focusOutEvent(self, QFocusEvent) """
        pass

    def hideEvent(self, QHideEvent): # real signature unknown; restored from __doc__
        """ hideEvent(self, QHideEvent) """
        pass

    def isShaded(self): # real signature unknown; restored from __doc__
        """ isShaded(self) -> bool """
        return False

    def keyboardPageStep(self): # real signature unknown; restored from __doc__
        """ keyboardPageStep(self) -> int """
        return 0

    def keyboardSingleStep(self): # real signature unknown; restored from __doc__
        """ keyboardSingleStep(self) -> int """
        return 0

    def keyPressEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, QKeyEvent) """
        pass

    def leaveEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ leaveEvent(self, QEvent) """
        pass

    def mdiArea(self): # real signature unknown; restored from __doc__
        """ mdiArea(self) -> QMdiArea """
        return QMdiArea

    def minimumSizeHint(self): # real signature unknown; restored from __doc__
        """ minimumSizeHint(self) -> QSize """
        pass

    def mouseDoubleClickEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ mouseDoubleClickEvent(self, QMouseEvent) """
        pass

    def mouseMoveEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ mouseMoveEvent(self, QMouseEvent) """
        pass

    def mousePressEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ mousePressEvent(self, QMouseEvent) """
        pass

    def mouseReleaseEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ mouseReleaseEvent(self, QMouseEvent) """
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

    def setKeyboardPageStep(self, p_int): # real signature unknown; restored from __doc__
        """ setKeyboardPageStep(self, int) """
        pass

    def setKeyboardSingleStep(self, p_int): # real signature unknown; restored from __doc__
        """ setKeyboardSingleStep(self, int) """
        pass

    def setOption(self, QMdiSubWindow_SubWindowOption, on=True): # real signature unknown; restored from __doc__
        """ setOption(self, QMdiSubWindow.SubWindowOption, on: bool = True) """
        pass

    def setSystemMenu(self, QMenu): # real signature unknown; restored from __doc__
        """ setSystemMenu(self, QMenu) """
        pass

    def setWidget(self, QWidget): # real signature unknown; restored from __doc__
        """ setWidget(self, QWidget) """
        pass

    def showEvent(self, QShowEvent): # real signature unknown; restored from __doc__
        """ showEvent(self, QShowEvent) """
        pass

    def showShaded(self): # real signature unknown; restored from __doc__
        """ showShaded(self) """
        pass

    def showSystemMenu(self): # real signature unknown; restored from __doc__
        """ showSystemMenu(self) """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> QSize """
        pass

    def systemMenu(self): # real signature unknown; restored from __doc__
        """ systemMenu(self) -> QMenu """
        return QMenu

    def testOption(self, QMdiSubWindow_SubWindowOption): # real signature unknown; restored from __doc__
        """ testOption(self, QMdiSubWindow.SubWindowOption) -> bool """
        return False

    def timerEvent(self, QTimerEvent): # real signature unknown; restored from __doc__
        """ timerEvent(self, QTimerEvent) """
        pass

    def widget(self): # real signature unknown; restored from __doc__
        """ widget(self) -> QWidget """
        return QWidget

    def __init__(self, parent=None, flags, Qt_WindowFlags=None, Qt_WindowType=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    RubberBandMove = 8
    RubberBandResize = 4


