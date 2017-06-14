# encoding: utf-8
# module PyQt5.QtCore
# from /usr/lib/python2.7/dist-packages/PyQt5/QtCore.x86_64-linux-gnu.so
# by generator 1.145
# no doc

# imports
import sip as __sip


from QObject import QObject

class QSocketNotifier(QObject):
    """ QSocketNotifier(sip.voidptr, QSocketNotifier.Type, parent: QObject = None) """
    def activated(self, p_int): # real signature unknown; restored from __doc__
        """ activated(self, int) [signal] """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def isEnabled(self): # real signature unknown; restored from __doc__
        """ isEnabled(self) -> bool """
        return False

    def setEnabled(self, bool): # real signature unknown; restored from __doc__
        """ setEnabled(self, bool) """
        pass

    def socket(self): # real signature unknown; restored from __doc__
        """ socket(self) -> sip.voidptr """
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> QSocketNotifier.Type """
        pass

    def __init__(self, sip_voidptr, QSocketNotifier_Type, parent=None): # real signature unknown; restored from __doc__
        pass

    Exception = 2
    Read = 0
    Write = 1


