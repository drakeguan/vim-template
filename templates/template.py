#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set hls is ai et sw=4 sts=4 ts=8 nu ft=python:
#
# Copyright © %YEAR% %USER% <%MAIL%>
#
# Distributed under terms of the %LICENSE% license.

###############################################################################
# Module docstring
###############################################################################
u"""Summary of the module in one sentence.

%HERE% Description of the module in multiple lines.

.. note::

    note

.. warning::

    warning

.. seealso:: modules :mod:`dracula`, :mod:`main`

Code ::

    def foo():
        print 'bar'

Code::

    class Foo:
        pass

===============
Module contents
===============

Variables:

* :data:`FOO`
* :data:`BAR`

Exceptions:

* :class:`FooError` - Short summary
* :class:`BarError` (or none)

Functions:

* :func:`getBar`

Classes:

* :class:`Foo`

========
Examples
========

    >>> import foobar
    >>> foobar.foo()
    123
    >>> foobar.bar()
    abc

==============
Module members
==============

"""


###############################################################################
# Import modules
###############################################################################

# Built-in modules
import sys
# Additional modules

# local modules


###############################################################################
# Constants
###############################################################################

#FOO = 123
#u"""docstring of FOO"""



###############################################################################
# Exceptions
###############################################################################

#class FooError(Exception):
    #u"""docstring of FooError"""



###############################################################################
# Functions
###############################################################################

def getBar(arg1, arg2='default'):
    u"""Summary of the function in one sentence.

    Description of the function in multiple lines.

    :param arg1: description of arg1
    :type  arg1: int
    :param arg2: description of arg2
    :type  arg2: str

    :returns: description of return value
    :rtype: type of return value

    :raises BarError: description of exception.

    Examples:

        >>> bar(123)
        456
        >>> bar(456, 'xxx')
        abc
        >>> bar()
        Traceback (most recent call last):
        ...
        BarError: error message

    """
    return BAR


###############################################################################
# Classes
###############################################################################

class Foo(object): # Use CamelCase for class name
    u"""Brief description of the class.

    Detailed description of the class.

    Attributes:

    * :attr:`var1` - summary
    * :attr:`var2`

    Methods:

    * :meth:`doSomething`
    * :meth:`meth1` - summary
    * :meth:`meth2`

    Signals:

    * :meth:`fooSignal`
    * :meth:`barSignal`

    Examples:

        >>> foo = Foo()
        >>> foo.bar()
        bar

    """
    # Class properties
    var1 = (1, 2, 3)
    u"""docstring for var1."""

    # Class methods or static methods
    @staticmethod
    def doSomething():
        u"""docstring same as method"""
        pass

    # Private methods
    #  use __ prefix for private methods
    def __private1(self):
        u"""Invisible in document."""

    # Public methods
    def __init__(self, arg):
        u"""Constructor:

        Description of constructor.

        :param arg: description of arg
        :type  arg: str

        """

        # Member data
        self.a = None
        self.b = None

    def meth1(self, arg1, arg2=u""):
        u"""Summary of the method.

        Description of the method.

        :param arg1: description of arg1
        :type  arg1: int
        :param arg2:
        :type  arg2:

        :returns: description of return value
        :rtype: type of return value

        :raises FooError: if arg is not a unicode string

        Examples:

            >>> foo = Foo()
            >>> foo.foo(u"foo")
            foo
            >>> foo.foo(123)
            Traceback (most recent call last):
              ...
            FooError: 123 is not a unicode string

        """

        if arg == u"":
            return FOO
        elif not isinstance(arg, unicode):
            raise FooError, u"%s is not a unicode string" % repr(arg)
        else:
            return arg

    def meth2(self, fieldType=None, sort=False):
        u"""Summary of the method."""
        pass




###############################################################################
# Main
###############################################################################

def main(argv=sys.argv[:]):
    """Empty main."""
    pass

if __name__ == '__main__':
    sys.exit(main())
