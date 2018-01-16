#!/usr/bin/env python
# coding:utf-8
# Author: Yuanjun Ren


class LazyDB(object):
    def __init__(self):
        self.exists = 5

    def __getattr__(self, name):
        value = "Value for %s" % name
        setattr(self, name, value)
        return value


class LoggingLazyDB(LazyDB):
    def __getattr__(self, name):
        print("Called __getattr__(%s)" % name)
        return super().__getattr__(name)


class ValidatingDB(object):
    def __init__(self):
        self.exists = 5

    def __getattribute__(self, name):
        print("Called __getattribute__(%s)" % name)
        try:
            return super().__getattribute__(name)
        except AttributeError:
            value = "Value for %s" % name
            setattr(self, name, value)
            return value


class MissingPropertyDB(object):
    def __getattr__(self, name):
        if name == "bad_name":
            raise AttributeError("%s is missing" % name)


class DictionaryDB(object):
    def __init__(self, data):
        self._data = data

    def __getattribute__(self, name):
        data_dict = super().__getattribute__('_data')
        return data_dict[name]
        pass
    pass


if __name__ == "__main__":
    pass