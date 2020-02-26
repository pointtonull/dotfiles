# encoding: utf-8
# module PyQt5.QtWidgets
# from /usr/lib/python3/dist-packages/PyQt5/QtWidgets.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui


from .QWidget import QWidget

class QAbstractSlider(QWidget):
    """ QAbstractSlider(parent: QWidget = None) """
    def actionTriggered(self, p_int): # real signature unknown; restored from __doc__
        """ actionTriggered(self, int) [signal] """
        pass

    def changeEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ changeEvent(self, QEvent) """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def hasTracking(self): # real signature unknown; restored from __doc__
        """ hasTracking(self) -> bool """
        return False

    def invertedAppearance(self): # real signature unknown; restored from __doc__
        """ invertedAppearance(self) -> bool """
        return False

    def invertedControls(self): # real signature unknown; restored from __doc__
        """ invertedControls(self) -> bool """
        return False

    def isSliderDown(self): # real signature unknown; restored from __doc__
        """ isSliderDown(self) -> bool """
        return False

    def keyPressEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, QKeyEvent) """
        pass

    def maximum(self): # real signature unknown; restored from __doc__
        """ maximum(self) -> int """
        return 0

    def minimum(self): # real signature unknown; restored from __doc__
        """ minimum(self) -> int """
        return 0

    def orientation(self): # real signature unknown; restored from __doc__
        """ orientation(self) -> Qt.Orientation """
        pass

    def pageStep(self): # real signature unknown; restored from __doc__
        """ pageStep(self) -> int """
        return 0

    def rangeChanged(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ rangeChanged(self, int, int) [signal] """
        pass

    def repeatAction(self): # real signature unknown; restored from __doc__
        """ repeatAction(self) -> QAbstractSlider.SliderAction """
        pass

    def setInvertedAppearance(self, bool): # real signature unknown; restored from __doc__
        """ setInvertedAppearance(self, bool) """
        pass

    def setInvertedControls(self, bool): # real signature unknown; restored from __doc__
        """ setInvertedControls(self, bool) """
        pass

    def setMaximum(self, p_int): # real signature unknown; restored from __doc__
        """ setMaximum(self, int) """
        pass

    def setMinimum(self, p_int): # real signature unknown; restored from __doc__
        """ setMinimum(self, int) """
        pass

    def setOrientation(self, Qt_Orientation): # real signature unknown; restored from __doc__
        """ setOrientation(self, Qt.Orientation) """
        pass

    def setPageStep(self, p_int): # real signature unknown; restored from __doc__
        """ setPageStep(self, int) """
        pass

    def setRange(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ setRange(self, int, int) """
        pass

    def setRepeatAction(self, QAbstractSlider_SliderAction, thresholdTime=500, repeatTime=50): # real signature unknown; restored from __doc__
        """ setRepeatAction(self, QAbstractSlider.SliderAction, thresholdTime: int = 500, repeatTime: int = 50) """
        pass

    def setSingleStep(self, p_int): # real signature unknown; restored from __doc__
        """ setSingleStep(self, int) """
        pass

    def setSliderDown(self, bool): # real signature unknown; restored from __doc__
        """ setSliderDown(self, bool) """
        pass

    def setSliderPosition(self, p_int): # real signature unknown; restored from __doc__
        """ setSliderPosition(self, int) """
        pass

    def setTracking(self, bool): # real signature unknown; restored from __doc__
        """ setTracking(self, bool) """
        pass

    def setValue(self, p_int): # real signature unknown; restored from __doc__
        """ setValue(self, int) """
        pass

    def singleStep(self): # real signature unknown; restored from __doc__
        """ singleStep(self) -> int """
        return 0

    def sliderChange(self, QAbstractSlider_SliderChange): # real signature unknown; restored from __doc__
        """ sliderChange(self, QAbstractSlider.SliderChange) """
        pass

    def sliderMoved(self, p_int): # real signature unknown; restored from __doc__
        """ sliderMoved(self, int) [signal] """
        pass

    def sliderPosition(self): # real signature unknown; restored from __doc__
        """ sliderPosition(self) -> int """
        return 0

    def sliderPressed(self): # real signature unknown; restored from __doc__
        """ sliderPressed(self) [signal] """
        pass

    def sliderReleased(self): # real signature unknown; restored from __doc__
        """ sliderReleased(self) [signal] """
        pass

    def timerEvent(self, QTimerEvent): # real signature unknown; restored from __doc__
        """ timerEvent(self, QTimerEvent) """
        pass

    def triggerAction(self, QAbstractSlider_SliderAction): # real signature unknown; restored from __doc__
        """ triggerAction(self, QAbstractSlider.SliderAction) """
        pass

    def value(self): # real signature unknown; restored from __doc__
        """ value(self) -> int """
        return 0

    def valueChanged(self, p_int): # real signature unknown; restored from __doc__
        """ valueChanged(self, int) [signal] """
        pass

    def wheelEvent(self, QWheelEvent): # real signature unknown; restored from __doc__
        """ wheelEvent(self, QWheelEvent) """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass

    SliderMove = 7
    SliderNoAction = 0
    SliderOrientationChange = 1
    SliderPageStepAdd = 3
    SliderPageStepSub = 4
    SliderRangeChange = 0
    SliderSingleStepAdd = 1
    SliderSingleStepSub = 2
    SliderStepsChange = 2
    SliderToMaximum = 6
    SliderToMinimum = 5
    SliderValueChange = 3


