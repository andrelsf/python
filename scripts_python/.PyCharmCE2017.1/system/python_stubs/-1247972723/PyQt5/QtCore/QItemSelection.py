# encoding: utf-8
# module PyQt5.QtCore
# from /usr/lib/python2.7/dist-packages/PyQt5/QtCore.x86_64-linux-gnu.so
# by generator 1.145
# no doc

# imports
import sip as __sip


class QItemSelection(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QItemSelection()
    QItemSelection(QModelIndex, QModelIndex)
    QItemSelection(QItemSelection)
    """
    def append(self, QItemSelectionRange): # real signature unknown; restored from __doc__
        """ append(self, QItemSelectionRange) """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def contains(self, QModelIndex): # real signature unknown; restored from __doc__
        """ contains(self, QModelIndex) -> bool """
        return False

    def count(self, QItemSelectionRange=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        count(self, QItemSelectionRange) -> int
        count(self) -> int
        """
        return 0

    def first(self): # real signature unknown; restored from __doc__
        """ first(self) -> QItemSelectionRange """
        return QItemSelectionRange

    def indexes(self): # real signature unknown; restored from __doc__
        """ indexes(self) -> object """
        return object()

    def indexOf(self, QItemSelectionRange, from_=0): # real signature unknown; restored from __doc__
        """ indexOf(self, QItemSelectionRange, from_: int = 0) -> int """
        return 0

    def insert(self, p_int, QItemSelectionRange): # real signature unknown; restored from __doc__
        """ insert(self, int, QItemSelectionRange) """
        pass

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def last(self): # real signature unknown; restored from __doc__
        """ last(self) -> QItemSelectionRange """
        return QItemSelectionRange

    def lastIndexOf(self, QItemSelectionRange, from_=-1): # real signature unknown; restored from __doc__
        """ lastIndexOf(self, QItemSelectionRange, from_: int = -1) -> int """
        return 0

    def merge(self, QItemSelection, Union, QItemSelectionModel_SelectionFlags=None, QItemSelectionModel_SelectionFlag=None): # real signature unknown; restored from __doc__
        """ merge(self, QItemSelection, Union[QItemSelectionModel.SelectionFlags, QItemSelectionModel.SelectionFlag]) """
        pass

    def move(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ move(self, int, int) """
        pass

    def prepend(self, QItemSelectionRange): # real signature unknown; restored from __doc__
        """ prepend(self, QItemSelectionRange) """
        pass

    def removeAll(self, QItemSelectionRange): # real signature unknown; restored from __doc__
        """ removeAll(self, QItemSelectionRange) -> int """
        return 0

    def removeAt(self, p_int): # real signature unknown; restored from __doc__
        """ removeAt(self, int) """
        pass

    def replace(self, p_int, QItemSelectionRange): # real signature unknown; restored from __doc__
        """ replace(self, int, QItemSelectionRange) """
        pass

    def select(self, QModelIndex, QModelIndex_1): # real signature unknown; restored from __doc__
        """ select(self, QModelIndex, QModelIndex) """
        pass

    def split(self, QItemSelectionRange, QItemSelectionRange_1, QItemSelection): # real signature unknown; restored from __doc__
        """ split(QItemSelectionRange, QItemSelectionRange, QItemSelection) """
        pass

    def swap(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ swap(self, int, int) """
        pass

    def takeAt(self, p_int): # real signature unknown; restored from __doc__
        """ takeAt(self, int) -> QItemSelectionRange """
        return QItemSelectionRange

    def takeFirst(self): # real signature unknown; restored from __doc__
        """ takeFirst(self) -> QItemSelectionRange """
        return QItemSelectionRange

    def takeLast(self): # real signature unknown; restored from __doc__
        """ takeLast(self) -> QItemSelectionRange """
        return QItemSelectionRange

    def __contains__(self, y): # real signature unknown; restored from __doc__
        """ x.__contains__(y) <==> y in x """
        pass

    def __delitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__delitem__(y) <==> del x[y] """
        pass

    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __getitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __ge__(self, y): # real signature unknown; restored from __doc__
        """ x.__ge__(y) <==> x>=y """
        pass

    def __gt__(self, y): # real signature unknown; restored from __doc__
        """ x.__gt__(y) <==> x>y """
        pass

    def __iadd__(self, y): # real signature unknown; restored from __doc__
        """ x.__iadd__(y) <==> x+=y """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """ x.__len__() <==> len(x) """
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

    def __setitem__(self, i, y): # real signature unknown; restored from __doc__
        """ x.__setitem__(i, y) <==> x[i]=y """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



