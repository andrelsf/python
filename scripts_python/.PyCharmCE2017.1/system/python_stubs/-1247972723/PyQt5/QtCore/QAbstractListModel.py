# encoding: utf-8
# module PyQt5.QtCore
# from /usr/lib/python2.7/dist-packages/PyQt5/QtCore.x86_64-linux-gnu.so
# by generator 1.145
# no doc

# imports
import sip as __sip


from QAbstractItemModel import QAbstractItemModel

class QAbstractListModel(QAbstractItemModel):
    """ QAbstractListModel(parent: QObject = None) """
    def columnCount(self, *args, **kwargs): # real signature unknown
        pass

    def dropMimeData(self, QMimeData, Qt_DropAction, p_int, p_int_1, QModelIndex): # real signature unknown; restored from __doc__
        """ dropMimeData(self, QMimeData, Qt.DropAction, int, int, QModelIndex) -> bool """
        return False

    def flags(self, QModelIndex): # real signature unknown; restored from __doc__
        """ flags(self, QModelIndex) -> Qt.ItemFlags """
        pass

    def hasChildren(self, *args, **kwargs): # real signature unknown
        pass

    def index(self, p_int, column=0, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ index(self, int, column: int = 0, parent: QModelIndex = QModelIndex()) -> QModelIndex """
        pass

    def parent(self): # real signature unknown; restored from __doc__
        """ parent(self) -> QObject """
        return QObject

    def sibling(self, p_int, p_int_1, QModelIndex): # real signature unknown; restored from __doc__
        """ sibling(self, int, int, QModelIndex) -> QModelIndex """
        return QModelIndex

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


