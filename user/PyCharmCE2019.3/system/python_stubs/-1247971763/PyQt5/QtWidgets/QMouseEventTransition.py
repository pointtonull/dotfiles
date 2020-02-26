# encoding: utf-8
# module PyQt5.QtWidgets
# from /usr/lib/python3/dist-packages/PyQt5/QtWidgets.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui


class QMouseEventTransition(__PyQt5_QtCore.QEventTransition):
    """
    QMouseEventTransition(sourceState: QState = None)
    QMouseEventTransition(QObject, QEvent.Type, Qt.MouseButton, sourceState: QState = None)
    """
    def button(self): # real signature unknown; restored from __doc__
        """ button(self) -> Qt.MouseButton """
        pass

    def eventTest(self, QEvent): # real signature unknown; restored from __doc__
        """ eventTest(self, QEvent) -> bool """
        return False

    def hitTestPath(self): # real signature unknown; restored from __doc__
        """ hitTestPath(self) -> QPainterPath """
        pass

    def modifierMask(self): # real signature unknown; restored from __doc__
        """ modifierMask(self) -> Qt.KeyboardModifiers """
        pass

    def onTransition(self, QEvent): # real signature unknown; restored from __doc__
        """ onTransition(self, QEvent) """
        pass

    def setButton(self, Qt_MouseButton): # real signature unknown; restored from __doc__
        """ setButton(self, Qt.MouseButton) """
        pass

    def setHitTestPath(self, QPainterPath): # real signature unknown; restored from __doc__
        """ setHitTestPath(self, QPainterPath) """
        pass

    def setModifierMask(self, Union, Qt_KeyboardModifiers=None, Qt_KeyboardModifier=None): # real signature unknown; restored from __doc__
        """ setModifierMask(self, Union[Qt.KeyboardModifiers, Qt.KeyboardModifier]) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


