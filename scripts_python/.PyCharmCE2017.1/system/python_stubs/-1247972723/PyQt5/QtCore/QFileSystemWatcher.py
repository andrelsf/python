# encoding: utf-8
# module PyQt5.QtCore
# from /usr/lib/python2.7/dist-packages/PyQt5/QtCore.x86_64-linux-gnu.so
# by generator 1.145
# no doc

# imports
import sip as __sip


from QObject import QObject

class QFileSystemWatcher(QObject):
    """
    QFileSystemWatcher(parent: QObject = None)
    QFileSystemWatcher(Iterable[str], parent: QObject = None)
    """
    def addPath(self, p_str): # real signature unknown; restored from __doc__
        """ addPath(self, str) -> bool """
        return False

    def addPaths(self, Iterable, p_str=None): # real signature unknown; restored from __doc__
        """ addPaths(self, Iterable[str]) -> List[str] """
        return []

    def directories(self): # real signature unknown; restored from __doc__
        """ directories(self) -> List[str] """
        return []

    def directoryChanged(self, p_str): # real signature unknown; restored from __doc__
        """ directoryChanged(self, str) [signal] """
        pass

    def fileChanged(self, p_str): # real signature unknown; restored from __doc__
        """ fileChanged(self, str) [signal] """
        pass

    def files(self): # real signature unknown; restored from __doc__
        """ files(self) -> List[str] """
        return []

    def removePath(self, p_str): # real signature unknown; restored from __doc__
        """ removePath(self, str) -> bool """
        return False

    def removePaths(self, Iterable, p_str=None): # real signature unknown; restored from __doc__
        """ removePaths(self, Iterable[str]) -> List[str] """
        return []

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


