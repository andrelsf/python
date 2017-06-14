# encoding: utf-8
# module PyQt5.QtCore
# from /usr/lib/python2.7/dist-packages/PyQt5/QtCore.x86_64-linux-gnu.so
# by generator 1.145
# no doc

# imports
import sip as __sip


from QVariantAnimation import QVariantAnimation

class QPropertyAnimation(QVariantAnimation):
    """
    QPropertyAnimation(parent: QObject = None)
    QPropertyAnimation(QObject, Union[QByteArray, bytes, bytearray], parent: QObject = None)
    """
    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def propertyName(self): # real signature unknown; restored from __doc__
        """ propertyName(self) -> QByteArray """
        return QByteArray

    def setPropertyName(self, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ setPropertyName(self, Union[QByteArray, bytes, bytearray]) """
        pass

    def setTargetObject(self, QObject): # real signature unknown; restored from __doc__
        """ setTargetObject(self, QObject) """
        pass

    def targetObject(self): # real signature unknown; restored from __doc__
        """ targetObject(self) -> QObject """
        return QObject

    def updateCurrentValue(self, Any): # real signature unknown; restored from __doc__
        """ updateCurrentValue(self, Any) """
        pass

    def updateState(self, QAbstractAnimation_State, QAbstractAnimation_State_1): # real signature unknown; restored from __doc__
        """ updateState(self, QAbstractAnimation.State, QAbstractAnimation.State) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


