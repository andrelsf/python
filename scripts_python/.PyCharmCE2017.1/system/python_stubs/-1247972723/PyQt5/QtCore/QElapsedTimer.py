# encoding: utf-8
# module PyQt5.QtCore
# from /usr/lib/python2.7/dist-packages/PyQt5/QtCore.x86_64-linux-gnu.so
# by generator 1.145
# no doc

# imports
import sip as __sip


class QElapsedTimer(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QElapsedTimer()
    QElapsedTimer(QElapsedTimer)
    """
    def clockType(self): # real signature unknown; restored from __doc__
        """ clockType() -> QElapsedTimer.ClockType """
        pass

    def elapsed(self): # real signature unknown; restored from __doc__
        """ elapsed(self) -> int """
        return 0

    def hasExpired(self, p_int): # real signature unknown; restored from __doc__
        """ hasExpired(self, int) -> bool """
        return False

    def invalidate(self): # real signature unknown; restored from __doc__
        """ invalidate(self) """
        pass

    def isMonotonic(self): # real signature unknown; restored from __doc__
        """ isMonotonic() -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def msecsSinceReference(self): # real signature unknown; restored from __doc__
        """ msecsSinceReference(self) -> int """
        return 0

    def msecsTo(self, QElapsedTimer): # real signature unknown; restored from __doc__
        """ msecsTo(self, QElapsedTimer) -> int """
        return 0

    def nsecsElapsed(self): # real signature unknown; restored from __doc__
        """ nsecsElapsed(self) -> int """
        return 0

    def restart(self): # real signature unknown; restored from __doc__
        """ restart(self) -> int """
        return 0

    def secsTo(self, QElapsedTimer): # real signature unknown; restored from __doc__
        """ secsTo(self, QElapsedTimer) -> int """
        return 0

    def start(self): # real signature unknown; restored from __doc__
        """ start(self) """
        pass

    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __ge__(self, y): # real signature unknown; restored from __doc__
        """ x.__ge__(y) <==> x>=y """
        pass

    def __gt__(self, y): # real signature unknown; restored from __doc__
        """ x.__gt__(y) <==> x>y """
        pass

    def __init__(self, QElapsedTimer=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __le__(self, y): # real signature unknown; restored from __doc__
        """ x.__le__(y) <==> x<=y """
        pass

    def __lt__(self, y): # real signature unknown; restored from __doc__
        """ x.__lt__(y) <==> x<y """
        pass

    def __ne__(self, y): # real signature unknown; restored from __doc__
        """ x.__ne__(y) <==> x!=y """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    MachAbsoluteTime = 3
    MonotonicClock = 1
    PerformanceCounter = 4
    SystemTime = 0
    TickCounter = 2


