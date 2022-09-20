from .Subject import Subject
from collections.abc import MutableSequence
from .NotifyType import NotifyUpdate, NotifyAdd, NotifyDelete


class NotifyList(MutableSequence, Subject):
    def __init__(self, type_list, data=None):
        super(NotifyList, self).__init__()
        if data is not None:
            if all(map(lambda x: isinstance(x, type_list), list(data))):
                self.__list = list(data)
            else:
                raise SyntaxError("List type does not match collection type")
        else:
            self.__list = list()
        self.__list_observer = []
        self.__type_list = type_list

    def __repr__(self):
        return "<{0} {1}>".format(self.__class__.__name__, self.__list)

    def __len__(self):
        return len(self.__list)

    def __getitem__(self, ii):
        if isinstance(ii, slice):
            return self.__class__(self.__list[ii])
        else:
            return self.__list[ii]

    def __delitem__(self, ii):
        self.notify(NotifyDelete(self.__list[ii]))
        del self.__list[ii]

    def __setitem__(self, ii, val):
        if isinstance(val, self.__type_list):
            self.__list[ii] = val
            self.notify(NotifyUpdate(val))
        else:
            raise SyntaxError("List type does not match collection type")

    def __str__(self):
        return str(self.__list)

    def insert(self, ii, val):
        if isinstance(val, self.__type_list):
            self.__list.insert(ii, val)
            self.notify(NotifyAdd(self.__list[ii]))
        else:
            raise SyntaxError("List type does not match collection type")

    def append(self, val):
        self.insert(len(self.__list), val)

    def attach(self, observer):
        self.__list_observer.append(observer)

    def detach(self, observer):
        self.__list_observer.remove(observer)

    def notify(self, type_notify):
        for observer in self.__list_observer:
            try:
                observer.update(type_notify)
            except AttributeError:
                observer(type_notify)

