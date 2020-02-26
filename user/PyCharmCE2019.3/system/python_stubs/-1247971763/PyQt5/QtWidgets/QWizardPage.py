# encoding: utf-8
# module PyQt5.QtWidgets
# from /usr/lib/python3/dist-packages/PyQt5/QtWidgets.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui


from .QWidget import QWidget

class QWizardPage(QWidget):
    """ QWizardPage(parent: QWidget = None) """
    def buttonText(self, QWizard_WizardButton): # real signature unknown; restored from __doc__
        """ buttonText(self, QWizard.WizardButton) -> str """
        return ""

    def cleanupPage(self): # real signature unknown; restored from __doc__
        """ cleanupPage(self) """
        pass

    def completeChanged(self): # real signature unknown; restored from __doc__
        """ completeChanged(self) [signal] """
        pass

    def field(self, p_str): # real signature unknown; restored from __doc__
        """ field(self, str) -> Any """
        pass

    def initializePage(self): # real signature unknown; restored from __doc__
        """ initializePage(self) """
        pass

    def isCommitPage(self): # real signature unknown; restored from __doc__
        """ isCommitPage(self) -> bool """
        return False

    def isComplete(self): # real signature unknown; restored from __doc__
        """ isComplete(self) -> bool """
        return False

    def isFinalPage(self): # real signature unknown; restored from __doc__
        """ isFinalPage(self) -> bool """
        return False

    def nextId(self): # real signature unknown; restored from __doc__
        """ nextId(self) -> int """
        return 0

    def pixmap(self, QWizard_WizardPixmap): # real signature unknown; restored from __doc__
        """ pixmap(self, QWizard.WizardPixmap) -> QPixmap """
        pass

    def registerField(self, p_str, QWidget, property=None, changedSignal=0): # real signature unknown; restored from __doc__
        """ registerField(self, str, QWidget, property: str = None, changedSignal: PYQT_SIGNAL = 0) """
        pass

    def setButtonText(self, QWizard_WizardButton, p_str): # real signature unknown; restored from __doc__
        """ setButtonText(self, QWizard.WizardButton, str) """
        pass

    def setCommitPage(self, bool): # real signature unknown; restored from __doc__
        """ setCommitPage(self, bool) """
        pass

    def setField(self, p_str, Any): # real signature unknown; restored from __doc__
        """ setField(self, str, Any) """
        pass

    def setFinalPage(self, bool): # real signature unknown; restored from __doc__
        """ setFinalPage(self, bool) """
        pass

    def setPixmap(self, QWizard_WizardPixmap, QPixmap): # real signature unknown; restored from __doc__
        """ setPixmap(self, QWizard.WizardPixmap, QPixmap) """
        pass

    def setSubTitle(self, p_str): # real signature unknown; restored from __doc__
        """ setSubTitle(self, str) """
        pass

    def setTitle(self, p_str): # real signature unknown; restored from __doc__
        """ setTitle(self, str) """
        pass

    def subTitle(self): # real signature unknown; restored from __doc__
        """ subTitle(self) -> str """
        return ""

    def title(self): # real signature unknown; restored from __doc__
        """ title(self) -> str """
        return ""

    def validatePage(self): # real signature unknown; restored from __doc__
        """ validatePage(self) -> bool """
        return False

    def wizard(self): # real signature unknown; restored from __doc__
        """ wizard(self) -> QWizard """
        return QWizard

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


