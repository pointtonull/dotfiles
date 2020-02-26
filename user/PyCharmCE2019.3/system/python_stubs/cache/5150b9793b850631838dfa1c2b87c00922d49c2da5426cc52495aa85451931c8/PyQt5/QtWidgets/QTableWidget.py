# encoding: utf-8
# module PyQt5.QtWidgets
# from /usr/lib/python3/dist-packages/PyQt5/QtWidgets.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui


from .QTableView import QTableView

class QTableWidget(QTableView):
    """
    QTableWidget(parent: QWidget = None)
    QTableWidget(int, int, parent: QWidget = None)
    """
    def cellActivated(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ cellActivated(self, int, int) [signal] """
        pass

    def cellChanged(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ cellChanged(self, int, int) [signal] """
        pass

    def cellClicked(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ cellClicked(self, int, int) [signal] """
        pass

    def cellDoubleClicked(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ cellDoubleClicked(self, int, int) [signal] """
        pass

    def cellEntered(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ cellEntered(self, int, int) [signal] """
        pass

    def cellPressed(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ cellPressed(self, int, int) [signal] """
        pass

    def cellWidget(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ cellWidget(self, int, int) -> QWidget """
        return QWidget

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def clearContents(self): # real signature unknown; restored from __doc__
        """ clearContents(self) """
        pass

    def closePersistentEditor(self, QTableWidgetItem): # real signature unknown; restored from __doc__
        """ closePersistentEditor(self, QTableWidgetItem) """
        pass

    def column(self, QTableWidgetItem): # real signature unknown; restored from __doc__
        """ column(self, QTableWidgetItem) -> int """
        return 0

    def columnCount(self): # real signature unknown; restored from __doc__
        """ columnCount(self) -> int """
        return 0

    def currentCellChanged(self, p_int, p_int_1, p_int_2, p_int_3): # real signature unknown; restored from __doc__
        """ currentCellChanged(self, int, int, int, int) [signal] """
        pass

    def currentColumn(self): # real signature unknown; restored from __doc__
        """ currentColumn(self) -> int """
        return 0

    def currentItem(self): # real signature unknown; restored from __doc__
        """ currentItem(self) -> QTableWidgetItem """
        return QTableWidgetItem

    def currentItemChanged(self, QTableWidgetItem, QTableWidgetItem_1): # real signature unknown; restored from __doc__
        """ currentItemChanged(self, QTableWidgetItem, QTableWidgetItem) [signal] """
        pass

    def currentRow(self): # real signature unknown; restored from __doc__
        """ currentRow(self) -> int """
        return 0

    def dropEvent(self, QDropEvent): # real signature unknown; restored from __doc__
        """ dropEvent(self, QDropEvent) """
        pass

    def dropMimeData(self, p_int, p_int_1, QMimeData, Qt_DropAction): # real signature unknown; restored from __doc__
        """ dropMimeData(self, int, int, QMimeData, Qt.DropAction) -> bool """
        return False

    def editItem(self, QTableWidgetItem): # real signature unknown; restored from __doc__
        """ editItem(self, QTableWidgetItem) """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def findItems(self, p_str, Union, Qt_MatchFlags=None, Qt_MatchFlag=None): # real signature unknown; restored from __doc__
        """ findItems(self, str, Union[Qt.MatchFlags, Qt.MatchFlag]) -> List[QTableWidgetItem] """
        return []

    def horizontalHeaderItem(self, p_int): # real signature unknown; restored from __doc__
        """ horizontalHeaderItem(self, int) -> QTableWidgetItem """
        return QTableWidgetItem

    def indexFromItem(self, QTableWidgetItem): # real signature unknown; restored from __doc__
        """ indexFromItem(self, QTableWidgetItem) -> QModelIndex """
        pass

    def insertColumn(self, p_int): # real signature unknown; restored from __doc__
        """ insertColumn(self, int) """
        pass

    def insertRow(self, p_int): # real signature unknown; restored from __doc__
        """ insertRow(self, int) """
        pass

    def isSortingEnabled(self): # real signature unknown; restored from __doc__
        """ isSortingEnabled(self) -> bool """
        return False

    def item(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ item(self, int, int) -> QTableWidgetItem """
        return QTableWidgetItem

    def itemActivated(self, QTableWidgetItem): # real signature unknown; restored from __doc__
        """ itemActivated(self, QTableWidgetItem) [signal] """
        pass

    def itemAt(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        itemAt(self, QPoint) -> QTableWidgetItem
        itemAt(self, int, int) -> QTableWidgetItem
        """
        return QTableWidgetItem

    def itemChanged(self, QTableWidgetItem): # real signature unknown; restored from __doc__
        """ itemChanged(self, QTableWidgetItem) [signal] """
        pass

    def itemClicked(self, QTableWidgetItem): # real signature unknown; restored from __doc__
        """ itemClicked(self, QTableWidgetItem) [signal] """
        pass

    def itemDoubleClicked(self, QTableWidgetItem): # real signature unknown; restored from __doc__
        """ itemDoubleClicked(self, QTableWidgetItem) [signal] """
        pass

    def itemEntered(self, QTableWidgetItem): # real signature unknown; restored from __doc__
        """ itemEntered(self, QTableWidgetItem) [signal] """
        pass

    def itemFromIndex(self, QModelIndex): # real signature unknown; restored from __doc__
        """ itemFromIndex(self, QModelIndex) -> QTableWidgetItem """
        return QTableWidgetItem

    def itemPressed(self, QTableWidgetItem): # real signature unknown; restored from __doc__
        """ itemPressed(self, QTableWidgetItem) [signal] """
        pass

    def itemPrototype(self): # real signature unknown; restored from __doc__
        """ itemPrototype(self) -> QTableWidgetItem """
        return QTableWidgetItem

    def items(self, QMimeData): # real signature unknown; restored from __doc__
        """ items(self, QMimeData) -> List[QTableWidgetItem] """
        return []

    def itemSelectionChanged(self): # real signature unknown; restored from __doc__
        """ itemSelectionChanged(self) [signal] """
        pass

    def mimeData(self, Iterable, QTableWidgetItem=None): # real signature unknown; restored from __doc__
        """ mimeData(self, Iterable[QTableWidgetItem]) -> QMimeData """
        pass

    def mimeTypes(self): # real signature unknown; restored from __doc__
        """ mimeTypes(self) -> List[str] """
        return []

    def openPersistentEditor(self, QTableWidgetItem): # real signature unknown; restored from __doc__
        """ openPersistentEditor(self, QTableWidgetItem) """
        pass

    def removeCellWidget(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ removeCellWidget(self, int, int) """
        pass

    def removeColumn(self, p_int): # real signature unknown; restored from __doc__
        """ removeColumn(self, int) """
        pass

    def removeRow(self, p_int): # real signature unknown; restored from __doc__
        """ removeRow(self, int) """
        pass

    def row(self, QTableWidgetItem): # real signature unknown; restored from __doc__
        """ row(self, QTableWidgetItem) -> int """
        return 0

    def rowCount(self): # real signature unknown; restored from __doc__
        """ rowCount(self) -> int """
        return 0

    def scrollToItem(self, QTableWidgetItem, hint=None): # real signature unknown; restored from __doc__
        """ scrollToItem(self, QTableWidgetItem, hint: QAbstractItemView.ScrollHint = QAbstractItemView.EnsureVisible) """
        pass

    def selectedItems(self): # real signature unknown; restored from __doc__
        """ selectedItems(self) -> object """
        return object()

    def selectedRanges(self): # real signature unknown; restored from __doc__
        """ selectedRanges(self) -> object """
        return object()

    def setCellWidget(self, p_int, p_int_1, QWidget): # real signature unknown; restored from __doc__
        """ setCellWidget(self, int, int, QWidget) """
        pass

    def setColumnCount(self, p_int): # real signature unknown; restored from __doc__
        """ setColumnCount(self, int) """
        pass

    def setCurrentCell(self, p_int, p_int_1, Union=None, QItemSelectionModel_SelectionFlags=None, QItemSelectionModel_SelectionFlag=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setCurrentCell(self, int, int)
        setCurrentCell(self, int, int, Union[QItemSelectionModel.SelectionFlags, QItemSelectionModel.SelectionFlag])
        """
        pass

    def setCurrentItem(self, QTableWidgetItem, Union=None, QItemSelectionModel_SelectionFlags=None, QItemSelectionModel_SelectionFlag=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setCurrentItem(self, QTableWidgetItem)
        setCurrentItem(self, QTableWidgetItem, Union[QItemSelectionModel.SelectionFlags, QItemSelectionModel.SelectionFlag])
        """
        pass

    def setHorizontalHeaderItem(self, p_int, QTableWidgetItem): # real signature unknown; restored from __doc__
        """ setHorizontalHeaderItem(self, int, QTableWidgetItem) """
        pass

    def setHorizontalHeaderLabels(self, Iterable, p_str=None): # real signature unknown; restored from __doc__
        """ setHorizontalHeaderLabels(self, Iterable[str]) """
        pass

    def setItem(self, p_int, p_int_1, QTableWidgetItem): # real signature unknown; restored from __doc__
        """ setItem(self, int, int, QTableWidgetItem) """
        pass

    def setItemPrototype(self, QTableWidgetItem): # real signature unknown; restored from __doc__
        """ setItemPrototype(self, QTableWidgetItem) """
        pass

    def setModel(self, *args, **kwargs): # real signature unknown
        pass

    def setRangeSelected(self, QTableWidgetSelectionRange, bool): # real signature unknown; restored from __doc__
        """ setRangeSelected(self, QTableWidgetSelectionRange, bool) """
        pass

    def setRowCount(self, p_int): # real signature unknown; restored from __doc__
        """ setRowCount(self, int) """
        pass

    def setSortingEnabled(self, bool): # real signature unknown; restored from __doc__
        """ setSortingEnabled(self, bool) """
        pass

    def setVerticalHeaderItem(self, p_int, QTableWidgetItem): # real signature unknown; restored from __doc__
        """ setVerticalHeaderItem(self, int, QTableWidgetItem) """
        pass

    def setVerticalHeaderLabels(self, Iterable, p_str=None): # real signature unknown; restored from __doc__
        """ setVerticalHeaderLabels(self, Iterable[str]) """
        pass

    def sortItems(self, p_int, order=None): # real signature unknown; restored from __doc__
        """ sortItems(self, int, order: Qt.SortOrder = Qt.AscendingOrder) """
        pass

    def supportedDropActions(self): # real signature unknown; restored from __doc__
        """ supportedDropActions(self) -> Qt.DropActions """
        pass

    def takeHorizontalHeaderItem(self, p_int): # real signature unknown; restored from __doc__
        """ takeHorizontalHeaderItem(self, int) -> QTableWidgetItem """
        return QTableWidgetItem

    def takeItem(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ takeItem(self, int, int) -> QTableWidgetItem """
        return QTableWidgetItem

    def takeVerticalHeaderItem(self, p_int): # real signature unknown; restored from __doc__
        """ takeVerticalHeaderItem(self, int) -> QTableWidgetItem """
        return QTableWidgetItem

    def verticalHeaderItem(self, p_int): # real signature unknown; restored from __doc__
        """ verticalHeaderItem(self, int) -> QTableWidgetItem """
        return QTableWidgetItem

    def visualColumn(self, p_int): # real signature unknown; restored from __doc__
        """ visualColumn(self, int) -> int """
        return 0

    def visualItemRect(self, QTableWidgetItem): # real signature unknown; restored from __doc__
        """ visualItemRect(self, QTableWidgetItem) -> QRect """
        pass

    def visualRow(self, p_int): # real signature unknown; restored from __doc__
        """ visualRow(self, int) -> int """
        return 0

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


