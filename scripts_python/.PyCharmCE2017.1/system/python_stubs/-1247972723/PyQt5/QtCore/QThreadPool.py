# encoding: utf-8
# module PyQt5.QtCore
# from /usr/lib/python2.7/dist-packages/PyQt5/QtCore.x86_64-linux-gnu.so
# by generator 1.145
# no doc

# imports
import sip as __sip


from QObject import QObject

class QThreadPool(QObject):
    """ QThreadPool(parent: QObject = None) """
    def activeThreadCount(self): # real signature unknown; restored from __doc__
        """ activeThreadCount(self) -> int """
        return 0

    def cancel(self, QRunnable): # real signature unknown; restored from __doc__
        """ cancel(self, QRunnable) """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def expiryTimeout(self): # real signature unknown; restored from __doc__
        """ expiryTimeout(self) -> int """
        return 0

    def globalInstance(self): # real signature unknown; restored from __doc__
        """ globalInstance() -> QThreadPool """
        return QThreadPool

    def maxThreadCount(self): # real signature unknown; restored from __doc__
        """ maxThreadCount(self) -> int """
        return 0

    def releaseThread(self): # real signature unknown; restored from __doc__
        """ releaseThread(self) """
        pass

    def reserveThread(self): # real signature unknown; restored from __doc__
        """ reserveThread(self) """
        pass

    def setExpiryTimeout(self, p_int): # real signature unknown; restored from __doc__
        """ setExpiryTimeout(self, int) """
        pass

    def setMaxThreadCount(self, p_int): # real signature unknown; restored from __doc__
        """ setMaxThreadCount(self, int) """
        pass

    def start(self, QRunnable, priority=0): # real signature unknown; restored from __doc__
        """ start(self, QRunnable, priority: int = 0) """
        pass

    def tryStart(self, QRunnable): # real signature unknown; restored from __doc__
        """ tryStart(self, QRunnable) -> bool """
        return False

    def waitForDone(self, msecs=-1): # real signature unknown; restored from __doc__
        """ waitForDone(self, msecs: int = -1) -> bool """
        return False

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


