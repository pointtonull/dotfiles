# encoding: utf-8
# module PyQt5.QtWidgets
# from /usr/lib/python3/dist-packages/PyQt5/QtWidgets.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui


from .QGraphicsEffect import QGraphicsEffect

class QGraphicsBlurEffect(QGraphicsEffect):
    """ QGraphicsBlurEffect(parent: QObject = None) """
    def blurHints(self): # real signature unknown; restored from __doc__
        """ blurHints(self) -> QGraphicsBlurEffect.BlurHints """
        pass

    def blurHintsChanged(self, Union, QGraphicsBlurEffect_BlurHints=None, QGraphicsBlurEffect_BlurHint=None): # real signature unknown; restored from __doc__
        """ blurHintsChanged(self, Union[QGraphicsBlurEffect.BlurHints, QGraphicsBlurEffect.BlurHint]) [signal] """
        pass

    def blurRadius(self): # real signature unknown; restored from __doc__
        """ blurRadius(self) -> float """
        return 0.0

    def blurRadiusChanged(self, p_float): # real signature unknown; restored from __doc__
        """ blurRadiusChanged(self, float) [signal] """
        pass

    def boundingRectFor(self, QRectF): # real signature unknown; restored from __doc__
        """ boundingRectFor(self, QRectF) -> QRectF """
        pass

    def draw(self, QPainter): # real signature unknown; restored from __doc__
        """ draw(self, QPainter) """
        pass

    def setBlurHints(self, Union, QGraphicsBlurEffect_BlurHints=None, QGraphicsBlurEffect_BlurHint=None): # real signature unknown; restored from __doc__
        """ setBlurHints(self, Union[QGraphicsBlurEffect.BlurHints, QGraphicsBlurEffect.BlurHint]) """
        pass

    def setBlurRadius(self, p_float): # real signature unknown; restored from __doc__
        """ setBlurRadius(self, float) """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass

    AnimationHint = 2
    PerformanceHint = 0
    QualityHint = 1


