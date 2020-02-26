# encoding: utf-8
# module PyQt5.QtWidgets
# from /usr/lib/python3/dist-packages/PyQt5/QtWidgets.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui


from .QWidget import QWidget

class QMenu(QWidget):
    """
    QMenu(parent: QWidget = None)
    QMenu(str, parent: QWidget = None)
    """
    def aboutToHide(self): # real signature unknown; restored from __doc__
        """ aboutToHide(self) [signal] """
        pass

    def aboutToShow(self): # real signature unknown; restored from __doc__
        """ aboutToShow(self) [signal] """
        pass

    def actionAt(self, QPoint): # real signature unknown; restored from __doc__
        """ actionAt(self, QPoint) -> QAction """
        return QAction

    def actionEvent(self, QActionEvent): # real signature unknown; restored from __doc__
        """ actionEvent(self, QActionEvent) """
        pass

    def actionGeometry(self, QAction): # real signature unknown; restored from __doc__
        """ actionGeometry(self, QAction) -> QRect """
        pass

    def activeAction(self): # real signature unknown; restored from __doc__
        """ activeAction(self) -> QAction """
        return QAction

    def addAction(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addAction(self, QAction)
        addAction(self, str) -> QAction
        addAction(self, QIcon, str) -> QAction
        addAction(self, str, PYQT_SLOT, shortcut: Union[QKeySequence, QKeySequence.StandardKey, str, int] = 0) -> QAction
        addAction(self, QIcon, str, PYQT_SLOT, shortcut: Union[QKeySequence, QKeySequence.StandardKey, str, int] = 0) -> QAction
        """
        return QAction

    def addMenu(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addMenu(self, QMenu) -> QAction
        addMenu(self, str) -> QMenu
        addMenu(self, QIcon, str) -> QMenu
        """
        return QAction or QMenu

    def addSection(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addSection(self, str) -> QAction
        addSection(self, QIcon, str) -> QAction
        """
        return QAction

    def addSeparator(self): # real signature unknown; restored from __doc__
        """ addSeparator(self) -> QAction """
        return QAction

    def changeEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ changeEvent(self, QEvent) """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def columnCount(self): # real signature unknown; restored from __doc__
        """ columnCount(self) -> int """
        return 0

    def defaultAction(self): # real signature unknown; restored from __doc__
        """ defaultAction(self) -> QAction """
        return QAction

    def enterEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ enterEvent(self, QEvent) """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def exec(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        exec(self) -> QAction
        exec(self, QPoint, action: QAction = None) -> QAction
        exec(Iterable[QAction], QPoint, at: QAction = None, parent: QWidget = None) -> QAction
        """
        return QAction

    def exec_(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        exec_(self) -> QAction
        exec_(self, QPoint, action: QAction = None) -> QAction
        exec_(Iterable[QAction], QPoint, at: QAction = None, parent: QWidget = None) -> QAction
        """
        return QAction

    def focusNextPrevChild(self, bool): # real signature unknown; restored from __doc__
        """ focusNextPrevChild(self, bool) -> bool """
        return False

    def hideEvent(self, QHideEvent): # real signature unknown; restored from __doc__
        """ hideEvent(self, QHideEvent) """
        pass

    def hideTearOffMenu(self): # real signature unknown; restored from __doc__
        """ hideTearOffMenu(self) """
        pass

    def hovered(self, QAction): # real signature unknown; restored from __doc__
        """ hovered(self, QAction) [signal] """
        pass

    def icon(self): # real signature unknown; restored from __doc__
        """ icon(self) -> QIcon """
        pass

    def initStyleOption(self, QStyleOptionMenuItem, QAction): # real signature unknown; restored from __doc__
        """ initStyleOption(self, QStyleOptionMenuItem, QAction) """
        pass

    def insertMenu(self, QAction, QMenu): # real signature unknown; restored from __doc__
        """ insertMenu(self, QAction, QMenu) -> QAction """
        return QAction

    def insertSection(self, QAction, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        insertSection(self, QAction, str) -> QAction
        insertSection(self, QAction, QIcon, str) -> QAction
        """
        return QAction

    def insertSeparator(self, QAction): # real signature unknown; restored from __doc__
        """ insertSeparator(self, QAction) -> QAction """
        return QAction

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def isTearOffEnabled(self): # real signature unknown; restored from __doc__
        """ isTearOffEnabled(self) -> bool """
        return False

    def isTearOffMenuVisible(self): # real signature unknown; restored from __doc__
        """ isTearOffMenuVisible(self) -> bool """
        return False

    def keyPressEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, QKeyEvent) """
        pass

    def leaveEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ leaveEvent(self, QEvent) """
        pass

    def menuAction(self): # real signature unknown; restored from __doc__
        """ menuAction(self) -> QAction """
        return QAction

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

    def popup(self, QPoint, action=None): # real signature unknown; restored from __doc__
        """ popup(self, QPoint, action: QAction = None) """
        pass

    def separatorsCollapsible(self): # real signature unknown; restored from __doc__
        """ separatorsCollapsible(self) -> bool """
        return False

    def setActiveAction(self, QAction): # real signature unknown; restored from __doc__
        """ setActiveAction(self, QAction) """
        pass

    def setDefaultAction(self, QAction): # real signature unknown; restored from __doc__
        """ setDefaultAction(self, QAction) """
        pass

    def setIcon(self, QIcon): # real signature unknown; restored from __doc__
        """ setIcon(self, QIcon) """
        pass

    def setNoReplayFor(self, QWidget): # real signature unknown; restored from __doc__
        """ setNoReplayFor(self, QWidget) """
        pass

    def setSeparatorsCollapsible(self, bool): # real signature unknown; restored from __doc__
        """ setSeparatorsCollapsible(self, bool) """
        pass

    def setTearOffEnabled(self, bool): # real signature unknown; restored from __doc__
        """ setTearOffEnabled(self, bool) """
        pass

    def setTitle(self, p_str): # real signature unknown; restored from __doc__
        """ setTitle(self, str) """
        pass

    def setToolTipsVisible(self, bool): # real signature unknown; restored from __doc__
        """ setToolTipsVisible(self, bool) """
        pass

    def showTearOffMenu(self, QPoint=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        showTearOffMenu(self)
        showTearOffMenu(self, QPoint)
        """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> QSize """
        pass

    def timerEvent(self, QTimerEvent): # real signature unknown; restored from __doc__
        """ timerEvent(self, QTimerEvent) """
        pass

    def title(self): # real signature unknown; restored from __doc__
        """ title(self) -> str """
        return ""

    def toolTipsVisible(self): # real signature unknown; restored from __doc__
        """ toolTipsVisible(self) -> bool """
        return False

    def triggered(self, QAction): # real signature unknown; restored from __doc__
        """ triggered(self, QAction) [signal] """
        pass

    def wheelEvent(self, QWheelEvent): # real signature unknown; restored from __doc__
        """ wheelEvent(self, QWheelEvent) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


