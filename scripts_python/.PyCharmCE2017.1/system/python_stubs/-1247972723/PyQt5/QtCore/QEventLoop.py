# encoding: utf-8
# module PyQt5.QtCore
# from /usr/lib/python2.7/dist-packages/PyQt5/QtCore.x86_64-linux-gnu.so
# by generator 1.145
# no doc

# imports
import sip as __sip


from QObject import QObject

class QEventLoop(QObject):
    """ QEventLoop(parent: QObject = None) """
    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def exec_(self, flags=None): # real signature unknown; restored from __doc__
        """ exec_(self, flags: QEventLoop.ProcessEventsFlags = QEventLoop.AllEvents) -> int """
        return 0

    def exit(self, returnCode=0): # real signature unknown; restored from __doc__
        """ exit(self, returnCode: int = 0) """
        pass

    def isRunning(self): # real signature unknown; restored from __doc__
        """ isRunning(self) -> bool """
        return False

    def processEvents(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        processEvents(self, flags: Union[QEventLoop.ProcessEventsFlags, QEventLoop.ProcessEventsFlag] = QEventLoop.AllEvents) -> bool
        processEvents(self, Union[QEventLoop.ProcessEventsFlags, QEventLoop.ProcessEventsFlag], int)
        """
        pass

    def quit(self): # real signature unknown; restored from __doc__
        """ quit(self) """
        pass

    def wakeUp(self): # real signature unknown; restored from __doc__
        """ wakeUp(self) """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass

    AllEvents = 0
    ExcludeSocketNotifiers = 2
    ExcludeUserInputEvents = 1
    WaitForMoreEvents = 4
    X11ExcludeTimers = 8


