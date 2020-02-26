# encoding: utf-8
# module PyQt5.QtWidgets
# from /usr/lib/python3/dist-packages/PyQt5/QtWidgets.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui


class QDirModel(__PyQt5_QtCore.QAbstractItemModel):
    """
    QDirModel(Iterable[str], Union[QDir.Filters, QDir.Filter], Union[QDir.SortFlags, QDir.SortFlag], parent: QObject = None)
    QDirModel(parent: QObject = None)
    """
    def columnCount(self, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ columnCount(self, parent: QModelIndex = QModelIndex()) -> int """
        pass

    def data(self, QModelIndex, role=None): # real signature unknown; restored from __doc__
        """ data(self, QModelIndex, role: int = Qt.DisplayRole) -> Any """
        pass

    def dropMimeData(self, QMimeData, Qt_DropAction, p_int, p_int_1, QModelIndex): # real signature unknown; restored from __doc__
        """ dropMimeData(self, QMimeData, Qt.DropAction, int, int, QModelIndex) -> bool """
        return False

    def fileIcon(self, QModelIndex): # real signature unknown; restored from __doc__
        """ fileIcon(self, QModelIndex) -> QIcon """
        pass

    def fileInfo(self, QModelIndex): # real signature unknown; restored from __doc__
        """ fileInfo(self, QModelIndex) -> QFileInfo """
        pass

    def fileName(self, QModelIndex): # real signature unknown; restored from __doc__
        """ fileName(self, QModelIndex) -> str """
        return ""

    def filePath(self, QModelIndex): # real signature unknown; restored from __doc__
        """ filePath(self, QModelIndex) -> str """
        return ""

    def filter(self): # real signature unknown; restored from __doc__
        """ filter(self) -> QDir.Filters """
        pass

    def flags(self, QModelIndex): # real signature unknown; restored from __doc__
        """ flags(self, QModelIndex) -> Qt.ItemFlags """
        pass

    def hasChildren(self, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ hasChildren(self, parent: QModelIndex = QModelIndex()) -> bool """
        pass

    def headerData(self, p_int, Qt_Orientation, role=None): # real signature unknown; restored from __doc__
        """ headerData(self, int, Qt.Orientation, role: int = Qt.DisplayRole) -> Any """
        pass

    def iconProvider(self): # real signature unknown; restored from __doc__
        """ iconProvider(self) -> QFileIconProvider """
        return QFileIconProvider

    def index(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        index(self, int, int, parent: QModelIndex = QModelIndex()) -> QModelIndex
        index(self, str, column: int = 0) -> QModelIndex
        """
        pass

    def isDir(self, QModelIndex): # real signature unknown; restored from __doc__
        """ isDir(self, QModelIndex) -> bool """
        return False

    def isReadOnly(self): # real signature unknown; restored from __doc__
        """ isReadOnly(self) -> bool """
        return False

    def lazyChildCount(self): # real signature unknown; restored from __doc__
        """ lazyChildCount(self) -> bool """
        return False

    def mimeData(self, p_object): # real signature unknown; restored from __doc__
        """ mimeData(self, object) -> QMimeData """
        pass

    def mimeTypes(self): # real signature unknown; restored from __doc__
        """ mimeTypes(self) -> List[str] """
        return []

    def mkdir(self, QModelIndex, p_str): # real signature unknown; restored from __doc__
        """ mkdir(self, QModelIndex, str) -> QModelIndex """
        pass

    def nameFilters(self): # real signature unknown; restored from __doc__
        """ nameFilters(self) -> List[str] """
        return []

    def parent(self, QModelIndex=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        parent(self, QModelIndex) -> QModelIndex
        parent(self) -> QObject
        """
        pass

    def refresh(self, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ refresh(self, parent: QModelIndex = QModelIndex()) """
        pass

    def remove(self, QModelIndex): # real signature unknown; restored from __doc__
        """ remove(self, QModelIndex) -> bool """
        return False

    def resolveSymlinks(self): # real signature unknown; restored from __doc__
        """ resolveSymlinks(self) -> bool """
        return False

    def rmdir(self, QModelIndex): # real signature unknown; restored from __doc__
        """ rmdir(self, QModelIndex) -> bool """
        return False

    def rowCount(self, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ rowCount(self, parent: QModelIndex = QModelIndex()) -> int """
        pass

    def setData(self, QModelIndex, Any, role=None): # real signature unknown; restored from __doc__
        """ setData(self, QModelIndex, Any, role: int = Qt.EditRole) -> bool """
        return False

    def setFilter(self, Union, QDir_Filters=None, QDir_Filter=None): # real signature unknown; restored from __doc__
        """ setFilter(self, Union[QDir.Filters, QDir.Filter]) """
        pass

    def setIconProvider(self, QFileIconProvider): # real signature unknown; restored from __doc__
        """ setIconProvider(self, QFileIconProvider) """
        pass

    def setLazyChildCount(self, bool): # real signature unknown; restored from __doc__
        """ setLazyChildCount(self, bool) """
        pass

    def setNameFilters(self, Iterable, p_str=None): # real signature unknown; restored from __doc__
        """ setNameFilters(self, Iterable[str]) """
        pass

    def setReadOnly(self, bool): # real signature unknown; restored from __doc__
        """ setReadOnly(self, bool) """
        pass

    def setResolveSymlinks(self, bool): # real signature unknown; restored from __doc__
        """ setResolveSymlinks(self, bool) """
        pass

    def setSorting(self, Union, QDir_SortFlags=None, QDir_SortFlag=None): # real signature unknown; restored from __doc__
        """ setSorting(self, Union[QDir.SortFlags, QDir.SortFlag]) """
        pass

    def sort(self, p_int, order=None): # real signature unknown; restored from __doc__
        """ sort(self, int, order: Qt.SortOrder = Qt.AscendingOrder) """
        pass

    def sorting(self): # real signature unknown; restored from __doc__
        """ sorting(self) -> QDir.SortFlags """
        pass

    def supportedDropActions(self): # real signature unknown; restored from __doc__
        """ supportedDropActions(self) -> Qt.DropActions """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    FileIconRole = 1
    FileNameRole = 258
    FilePathRole = 257


