# encoding: utf-8
# module PyQt5.QtWidgets
# from /usr/lib/python3/dist-packages/PyQt5/QtWidgets.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui


from .QComboBox import QComboBox

class QFontComboBox(QComboBox):
    """ QFontComboBox(parent: QWidget = None) """
    def currentFont(self): # real signature unknown; restored from __doc__
        """ currentFont(self) -> QFont """
        pass

    def currentFontChanged(self, QFont): # real signature unknown; restored from __doc__
        """ currentFontChanged(self, QFont) [signal] """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def fontFilters(self): # real signature unknown; restored from __doc__
        """ fontFilters(self) -> QFontComboBox.FontFilters """
        pass

    def setCurrentFont(self, QFont): # real signature unknown; restored from __doc__
        """ setCurrentFont(self, QFont) """
        pass

    def setFontFilters(self, Union, QFontComboBox_FontFilters=None, QFontComboBox_FontFilter=None): # real signature unknown; restored from __doc__
        """ setFontFilters(self, Union[QFontComboBox.FontFilters, QFontComboBox.FontFilter]) """
        pass

    def setWritingSystem(self, QFontDatabase_WritingSystem): # real signature unknown; restored from __doc__
        """ setWritingSystem(self, QFontDatabase.WritingSystem) """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> QSize """
        pass

    def writingSystem(self): # real signature unknown; restored from __doc__
        """ writingSystem(self) -> QFontDatabase.WritingSystem """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass

    AllFonts = 0
    MonospacedFonts = 4
    NonScalableFonts = 2
    ProportionalFonts = 8
    ScalableFonts = 1


