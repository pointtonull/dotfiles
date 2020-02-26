# encoding: utf-8
# module PyQt5.QtWidgets
# from /usr/lib/python3/dist-packages/PyQt5/QtWidgets.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui


from .QWidget import QWidget

class QAbstractSpinBox(QWidget):
    """ QAbstractSpinBox(parent: QWidget = None) """
    def alignment(self): # real signature unknown; restored from __doc__
        """ alignment(self) -> Qt.Alignment """
        pass

    def buttonSymbols(self): # real signature unknown; restored from __doc__
        """ buttonSymbols(self) -> QAbstractSpinBox.ButtonSymbols """
        pass

    def changeEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ changeEvent(self, QEvent) """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def closeEvent(self, QCloseEvent): # real signature unknown; restored from __doc__
        """ closeEvent(self, QCloseEvent) """
        pass

    def contextMenuEvent(self, QContextMenuEvent): # real signature unknown; restored from __doc__
        """ contextMenuEvent(self, QContextMenuEvent) """
        pass

    def correctionMode(self): # real signature unknown; restored from __doc__
        """ correctionMode(self) -> QAbstractSpinBox.CorrectionMode """
        pass

    def editingFinished(self): # real signature unknown; restored from __doc__
        """ editingFinished(self) [signal] """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def fixup(self, p_str): # real signature unknown; restored from __doc__
        """ fixup(self, str) -> str """
        return ""

    def focusInEvent(self, QFocusEvent): # real signature unknown; restored from __doc__
        """ focusInEvent(self, QFocusEvent) """
        pass

    def focusOutEvent(self, QFocusEvent): # real signature unknown; restored from __doc__
        """ focusOutEvent(self, QFocusEvent) """
        pass

    def hasAcceptableInput(self): # real signature unknown; restored from __doc__
        """ hasAcceptableInput(self) -> bool """
        return False

    def hasFrame(self): # real signature unknown; restored from __doc__
        """ hasFrame(self) -> bool """
        return False

    def hideEvent(self, QHideEvent): # real signature unknown; restored from __doc__
        """ hideEvent(self, QHideEvent) """
        pass

    def initStyleOption(self, QStyleOptionSpinBox): # real signature unknown; restored from __doc__
        """ initStyleOption(self, QStyleOptionSpinBox) """
        pass

    def inputMethodQuery(self, Qt_InputMethodQuery): # real signature unknown; restored from __doc__
        """ inputMethodQuery(self, Qt.InputMethodQuery) -> Any """
        pass

    def interpretText(self): # real signature unknown; restored from __doc__
        """ interpretText(self) """
        pass

    def isAccelerated(self): # real signature unknown; restored from __doc__
        """ isAccelerated(self) -> bool """
        return False

    def isGroupSeparatorShown(self): # real signature unknown; restored from __doc__
        """ isGroupSeparatorShown(self) -> bool """
        return False

    def isReadOnly(self): # real signature unknown; restored from __doc__
        """ isReadOnly(self) -> bool """
        return False

    def keyboardTracking(self): # real signature unknown; restored from __doc__
        """ keyboardTracking(self) -> bool """
        return False

    def keyPressEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, QKeyEvent) """
        pass

    def keyReleaseEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ keyReleaseEvent(self, QKeyEvent) """
        pass

    def lineEdit(self): # real signature unknown; restored from __doc__
        """ lineEdit(self) -> QLineEdit """
        return QLineEdit

    def minimumSizeHint(self): # real signature unknown; restored from __doc__
        """ minimumSizeHint(self) -> QSize """
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

    def paintEvent(self, QPaintEvent): # real signature unknown; restored from __doc__
        """ paintEvent(self, QPaintEvent) """
        pass

    def resizeEvent(self, QResizeEvent): # real signature unknown; restored from __doc__
        """ resizeEvent(self, QResizeEvent) """
        pass

    def selectAll(self): # real signature unknown; restored from __doc__
        """ selectAll(self) """
        pass

    def setAccelerated(self, bool): # real signature unknown; restored from __doc__
        """ setAccelerated(self, bool) """
        pass

    def setAlignment(self, Union, Qt_Alignment=None, Qt_AlignmentFlag=None): # real signature unknown; restored from __doc__
        """ setAlignment(self, Union[Qt.Alignment, Qt.AlignmentFlag]) """
        pass

    def setButtonSymbols(self, QAbstractSpinBox_ButtonSymbols): # real signature unknown; restored from __doc__
        """ setButtonSymbols(self, QAbstractSpinBox.ButtonSymbols) """
        pass

    def setCorrectionMode(self, QAbstractSpinBox_CorrectionMode): # real signature unknown; restored from __doc__
        """ setCorrectionMode(self, QAbstractSpinBox.CorrectionMode) """
        pass

    def setFrame(self, bool): # real signature unknown; restored from __doc__
        """ setFrame(self, bool) """
        pass

    def setGroupSeparatorShown(self, bool): # real signature unknown; restored from __doc__
        """ setGroupSeparatorShown(self, bool) """
        pass

    def setKeyboardTracking(self, bool): # real signature unknown; restored from __doc__
        """ setKeyboardTracking(self, bool) """
        pass

    def setLineEdit(self, QLineEdit): # real signature unknown; restored from __doc__
        """ setLineEdit(self, QLineEdit) """
        pass

    def setReadOnly(self, bool): # real signature unknown; restored from __doc__
        """ setReadOnly(self, bool) """
        pass

    def setSpecialValueText(self, p_str): # real signature unknown; restored from __doc__
        """ setSpecialValueText(self, str) """
        pass

    def setWrapping(self, bool): # real signature unknown; restored from __doc__
        """ setWrapping(self, bool) """
        pass

    def showEvent(self, QShowEvent): # real signature unknown; restored from __doc__
        """ showEvent(self, QShowEvent) """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> QSize """
        pass

    def specialValueText(self): # real signature unknown; restored from __doc__
        """ specialValueText(self) -> str """
        return ""

    def stepBy(self, p_int): # real signature unknown; restored from __doc__
        """ stepBy(self, int) """
        pass

    def stepDown(self): # real signature unknown; restored from __doc__
        """ stepDown(self) """
        pass

    def stepEnabled(self): # real signature unknown; restored from __doc__
        """ stepEnabled(self) -> QAbstractSpinBox.StepEnabled """
        pass

    def stepUp(self): # real signature unknown; restored from __doc__
        """ stepUp(self) """
        pass

    def text(self): # real signature unknown; restored from __doc__
        """ text(self) -> str """
        return ""

    def timerEvent(self, QTimerEvent): # real signature unknown; restored from __doc__
        """ timerEvent(self, QTimerEvent) """
        pass

    def validate(self, p_str, p_int): # real signature unknown; restored from __doc__
        """ validate(self, str, int) -> Tuple[QValidator.State, str, int] """
        pass

    def wheelEvent(self, QWheelEvent): # real signature unknown; restored from __doc__
        """ wheelEvent(self, QWheelEvent) """
        pass

    def wrapping(self): # real signature unknown; restored from __doc__
        """ wrapping(self) -> bool """
        return False

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass

    CorrectToNearestValue = 1
    CorrectToPreviousValue = 0
    NoButtons = 2
    PlusMinus = 1
    StepDownEnabled = 2
    StepNone = 0
    StepUpEnabled = 1
    UpDownArrows = 0


