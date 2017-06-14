# encoding: utf-8
# module PyQt5.QtCore
# from /usr/lib/python2.7/dist-packages/PyQt5/QtCore.x86_64-linux-gnu.so
# by generator 1.145
# no doc

# imports
import sip as __sip


class QItemSelectionRange(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QItemSelectionRange()
    QItemSelectionRange(QItemSelectionRange)
    QItemSelectionRange(QModelIndex, QModelIndex)
    QItemSelectionRange(QModelIndex)
    """
    def bottom(self): # real signature unknown; restored from __doc__
        """ bottom(self) -> int """
        return 0

    def bottomRight(self): # real signature unknown; restored from __doc__
        """ bottomRight(self) -> QPersistentModelIndex """
        return QPersistentModelIndex

    def contains(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        contains(self, QModelIndex) -> bool
        contains(self, int, int, QModelIndex) -> bool
        """
        return False

    def height(self): # real signature unknown; restored from __doc__
        """ height(self) -> int """
        return 0

    def indexes(self): # real signature unknown; restored from __doc__
        """ indexes(self) -> object """
        return object()

    def intersected(self, QItemSelectionRange): # real signature unknown; restored from __doc__
        """ intersected(self, QItemSelectionRange) -> QItemSelectionRange """
        return QItemSelectionRange

    def intersects(self, QItemSelectionRange): # real signature unknown; restored from __doc__
        """ intersects(self, QItemSelectionRange) -> bool """
        return False

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def left(self): # real signature unknown; restored from __doc__
        """ left(self) -> int """
        return 0

    def model(self): # real signature unknown; restored from __doc__
        """ model(self) -> QAbstractItemModel """
        return QAbstractItemModel

    def parent(self): # real signature unknown; restored from __doc__
        """ parent(self) -> QModelIndex """
        return QModelIndex

    def right(self): # real signature unknown; restored from __doc__
        """ right(self) -> int """
        return 0

    def swap(self, QItemSelectionRange): # real signature unknown; restored from __doc__
        """ swap(self, QItemSelectionRange) """
        pass

    def top(self): # real signature unknown; restored from __doc__
        """ top(self) -> int """
        return 0

    def topLeft(self): # real signature unknown; restored from __doc__
        """ topLeft(self) -> QPersistentModelIndex """
        return QPersistentModelIndex

    def width(self): # real signature unknown; restored from __doc__
        """ width(self) -> int """
        return 0

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



