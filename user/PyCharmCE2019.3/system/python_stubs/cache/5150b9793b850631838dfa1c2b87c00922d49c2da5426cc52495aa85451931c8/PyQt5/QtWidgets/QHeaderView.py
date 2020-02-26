# encoding: utf-8
# module PyQt5.QtWidgets
# from /usr/lib/python3/dist-packages/PyQt5/QtWidgets.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui


from .QAbstractItemView import QAbstractItemView

class QHeaderView(QAbstractItemView):
    """ QHeaderView(Qt.Orientation, parent: QWidget = None) """
    def cascadingSectionResizes(self): # real signature unknown; restored from __doc__
        """ cascadingSectionResizes(self) -> bool """
        return False

    def count(self): # real signature unknown; restored from __doc__
        """ count(self) -> int """
        return 0

    def currentChanged(self, QModelIndex, QModelIndex_1): # real signature unknown; restored from __doc__
        """ currentChanged(self, QModelIndex, QModelIndex) """
        pass

    def dataChanged(self, QModelIndex, QModelIndex_1, roles, p_int=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ dataChanged(self, QModelIndex, QModelIndex, roles: Iterable[int] = []) """
        pass

    def defaultAlignment(self): # real signature unknown; restored from __doc__
        """ defaultAlignment(self) -> Qt.Alignment """
        pass

    def defaultSectionSize(self): # real signature unknown; restored from __doc__
        """ defaultSectionSize(self) -> int """
        return 0

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def geometriesChanged(self): # real signature unknown; restored from __doc__
        """ geometriesChanged(self) [signal] """
        pass

    def headerDataChanged(self, Qt_Orientation, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ headerDataChanged(self, Qt.Orientation, int, int) """
        pass

    def hiddenSectionCount(self): # real signature unknown; restored from __doc__
        """ hiddenSectionCount(self) -> int """
        return 0

    def hideSection(self, p_int): # real signature unknown; restored from __doc__
        """ hideSection(self, int) """
        pass

    def highlightSections(self): # real signature unknown; restored from __doc__
        """ highlightSections(self) -> bool """
        return False

    def horizontalOffset(self): # real signature unknown; restored from __doc__
        """ horizontalOffset(self) -> int """
        return 0

    def indexAt(self, QPoint): # real signature unknown; restored from __doc__
        """ indexAt(self, QPoint) -> QModelIndex """
        pass

    def initialize(self): # real signature unknown; restored from __doc__
        """ initialize(self) """
        pass

    def initializeSections(self, p_int=None, p_int_1=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        initializeSections(self)
        initializeSections(self, int, int)
        """
        pass

    def initStyleOption(self, QStyleOptionHeader): # real signature unknown; restored from __doc__
        """ initStyleOption(self, QStyleOptionHeader) """
        pass

    def isIndexHidden(self, QModelIndex): # real signature unknown; restored from __doc__
        """ isIndexHidden(self, QModelIndex) -> bool """
        return False

    def isSectionHidden(self, p_int): # real signature unknown; restored from __doc__
        """ isSectionHidden(self, int) -> bool """
        return False

    def isSortIndicatorShown(self): # real signature unknown; restored from __doc__
        """ isSortIndicatorShown(self) -> bool """
        return False

    def length(self): # real signature unknown; restored from __doc__
        """ length(self) -> int """
        return 0

    def logicalIndex(self, p_int): # real signature unknown; restored from __doc__
        """ logicalIndex(self, int) -> int """
        return 0

    def logicalIndexAt(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        logicalIndexAt(self, int) -> int
        logicalIndexAt(self, int, int) -> int
        logicalIndexAt(self, QPoint) -> int
        """
        return 0

    def maximumSectionSize(self): # real signature unknown; restored from __doc__
        """ maximumSectionSize(self) -> int """
        return 0

    def minimumSectionSize(self): # real signature unknown; restored from __doc__
        """ minimumSectionSize(self) -> int """
        return 0

    def mouseDoubleClickEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ mouseDoubleClickEvent(self, QMouseEvent) """
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

    def moveCursor(self, QAbstractItemView_CursorAction, Union, Qt_KeyboardModifiers=None, Qt_KeyboardModifier=None): # real signature unknown; restored from __doc__
        """ moveCursor(self, QAbstractItemView.CursorAction, Union[Qt.KeyboardModifiers, Qt.KeyboardModifier]) -> QModelIndex """
        pass

    def moveSection(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ moveSection(self, int, int) """
        pass

    def offset(self): # real signature unknown; restored from __doc__
        """ offset(self) -> int """
        return 0

    def orientation(self): # real signature unknown; restored from __doc__
        """ orientation(self) -> Qt.Orientation """
        pass

    def paintEvent(self, QPaintEvent): # real signature unknown; restored from __doc__
        """ paintEvent(self, QPaintEvent) """
        pass

    def paintSection(self, QPainter, QRect, p_int): # real signature unknown; restored from __doc__
        """ paintSection(self, QPainter, QRect, int) """
        pass

    def reset(self): # real signature unknown; restored from __doc__
        """ reset(self) """
        pass

    def resetDefaultSectionSize(self): # real signature unknown; restored from __doc__
        """ resetDefaultSectionSize(self) """
        pass

    def resizeContentsPrecision(self): # real signature unknown; restored from __doc__
        """ resizeContentsPrecision(self) -> int """
        return 0

    def resizeSection(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ resizeSection(self, int, int) """
        pass

    def resizeSections(self, QHeaderView_ResizeMode=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        resizeSections(self)
        resizeSections(self, QHeaderView.ResizeMode)
        """
        pass

    def restoreState(self, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ restoreState(self, Union[QByteArray, bytes, bytearray]) -> bool """
        return False

    def rowsInserted(self, QModelIndex, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ rowsInserted(self, QModelIndex, int, int) """
        pass

    def saveState(self): # real signature unknown; restored from __doc__
        """ saveState(self) -> QByteArray """
        pass

    def scrollContentsBy(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ scrollContentsBy(self, int, int) """
        pass

    def scrollTo(self, QModelIndex, QAbstractItemView_ScrollHint): # real signature unknown; restored from __doc__
        """ scrollTo(self, QModelIndex, QAbstractItemView.ScrollHint) """
        pass

    def sectionClicked(self, p_int): # real signature unknown; restored from __doc__
        """ sectionClicked(self, int) [signal] """
        pass

    def sectionCountChanged(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ sectionCountChanged(self, int, int) [signal] """
        pass

    def sectionDoubleClicked(self, p_int): # real signature unknown; restored from __doc__
        """ sectionDoubleClicked(self, int) [signal] """
        pass

    def sectionEntered(self, p_int): # real signature unknown; restored from __doc__
        """ sectionEntered(self, int) [signal] """
        pass

    def sectionHandleDoubleClicked(self, p_int): # real signature unknown; restored from __doc__
        """ sectionHandleDoubleClicked(self, int) [signal] """
        pass

    def sectionMoved(self, p_int, p_int_1, p_int_2): # real signature unknown; restored from __doc__
        """ sectionMoved(self, int, int, int) [signal] """
        pass

    def sectionPosition(self, p_int): # real signature unknown; restored from __doc__
        """ sectionPosition(self, int) -> int """
        return 0

    def sectionPressed(self, p_int): # real signature unknown; restored from __doc__
        """ sectionPressed(self, int) [signal] """
        pass

    def sectionResized(self, p_int, p_int_1, p_int_2): # real signature unknown; restored from __doc__
        """ sectionResized(self, int, int, int) [signal] """
        pass

    def sectionResizeMode(self, p_int): # real signature unknown; restored from __doc__
        """ sectionResizeMode(self, int) -> QHeaderView.ResizeMode """
        pass

    def sectionsAboutToBeRemoved(self, QModelIndex, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ sectionsAboutToBeRemoved(self, QModelIndex, int, int) """
        pass

    def sectionsClickable(self): # real signature unknown; restored from __doc__
        """ sectionsClickable(self) -> bool """
        return False

    def sectionsHidden(self): # real signature unknown; restored from __doc__
        """ sectionsHidden(self) -> bool """
        return False

    def sectionsInserted(self, QModelIndex, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ sectionsInserted(self, QModelIndex, int, int) """
        pass

    def sectionSize(self, p_int): # real signature unknown; restored from __doc__
        """ sectionSize(self, int) -> int """
        return 0

    def sectionSizeFromContents(self, p_int): # real signature unknown; restored from __doc__
        """ sectionSizeFromContents(self, int) -> QSize """
        pass

    def sectionSizeHint(self, p_int): # real signature unknown; restored from __doc__
        """ sectionSizeHint(self, int) -> int """
        return 0

    def sectionsMovable(self): # real signature unknown; restored from __doc__
        """ sectionsMovable(self) -> bool """
        return False

    def sectionsMoved(self): # real signature unknown; restored from __doc__
        """ sectionsMoved(self) -> bool """
        return False

    def sectionViewportPosition(self, p_int): # real signature unknown; restored from __doc__
        """ sectionViewportPosition(self, int) -> int """
        return 0

    def setCascadingSectionResizes(self, bool): # real signature unknown; restored from __doc__
        """ setCascadingSectionResizes(self, bool) """
        pass

    def setDefaultAlignment(self, Union, Qt_Alignment=None, Qt_AlignmentFlag=None): # real signature unknown; restored from __doc__
        """ setDefaultAlignment(self, Union[Qt.Alignment, Qt.AlignmentFlag]) """
        pass

    def setDefaultSectionSize(self, p_int): # real signature unknown; restored from __doc__
        """ setDefaultSectionSize(self, int) """
        pass

    def setHighlightSections(self, bool): # real signature unknown; restored from __doc__
        """ setHighlightSections(self, bool) """
        pass

    def setMaximumSectionSize(self, p_int): # real signature unknown; restored from __doc__
        """ setMaximumSectionSize(self, int) """
        pass

    def setMinimumSectionSize(self, p_int): # real signature unknown; restored from __doc__
        """ setMinimumSectionSize(self, int) """
        pass

    def setModel(self, QAbstractItemModel): # real signature unknown; restored from __doc__
        """ setModel(self, QAbstractItemModel) """
        pass

    def setOffset(self, p_int): # real signature unknown; restored from __doc__
        """ setOffset(self, int) """
        pass

    def setOffsetToLastSection(self): # real signature unknown; restored from __doc__
        """ setOffsetToLastSection(self) """
        pass

    def setOffsetToSectionPosition(self, p_int): # real signature unknown; restored from __doc__
        """ setOffsetToSectionPosition(self, int) """
        pass

    def setResizeContentsPrecision(self, p_int): # real signature unknown; restored from __doc__
        """ setResizeContentsPrecision(self, int) """
        pass

    def setSectionHidden(self, p_int, bool): # real signature unknown; restored from __doc__
        """ setSectionHidden(self, int, bool) """
        pass

    def setSectionResizeMode(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setSectionResizeMode(self, int, QHeaderView.ResizeMode)
        setSectionResizeMode(self, QHeaderView.ResizeMode)
        """
        pass

    def setSectionsClickable(self, bool): # real signature unknown; restored from __doc__
        """ setSectionsClickable(self, bool) """
        pass

    def setSectionsMovable(self, bool): # real signature unknown; restored from __doc__
        """ setSectionsMovable(self, bool) """
        pass

    def setSelection(self, QRect, Union, QItemSelectionModel_SelectionFlags=None, QItemSelectionModel_SelectionFlag=None): # real signature unknown; restored from __doc__
        """ setSelection(self, QRect, Union[QItemSelectionModel.SelectionFlags, QItemSelectionModel.SelectionFlag]) """
        pass

    def setSortIndicator(self, p_int, Qt_SortOrder): # real signature unknown; restored from __doc__
        """ setSortIndicator(self, int, Qt.SortOrder) """
        pass

    def setSortIndicatorShown(self, bool): # real signature unknown; restored from __doc__
        """ setSortIndicatorShown(self, bool) """
        pass

    def setStretchLastSection(self, bool): # real signature unknown; restored from __doc__
        """ setStretchLastSection(self, bool) """
        pass

    def setVisible(self, bool): # real signature unknown; restored from __doc__
        """ setVisible(self, bool) """
        pass

    def showSection(self, p_int): # real signature unknown; restored from __doc__
        """ showSection(self, int) """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> QSize """
        pass

    def sortIndicatorOrder(self): # real signature unknown; restored from __doc__
        """ sortIndicatorOrder(self) -> Qt.SortOrder """
        pass

    def sortIndicatorSection(self): # real signature unknown; restored from __doc__
        """ sortIndicatorSection(self) -> int """
        return 0

    def stretchLastSection(self): # real signature unknown; restored from __doc__
        """ stretchLastSection(self) -> bool """
        return False

    def stretchSectionCount(self): # real signature unknown; restored from __doc__
        """ stretchSectionCount(self) -> int """
        return 0

    def swapSections(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ swapSections(self, int, int) """
        pass

    def updateGeometries(self): # real signature unknown; restored from __doc__
        """ updateGeometries(self) """
        pass

    def updateSection(self, p_int): # real signature unknown; restored from __doc__
        """ updateSection(self, int) """
        pass

    def verticalOffset(self): # real signature unknown; restored from __doc__
        """ verticalOffset(self) -> int """
        return 0

    def viewportEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ viewportEvent(self, QEvent) -> bool """
        return False

    def visualIndex(self, p_int): # real signature unknown; restored from __doc__
        """ visualIndex(self, int) -> int """
        return 0

    def visualIndexAt(self, p_int): # real signature unknown; restored from __doc__
        """ visualIndexAt(self, int) -> int """
        return 0

    def visualRect(self, QModelIndex): # real signature unknown; restored from __doc__
        """ visualRect(self, QModelIndex) -> QRect """
        pass

    def visualRegionForSelection(self, QItemSelection): # real signature unknown; restored from __doc__
        """ visualRegionForSelection(self, QItemSelection) -> QRegion """
        pass

    def __init__(self, Qt_Orientation, parent=None): # real signature unknown; restored from __doc__
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    Custom = 2
    Fixed = 2
    Interactive = 0
    ResizeToContents = 3
    Stretch = 1


