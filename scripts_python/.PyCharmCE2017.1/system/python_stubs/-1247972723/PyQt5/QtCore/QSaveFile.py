# encoding: utf-8
# module PyQt5.QtCore
# from /usr/lib/python2.7/dist-packages/PyQt5/QtCore.x86_64-linux-gnu.so
# by generator 1.145
# no doc

# imports
import sip as __sip


from QFileDevice import QFileDevice

class QSaveFile(QFileDevice):
    """
    QSaveFile(str)
    QSaveFile(parent: QObject = None)
    QSaveFile(str, QObject)
    """
    def cancelWriting(self): # real signature unknown; restored from __doc__
        """ cancelWriting(self) """
        pass

    def close(self, *args, **kwargs): # real signature unknown
        pass

    def commit(self): # real signature unknown; restored from __doc__
        """ commit(self) -> bool """
        return False

    def directWriteFallback(self): # real signature unknown; restored from __doc__
        """ directWriteFallback(self) -> bool """
        return False

    def fileName(self): # real signature unknown; restored from __doc__
        """ fileName(self) -> str """
        return ""

    def open(self, Union, QIODevice_OpenMode=None, QIODevice_OpenModeFlag=None): # real signature unknown; restored from __doc__
        """ open(self, Union[QIODevice.OpenMode, QIODevice.OpenModeFlag]) -> bool """
        return False

    def setDirectWriteFallback(self, bool): # real signature unknown; restored from __doc__
        """ setDirectWriteFallback(self, bool) """
        pass

    def setFileName(self, p_str): # real signature unknown; restored from __doc__
        """ setFileName(self, str) """
        pass

    def writeData(self, bytes): # real signature unknown; restored from __doc__
        """ writeData(self, bytes) -> int """
        return 0

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


