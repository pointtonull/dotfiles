# encoding: utf-8
# module PyQt5.QtWidgets
# from /usr/lib/python3/dist-packages/PyQt5/QtWidgets.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui


from .QAbstractSpinBox import QAbstractSpinBox

class QDateTimeEdit(QAbstractSpinBox):
    """
    QDateTimeEdit(parent: QWidget = None)
    QDateTimeEdit(Union[QDateTime, datetime.datetime], parent: QWidget = None)
    QDateTimeEdit(Union[QDate, datetime.date], parent: QWidget = None)
    QDateTimeEdit(Union[QTime, datetime.time], parent: QWidget = None)
    """
    def calendarPopup(self): # real signature unknown; restored from __doc__
        """ calendarPopup(self) -> bool """
        return False

    def calendarWidget(self): # real signature unknown; restored from __doc__
        """ calendarWidget(self) -> QCalendarWidget """
        return QCalendarWidget

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def clearMaximumDate(self): # real signature unknown; restored from __doc__
        """ clearMaximumDate(self) """
        pass

    def clearMaximumDateTime(self): # real signature unknown; restored from __doc__
        """ clearMaximumDateTime(self) """
        pass

    def clearMaximumTime(self): # real signature unknown; restored from __doc__
        """ clearMaximumTime(self) """
        pass

    def clearMinimumDate(self): # real signature unknown; restored from __doc__
        """ clearMinimumDate(self) """
        pass

    def clearMinimumDateTime(self): # real signature unknown; restored from __doc__
        """ clearMinimumDateTime(self) """
        pass

    def clearMinimumTime(self): # real signature unknown; restored from __doc__
        """ clearMinimumTime(self) """
        pass

    def currentSection(self): # real signature unknown; restored from __doc__
        """ currentSection(self) -> QDateTimeEdit.Section """
        pass

    def currentSectionIndex(self): # real signature unknown; restored from __doc__
        """ currentSectionIndex(self) -> int """
        return 0

    def date(self): # real signature unknown; restored from __doc__
        """ date(self) -> QDate """
        pass

    def dateChanged(self, Union, QDate=None, datetime_date=None): # real signature unknown; restored from __doc__
        """ dateChanged(self, Union[QDate, datetime.date]) [signal] """
        pass

    def dateTime(self): # real signature unknown; restored from __doc__
        """ dateTime(self) -> QDateTime """
        pass

    def dateTimeChanged(self, Union, QDateTime=None, datetime_datetime=None): # real signature unknown; restored from __doc__
        """ dateTimeChanged(self, Union[QDateTime, datetime.datetime]) [signal] """
        pass

    def dateTimeFromText(self, p_str): # real signature unknown; restored from __doc__
        """ dateTimeFromText(self, str) -> QDateTime """
        pass

    def displayedSections(self): # real signature unknown; restored from __doc__
        """ displayedSections(self) -> QDateTimeEdit.Sections """
        pass

    def displayFormat(self): # real signature unknown; restored from __doc__
        """ displayFormat(self) -> str """
        return ""

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def fixup(self, p_str): # real signature unknown; restored from __doc__
        """ fixup(self, str) -> str """
        return ""

    def focusInEvent(self, QFocusEvent): # real signature unknown; restored from __doc__
        """ focusInEvent(self, QFocusEvent) """
        pass

    def focusNextPrevChild(self, bool): # real signature unknown; restored from __doc__
        """ focusNextPrevChild(self, bool) -> bool """
        return False

    def initStyleOption(self, QStyleOptionSpinBox): # real signature unknown; restored from __doc__
        """ initStyleOption(self, QStyleOptionSpinBox) """
        pass

    def keyPressEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, QKeyEvent) """
        pass

    def maximumDate(self): # real signature unknown; restored from __doc__
        """ maximumDate(self) -> QDate """
        pass

    def maximumDateTime(self): # real signature unknown; restored from __doc__
        """ maximumDateTime(self) -> QDateTime """
        pass

    def maximumTime(self): # real signature unknown; restored from __doc__
        """ maximumTime(self) -> QTime """
        pass

    def minimumDate(self): # real signature unknown; restored from __doc__
        """ minimumDate(self) -> QDate """
        pass

    def minimumDateTime(self): # real signature unknown; restored from __doc__
        """ minimumDateTime(self) -> QDateTime """
        pass

    def minimumTime(self): # real signature unknown; restored from __doc__
        """ minimumTime(self) -> QTime """
        pass

    def mousePressEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ mousePressEvent(self, QMouseEvent) """
        pass

    def paintEvent(self, QPaintEvent): # real signature unknown; restored from __doc__
        """ paintEvent(self, QPaintEvent) """
        pass

    def sectionAt(self, p_int): # real signature unknown; restored from __doc__
        """ sectionAt(self, int) -> QDateTimeEdit.Section """
        pass

    def sectionCount(self): # real signature unknown; restored from __doc__
        """ sectionCount(self) -> int """
        return 0

    def sectionText(self, QDateTimeEdit_Section): # real signature unknown; restored from __doc__
        """ sectionText(self, QDateTimeEdit.Section) -> str """
        return ""

    def setCalendarPopup(self, bool): # real signature unknown; restored from __doc__
        """ setCalendarPopup(self, bool) """
        pass

    def setCalendarWidget(self, QCalendarWidget): # real signature unknown; restored from __doc__
        """ setCalendarWidget(self, QCalendarWidget) """
        pass

    def setCurrentSection(self, QDateTimeEdit_Section): # real signature unknown; restored from __doc__
        """ setCurrentSection(self, QDateTimeEdit.Section) """
        pass

    def setCurrentSectionIndex(self, p_int): # real signature unknown; restored from __doc__
        """ setCurrentSectionIndex(self, int) """
        pass

    def setDate(self, Union, QDate=None, datetime_date=None): # real signature unknown; restored from __doc__
        """ setDate(self, Union[QDate, datetime.date]) """
        pass

    def setDateRange(self, Union, QDate=None, datetime_date=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setDateRange(self, Union[QDate, datetime.date], Union[QDate, datetime.date]) """
        pass

    def setDateTime(self, Union, QDateTime=None, datetime_datetime=None): # real signature unknown; restored from __doc__
        """ setDateTime(self, Union[QDateTime, datetime.datetime]) """
        pass

    def setDateTimeRange(self, Union, QDateTime=None, datetime_datetime=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setDateTimeRange(self, Union[QDateTime, datetime.datetime], Union[QDateTime, datetime.datetime]) """
        pass

    def setDisplayFormat(self, p_str): # real signature unknown; restored from __doc__
        """ setDisplayFormat(self, str) """
        pass

    def setMaximumDate(self, Union, QDate=None, datetime_date=None): # real signature unknown; restored from __doc__
        """ setMaximumDate(self, Union[QDate, datetime.date]) """
        pass

    def setMaximumDateTime(self, Union, QDateTime=None, datetime_datetime=None): # real signature unknown; restored from __doc__
        """ setMaximumDateTime(self, Union[QDateTime, datetime.datetime]) """
        pass

    def setMaximumTime(self, Union, QTime=None, datetime_time=None): # real signature unknown; restored from __doc__
        """ setMaximumTime(self, Union[QTime, datetime.time]) """
        pass

    def setMinimumDate(self, Union, QDate=None, datetime_date=None): # real signature unknown; restored from __doc__
        """ setMinimumDate(self, Union[QDate, datetime.date]) """
        pass

    def setMinimumDateTime(self, Union, QDateTime=None, datetime_datetime=None): # real signature unknown; restored from __doc__
        """ setMinimumDateTime(self, Union[QDateTime, datetime.datetime]) """
        pass

    def setMinimumTime(self, Union, QTime=None, datetime_time=None): # real signature unknown; restored from __doc__
        """ setMinimumTime(self, Union[QTime, datetime.time]) """
        pass

    def setSelectedSection(self, QDateTimeEdit_Section): # real signature unknown; restored from __doc__
        """ setSelectedSection(self, QDateTimeEdit.Section) """
        pass

    def setTime(self, Union, QTime=None, datetime_time=None): # real signature unknown; restored from __doc__
        """ setTime(self, Union[QTime, datetime.time]) """
        pass

    def setTimeRange(self, Union, QTime=None, datetime_time=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setTimeRange(self, Union[QTime, datetime.time], Union[QTime, datetime.time]) """
        pass

    def setTimeSpec(self, Qt_TimeSpec): # real signature unknown; restored from __doc__
        """ setTimeSpec(self, Qt.TimeSpec) """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> QSize """
        pass

    def stepBy(self, p_int): # real signature unknown; restored from __doc__
        """ stepBy(self, int) """
        pass

    def stepEnabled(self): # real signature unknown; restored from __doc__
        """ stepEnabled(self) -> QAbstractSpinBox.StepEnabled """
        pass

    def textFromDateTime(self, Union, QDateTime=None, datetime_datetime=None): # real signature unknown; restored from __doc__
        """ textFromDateTime(self, Union[QDateTime, datetime.datetime]) -> str """
        return ""

    def time(self): # real signature unknown; restored from __doc__
        """ time(self) -> QTime """
        pass

    def timeChanged(self, Union, QTime=None, datetime_time=None): # real signature unknown; restored from __doc__
        """ timeChanged(self, Union[QTime, datetime.time]) [signal] """
        pass

    def timeSpec(self): # real signature unknown; restored from __doc__
        """ timeSpec(self) -> Qt.TimeSpec """
        pass

    def validate(self, p_str, p_int): # real signature unknown; restored from __doc__
        """ validate(self, str, int) -> Tuple[QValidator.State, str, int] """
        pass

    def wheelEvent(self, QWheelEvent): # real signature unknown; restored from __doc__
        """ wheelEvent(self, QWheelEvent) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    AmPmSection = 1
    DateSections_Mask = 1792
    DaySection = 256
    HourSection = 16
    MinuteSection = 8
    MonthSection = 512
    MSecSection = 2
    NoSection = 0
    SecondSection = 4
    TimeSections_Mask = 31
    YearSection = 1024


