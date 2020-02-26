# encoding: utf-8
# module PyQt5.QtTest
# from /usr/lib/python3/dist-packages/PyQt5/QtTest.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore


# no functions
# classes

class QSignalSpy(__PyQt5_QtCore.QObject):
    """ QSignalSpy(pyqtBoundSignal) """
    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def signal(self): # real signature unknown; restored from __doc__
        """ signal(self) -> QByteArray """
        pass

    def wait(self, timeout=5000): # real signature unknown; restored from __doc__
        """ wait(self, timeout: int = 5000) -> bool """
        return False

    def __delitem__(self, *args, **kwargs): # real signature unknown
        """ Delete self[key]. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __init__(self, pyqtBoundSignal): # real signature unknown; restored from __doc__
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    def __setitem__(self, *args, **kwargs): # real signature unknown
        """ Set self[key] to value. """
        pass


class QTest(): # skipped bases: <class 'sip.simplewrapper'>
    # no doc
    def keyClick(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        keyClick(QWidget, Qt.Key, modifier: Union[Qt.KeyboardModifiers, Qt.KeyboardModifier] = Qt.NoModifier, delay: int = -1)
        keyClick(QWidget, str, modifier: Union[Qt.KeyboardModifiers, Qt.KeyboardModifier] = Qt.NoModifier, delay: int = -1)
        keyClick(QWindow, Qt.Key, modifier: Union[Qt.KeyboardModifiers, Qt.KeyboardModifier] = Qt.NoModifier, delay: int = -1)
        keyClick(QWindow, str, modifier: Union[Qt.KeyboardModifiers, Qt.KeyboardModifier] = Qt.NoModifier, delay: int = -1)
        """
        pass

    def keyClicks(self, QWidget, p_str, modifier, Qt_KeyboardModifiers=None, Qt_KeyboardModifier=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ keyClicks(QWidget, str, modifier: Union[Qt.KeyboardModifiers, Qt.KeyboardModifier] = Qt.NoModifier, delay: int = -1) """
        pass

    def keyEvent(self, QTest_KeyAction, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        keyEvent(QTest.KeyAction, QWidget, Qt.Key, modifier: Union[Qt.KeyboardModifiers, Qt.KeyboardModifier] = Qt.NoModifier, delay: int = -1)
        keyEvent(QTest.KeyAction, QWidget, str, modifier: Union[Qt.KeyboardModifiers, Qt.KeyboardModifier] = Qt.NoModifier, delay: int = -1)
        keyEvent(QTest.KeyAction, QWindow, Qt.Key, modifier: Union[Qt.KeyboardModifiers, Qt.KeyboardModifier] = Qt.NoModifier, delay: int = -1)
        keyEvent(QTest.KeyAction, QWindow, str, modifier: Union[Qt.KeyboardModifiers, Qt.KeyboardModifier] = Qt.NoModifier, delay: int = -1)
        """
        pass

    def keyPress(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        keyPress(QWidget, Qt.Key, modifier: Union[Qt.KeyboardModifiers, Qt.KeyboardModifier] = Qt.NoModifier, delay: int = -1)
        keyPress(QWidget, str, modifier: Union[Qt.KeyboardModifiers, Qt.KeyboardModifier] = Qt.NoModifier, delay: int = -1)
        keyPress(QWindow, Qt.Key, modifier: Union[Qt.KeyboardModifiers, Qt.KeyboardModifier] = Qt.NoModifier, delay: int = -1)
        keyPress(QWindow, str, modifier: Union[Qt.KeyboardModifiers, Qt.KeyboardModifier] = Qt.NoModifier, delay: int = -1)
        """
        pass

    def keyRelease(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        keyRelease(QWidget, Qt.Key, modifier: Union[Qt.KeyboardModifiers, Qt.KeyboardModifier] = Qt.NoModifier, delay: int = -1)
        keyRelease(QWidget, str, modifier: Union[Qt.KeyboardModifiers, Qt.KeyboardModifier] = Qt.NoModifier, delay: int = -1)
        keyRelease(QWindow, Qt.Key, modifier: Union[Qt.KeyboardModifiers, Qt.KeyboardModifier] = Qt.NoModifier, delay: int = -1)
        keyRelease(QWindow, str, modifier: Union[Qt.KeyboardModifiers, Qt.KeyboardModifier] = Qt.NoModifier, delay: int = -1)
        """
        pass

    def mouseClick(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        mouseClick(QWidget, Qt.MouseButton, modifier: Union[Qt.KeyboardModifiers, Qt.KeyboardModifier] = 0, pos: QPoint = QPoint(), delay: int = -1)
        mouseClick(QWindow, Qt.MouseButton, modifier: Union[Qt.KeyboardModifiers, Qt.KeyboardModifier] = Qt.KeyboardModifiers(), pos: QPoint = QPoint(), delay: int = -1)
        """
        pass

    def mouseDClick(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        mouseDClick(QWidget, Qt.MouseButton, modifier: Union[Qt.KeyboardModifiers, Qt.KeyboardModifier] = 0, pos: QPoint = QPoint(), delay: int = -1)
        mouseDClick(QWindow, Qt.MouseButton, modifier: Union[Qt.KeyboardModifiers, Qt.KeyboardModifier] = Qt.KeyboardModifiers(), pos: QPoint = QPoint(), delay: int = -1)
        """
        pass

    def mouseEvent(self, QTest_MouseAction, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        mouseEvent(QTest.MouseAction, QWidget, Qt.MouseButton, Union[Qt.KeyboardModifiers, Qt.KeyboardModifier], QPoint, delay: int = -1)
        mouseEvent(QTest.MouseAction, QWindow, Qt.MouseButton, Union[Qt.KeyboardModifiers, Qt.KeyboardModifier], QPoint, delay: int = -1)
        """
        pass

    def mouseMove(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        mouseMove(QWidget, pos: QPoint = QPoint(), delay: int = -1)
        mouseMove(QWindow, pos: QPoint = QPoint(), delay: int = -1)
        """
        pass

    def mousePress(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        mousePress(QWidget, Qt.MouseButton, modifier: Union[Qt.KeyboardModifiers, Qt.KeyboardModifier] = 0, pos: QPoint = QPoint(), delay: int = -1)
        mousePress(QWindow, Qt.MouseButton, modifier: Union[Qt.KeyboardModifiers, Qt.KeyboardModifier] = Qt.KeyboardModifiers(), pos: QPoint = QPoint(), delay: int = -1)
        """
        pass

    def mouseRelease(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        mouseRelease(QWidget, Qt.MouseButton, modifier: Union[Qt.KeyboardModifiers, Qt.KeyboardModifier] = 0, pos: QPoint = QPoint(), delay: int = -1)
        mouseRelease(QWindow, Qt.MouseButton, modifier: Union[Qt.KeyboardModifiers, Qt.KeyboardModifier] = Qt.KeyboardModifiers(), pos: QPoint = QPoint(), delay: int = -1)
        """
        pass

    def qSleep(self, p_int): # real signature unknown; restored from __doc__
        """ qSleep(int) """
        pass

    def qWait(self, p_int): # real signature unknown; restored from __doc__
        """ qWait(int) """
        pass

    def qWaitForWindowActive(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        qWaitForWindowActive(QWindow, timeout: int = 5000) -> bool
        qWaitForWindowActive(QWidget, timeout: int = 1000) -> bool
        """
        return False

    def qWaitForWindowExposed(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        qWaitForWindowExposed(QWindow, timeout: int = 5000) -> bool
        qWaitForWindowExposed(QWidget, timeout: int = 1000) -> bool
        """
        return False

    def touchEvent(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        touchEvent(QWidget, QTouchDevice) -> QTest.QTouchEventSequence
        touchEvent(QWindow, QTouchDevice) -> QTest.QTouchEventSequence
        """
        pass

    def waitForEvents(self): # real signature unknown; restored from __doc__
        """ waitForEvents() """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    Click = 2
    MouseClick = 2
    MouseDClick = 3
    MouseMove = 4
    MousePress = 0
    MouseRelease = 1
    Press = 0
    Release = 1
    Shortcut = 3


# variables with complex values



