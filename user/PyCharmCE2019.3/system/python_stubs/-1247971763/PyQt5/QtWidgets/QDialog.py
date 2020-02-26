# encoding: utf-8
# module PyQt5.QtWidgets
# from /usr/lib/python3/dist-packages/PyQt5/QtWidgets.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui


from .QWidget import QWidget

class QDialog(QWidget):
    """ QDialog(parent: QWidget = None, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags()) """
    def accept(self): # real signature unknown; restored from __doc__
        """ accept(self) """
        pass

    def accepted(self): # real signature unknown; restored from __doc__
        """ accepted(self) [signal] """
        pass

    def closeEvent(self, QCloseEvent): # real signature unknown; restored from __doc__
        """ closeEvent(self, QCloseEvent) """
        pass

    def contextMenuEvent(self, QContextMenuEvent): # real signature unknown; restored from __doc__
        """ contextMenuEvent(self, QContextMenuEvent) """
        pass

    def done(self, p_int): # real signature unknown; restored from __doc__
        """ done(self, int) """
        pass

    def eventFilter(self, QObject, QEvent): # real signature unknown; restored from __doc__
        """ eventFilter(self, QObject, QEvent) -> bool """
        return False

    def exec(self): # real signature unknown; restored from __doc__
        """ exec(self) -> int """
        return 0

    def exec_(self): # real signature unknown; restored from __doc__
        """ exec_(self) -> int """
        return 0

    def finished(self, p_int): # real signature unknown; restored from __doc__
        """ finished(self, int) [signal] """
        pass

    def isSizeGripEnabled(self): # real signature unknown; restored from __doc__
        """ isSizeGripEnabled(self) -> bool """
        return False

    def keyPressEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, QKeyEvent) """
        pass

    def minimumSizeHint(self): # real signature unknown; restored from __doc__
        """ minimumSizeHint(self) -> QSize """
        pass

    def open(self): # real signature unknown; restored from __doc__
        """ open(self) """
        pass

    def reject(self): # real signature unknown; restored from __doc__
        """ reject(self) """
        pass

    def rejected(self): # real signature unknown; restored from __doc__
        """ rejected(self) [signal] """
        pass

    def resizeEvent(self, QResizeEvent): # real signature unknown; restored from __doc__
        """ resizeEvent(self, QResizeEvent) """
        pass

    def result(self): # real signature unknown; restored from __doc__
        """ result(self) -> int """
        return 0

    def setModal(self, bool): # real signature unknown; restored from __doc__
        """ setModal(self, bool) """
        pass

    def setResult(self, p_int): # real signature unknown; restored from __doc__
        """ setResult(self, int) """
        pass

    def setSizeGripEnabled(self, bool): # real signature unknown; restored from __doc__
        """ setSizeGripEnabled(self, bool) """
        pass

    def setVisible(self, bool): # real signature unknown; restored from __doc__
        """ setVisible(self, bool) """
        pass

    def showEvent(self, QShowEvent): # real signature unknown; restored from __doc__
        """ showEvent(self, QShowEvent) """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> QSize """
        pass

    def __init__(self, parent=None, flags, Qt_WindowFlags=None, Qt_WindowType=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    Accepted = 1
    Rejected = 0


