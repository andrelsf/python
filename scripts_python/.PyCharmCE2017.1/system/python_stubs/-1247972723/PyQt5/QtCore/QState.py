# encoding: utf-8
# module PyQt5.QtCore
# from /usr/lib/python2.7/dist-packages/PyQt5/QtCore.x86_64-linux-gnu.so
# by generator 1.145
# no doc

# imports
import sip as __sip


from QAbstractState import QAbstractState

class QState(QAbstractState):
    """
    QState(parent: QState = None)
    QState(QState.ChildMode, parent: QState = None)
    """
    def addTransition(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addTransition(self, QAbstractTransition)
        addTransition(self, pyqtBoundSignal, QAbstractState) -> QSignalTransition
        addTransition(self, QAbstractState) -> QAbstractTransition
        """
        return QSignalTransition or QAbstractTransition

    def assignProperty(self, QObject, p_str, Any): # real signature unknown; restored from __doc__
        """ assignProperty(self, QObject, str, Any) """
        pass

    def childMode(self): # real signature unknown; restored from __doc__
        """ childMode(self) -> QState.ChildMode """
        pass

    def childModeChanged(self): # real signature unknown; restored from __doc__
        """ childModeChanged(self) [signal] """
        pass

    def errorState(self): # real signature unknown; restored from __doc__
        """ errorState(self) -> QAbstractState """
        return QAbstractState

    def errorStateChanged(self): # real signature unknown; restored from __doc__
        """ errorStateChanged(self) [signal] """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def finished(self): # real signature unknown; restored from __doc__
        """ finished(self) [signal] """
        pass

    def initialState(self): # real signature unknown; restored from __doc__
        """ initialState(self) -> QAbstractState """
        return QAbstractState

    def initialStateChanged(self): # real signature unknown; restored from __doc__
        """ initialStateChanged(self) [signal] """
        pass

    def onEntry(self, QEvent): # real signature unknown; restored from __doc__
        """ onEntry(self, QEvent) """
        pass

    def onExit(self, QEvent): # real signature unknown; restored from __doc__
        """ onExit(self, QEvent) """
        pass

    def propertiesAssigned(self): # real signature unknown; restored from __doc__
        """ propertiesAssigned(self) [signal] """
        pass

    def removeTransition(self, QAbstractTransition): # real signature unknown; restored from __doc__
        """ removeTransition(self, QAbstractTransition) """
        pass

    def setChildMode(self, QState_ChildMode): # real signature unknown; restored from __doc__
        """ setChildMode(self, QState.ChildMode) """
        pass

    def setErrorState(self, QAbstractState): # real signature unknown; restored from __doc__
        """ setErrorState(self, QAbstractState) """
        pass

    def setInitialState(self, QAbstractState): # real signature unknown; restored from __doc__
        """ setInitialState(self, QAbstractState) """
        pass

    def transitions(self): # real signature unknown; restored from __doc__
        """ transitions(self) -> object """
        return object()

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    DontRestoreProperties = 0
    ExclusiveStates = 0
    ParallelStates = 1
    RestoreProperties = 1


