# encoding: utf-8
# module PyQt5.QtWidgets
# from /usr/lib/python3/dist-packages/PyQt5/QtWidgets.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui


from .QTextEdit import QTextEdit

class QTextBrowser(QTextEdit):
    """ QTextBrowser(parent: QWidget = None) """
    def anchorClicked(self, QUrl): # real signature unknown; restored from __doc__
        """ anchorClicked(self, QUrl) [signal] """
        pass

    def backward(self): # real signature unknown; restored from __doc__
        """ backward(self) """
        pass

    def backwardAvailable(self, bool): # real signature unknown; restored from __doc__
        """ backwardAvailable(self, bool) [signal] """
        pass

    def backwardHistoryCount(self): # real signature unknown; restored from __doc__
        """ backwardHistoryCount(self) -> int """
        return 0

    def clearHistory(self): # real signature unknown; restored from __doc__
        """ clearHistory(self) """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def focusNextPrevChild(self, bool): # real signature unknown; restored from __doc__
        """ focusNextPrevChild(self, bool) -> bool """
        return False

    def focusOutEvent(self, QFocusEvent): # real signature unknown; restored from __doc__
        """ focusOutEvent(self, QFocusEvent) """
        pass

    def forward(self): # real signature unknown; restored from __doc__
        """ forward(self) """
        pass

    def forwardAvailable(self, bool): # real signature unknown; restored from __doc__
        """ forwardAvailable(self, bool) [signal] """
        pass

    def forwardHistoryCount(self): # real signature unknown; restored from __doc__
        """ forwardHistoryCount(self) -> int """
        return 0

    def highlighted(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        highlighted(self, QUrl) [signal]
        highlighted(self, str) [signal]
        """
        pass

    def historyChanged(self): # real signature unknown; restored from __doc__
        """ historyChanged(self) [signal] """
        pass

    def historyTitle(self, p_int): # real signature unknown; restored from __doc__
        """ historyTitle(self, int) -> str """
        return ""

    def historyUrl(self, p_int): # real signature unknown; restored from __doc__
        """ historyUrl(self, int) -> QUrl """
        pass

    def home(self): # real signature unknown; restored from __doc__
        """ home(self) """
        pass

    def isBackwardAvailable(self): # real signature unknown; restored from __doc__
        """ isBackwardAvailable(self) -> bool """
        return False

    def isForwardAvailable(self): # real signature unknown; restored from __doc__
        """ isForwardAvailable(self) -> bool """
        return False

    def keyPressEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, QKeyEvent) """
        pass

    def loadResource(self, p_int, QUrl): # real signature unknown; restored from __doc__
        """ loadResource(self, int, QUrl) -> Any """
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

    def openExternalLinks(self): # real signature unknown; restored from __doc__
        """ openExternalLinks(self) -> bool """
        return False

    def openLinks(self): # real signature unknown; restored from __doc__
        """ openLinks(self) -> bool """
        return False

    def paintEvent(self, QPaintEvent): # real signature unknown; restored from __doc__
        """ paintEvent(self, QPaintEvent) """
        pass

    def reload(self): # real signature unknown; restored from __doc__
        """ reload(self) """
        pass

    def searchPaths(self): # real signature unknown; restored from __doc__
        """ searchPaths(self) -> List[str] """
        return []

    def setOpenExternalLinks(self, bool): # real signature unknown; restored from __doc__
        """ setOpenExternalLinks(self, bool) """
        pass

    def setOpenLinks(self, bool): # real signature unknown; restored from __doc__
        """ setOpenLinks(self, bool) """
        pass

    def setSearchPaths(self, Iterable, p_str=None): # real signature unknown; restored from __doc__
        """ setSearchPaths(self, Iterable[str]) """
        pass

    def setSource(self, QUrl): # real signature unknown; restored from __doc__
        """ setSource(self, QUrl) """
        pass

    def source(self): # real signature unknown; restored from __doc__
        """ source(self) -> QUrl """
        pass

    def sourceChanged(self, QUrl): # real signature unknown; restored from __doc__
        """ sourceChanged(self, QUrl) [signal] """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


