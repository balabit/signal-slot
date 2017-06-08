# coding: utf-8
#
# Copyright (c) 2000-2017 BalaBit
# All Rights Reserved.
#
# Author: Zoltán Máté <zoltan.mate@balabit.com>
#

"""
The signal-slot framework can be used to statically create method callbacks
without using interface superclasses in all mixin classes in the class hierarchy.

Slots can be registered to be called when a signal is called.
Only the slots belonging to the actual instance will be called.

Slots will be called
- with the same arguments as the arguments of the signal;
- at the end of the call of the signal;
The execution order of the slots is not defined.

Example:
>>> class A(object):
...     @signal
...     def startup(self):
...         print("Hello.")
...
...
>>> class X(A):
...     @slot(A.startup)
...     def make_my_special_startup_stuff(self):
...         print("Szia.")
...
...     @slot(A.startup)
...     def make_my_other_special_startup_stuff(self):
...         print("Salut.")
...
...
>>> class B(object):
...     @slot(A.startup)
...     def make_my_special_startup_stuff(self):
...         print("Ciao.")
...
...
>>> class Y(A, B):
...     @slot(A.startup)
...     def make_my_special_startup_stuff(self):
...         print("Bok.")
...
...
>>> X().startup()
Hello.
Szia.
Salut.

>>> Y().startup()
Hello.
Ciao.
Bok.
"""


__author__ = "Zoltán Máté <zoltan.mate@balabit.com>"


def signal(method):
    """
    Mark the decorated method as a signal.
    """
    def decorated_method(self, *args, **kwargs):
        result = method(self, *args, **kwargs)
        for callback in decorated_method._queue:
            if has_method(self, callback):
                callback(self, *args, **kwargs)
        return result
    decorated_method._queue = []
    return decorated_method


def has_method(obj, method):
    for cls in obj.__class__.__mro__:
        if method in cls.__dict__.values():
            return True
    return False


def slot(signal_method):
    """
    Mark the decorated method as a slot.
    """
    def wrap(method):
        def decorated_method(*args, **kwargs):
            return method(*args, **kwargs)
        signal_method._queue.append(decorated_method)
        return decorated_method
    return wrap
