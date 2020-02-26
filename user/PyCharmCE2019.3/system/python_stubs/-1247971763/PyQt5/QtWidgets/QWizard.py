# encoding: utf-8
# module PyQt5.QtWidgets
# from /usr/lib/python3/dist-packages/PyQt5/QtWidgets.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui


from .QDialog import QDialog

class QWizard(QDialog):
    """ QWizard(parent: QWidget = None, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags()) """
    def addPage(self, QWizardPage): # real signature unknown; restored from __doc__
        """ addPage(self, QWizardPage) -> int """
        return 0

    def back(self): # real signature unknown; restored from __doc__
        """ back(self) """
        pass

    def button(self, QWizard_WizardButton): # real signature unknown; restored from __doc__
        """ button(self, QWizard.WizardButton) -> QAbstractButton """
        return QAbstractButton

    def buttonText(self, QWizard_WizardButton): # real signature unknown; restored from __doc__
        """ buttonText(self, QWizard.WizardButton) -> str """
        return ""

    def cleanupPage(self, p_int): # real signature unknown; restored from __doc__
        """ cleanupPage(self, int) """
        pass

    def currentId(self): # real signature unknown; restored from __doc__
        """ currentId(self) -> int """
        return 0

    def currentIdChanged(self, p_int): # real signature unknown; restored from __doc__
        """ currentIdChanged(self, int) [signal] """
        pass

    def currentPage(self): # real signature unknown; restored from __doc__
        """ currentPage(self) -> QWizardPage """
        return QWizardPage

    def customButtonClicked(self, p_int): # real signature unknown; restored from __doc__
        """ customButtonClicked(self, int) [signal] """
        pass

    def done(self, p_int): # real signature unknown; restored from __doc__
        """ done(self, int) """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def field(self, p_str): # real signature unknown; restored from __doc__
        """ field(self, str) -> Any """
        pass

    def hasVisitedPage(self, p_int): # real signature unknown; restored from __doc__
        """ hasVisitedPage(self, int) -> bool """
        return False

    def helpRequested(self): # real signature unknown; restored from __doc__
        """ helpRequested(self) [signal] """
        pass

    def initializePage(self, p_int): # real signature unknown; restored from __doc__
        """ initializePage(self, int) """
        pass

    def next(self): # real signature unknown; restored from __doc__
        """ next(self) """
        pass

    def nextId(self): # real signature unknown; restored from __doc__
        """ nextId(self) -> int """
        return 0

    def options(self): # real signature unknown; restored from __doc__
        """ options(self) -> QWizard.WizardOptions """
        pass

    def page(self, p_int): # real signature unknown; restored from __doc__
        """ page(self, int) -> QWizardPage """
        return QWizardPage

    def pageAdded(self, p_int): # real signature unknown; restored from __doc__
        """ pageAdded(self, int) [signal] """
        pass

    def pageIds(self): # real signature unknown; restored from __doc__
        """ pageIds(self) -> List[int] """
        return []

    def pageRemoved(self, p_int): # real signature unknown; restored from __doc__
        """ pageRemoved(self, int) [signal] """
        pass

    def paintEvent(self, QPaintEvent): # real signature unknown; restored from __doc__
        """ paintEvent(self, QPaintEvent) """
        pass

    def pixmap(self, QWizard_WizardPixmap): # real signature unknown; restored from __doc__
        """ pixmap(self, QWizard.WizardPixmap) -> QPixmap """
        pass

    def removePage(self, p_int): # real signature unknown; restored from __doc__
        """ removePage(self, int) """
        pass

    def resizeEvent(self, QResizeEvent): # real signature unknown; restored from __doc__
        """ resizeEvent(self, QResizeEvent) """
        pass

    def restart(self): # real signature unknown; restored from __doc__
        """ restart(self) """
        pass

    def setButton(self, QWizard_WizardButton, QAbstractButton): # real signature unknown; restored from __doc__
        """ setButton(self, QWizard.WizardButton, QAbstractButton) """
        pass

    def setButtonLayout(self, Iterable, QWizard_WizardButton=None): # real signature unknown; restored from __doc__
        """ setButtonLayout(self, Iterable[QWizard.WizardButton]) """
        pass

    def setButtonText(self, QWizard_WizardButton, p_str): # real signature unknown; restored from __doc__
        """ setButtonText(self, QWizard.WizardButton, str) """
        pass

    def setDefaultProperty(self, p_str, p_str_1, PYQT_SIGNAL): # real signature unknown; restored from __doc__
        """ setDefaultProperty(self, str, str, PYQT_SIGNAL) """
        pass

    def setField(self, p_str, Any): # real signature unknown; restored from __doc__
        """ setField(self, str, Any) """
        pass

    def setOption(self, QWizard_WizardOption, on=True): # real signature unknown; restored from __doc__
        """ setOption(self, QWizard.WizardOption, on: bool = True) """
        pass

    def setOptions(self, Union, QWizard_WizardOptions=None, QWizard_WizardOption=None): # real signature unknown; restored from __doc__
        """ setOptions(self, Union[QWizard.WizardOptions, QWizard.WizardOption]) """
        pass

    def setPage(self, p_int, QWizardPage): # real signature unknown; restored from __doc__
        """ setPage(self, int, QWizardPage) """
        pass

    def setPixmap(self, QWizard_WizardPixmap, QPixmap): # real signature unknown; restored from __doc__
        """ setPixmap(self, QWizard.WizardPixmap, QPixmap) """
        pass

    def setSideWidget(self, QWidget): # real signature unknown; restored from __doc__
        """ setSideWidget(self, QWidget) """
        pass

    def setStartId(self, p_int): # real signature unknown; restored from __doc__
        """ setStartId(self, int) """
        pass

    def setSubTitleFormat(self, Qt_TextFormat): # real signature unknown; restored from __doc__
        """ setSubTitleFormat(self, Qt.TextFormat) """
        pass

    def setTitleFormat(self, Qt_TextFormat): # real signature unknown; restored from __doc__
        """ setTitleFormat(self, Qt.TextFormat) """
        pass

    def setVisible(self, bool): # real signature unknown; restored from __doc__
        """ setVisible(self, bool) """
        pass

    def setWizardStyle(self, QWizard_WizardStyle): # real signature unknown; restored from __doc__
        """ setWizardStyle(self, QWizard.WizardStyle) """
        pass

    def sideWidget(self): # real signature unknown; restored from __doc__
        """ sideWidget(self) -> QWidget """
        return QWidget

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> QSize """
        pass

    def startId(self): # real signature unknown; restored from __doc__
        """ startId(self) -> int """
        return 0

    def subTitleFormat(self): # real signature unknown; restored from __doc__
        """ subTitleFormat(self) -> Qt.TextFormat """
        pass

    def testOption(self, QWizard_WizardOption): # real signature unknown; restored from __doc__
        """ testOption(self, QWizard.WizardOption) -> bool """
        return False

    def titleFormat(self): # real signature unknown; restored from __doc__
        """ titleFormat(self) -> Qt.TextFormat """
        pass

    def validateCurrentPage(self): # real signature unknown; restored from __doc__
        """ validateCurrentPage(self) -> bool """
        return False

    def visitedPages(self): # real signature unknown; restored from __doc__
        """ visitedPages(self) -> List[int] """
        return []

    def wizardStyle(self): # real signature unknown; restored from __doc__
        """ wizardStyle(self) -> QWizard.WizardStyle """
        pass

    def __init__(self, parent=None, flags, Qt_WindowFlags=None, Qt_WindowType=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    AeroStyle = 3
    BackButton = 0
    BackgroundPixmap = 3
    BannerPixmap = 2
    CancelButton = 4
    CancelButtonOnLeft = 1024
    ClassicStyle = 0
    CommitButton = 2
    CustomButton1 = 6
    CustomButton2 = 7
    CustomButton3 = 8
    DisabledBackButtonOnLastPage = 64
    ExtendedWatermarkPixmap = 4
    FinishButton = 3
    HaveCustomButton1 = 8192
    HaveCustomButton2 = 16384
    HaveCustomButton3 = 32768
    HaveFinishButtonOnEarlyPages = 256
    HaveHelpButton = 2048
    HaveNextButtonOnLastPage = 128
    HelpButton = 5
    HelpButtonOnRight = 4096
    IgnoreSubTitles = 2
    IndependentPages = 1
    LogoPixmap = 1
    MacStyle = 2
    ModernStyle = 1
    NextButton = 1
    NoBackButtonOnLastPage = 32
    NoBackButtonOnStartPage = 16
    NoCancelButton = 512
    NoCancelButtonOnLastPage = 65536
    NoDefaultButton = 8
    Stretch = 9
    WatermarkPixmap = 0


