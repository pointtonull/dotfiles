# encoding: utf-8
# module typing.io
# from /home/deimos/.virtualenvs/algorithms/lib/python3.6/site-packages/aiohttp/_frozenlist.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
""" Wrapper namespace for IO generic classes. """

# imports
import typing as __typing


# no functions
# classes

class IO(__typing.Generic):
    """
    Generic base class for TextIO and BinaryIO.
    
        This is an abstract, generic version of the return of open().
    
        NOTE: This does not distinguish between the different possible
        classes (text vs. binary, read vs. write vs. read/write,
        append-only, unbuffered).  The TextIO and BinaryIO subclasses
        below capture the distinctions between text vs. binary, which is
        pervasive in the interface; however we currently do not offer a
        way to track the other distinctions in the type system.
    """
# Error generating skeleton for function close: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them

# Error generating skeleton for function closed: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them

# Error generating skeleton for function fileno: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them

# Error generating skeleton for function flush: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them

# Error generating skeleton for function isatty: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them

# Error generating skeleton for function read: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them

# Error generating skeleton for function readable: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them

# Error generating skeleton for function readline: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them

# Error generating skeleton for function readlines: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them

# Error generating skeleton for function seek: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them

# Error generating skeleton for function seekable: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them

# Error generating skeleton for function tell: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them

# Error generating skeleton for function truncate: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them

# Error generating skeleton for function writable: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them

# Error generating skeleton for function write: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them

# Error generating skeleton for function writelines: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them

# Error generating skeleton for function __enter__: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them

# Error generating skeleton for function __exit__: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    _abc_cache = None # (!) real value is '<_weakrefset.WeakSet object at 0x7fadf590d198>'
    _abc_generic_negative_cache = None # (!) real value is '<_weakrefset.WeakSet object at 0x7fadf590d390>'
    _abc_generic_negative_cache_version = 35
    _abc_registry = None # (!) real value is '<_weakrefset.WeakSet object at 0x7fadf590d160>'
    _gorg = typing.IO # (!) forward: IO, real value is 'typing.IO'
    __abstractmethods__ = frozenset({'readable', '__enter__', 'writelines', '__exit__', 'flush', 'mode', 'tell', 'fileno', 'readlines', 'name', 'seek', 'write', 'writable', 'readline', 'read', 'isatty', 'closed', 'close', 'seekable', 'truncate'})
    __args__ = None
    __extra__ = None
    __next_in_mro__ = object
    __origin__ = None
    __orig_bases__ = (
        typing.Generic[~AnyStr],
    )
    __parameters__ = (
        None, # (!) real value is '~AnyStr'
    )
    __slots__ = ()
    __tree_hash__ = -9223372036852819186


class BinaryIO(__typing.IO):
    """ Typed version of the return of open() in binary mode. """
# Error generating skeleton for function write: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them

# Error generating skeleton for function __enter__: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _abc_cache = None # (!) real value is '<_weakrefset.WeakSet object at 0x7fadf590d5f8>'
    _abc_generic_negative_cache = None # (!) real value is '<_weakrefset.WeakSet object at 0x7fadf590d630>'
    _abc_generic_negative_cache_version = 35
    _abc_registry = None # (!) real value is '<_weakrefset.WeakSet object at 0x7fadf590d5c0>'
    _gorg = typing.BinaryIO # (!) forward: BinaryIO, real value is 'typing.BinaryIO'
    __abstractmethods__ = frozenset({'readable', '__enter__', 'writelines', '__exit__', 'flush', 'mode', 'tell', 'fileno', 'readlines', 'name', 'write', 'seek', 'writable', 'readline', 'read', 'isatty', 'closed', 'close', 'seekable', 'truncate'})
    __args__ = None
    __extra__ = None
    __next_in_mro__ = object
    __origin__ = None
    __orig_bases__ = (
        typing.IO[bytes],
    )
    __parameters__ = ()
    __slots__ = ()
    __tree_hash__ = -9223372036852819326


class TextIO(__typing.IO):
    """ Typed version of the return of open() in text mode. """
# Error generating skeleton for function __enter__: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    buffer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    encoding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    errors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    line_buffering = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    newlines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    _abc_cache = None # (!) real value is '<_weakrefset.WeakSet object at 0x7fadf590d860>'
    _abc_generic_negative_cache = None # (!) real value is '<_weakrefset.WeakSet object at 0x7fadf590d898>'
    _abc_generic_negative_cache_version = 35
    _abc_registry = None # (!) real value is '<_weakrefset.WeakSet object at 0x7fadf590d828>'
    _gorg = typing.TextIO # (!) forward: TextIO, real value is 'typing.TextIO'
    __abstractmethods__ = frozenset({'buffer', 'readable', '__enter__', 'newlines', 'writelines', '__exit__', 'flush', 'mode', 'errors', 'tell', 'readlines', 'encoding', 'fileno', 'name', 'seek', 'write', 'writable', 'readline', 'line_buffering', 'read', 'isatty', 'closed', 'close', 'seekable', 'truncate'})
    __args__ = None
    __extra__ = None
    __next_in_mro__ = object
    __origin__ = None
    __orig_bases__ = (
        typing.IO[str],
    )
    __parameters__ = ()
    __slots__ = ()
    __tree_hash__ = -9223372036852818799


# variables with complex values

__all__ = [
    'IO',
    'TextIO',
    'BinaryIO',
]

__weakref__ = None # (!) real value is "<attribute '__weakref__' of 'typing.io' objects>"

