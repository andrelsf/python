# encoding: utf-8
# module PyQt5.QtCore
# from /usr/lib/python2.7/dist-packages/PyQt5/QtCore.x86_64-linux-gnu.so
# by generator 1.145
# no doc

# imports
import sip as __sip


from QObject import QObject

class QSharedMemory(QObject):
    """
    QSharedMemory(parent: QObject = None)
    QSharedMemory(str, parent: QObject = None)
    """
    def attach(self, mode=None): # real signature unknown; restored from __doc__
        """ attach(self, mode: QSharedMemory.AccessMode = QSharedMemory.ReadWrite) -> bool """
        return False

    def constData(self): # real signature unknown; restored from __doc__
        """ constData(self) -> sip.voidptr """
        pass

    def create(self, p_int, mode=None): # real signature unknown; restored from __doc__
        """ create(self, int, mode: QSharedMemory.AccessMode = QSharedMemory.ReadWrite) -> bool """
        return False

    def data(self): # real signature unknown; restored from __doc__
        """ data(self) -> sip.voidptr """
        pass

    def detach(self): # real signature unknown; restored from __doc__
        """ detach(self) -> bool """
        return False

    def error(self): # real signature unknown; restored from __doc__
        """ error(self) -> QSharedMemory.SharedMemoryError """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def isAttached(self): # real signature unknown; restored from __doc__
        """ isAttached(self) -> bool """
        return False

    def key(self): # real signature unknown; restored from __doc__
        """ key(self) -> str """
        return ""

    def lock(self): # real signature unknown; restored from __doc__
        """ lock(self) -> bool """
        return False

    def nativeKey(self): # real signature unknown; restored from __doc__
        """ nativeKey(self) -> str """
        return ""

    def setKey(self, p_str): # real signature unknown; restored from __doc__
        """ setKey(self, str) """
        pass

    def setNativeKey(self, p_str): # real signature unknown; restored from __doc__
        """ setNativeKey(self, str) """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> int """
        return 0

    def unlock(self): # real signature unknown; restored from __doc__
        """ unlock(self) -> bool """
        return False

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    AlreadyExists = 4
    InvalidSize = 2
    KeyError = 3
    LockError = 6
    NoError = 0
    NotFound = 5
    OutOfResources = 7
    PermissionDenied = 1
    ReadOnly = 0
    ReadWrite = 1
    UnknownError = 8


