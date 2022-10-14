#!/usr/bin/python3


class Storage:
    """ Class interface for Storage Engines """

    def all(self, cls=None):
        """ Returns the list of objects of one type of class. All types if None. """
        raise NotImplemented

    def new(self, obj):
        raise NotImplemented

    def save(self):
        raise NotImplemented

    def reload(self):
        raise NotImplemented

    def delete(self, obj=None):
        """ deletes obj - if obj is equal to None, the method should not do anything """
        raise NotImplemented