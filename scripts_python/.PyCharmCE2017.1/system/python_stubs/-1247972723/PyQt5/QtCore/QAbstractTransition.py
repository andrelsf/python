# encoding: utf-8
# module PyQt5.QtCore
# from /usr/lib/python2.7/dist-packages/PyQt5/QtCore.x86_64-linux-gnu.so
# by generator 1.145
# no doc

# imports
import sip as __sip


from QObject import QObject

class QAbstractTransition(QObject):
    """ QAbstractTransition(sourceState: QState = None) """
    def addAnimation(self, QAbstractAnimation): # real signature unknown; restored from __doc__
        """ addAnimation(self, QAbstractAnimation) """
        pass

    def animations(self): # real signature unknown; restored from __doc__
        """ animations(self) -> object """
        return object()

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def eventTest(self, QEvent): # real signature unknown; restored from __doc__
        """ eventTest(self, QEvent) -> bool """
        return False

    def machine(self): # real signature unknown; restored from __doc__
        """ machine(self) -> QStateMachine """
        return QStateMachine

    def onTransition(self, QEvent): # real signature unknown; restored from __doc__
        """ onTransition(self, QEvent) """
        pass

    def removeAnimation(self, QAbstractAnimation): # real signature unknown; restored from __doc__
        """ removeAnimation(self, QAbstractAnimation) """
        pass

    def setTargetState(self, QAbstractState): # real signature unknown; restored from __doc__
        """ setTargetState(self, QAbstractState) """
        pass

    def setTargetStates(self, Iterable, QAbstractState=None): # real signature unknown; restored from __doc__
        """ setTargetStates(self, Iterable[QAbstractState]) """
        pass

    def setTransitionType(self, QAbstractTransition_TransitionType): # real signature unknown; restored from __doc__
        """ setTransitionType(self, QAbstractTransition.TransitionType) """
        pass

    def sourceState(self): # real signature unknown; restored from __doc__
        """ sourceState(self) -> QState """
        return QState

    def targetState(self): # real signature unknown; restored from __doc__
        """ targetState(self) -> QAbstractState """
        return QAbstractState

    def targetStateChanged(self): # real signature unknown; restored from __doc__
        """ targetStateChanged(self) [signal] """
        pass

    def targetStates(self): # real signature unknown; restored from __doc__
        """ targetStates(self) -> object """
        return object()

    def targetStatesChanged(self): # real signature unknown; restored from __doc__
        """ targetStatesChanged(self) [signal] """
        pass

    def transitionType(self): # real signature unknown; restored from __doc__
        """ transitionType(self) -> QAbstractTransition.TransitionType """
        pass

    def triggered(self): # real signature unknown; restored from __doc__
        """ triggered(self) [signal] """
        pass

    def __init__(self, sourceState=None): # real signature unknown; restored from __doc__
        pass

    ExternalTransition = 0
    InternalTransition = 1


