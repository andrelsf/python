# encoding: utf-8
# module PyQt5.QtCore
# from /usr/lib/python2.7/dist-packages/PyQt5/QtCore.x86_64-linux-gnu.so
# by generator 1.145
# no doc

# imports
import sip as __sip


class QUuid(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QUuid()
    QUuid(int, int, int, int, int, int, int, int, int, int, int)
    QUuid(str)
    QUuid(Union[QByteArray, bytes, bytearray])
    QUuid(QUuid)
    """
    def createUuid(self): # real signature unknown; restored from __doc__
        """ createUuid() -> QUuid """
        return QUuid

    def createUuidV3(self, QUuid, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        createUuidV3(QUuid, Union[QByteArray, bytes, bytearray]) -> QUuid
        createUuidV3(QUuid, str) -> QUuid
        """
        return QUuid

    def createUuidV5(self, QUuid, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        createUuidV5(QUuid, Union[QByteArray, bytes, bytearray]) -> QUuid
        createUuidV5(QUuid, str) -> QUuid
        """
        return QUuid

    def fromRfc4122(self, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ fromRfc4122(Union[QByteArray, bytes, bytearray]) -> QUuid """
        return QUuid

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def toByteArray(self): # real signature unknown; restored from __doc__
        """ toByteArray(self) -> QByteArray """
        return QByteArray

    def toRfc4122(self): # real signature unknown; restored from __doc__
        """ toRfc4122(self) -> QByteArray """
        return QByteArray

    def toString(self): # real signature unknown; restored from __doc__
        """ toString(self) -> str """
        return ""

    def variant(self): # real signature unknown; restored from __doc__
        """ variant(self) -> QUuid.Variant """
        pass

    def version(self): # real signature unknown; restored from __doc__
        """ version(self) -> QUuid.Version """
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

    def __hash__(self): # real signature unknown; restored from __doc__
        """ x.__hash__() <==> hash(x) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
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

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    DCE = 2
    EmbeddedPOSIX = 2
    Md5 = 3
    Microsoft = 6
    Name = 3
    NCS = 0
    Random = 4
    Reserved = 7
    Sha1 = 5
    Time = 1
    VarUnknown = -1
    VerUnknown = -1


