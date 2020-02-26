# encoding: utf-8
# module PyQt5.QtWidgets
# from /usr/lib/python3/dist-packages/PyQt5/QtWidgets.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui


from .QDialog import QDialog

class QColorDialog(QDialog):
    """
    QColorDialog(parent: QWidget = None)
    QColorDialog(Union[QColor, Qt.GlobalColor, QGradient], parent: QWidget = None)
    """
    def changeEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ changeEvent(self, QEvent) """
        pass

    def colorSelected(self, Union, QColor=None, Qt_GlobalColor=None, QGradient=None): # real signature unknown; restored from __doc__
        """ colorSelected(self, Union[QColor, Qt.GlobalColor, QGradient]) [signal] """
        pass

    def currentColor(self): # real signature unknown; restored from __doc__
        """ currentColor(self) -> QColor """
        pass

    def currentColorChanged(self, Union, QColor=None, Qt_GlobalColor=None, QGradient=None): # real signature unknown; restored from __doc__
        """ currentColorChanged(self, Union[QColor, Qt.GlobalColor, QGradient]) [signal] """
        pass

    def customColor(self, p_int): # real signature unknown; restored from __doc__
        """ customColor(int) -> QColor """
        pass

    def customCount(self): # real signature unknown; restored from __doc__
        """ customCount() -> int """
        return 0

    def done(self, p_int): # real signature unknown; restored from __doc__
        """ done(self, int) """
        pass

    def getColor(self, initial, QColor=None, Qt_GlobalColor=None, QGradient=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ getColor(initial: Union[QColor, Qt.GlobalColor, QGradient] = Qt.white, parent: QWidget = None, title: str = '', options: Union[QColorDialog.ColorDialogOptions, QColorDialog.ColorDialogOption] = QColorDialog.ColorDialogOptions()) -> QColor """
        pass

    def open(self, PYQT_SLOT=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        open(self)
        open(self, PYQT_SLOT)
        """
        pass

    def options(self): # real signature unknown; restored from __doc__
        """ options(self) -> QColorDialog.ColorDialogOptions """
        pass

    def selectedColor(self): # real signature unknown; restored from __doc__
        """ selectedColor(self) -> QColor """
        pass

    def setCurrentColor(self, Union, QColor=None, Qt_GlobalColor=None, QGradient=None): # real signature unknown; restored from __doc__
        """ setCurrentColor(self, Union[QColor, Qt.GlobalColor, QGradient]) """
        pass

    def setCustomColor(self, p_int, Union, QColor=None, Qt_GlobalColor=None, QGradient=None): # real signature unknown; restored from __doc__
        """ setCustomColor(int, Union[QColor, Qt.GlobalColor, QGradient]) """
        pass

    def setOption(self, QColorDialog_ColorDialogOption, on=True): # real signature unknown; restored from __doc__
        """ setOption(self, QColorDialog.ColorDialogOption, on: bool = True) """
        pass

    def setOptions(self, Union, QColorDialog_ColorDialogOptions=None, QColorDialog_ColorDialogOption=None): # real signature unknown; restored from __doc__
        """ setOptions(self, Union[QColorDialog.ColorDialogOptions, QColorDialog.ColorDialogOption]) """
        pass

    def setStandardColor(self, p_int, Union, QColor=None, Qt_GlobalColor=None, QGradient=None): # real signature unknown; restored from __doc__
        """ setStandardColor(int, Union[QColor, Qt.GlobalColor, QGradient]) """
        pass

    def setVisible(self, bool): # real signature unknown; restored from __doc__
        """ setVisible(self, bool) """
        pass

    def standardColor(self, p_int): # real signature unknown; restored from __doc__
        """ standardColor(int) -> QColor """
        pass

    def testOption(self, QColorDialog_ColorDialogOption): # real signature unknown; restored from __doc__
        """ testOption(self, QColorDialog.ColorDialogOption) -> bool """
        return False

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    DontUseNativeDialog = 4
    NoButtons = 2
    ShowAlphaChannel = 1


