# encoding: utf-8
# module PyQt5.QtWidgets
# from /usr/lib/python3/dist-packages/PyQt5/QtWidgets.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui


from .QWidget import QWidget

class QComboBox(QWidget):
    """ QComboBox(parent: QWidget = None) """
    def activated(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        activated(self, int) [signal]
        activated(self, str) [signal]
        """
        pass

    def addItem(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addItem(self, str, userData: Any = None)
        addItem(self, QIcon, str, userData: Any = None)
        """
        pass

    def addItems(self, Iterable, p_str=None): # real signature unknown; restored from __doc__
        """ addItems(self, Iterable[str]) """
        pass

    def changeEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ changeEvent(self, QEvent) """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def clearEditText(self): # real signature unknown; restored from __doc__
        """ clearEditText(self) """
        pass

    def completer(self): # real signature unknown; restored from __doc__
        """ completer(self) -> QCompleter """
        return QCompleter

    def contextMenuEvent(self, QContextMenuEvent): # real signature unknown; restored from __doc__
        """ contextMenuEvent(self, QContextMenuEvent) """
        pass

    def count(self): # real signature unknown; restored from __doc__
        """ count(self) -> int """
        return 0

    def currentData(self, role=None): # real signature unknown; restored from __doc__
        """ currentData(self, role: int = Qt.UserRole) -> Any """
        pass

    def currentIndex(self): # real signature unknown; restored from __doc__
        """ currentIndex(self) -> int """
        return 0

    def currentIndexChanged(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        currentIndexChanged(self, int) [signal]
        currentIndexChanged(self, str) [signal]
        """
        pass

    def currentText(self): # real signature unknown; restored from __doc__
        """ currentText(self) -> str """
        return ""

    def currentTextChanged(self, p_str): # real signature unknown; restored from __doc__
        """ currentTextChanged(self, str) [signal] """
        pass

    def duplicatesEnabled(self): # real signature unknown; restored from __doc__
        """ duplicatesEnabled(self) -> bool """
        return False

    def editTextChanged(self, p_str): # real signature unknown; restored from __doc__
        """ editTextChanged(self, str) [signal] """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def findData(self, Any, role=None, flags, Qt_MatchFlags=None, Qt_MatchFlag=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ findData(self, Any, role: int = Qt.UserRole, flags: Union[Qt.MatchFlags, Qt.MatchFlag] = Qt.MatchExactly|Qt.MatchCaseSensitive) -> int """
        pass

    def findText(self, p_str, flags, Qt_MatchFlags=None, Qt_MatchFlag=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ findText(self, str, flags: Union[Qt.MatchFlags, Qt.MatchFlag] = Qt.MatchExactly|Qt.MatchCaseSensitive) -> int """
        pass

    def focusInEvent(self, QFocusEvent): # real signature unknown; restored from __doc__
        """ focusInEvent(self, QFocusEvent) """
        pass

    def focusOutEvent(self, QFocusEvent): # real signature unknown; restored from __doc__
        """ focusOutEvent(self, QFocusEvent) """
        pass

    def hasFrame(self): # real signature unknown; restored from __doc__
        """ hasFrame(self) -> bool """
        return False

    def hideEvent(self, QHideEvent): # real signature unknown; restored from __doc__
        """ hideEvent(self, QHideEvent) """
        pass

    def hidePopup(self): # real signature unknown; restored from __doc__
        """ hidePopup(self) """
        pass

    def highlighted(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        highlighted(self, int) [signal]
        highlighted(self, str) [signal]
        """
        pass

    def iconSize(self): # real signature unknown; restored from __doc__
        """ iconSize(self) -> QSize """
        pass

    def initStyleOption(self, QStyleOptionComboBox): # real signature unknown; restored from __doc__
        """ initStyleOption(self, QStyleOptionComboBox) """
        pass

    def inputMethodEvent(self, QInputMethodEvent): # real signature unknown; restored from __doc__
        """ inputMethodEvent(self, QInputMethodEvent) """
        pass

    def inputMethodQuery(self, Qt_InputMethodQuery, Any=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        inputMethodQuery(self, Qt.InputMethodQuery) -> Any
        inputMethodQuery(self, Qt.InputMethodQuery, Any) -> Any
        """
        pass

    def insertItem(self, p_int, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        insertItem(self, int, str, userData: Any = None)
        insertItem(self, int, QIcon, str, userData: Any = None)
        """
        pass

    def insertItems(self, p_int, Iterable, p_str=None): # real signature unknown; restored from __doc__
        """ insertItems(self, int, Iterable[str]) """
        pass

    def insertPolicy(self): # real signature unknown; restored from __doc__
        """ insertPolicy(self) -> QComboBox.InsertPolicy """
        pass

    def insertSeparator(self, p_int): # real signature unknown; restored from __doc__
        """ insertSeparator(self, int) """
        pass

    def isEditable(self): # real signature unknown; restored from __doc__
        """ isEditable(self) -> bool """
        return False

    def itemData(self, p_int, role=None): # real signature unknown; restored from __doc__
        """ itemData(self, int, role: int = Qt.UserRole) -> Any """
        pass

    def itemDelegate(self): # real signature unknown; restored from __doc__
        """ itemDelegate(self) -> QAbstractItemDelegate """
        return QAbstractItemDelegate

    def itemIcon(self, p_int): # real signature unknown; restored from __doc__
        """ itemIcon(self, int) -> QIcon """
        pass

    def itemText(self, p_int): # real signature unknown; restored from __doc__
        """ itemText(self, int) -> str """
        return ""

    def keyPressEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, QKeyEvent) """
        pass

    def keyReleaseEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ keyReleaseEvent(self, QKeyEvent) """
        pass

    def lineEdit(self): # real signature unknown; restored from __doc__
        """ lineEdit(self) -> QLineEdit """
        return QLineEdit

    def maxCount(self): # real signature unknown; restored from __doc__
        """ maxCount(self) -> int """
        return 0

    def maxVisibleItems(self): # real signature unknown; restored from __doc__
        """ maxVisibleItems(self) -> int """
        return 0

    def minimumContentsLength(self): # real signature unknown; restored from __doc__
        """ minimumContentsLength(self) -> int """
        return 0

    def minimumSizeHint(self): # real signature unknown; restored from __doc__
        """ minimumSizeHint(self) -> QSize """
        pass

    def model(self): # real signature unknown; restored from __doc__
        """ model(self) -> QAbstractItemModel """
        pass

    def modelColumn(self): # real signature unknown; restored from __doc__
        """ modelColumn(self) -> int """
        return 0

    def mousePressEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ mousePressEvent(self, QMouseEvent) """
        pass

    def mouseReleaseEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ mouseReleaseEvent(self, QMouseEvent) """
        pass

    def paintEvent(self, QPaintEvent): # real signature unknown; restored from __doc__
        """ paintEvent(self, QPaintEvent) """
        pass

    def removeItem(self, p_int): # real signature unknown; restored from __doc__
        """ removeItem(self, int) """
        pass

    def resizeEvent(self, QResizeEvent): # real signature unknown; restored from __doc__
        """ resizeEvent(self, QResizeEvent) """
        pass

    def rootModelIndex(self): # real signature unknown; restored from __doc__
        """ rootModelIndex(self) -> QModelIndex """
        pass

    def setCompleter(self, QCompleter): # real signature unknown; restored from __doc__
        """ setCompleter(self, QCompleter) """
        pass

    def setCurrentIndex(self, p_int): # real signature unknown; restored from __doc__
        """ setCurrentIndex(self, int) """
        pass

    def setCurrentText(self, p_str): # real signature unknown; restored from __doc__
        """ setCurrentText(self, str) """
        pass

    def setDuplicatesEnabled(self, bool): # real signature unknown; restored from __doc__
        """ setDuplicatesEnabled(self, bool) """
        pass

    def setEditable(self, bool): # real signature unknown; restored from __doc__
        """ setEditable(self, bool) """
        pass

    def setEditText(self, p_str): # real signature unknown; restored from __doc__
        """ setEditText(self, str) """
        pass

    def setFrame(self, bool): # real signature unknown; restored from __doc__
        """ setFrame(self, bool) """
        pass

    def setIconSize(self, QSize): # real signature unknown; restored from __doc__
        """ setIconSize(self, QSize) """
        pass

    def setInsertPolicy(self, QComboBox_InsertPolicy): # real signature unknown; restored from __doc__
        """ setInsertPolicy(self, QComboBox.InsertPolicy) """
        pass

    def setItemData(self, p_int, Any, role=None): # real signature unknown; restored from __doc__
        """ setItemData(self, int, Any, role: int = Qt.UserRole) """
        pass

    def setItemDelegate(self, QAbstractItemDelegate): # real signature unknown; restored from __doc__
        """ setItemDelegate(self, QAbstractItemDelegate) """
        pass

    def setItemIcon(self, p_int, QIcon): # real signature unknown; restored from __doc__
        """ setItemIcon(self, int, QIcon) """
        pass

    def setItemText(self, p_int, p_str): # real signature unknown; restored from __doc__
        """ setItemText(self, int, str) """
        pass

    def setLineEdit(self, QLineEdit): # real signature unknown; restored from __doc__
        """ setLineEdit(self, QLineEdit) """
        pass

    def setMaxCount(self, p_int): # real signature unknown; restored from __doc__
        """ setMaxCount(self, int) """
        pass

    def setMaxVisibleItems(self, p_int): # real signature unknown; restored from __doc__
        """ setMaxVisibleItems(self, int) """
        pass

    def setMinimumContentsLength(self, p_int): # real signature unknown; restored from __doc__
        """ setMinimumContentsLength(self, int) """
        pass

    def setModel(self, QAbstractItemModel): # real signature unknown; restored from __doc__
        """ setModel(self, QAbstractItemModel) """
        pass

    def setModelColumn(self, p_int): # real signature unknown; restored from __doc__
        """ setModelColumn(self, int) """
        pass

    def setRootModelIndex(self, QModelIndex): # real signature unknown; restored from __doc__
        """ setRootModelIndex(self, QModelIndex) """
        pass

    def setSizeAdjustPolicy(self, QComboBox_SizeAdjustPolicy): # real signature unknown; restored from __doc__
        """ setSizeAdjustPolicy(self, QComboBox.SizeAdjustPolicy) """
        pass

    def setValidator(self, QValidator): # real signature unknown; restored from __doc__
        """ setValidator(self, QValidator) """
        pass

    def setView(self, QAbstractItemView): # real signature unknown; restored from __doc__
        """ setView(self, QAbstractItemView) """
        pass

    def showEvent(self, QShowEvent): # real signature unknown; restored from __doc__
        """ showEvent(self, QShowEvent) """
        pass

    def showPopup(self): # real signature unknown; restored from __doc__
        """ showPopup(self) """
        pass

    def sizeAdjustPolicy(self): # real signature unknown; restored from __doc__
        """ sizeAdjustPolicy(self) -> QComboBox.SizeAdjustPolicy """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> QSize """
        pass

    def validator(self): # real signature unknown; restored from __doc__
        """ validator(self) -> QValidator """
        pass

    def view(self): # real signature unknown; restored from __doc__
        """ view(self) -> QAbstractItemView """
        return QAbstractItemView

    def wheelEvent(self, QWheelEvent): # real signature unknown; restored from __doc__
        """ wheelEvent(self, QWheelEvent) """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    AdjustToContents = 0
    AdjustToContentsOnFirstShow = 1
    AdjustToMinimumContentsLength = 2
    AdjustToMinimumContentsLengthWithIcon = 3
    InsertAfterCurrent = 4
    InsertAlphabetically = 6
    InsertAtBottom = 3
    InsertAtCurrent = 2
    InsertAtTop = 1
    InsertBeforeCurrent = 5
    NoInsert = 0


