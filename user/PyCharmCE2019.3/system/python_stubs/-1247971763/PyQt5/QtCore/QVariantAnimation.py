# encoding: utf-8
# module PyQt5.QtCore
# from /usr/lib/python3/dist-packages/PyQt5/QtCore.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc
# no imports

from .QAbstractAnimation import QAbstractAnimation

class QVariantAnimation(QAbstractAnimation):
    """ QVariantAnimation(parent: QObject = None) """
    def currentValue(self): # real signature unknown; restored from __doc__
        """ currentValue(self) -> Any """
        pass

    def duration(self): # real signature unknown; restored from __doc__
        """ duration(self) -> int """
        return 0

    def easingCurve(self): # real signature unknown; restored from __doc__
        """ easingCurve(self) -> QEasingCurve """
        return QEasingCurve

    def endValue(self): # real signature unknown; restored from __doc__
        """ endValue(self) -> Any """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def interpolated(self, Any, Any_1, p_float): # real signature unknown; restored from __doc__
        """ interpolated(self, Any, Any, float) -> Any """
        pass

    def keyValueAt(self, p_float): # real signature unknown; restored from __doc__
        """ keyValueAt(self, float) -> Any """
        pass

    def keyValues(self): # real signature unknown; restored from __doc__
        """ keyValues(self) -> object """
        return object()

    def setDuration(self, p_int): # real signature unknown; restored from __doc__
        """ setDuration(self, int) """
        pass

    def setEasingCurve(self, Union, QEasingCurve=None, QEasingCurve_Type=None): # real signature unknown; restored from __doc__
        """ setEasingCurve(self, Union[QEasingCurve, QEasingCurve.Type]) """
        pass

    def setEndValue(self, Any): # real signature unknown; restored from __doc__
        """ setEndValue(self, Any) """
        pass

    def setKeyValueAt(self, p_float, Any): # real signature unknown; restored from __doc__
        """ setKeyValueAt(self, float, Any) """
        pass

    def setKeyValues(self, p_object): # real signature unknown; restored from __doc__
        """ setKeyValues(self, object) """
        pass

    def setStartValue(self, Any): # real signature unknown; restored from __doc__
        """ setStartValue(self, Any) """
        pass

    def startValue(self): # real signature unknown; restored from __doc__
        """ startValue(self) -> Any """
        pass

    def updateCurrentTime(self, p_int): # real signature unknown; restored from __doc__
        """ updateCurrentTime(self, int) """
        pass

    def updateCurrentValue(self, Any): # real signature unknown; restored from __doc__
        """ updateCurrentValue(self, Any) """
        pass

    def updateState(self, QAbstractAnimation_State, QAbstractAnimation_State_1): # real signature unknown; restored from __doc__
        """ updateState(self, QAbstractAnimation.State, QAbstractAnimation.State) """
        pass

    def valueChanged(self, Any): # real signature unknown; restored from __doc__
        """ valueChanged(self, Any) [signal] """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


