# encoding: utf-8
# module PyQt5.QtCore
# from /usr/lib/python2.7/dist-packages/PyQt5/QtCore.x86_64-linux-gnu.so
# by generator 1.145
# no doc

# imports
import sip as __sip


class QWaitCondition(): # skipped bases: <type 'sip.simplewrapper'>
    """ QWaitCondition() """
    def wait(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        wait(self, QMutex, msecs: int = ULONG_MAX) -> bool
        wait(self, QReadWriteLock, msecs: int = ULONG_MAX) -> bool
        """
        return False

    def wakeAll(self): # real signature unknown; restored from __doc__
        """ wakeAll(self) """
        pass

    def wakeOne(self): # real signature unknown; restored from __doc__
        """ wakeOne(self) """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



