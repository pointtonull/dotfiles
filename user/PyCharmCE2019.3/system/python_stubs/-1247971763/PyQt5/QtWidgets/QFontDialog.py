# encoding: utf-8
# module PyQt5.QtWidgets
# from /usr/lib/python3/dist-packages/PyQt5/QtWidgets.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui


from .QDialog import QDialog

class QFontDialog(QDialog):
    """
    QFontDialog(parent: QWidget = None)
    QFontDialog(QFont, parent: QWidget = None)
    """
    def changeEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ changeEvent(self, QEvent) """
        pass

    def currentFont(self): # real signature unknown; restored from __doc__
        """ currentFont(self) -> QFont """
        pass

    def currentFontChanged(self, QFont): # real signature unknown; restored from __doc__
        """ currentFontChanged(self, QFont) [signal] """
        pass

    def done(self, p_int): # real signature unknown; restored from __doc__
        """ done(self, int) """
        pass

    def eventFilter(self, QObject, QEvent): # real signature unknown; restored from __doc__
        """ eventFilter(self, QObject, QEvent) -> bool """
        return False

    def fontSelected(self, QFont): # real signature unknown; restored from __doc__
        """ fontSelected(self, QFont) [signal] """
        pass

    def getFont(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        getFont(QFont, parent: QWidget = None, caption: str = '', options: Union[QFontDialog.FontDialogOptions, QFontDialog.FontDialogOption] = QFontDialog.FontDialogOptions()) -> Tuple[QFont, bool]
        getFont(parent: QWidget = None) -> Tuple[QFont, bool]
        """
        pass

    def open(self, PYQT_SLOT=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        open(self)
        open(self, PYQT_SLOT)
        """
        pass

    def options(self): # real signature unknown; restored from __doc__
        """ options(self) -> QFontDialog.FontDialogOptions """
        pass

    def selectedFont(self): # real signature unknown; restored from __doc__
        """ selectedFont(self) -> QFont """
        pass

    def setCurrentFont(self, QFont): # real signature unknown; restored from __doc__
        """ setCurrentFont(self, QFont) """
        pass

    def setOption(self, QFontDialog_FontDialogOption, on=True): # real signature unknown; restored from __doc__
        """ setOption(self, QFontDialog.FontDialogOption, on: bool = True) """
        pass

    def setOptions(self, Union, QFontDialog_FontDialogOptions=None, QFontDialog_FontDialogOption=None): # real signature unknown; restored from __doc__
        """ setOptions(self, Union[QFontDialog.FontDialogOptions, QFontDialog.FontDialogOption]) """
        pass

    def setVisible(self, bool): # real signature unknown; restored from __doc__
        """ setVisible(self, bool) """
        pass

    def testOption(self, QFontDialog_FontDialogOption): # real signature unknown; restored from __doc__
        """ testOption(self, QFontDialog.FontDialogOption) -> bool """
        return False

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    DontUseNativeDialog = 2
    MonospacedFonts = 16
    NoButtons = 1
    NonScalableFonts = 8
    ProportionalFonts = 32
    ScalableFonts = 4


