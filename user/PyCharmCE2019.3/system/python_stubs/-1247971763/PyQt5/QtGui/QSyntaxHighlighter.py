# encoding: utf-8
# module PyQt5.QtGui
# from /usr/lib/python3/dist-packages/PyQt5/QtGui.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore


class QSyntaxHighlighter(__PyQt5_QtCore.QObject):
    """
    QSyntaxHighlighter(QTextDocument)
    QSyntaxHighlighter(QObject)
    """
    def currentBlock(self): # real signature unknown; restored from __doc__
        """ currentBlock(self) -> QTextBlock """
        return QTextBlock

    def currentBlockState(self): # real signature unknown; restored from __doc__
        """ currentBlockState(self) -> int """
        return 0

    def currentBlockUserData(self): # real signature unknown; restored from __doc__
        """ currentBlockUserData(self) -> QTextBlockUserData """
        return QTextBlockUserData

    def document(self): # real signature unknown; restored from __doc__
        """ document(self) -> QTextDocument """
        return QTextDocument

    def format(self, p_int): # real signature unknown; restored from __doc__
        """ format(self, int) -> QTextCharFormat """
        return QTextCharFormat

    def highlightBlock(self, p_str): # real signature unknown; restored from __doc__
        """ highlightBlock(self, str) """
        pass

    def previousBlockState(self): # real signature unknown; restored from __doc__
        """ previousBlockState(self) -> int """
        return 0

    def rehighlight(self): # real signature unknown; restored from __doc__
        """ rehighlight(self) """
        pass

    def rehighlightBlock(self, QTextBlock): # real signature unknown; restored from __doc__
        """ rehighlightBlock(self, QTextBlock) """
        pass

    def setCurrentBlockState(self, p_int): # real signature unknown; restored from __doc__
        """ setCurrentBlockState(self, int) """
        pass

    def setCurrentBlockUserData(self, QTextBlockUserData): # real signature unknown; restored from __doc__
        """ setCurrentBlockUserData(self, QTextBlockUserData) """
        pass

    def setDocument(self, QTextDocument): # real signature unknown; restored from __doc__
        """ setDocument(self, QTextDocument) """
        pass

    def setFormat(self, p_int, p_int_1, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setFormat(self, int, int, QTextCharFormat)
        setFormat(self, int, int, Union[QColor, Qt.GlobalColor, QGradient])
        setFormat(self, int, int, QFont)
        """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


