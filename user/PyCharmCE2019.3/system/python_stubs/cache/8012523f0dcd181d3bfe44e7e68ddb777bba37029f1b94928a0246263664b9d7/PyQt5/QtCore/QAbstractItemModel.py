# encoding: utf-8
# module PyQt5.QtCore
# from /usr/lib/python3/dist-packages/PyQt5/QtCore.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc
# no imports

from .QObject import QObject

class QAbstractItemModel(QObject):
    """ QAbstractItemModel(parent: QObject = None) """
    def beginInsertColumns(self, QModelIndex, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ beginInsertColumns(self, QModelIndex, int, int) """
        pass

    def beginInsertRows(self, QModelIndex, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ beginInsertRows(self, QModelIndex, int, int) """
        pass

    def beginMoveColumns(self, QModelIndex, p_int, p_int_1, QModelIndex_1, p_int_2): # real signature unknown; restored from __doc__
        """ beginMoveColumns(self, QModelIndex, int, int, QModelIndex, int) -> bool """
        return False

    def beginMoveRows(self, QModelIndex, p_int, p_int_1, QModelIndex_1, p_int_2): # real signature unknown; restored from __doc__
        """ beginMoveRows(self, QModelIndex, int, int, QModelIndex, int) -> bool """
        return False

    def beginRemoveColumns(self, QModelIndex, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ beginRemoveColumns(self, QModelIndex, int, int) """
        pass

    def beginRemoveRows(self, QModelIndex, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ beginRemoveRows(self, QModelIndex, int, int) """
        pass

    def beginResetModel(self): # real signature unknown; restored from __doc__
        """ beginResetModel(self) """
        pass

    def buddy(self, QModelIndex): # real signature unknown; restored from __doc__
        """ buddy(self, QModelIndex) -> QModelIndex """
        return QModelIndex

    def canDropMimeData(self, QMimeData, Qt_DropAction, p_int, p_int_1, QModelIndex): # real signature unknown; restored from __doc__
        """ canDropMimeData(self, QMimeData, Qt.DropAction, int, int, QModelIndex) -> bool """
        return False

    def canFetchMore(self, QModelIndex): # real signature unknown; restored from __doc__
        """ canFetchMore(self, QModelIndex) -> bool """
        return False

    def changePersistentIndex(self, QModelIndex, QModelIndex_1): # real signature unknown; restored from __doc__
        """ changePersistentIndex(self, QModelIndex, QModelIndex) """
        pass

    def changePersistentIndexList(self, p_object, p_object_1): # real signature unknown; restored from __doc__
        """ changePersistentIndexList(self, object, object) """
        pass

    def columnCount(self, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ columnCount(self, parent: QModelIndex = QModelIndex()) -> int """
        pass

    def columnsAboutToBeInserted(self, QModelIndex, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ columnsAboutToBeInserted(self, QModelIndex, int, int) [signal] """
        pass

    def columnsAboutToBeMoved(self, QModelIndex, p_int, p_int_1, QModelIndex_1, p_int_2): # real signature unknown; restored from __doc__
        """ columnsAboutToBeMoved(self, QModelIndex, int, int, QModelIndex, int) [signal] """
        pass

    def columnsAboutToBeRemoved(self, QModelIndex, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ columnsAboutToBeRemoved(self, QModelIndex, int, int) [signal] """
        pass

    def columnsInserted(self, QModelIndex, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ columnsInserted(self, QModelIndex, int, int) [signal] """
        pass

    def columnsMoved(self, QModelIndex, p_int, p_int_1, QModelIndex_1, p_int_2): # real signature unknown; restored from __doc__
        """ columnsMoved(self, QModelIndex, int, int, QModelIndex, int) [signal] """
        pass

    def columnsRemoved(self, QModelIndex, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ columnsRemoved(self, QModelIndex, int, int) [signal] """
        pass

    def createIndex(self, p_int, p_int_1, p_object=0): # real signature unknown; restored from __doc__
        """ createIndex(self, int, int, object: object = 0) -> QModelIndex """
        return QModelIndex

    def data(self, QModelIndex, role=None): # real signature unknown; restored from __doc__
        """ data(self, QModelIndex, role: int = Qt.DisplayRole) -> Any """
        pass

    def dataChanged(self, QModelIndex, QModelIndex_1, Iterable, p_int=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ dataChanged(self, QModelIndex, QModelIndex, Iterable[int] = []) [signal] """
        pass

    def decodeData(self, p_int, p_int_1, QModelIndex, QDataStream): # real signature unknown; restored from __doc__
        """ decodeData(self, int, int, QModelIndex, QDataStream) -> bool """
        return False

    def dropMimeData(self, QMimeData, Qt_DropAction, p_int, p_int_1, QModelIndex): # real signature unknown; restored from __doc__
        """ dropMimeData(self, QMimeData, Qt.DropAction, int, int, QModelIndex) -> bool """
        return False

    def encodeData(self, p_object, QDataStream): # real signature unknown; restored from __doc__
        """ encodeData(self, object, QDataStream) """
        pass

    def endInsertColumns(self): # real signature unknown; restored from __doc__
        """ endInsertColumns(self) """
        pass

    def endInsertRows(self): # real signature unknown; restored from __doc__
        """ endInsertRows(self) """
        pass

    def endMoveColumns(self): # real signature unknown; restored from __doc__
        """ endMoveColumns(self) """
        pass

    def endMoveRows(self): # real signature unknown; restored from __doc__
        """ endMoveRows(self) """
        pass

    def endRemoveColumns(self): # real signature unknown; restored from __doc__
        """ endRemoveColumns(self) """
        pass

    def endRemoveRows(self): # real signature unknown; restored from __doc__
        """ endRemoveRows(self) """
        pass

    def endResetModel(self): # real signature unknown; restored from __doc__
        """ endResetModel(self) """
        pass

    def fetchMore(self, QModelIndex): # real signature unknown; restored from __doc__
        """ fetchMore(self, QModelIndex) """
        pass

    def flags(self, QModelIndex): # real signature unknown; restored from __doc__
        """ flags(self, QModelIndex) -> Qt.ItemFlags """
        pass

    def hasChildren(self, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ hasChildren(self, parent: QModelIndex = QModelIndex()) -> bool """
        pass

    def hasIndex(self, p_int, p_int_1, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ hasIndex(self, int, int, parent: QModelIndex = QModelIndex()) -> bool """
        pass

    def headerData(self, p_int, Qt_Orientation, role=None): # real signature unknown; restored from __doc__
        """ headerData(self, int, Qt.Orientation, role: int = Qt.DisplayRole) -> Any """
        pass

    def index(self, p_int, p_int_1, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ index(self, int, int, parent: QModelIndex = QModelIndex()) -> QModelIndex """
        pass

    def insertColumn(self, p_int, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ insertColumn(self, int, parent: QModelIndex = QModelIndex()) -> bool """
        pass

    def insertColumns(self, p_int, p_int_1, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ insertColumns(self, int, int, parent: QModelIndex = QModelIndex()) -> bool """
        pass

    def insertRow(self, p_int, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ insertRow(self, int, parent: QModelIndex = QModelIndex()) -> bool """
        pass

    def insertRows(self, p_int, p_int_1, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ insertRows(self, int, int, parent: QModelIndex = QModelIndex()) -> bool """
        pass

    def itemData(self, QModelIndex): # real signature unknown; restored from __doc__
        """ itemData(self, QModelIndex) -> object """
        return object()

    def layoutAboutToBeChanged(self, p_object=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ layoutAboutToBeChanged(self, object = QList&lt;QPersistentModelIndex&gt;(), QAbstractItemModel.LayoutChangeHint = QAbstractItemModel.NoLayoutChangeHint) [signal] """
        pass

    def layoutChanged(self, Iterable, QPersistentModelIndex=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ layoutChanged(self, Iterable[QPersistentModelIndex] = [], QAbstractItemModel.LayoutChangeHint = QAbstractItemModel.NoLayoutChangeHint) [signal] """
        pass

    def match(self, QModelIndex, p_int, Any, hits=1, flags, Qt_MatchFlags=None, Qt_MatchFlag=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ match(self, QModelIndex, int, Any, hits: int = 1, flags: Union[Qt.MatchFlags, Qt.MatchFlag] = Qt.MatchStartsWith|Qt.MatchWrap) -> object """
        pass

    def mimeData(self, p_object): # real signature unknown; restored from __doc__
        """ mimeData(self, object) -> QMimeData """
        return QMimeData

    def mimeTypes(self): # real signature unknown; restored from __doc__
        """ mimeTypes(self) -> List[str] """
        return []

    def modelAboutToBeReset(self): # real signature unknown; restored from __doc__
        """ modelAboutToBeReset(self) [signal] """
        pass

    def modelReset(self): # real signature unknown; restored from __doc__
        """ modelReset(self) [signal] """
        pass

    def moveColumn(self, QModelIndex, p_int, QModelIndex_1, p_int_1): # real signature unknown; restored from __doc__
        """ moveColumn(self, QModelIndex, int, QModelIndex, int) -> bool """
        return False

    def moveColumns(self, QModelIndex, p_int, p_int_1, QModelIndex_1, p_int_2): # real signature unknown; restored from __doc__
        """ moveColumns(self, QModelIndex, int, int, QModelIndex, int) -> bool """
        return False

    def moveRow(self, QModelIndex, p_int, QModelIndex_1, p_int_1): # real signature unknown; restored from __doc__
        """ moveRow(self, QModelIndex, int, QModelIndex, int) -> bool """
        return False

    def moveRows(self, QModelIndex, p_int, p_int_1, QModelIndex_1, p_int_2): # real signature unknown; restored from __doc__
        """ moveRows(self, QModelIndex, int, int, QModelIndex, int) -> bool """
        return False

    def parent(self, QModelIndex=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        parent(self, QModelIndex) -> QModelIndex
        parent(self) -> QObject
        """
        return QModelIndex or QObject

    def persistentIndexList(self): # real signature unknown; restored from __doc__
        """ persistentIndexList(self) -> object """
        return object()

    def removeColumn(self, p_int, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ removeColumn(self, int, parent: QModelIndex = QModelIndex()) -> bool """
        pass

    def removeColumns(self, p_int, p_int_1, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ removeColumns(self, int, int, parent: QModelIndex = QModelIndex()) -> bool """
        pass

    def removeRow(self, p_int, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ removeRow(self, int, parent: QModelIndex = QModelIndex()) -> bool """
        pass

    def removeRows(self, p_int, p_int_1, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ removeRows(self, int, int, parent: QModelIndex = QModelIndex()) -> bool """
        pass

    def resetInternalData(self): # real signature unknown; restored from __doc__
        """ resetInternalData(self) """
        pass

    def revert(self): # real signature unknown; restored from __doc__
        """ revert(self) """
        pass

    def roleNames(self): # real signature unknown; restored from __doc__
        """ roleNames(self) -> object """
        return object()

    def rowCount(self, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ rowCount(self, parent: QModelIndex = QModelIndex()) -> int """
        pass

    def rowsAboutToBeInserted(self, QModelIndex, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ rowsAboutToBeInserted(self, QModelIndex, int, int) [signal] """
        pass

    def rowsAboutToBeMoved(self, QModelIndex, p_int, p_int_1, QModelIndex_1, p_int_2): # real signature unknown; restored from __doc__
        """ rowsAboutToBeMoved(self, QModelIndex, int, int, QModelIndex, int) [signal] """
        pass

    def rowsAboutToBeRemoved(self, QModelIndex, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ rowsAboutToBeRemoved(self, QModelIndex, int, int) [signal] """
        pass

    def rowsInserted(self, QModelIndex, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ rowsInserted(self, QModelIndex, int, int) [signal] """
        pass

    def rowsMoved(self, QModelIndex, p_int, p_int_1, QModelIndex_1, p_int_2): # real signature unknown; restored from __doc__
        """ rowsMoved(self, QModelIndex, int, int, QModelIndex, int) [signal] """
        pass

    def rowsRemoved(self, QModelIndex, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ rowsRemoved(self, QModelIndex, int, int) [signal] """
        pass

    def setData(self, QModelIndex, Any, role=None): # real signature unknown; restored from __doc__
        """ setData(self, QModelIndex, Any, role: int = Qt.EditRole) -> bool """
        return False

    def setHeaderData(self, p_int, Qt_Orientation, Any, role=None): # real signature unknown; restored from __doc__
        """ setHeaderData(self, int, Qt.Orientation, Any, role: int = Qt.EditRole) -> bool """
        return False

    def setItemData(self, QModelIndex, Dict, p_int=None, Any=None): # real signature unknown; restored from __doc__
        """ setItemData(self, QModelIndex, Dict[int, Any]) -> bool """
        return False

    def sibling(self, p_int, p_int_1, QModelIndex): # real signature unknown; restored from __doc__
        """ sibling(self, int, int, QModelIndex) -> QModelIndex """
        return QModelIndex

    def sort(self, p_int, order=None): # real signature unknown; restored from __doc__
        """ sort(self, int, order: Qt.SortOrder = Qt.AscendingOrder) """
        pass

    def span(self, QModelIndex): # real signature unknown; restored from __doc__
        """ span(self, QModelIndex) -> QSize """
        return QSize

    def submit(self): # real signature unknown; restored from __doc__
        """ submit(self) -> bool """
        return False

    def supportedDragActions(self): # real signature unknown; restored from __doc__
        """ supportedDragActions(self) -> Qt.DropActions """
        pass

    def supportedDropActions(self): # real signature unknown; restored from __doc__
        """ supportedDropActions(self) -> Qt.DropActions """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass

    HorizontalSortHint = 2
    NoLayoutChangeHint = 0
    VerticalSortHint = 1


