# encoding: utf-8
# module PyQt5.QtCore
# from /usr/lib/python2.7/dist-packages/PyQt5/QtCore.x86_64-linux-gnu.so
# by generator 1.145
# no doc

# imports
import sip as __sip


class QPersistentModelIndex(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QPersistentModelIndex()
    QPersistentModelIndex(QModelIndex)
    QPersistentModelIndex(QPersistentModelIndex)
    """
    def child(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ child(self, int, int) -> QModelIndex """
        return QModelIndex

    def column(self): # real signature unknown; restored from __doc__
        """ column(self) -> int """
        return 0

    def data(self, role=None): # real signature unknown; restored from __doc__
        """ data(self, role: int = Qt.DisplayRole) -> Any """
        pass

    def flags(self): # real signature unknown; restored from __doc__
        """ flags(self) -> Qt.ItemFlags """
        pass

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def model(self): # real signature unknown; restored from __doc__
        """ model(self) -> QAbstractItemModel """
        return QAbstractItemModel

    def parent(self): # real signature unknown; restored from __doc__
        """ parent(self) -> QModelIndex """
        return QModelIndex

    def row(self): # real signature unknown; restored from __doc__
        """ row(self) -> int """
        return 0

    def sibling(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ sibling(self, int, int) -> QModelIndex """
        return QModelIndex

    def swap(self, QPersistentModelIndex): # real signature unknown; restored from __doc__
        """ swap(self, QPersistentModelIndex) """
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

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



