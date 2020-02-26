# encoding: utf-8
# module PyQt5.QtWidgets
# from /usr/lib/python3/dist-packages/PyQt5/QtWidgets.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui


from .QAction import QAction

class QWidgetAction(QAction):
    """ QWidgetAction(QObject) """
    def createdWidgets(self): # real signature unknown; restored from __doc__
        """ createdWidgets(self) -> List[QWidget] """
        return []

    def createWidget(self, QWidget): # real signature unknown; restored from __doc__
        """ createWidget(self, QWidget) -> QWidget """
        return QWidget

    def defaultWidget(self): # real signature unknown; restored from __doc__
        """ defaultWidget(self) -> QWidget """
        return QWidget

    def deleteWidget(self, QWidget): # real signature unknown; restored from __doc__
        """ deleteWidget(self, QWidget) """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def eventFilter(self, QObject, QEvent): # real signature unknown; restored from __doc__
        """ eventFilter(self, QObject, QEvent) -> bool """
        return False

    def releaseWidget(self, QWidget): # real signature unknown; restored from __doc__
        """ releaseWidget(self, QWidget) """
        pass

    def requestWidget(self, QWidget): # real signature unknown; restored from __doc__
        """ requestWidget(self, QWidget) -> QWidget """
        return QWidget

    def setDefaultWidget(self, QWidget): # real signature unknown; restored from __doc__
        """ setDefaultWidget(self, QWidget) """
        pass

    def __init__(self, QObject): # real signature unknown; restored from __doc__
        pass


