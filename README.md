# Signal-slot framework in [Python](https://www.python.org/)

## Overview

The signal-slot framework can be used to statically create method callbacks
without using interface superclasses in all mixin classes in the class hierarchy.

Slots can be registered to be called when a signal is called.
Only the slots belonging to the actual instance will be called.

Slots will be called
- with the same arguments as the arguments of the signal;
- at the end of the call of the signal;

The execution order of the slots is not defined.

## Usage

There is a detailed example in [the python module](./signal_slot.py).
Test it by `python -m doctest -v`.

## Note

The framework is publicated "AS IS", further development is not guaranteed.
