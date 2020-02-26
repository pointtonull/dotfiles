# encoding: utf-8
# module PyQt5.QtWidgets
# from /usr/lib/python3/dist-packages/PyQt5/QtWidgets.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui


from .QGraphicsItem import QGraphicsItem

class QGraphicsObject(__PyQt5_QtCore.QObject, QGraphicsItem):
    """ QGraphicsObject(parent: QGraphicsItem = None) """
    def enabledChanged(self): # real signature unknown; restored from __doc__
        """ enabledChanged(self) [signal] """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def grabGesture(self, Qt_GestureType, flags, Qt_GestureFlags=None, Qt_GestureFlag=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ grabGesture(self, Qt.GestureType, flags: Union[Qt.GestureFlags, Qt.GestureFlag] = Qt.GestureFlags()) """
        pass

    def opacityChanged(self): # real signature unknown; restored from __doc__
        """ opacityChanged(self) [signal] """
        pass

    def parentChanged(self): # real signature unknown; restored from __doc__
        """ parentChanged(self) [signal] """
        pass

    def rotationChanged(self): # real signature unknown; restored from __doc__
        """ rotationChanged(self) [signal] """
        pass

    def scaleChanged(self): # real signature unknown; restored from __doc__
        """ scaleChanged(self) [signal] """
        pass

    def ungrabGesture(self, Qt_GestureType): # real signature unknown; restored from __doc__
        """ ungrabGesture(self, Qt.GestureType) """
        pass

    def updateMicroFocus(self): # real signature unknown; restored from __doc__
        """ updateMicroFocus(self) """
        pass

    def visibleChanged(self): # real signature unknown; restored from __doc__
        """ visibleChanged(self) [signal] """
        pass

    def xChanged(self): # real signature unknown; restored from __doc__
        """ xChanged(self) [signal] """
        pass

    def yChanged(self): # real signature unknown; restored from __doc__
        """ yChanged(self) [signal] """
        pass

    def zChanged(self): # real signature unknown; restored from __doc__
        """ zChanged(self) [signal] """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


