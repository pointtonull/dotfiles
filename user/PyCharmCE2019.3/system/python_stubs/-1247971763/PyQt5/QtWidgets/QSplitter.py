# encoding: utf-8
# module PyQt5.QtWidgets
# from /usr/lib/python3/dist-packages/PyQt5/QtWidgets.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui


from .QFrame import QFrame

class QSplitter(QFrame):
    """
    QSplitter(parent: QWidget = None)
    QSplitter(Qt.Orientation, parent: QWidget = None)
    """
    def addWidget(self, QWidget): # real signature unknown; restored from __doc__
        """ addWidget(self, QWidget) """
        pass

    def changeEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ changeEvent(self, QEvent) """
        pass

    def childEvent(self, QChildEvent): # real signature unknown; restored from __doc__
        """ childEvent(self, QChildEvent) """
        pass

    def childrenCollapsible(self): # real signature unknown; restored from __doc__
        """ childrenCollapsible(self) -> bool """
        return False

    def closestLegalPosition(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ closestLegalPosition(self, int, int) -> int """
        return 0

    def count(self): # real signature unknown; restored from __doc__
        """ count(self) -> int """
        return 0

    def createHandle(self): # real signature unknown; restored from __doc__
        """ createHandle(self) -> QSplitterHandle """
        return QSplitterHandle

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def getRange(self, p_int): # real signature unknown; restored from __doc__
        """ getRange(self, int) -> Tuple[int, int] """
        pass

    def handle(self, p_int): # real signature unknown; restored from __doc__
        """ handle(self, int) -> QSplitterHandle """
        return QSplitterHandle

    def handleWidth(self): # real signature unknown; restored from __doc__
        """ handleWidth(self) -> int """
        return 0

    def indexOf(self, QWidget): # real signature unknown; restored from __doc__
        """ indexOf(self, QWidget) -> int """
        return 0

    def insertWidget(self, p_int, QWidget): # real signature unknown; restored from __doc__
        """ insertWidget(self, int, QWidget) """
        pass

    def isCollapsible(self, p_int): # real signature unknown; restored from __doc__
        """ isCollapsible(self, int) -> bool """
        return False

    def minimumSizeHint(self): # real signature unknown; restored from __doc__
        """ minimumSizeHint(self) -> QSize """
        pass

    def moveSplitter(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ moveSplitter(self, int, int) """
        pass

    def opaqueResize(self): # real signature unknown; restored from __doc__
        """ opaqueResize(self) -> bool """
        return False

    def orientation(self): # real signature unknown; restored from __doc__
        """ orientation(self) -> Qt.Orientation """
        pass

    def refresh(self): # real signature unknown; restored from __doc__
        """ refresh(self) """
        pass

    def replaceWidget(self, p_int, QWidget): # real signature unknown; restored from __doc__
        """ replaceWidget(self, int, QWidget) -> QWidget """
        return QWidget

    def resizeEvent(self, QResizeEvent): # real signature unknown; restored from __doc__
        """ resizeEvent(self, QResizeEvent) """
        pass

    def restoreState(self, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ restoreState(self, Union[QByteArray, bytes, bytearray]) -> bool """
        return False

    def saveState(self): # real signature unknown; restored from __doc__
        """ saveState(self) -> QByteArray """
        pass

    def setChildrenCollapsible(self, bool): # real signature unknown; restored from __doc__
        """ setChildrenCollapsible(self, bool) """
        pass

    def setCollapsible(self, p_int, bool): # real signature unknown; restored from __doc__
        """ setCollapsible(self, int, bool) """
        pass

    def setHandleWidth(self, p_int): # real signature unknown; restored from __doc__
        """ setHandleWidth(self, int) """
        pass

    def setOpaqueResize(self, opaque=True): # real signature unknown; restored from __doc__
        """ setOpaqueResize(self, opaque: bool = True) """
        pass

    def setOrientation(self, Qt_Orientation): # real signature unknown; restored from __doc__
        """ setOrientation(self, Qt.Orientation) """
        pass

    def setRubberBand(self, p_int): # real signature unknown; restored from __doc__
        """ setRubberBand(self, int) """
        pass

    def setSizes(self, Iterable, p_int=None): # real signature unknown; restored from __doc__
        """ setSizes(self, Iterable[int]) """
        pass

    def setStretchFactor(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ setStretchFactor(self, int, int) """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> QSize """
        pass

    def sizes(self): # real signature unknown; restored from __doc__
        """ sizes(self) -> List[int] """
        return []

    def splitterMoved(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ splitterMoved(self, int, int) [signal] """
        pass

    def widget(self, p_int): # real signature unknown; restored from __doc__
        """ widget(self, int) -> QWidget """
        return QWidget

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass


