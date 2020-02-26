# encoding: utf-8
# module PyQt5.QtWidgets
# from /usr/lib/python3/dist-packages/PyQt5/QtWidgets.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui


from .QWidget import QWidget

class QSplashScreen(QWidget):
    """
    QSplashScreen(pixmap: QPixmap = QPixmap(), flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags())
    QSplashScreen(QWidget, pixmap: QPixmap = QPixmap(), flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags())
    """
    def clearMessage(self): # real signature unknown; restored from __doc__
        """ clearMessage(self) """
        pass

    def drawContents(self, QPainter): # real signature unknown; restored from __doc__
        """ drawContents(self, QPainter) """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def finish(self, QWidget): # real signature unknown; restored from __doc__
        """ finish(self, QWidget) """
        pass

    def message(self): # real signature unknown; restored from __doc__
        """ message(self) -> str """
        return ""

    def messageChanged(self, p_str): # real signature unknown; restored from __doc__
        """ messageChanged(self, str) [signal] """
        pass

    def mousePressEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ mousePressEvent(self, QMouseEvent) """
        pass

    def pixmap(self): # real signature unknown; restored from __doc__
        """ pixmap(self) -> QPixmap """
        pass

    def repaint(self): # real signature unknown; restored from __doc__
        """ repaint(self) """
        pass

    def setPixmap(self, QPixmap): # real signature unknown; restored from __doc__
        """ setPixmap(self, QPixmap) """
        pass

    def showMessage(self, p_str, alignment=None, color, QColor=None, Qt_GlobalColor=None, QGradient=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ showMessage(self, str, alignment: int = Qt.AlignLeft, color: Union[QColor, Qt.GlobalColor, QGradient] = Qt.black) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


