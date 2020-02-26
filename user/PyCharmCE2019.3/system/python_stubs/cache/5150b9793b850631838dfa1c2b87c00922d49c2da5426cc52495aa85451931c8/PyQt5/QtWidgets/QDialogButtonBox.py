# encoding: utf-8
# module PyQt5.QtWidgets
# from /usr/lib/python3/dist-packages/PyQt5/QtWidgets.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui


from .QWidget import QWidget

class QDialogButtonBox(QWidget):
    """
    QDialogButtonBox(parent: QWidget = None)
    QDialogButtonBox(Qt.Orientation, parent: QWidget = None)
    QDialogButtonBox(Union[QDialogButtonBox.StandardButtons, QDialogButtonBox.StandardButton], parent: QWidget = None)
    QDialogButtonBox(Union[QDialogButtonBox.StandardButtons, QDialogButtonBox.StandardButton], Qt.Orientation, parent: QWidget = None)
    """
    def accepted(self): # real signature unknown; restored from __doc__
        """ accepted(self) [signal] """
        pass

    def addButton(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addButton(self, QAbstractButton, QDialogButtonBox.ButtonRole)
        addButton(self, str, QDialogButtonBox.ButtonRole) -> QPushButton
        addButton(self, QDialogButtonBox.StandardButton) -> QPushButton
        """
        return QPushButton

    def button(self, QDialogButtonBox_StandardButton): # real signature unknown; restored from __doc__
        """ button(self, QDialogButtonBox.StandardButton) -> QPushButton """
        return QPushButton

    def buttonRole(self, QAbstractButton): # real signature unknown; restored from __doc__
        """ buttonRole(self, QAbstractButton) -> QDialogButtonBox.ButtonRole """
        pass

    def buttons(self): # real signature unknown; restored from __doc__
        """ buttons(self) -> List[QAbstractButton] """
        return []

    def centerButtons(self): # real signature unknown; restored from __doc__
        """ centerButtons(self) -> bool """
        return False

    def changeEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ changeEvent(self, QEvent) """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def clicked(self, QAbstractButton): # real signature unknown; restored from __doc__
        """ clicked(self, QAbstractButton) [signal] """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def helpRequested(self): # real signature unknown; restored from __doc__
        """ helpRequested(self) [signal] """
        pass

    def orientation(self): # real signature unknown; restored from __doc__
        """ orientation(self) -> Qt.Orientation """
        pass

    def rejected(self): # real signature unknown; restored from __doc__
        """ rejected(self) [signal] """
        pass

    def removeButton(self, QAbstractButton): # real signature unknown; restored from __doc__
        """ removeButton(self, QAbstractButton) """
        pass

    def setCenterButtons(self, bool): # real signature unknown; restored from __doc__
        """ setCenterButtons(self, bool) """
        pass

    def setOrientation(self, Qt_Orientation): # real signature unknown; restored from __doc__
        """ setOrientation(self, Qt.Orientation) """
        pass

    def setStandardButtons(self, Union, QDialogButtonBox_StandardButtons=None, QDialogButtonBox_StandardButton=None): # real signature unknown; restored from __doc__
        """ setStandardButtons(self, Union[QDialogButtonBox.StandardButtons, QDialogButtonBox.StandardButton]) """
        pass

    def standardButton(self, QAbstractButton): # real signature unknown; restored from __doc__
        """ standardButton(self, QAbstractButton) -> QDialogButtonBox.StandardButton """
        pass

    def standardButtons(self): # real signature unknown; restored from __doc__
        """ standardButtons(self) -> QDialogButtonBox.StandardButtons """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    Abort = 262144
    AcceptRole = 0
    ActionRole = 3
    Apply = 33554432
    ApplyRole = 8
    Cancel = 4194304
    Close = 2097152
    DestructiveRole = 2
    Discard = 8388608
    GnomeLayout = 3
    Help = 16777216
    HelpRole = 4
    Ignore = 1048576
    InvalidRole = -1
    KdeLayout = 2
    MacLayout = 1
    No = 65536
    NoButton = 0
    NoRole = 6
    NoToAll = 131072
    Ok = 1024
    Open = 8192
    RejectRole = 1
    Reset = 67108864
    ResetRole = 7
    RestoreDefaults = 134217728
    Retry = 524288
    Save = 2048
    SaveAll = 4096
    WinLayout = 0
    Yes = 16384
    YesRole = 5
    YesToAll = 32768


