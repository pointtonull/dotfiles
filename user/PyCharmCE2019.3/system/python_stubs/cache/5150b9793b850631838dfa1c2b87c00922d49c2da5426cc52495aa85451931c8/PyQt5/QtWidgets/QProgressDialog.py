# encoding: utf-8
# module PyQt5.QtWidgets
# from /usr/lib/python3/dist-packages/PyQt5/QtWidgets.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui


from .QDialog import QDialog

class QProgressDialog(QDialog):
    """
    QProgressDialog(parent: QWidget = None, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags())
    QProgressDialog(str, str, int, int, parent: QWidget = None, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags())
    """
    def autoClose(self): # real signature unknown; restored from __doc__
        """ autoClose(self) -> bool """
        return False

    def autoReset(self): # real signature unknown; restored from __doc__
        """ autoReset(self) -> bool """
        return False

    def cancel(self): # real signature unknown; restored from __doc__
        """ cancel(self) """
        pass

    def canceled(self): # real signature unknown; restored from __doc__
        """ canceled(self) [signal] """
        pass

    def changeEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ changeEvent(self, QEvent) """
        pass

    def closeEvent(self, QCloseEvent): # real signature unknown; restored from __doc__
        """ closeEvent(self, QCloseEvent) """
        pass

    def forceShow(self): # real signature unknown; restored from __doc__
        """ forceShow(self) """
        pass

    def labelText(self): # real signature unknown; restored from __doc__
        """ labelText(self) -> str """
        return ""

    def maximum(self): # real signature unknown; restored from __doc__
        """ maximum(self) -> int """
        return 0

    def minimum(self): # real signature unknown; restored from __doc__
        """ minimum(self) -> int """
        return 0

    def minimumDuration(self): # real signature unknown; restored from __doc__
        """ minimumDuration(self) -> int """
        return 0

    def open(self, PYQT_SLOT=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        open(self)
        open(self, PYQT_SLOT)
        """
        pass

    def reset(self): # real signature unknown; restored from __doc__
        """ reset(self) """
        pass

    def resizeEvent(self, QResizeEvent): # real signature unknown; restored from __doc__
        """ resizeEvent(self, QResizeEvent) """
        pass

    def setAutoClose(self, bool): # real signature unknown; restored from __doc__
        """ setAutoClose(self, bool) """
        pass

    def setAutoReset(self, bool): # real signature unknown; restored from __doc__
        """ setAutoReset(self, bool) """
        pass

    def setBar(self, QProgressBar): # real signature unknown; restored from __doc__
        """ setBar(self, QProgressBar) """
        pass

    def setCancelButton(self, QPushButton): # real signature unknown; restored from __doc__
        """ setCancelButton(self, QPushButton) """
        pass

    def setCancelButtonText(self, p_str): # real signature unknown; restored from __doc__
        """ setCancelButtonText(self, str) """
        pass

    def setLabel(self, QLabel): # real signature unknown; restored from __doc__
        """ setLabel(self, QLabel) """
        pass

    def setLabelText(self, p_str): # real signature unknown; restored from __doc__
        """ setLabelText(self, str) """
        pass

    def setMaximum(self, p_int): # real signature unknown; restored from __doc__
        """ setMaximum(self, int) """
        pass

    def setMinimum(self, p_int): # real signature unknown; restored from __doc__
        """ setMinimum(self, int) """
        pass

    def setMinimumDuration(self, p_int): # real signature unknown; restored from __doc__
        """ setMinimumDuration(self, int) """
        pass

    def setRange(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ setRange(self, int, int) """
        pass

    def setValue(self, p_int): # real signature unknown; restored from __doc__
        """ setValue(self, int) """
        pass

    def showEvent(self, QShowEvent): # real signature unknown; restored from __doc__
        """ showEvent(self, QShowEvent) """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> QSize """
        pass

    def value(self): # real signature unknown; restored from __doc__
        """ value(self) -> int """
        return 0

    def wasCanceled(self): # real signature unknown; restored from __doc__
        """ wasCanceled(self) -> bool """
        return False

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


