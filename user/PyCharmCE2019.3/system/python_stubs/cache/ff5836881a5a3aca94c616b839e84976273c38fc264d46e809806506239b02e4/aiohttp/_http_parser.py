# encoding: utf-8
# module aiohttp._http_parser
# from /home/deimos/.virtualenvs/algorithms/lib/python3.6/site-packages/aiohttp/_http_parser.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import aiohttp.hdrs as hdrs # /home/deimos/.virtualenvs/algorithms/lib/python3.6/site-packages/aiohttp/hdrs.py
from multidict._multidict import _CIMultiDict, _CIMultiDictProxy

import aiohttp.http_exceptions as __aiohttp_http_exceptions
import aiohttp.streams as __aiohttp_streams


# Variables with simple values
i = 33

# functions

def parse_url(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_RawRequestMessage(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_RawResponseMessage(*args, **kwargs): # real signature unknown
    pass

# classes

class BadHttpMessage(__aiohttp_http_exceptions.HttpProcessingError):
    # no doc
# Error generating skeleton for function __init__: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them

    code = 400
    message = 'Bad Request'


class BadStatusLine(__aiohttp_http_exceptions.BadHttpMessage):
    # no doc
# Error generating skeleton for function __init__: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass


class PayloadEncodingError(__aiohttp_http_exceptions.BadHttpMessage):
    """ Base class for payload errors """
# Error generating skeleton for function __init__: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them


class ContentLengthError(__aiohttp_http_exceptions.PayloadEncodingError):
    """ Not enough data for satisfy content length header. """
# Error generating skeleton for function __init__: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them


class HttpRequestParser(HttpParser):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7fadf439cf90>'


class HttpResponseParser(HttpParser):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7fadf416a300>'


class InvalidHeader(__aiohttp_http_exceptions.BadHttpMessage):
    # no doc
# Error generating skeleton for function __init__: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them


class InvalidURLError(__aiohttp_http_exceptions.BadHttpMessage):
    # no doc
# Error generating skeleton for function __init__: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them


class LineTooLong(__aiohttp_http_exceptions.BadHttpMessage):
    # no doc
# Error generating skeleton for function __init__: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them


class RawRequestMessage(object):
    # no doc
    def _replace(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    chunked = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    compression = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    headers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    method = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    raw_headers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    should_close = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    upgrade = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    url = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class RawResponseMessage(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    chunked = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    compression = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    headers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    raw_headers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    reason = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    should_close = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    upgrade = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class TransferEncodingError(__aiohttp_http_exceptions.PayloadEncodingError):
    """ transfer encoding error. """
# Error generating skeleton for function __init__: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them


class _DeflateBuffer(object):
    """ DeflateStream decompress stream and feed data into specified stream. """
# Error generating skeleton for function begin_http_chunk_receiving: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them

# Error generating skeleton for function end_http_chunk_receiving: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them

# Error generating skeleton for function feed_data: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them

# Error generating skeleton for function feed_eof: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them

# Error generating skeleton for function set_exception: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them

# Error generating skeleton for function __init__: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'aiohttp.http_parser', '__doc__': 'DeflateStream decompress stream and feed data into specified stream.', '__init__': <function DeflateBuffer.__init__ at 0x7fadf417b598>, 'set_exception': <function DeflateBuffer.set_exception at 0x7fadf417b730>, 'feed_data': <function DeflateBuffer.feed_data at 0x7fadf417b7b8>, 'feed_eof': <function DeflateBuffer.feed_eof at 0x7fadf417b840>, 'begin_http_chunk_receiving': <function DeflateBuffer.begin_http_chunk_receiving at 0x7fadf417b8c8>, 'end_http_chunk_receiving': <function DeflateBuffer.end_http_chunk_receiving at 0x7fadf417b950>, '__dict__': <attribute '__dict__' of 'DeflateBuffer' objects>, '__weakref__': <attribute '__weakref__' of 'DeflateBuffer' objects>})"


class _HttpVersion(tuple):
    """ HttpVersion(major, minor) """
    def _asdict(self): # reliably restored by inspect
        """ Return a new OrderedDict which maps field names to their values. """
        pass

    @classmethod
    def _make(cls, *args, **kwargs): # real signature unknown
        """ Make a new HttpVersion object from a sequence or iterable """
        pass

    def _replace(_self, **kwds): # reliably restored by inspect
        """ Return a new HttpVersion object replacing specified fields with new values """
        pass

    def __getnewargs__(self): # reliably restored by inspect
        """ Return self as a plain tuple.  Used by copy and pickle. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(_cls, major, minor): # reliably restored by inspect
        """ Create new instance of HttpVersion(major, minor) """
        pass

    def __repr__(self): # reliably restored by inspect
        """ Return a nicely formatted representation string """
        pass

    major = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Alias for field number 0"""

    minor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Alias for field number 1"""


    _fields = (
        'major',
        'minor',
    )
    _source = "from builtins import property as _property, tuple as _tuple\nfrom operator import itemgetter as _itemgetter\nfrom collections import OrderedDict\n\nclass HttpVersion(tuple):\n    'HttpVersion(major, minor)'\n\n    __slots__ = ()\n\n    _fields = ('major', 'minor')\n\n    def __new__(_cls, major, minor):\n        'Create new instance of HttpVersion(major, minor)'\n        return _tuple.__new__(_cls, (major, minor))\n\n    @classmethod\n    def _make(cls, iterable, new=tuple.__new__, len=len):\n        'Make a new HttpVersion object from a sequence or iterable'\n        result = new(cls, iterable)\n        if len(result) != 2:\n            raise TypeError('Expected 2 arguments, got %d' % len(result))\n        return result\n\n    def _replace(_self, **kwds):\n        'Return a new HttpVersion object replacing specified fields with new values'\n        result = _self._make(map(kwds.pop, ('major', 'minor'), _self))\n        if kwds:\n            raise ValueError('Got unexpected field names: %r' % list(kwds))\n        return result\n\n    def __repr__(self):\n        'Return a nicely formatted representation string'\n        return self.__class__.__name__ + '(major=%r, minor=%r)' % self\n\n    def _asdict(self):\n        'Return a new OrderedDict which maps field names to their values.'\n        return OrderedDict(zip(self._fields, self))\n\n    def __getnewargs__(self):\n        'Return self as a plain tuple.  Used by copy and pickle.'\n        return tuple(self)\n\n    major = _property(_itemgetter(0), doc='Alias for field number 0')\n\n    minor = _property(_itemgetter(1), doc='Alias for field number 1')\n\n"
    __slots__ = ()


class _StreamReader(__aiohttp_streams.AsyncStreamReaderMixin):
    """
    An enhancement of asyncio.StreamReader.
    
        Supports asynchronous iteration by line, chunk or as available::
    
            async for line in reader:
                ...
            async for chunk in reader.iter_chunked(1024):
                ...
            async for slice in reader.iter_any():
                ...
    """
# Error generating skeleton for function at_eof: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them

# Error generating skeleton for function begin_http_chunk_receiving: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them

# Error generating skeleton for function end_http_chunk_receiving: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them

# Error generating skeleton for function exception: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them

# Error generating skeleton for function feed_data: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them

# Error generating skeleton for function feed_eof: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them

# Error generating skeleton for function is_eof: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them

# Error generating skeleton for function on_eof: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them

# Error generating skeleton for function read: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them

# Error generating skeleton for function readany: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them

# Error generating skeleton for function readchunk: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them

# Error generating skeleton for function readexactly: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them

# Error generating skeleton for function readline: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them

# Error generating skeleton for function read_nowait: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them

# Error generating skeleton for function set_exception: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them

# Error generating skeleton for function unread_data: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them

# Error generating skeleton for function wait_eof: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them

# Error generating skeleton for function _read_nowait: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them

# Error generating skeleton for function _read_nowait_chunk: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them

# Error generating skeleton for function _wait: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them

# Error generating skeleton for function __init__: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them

# Error generating skeleton for function __repr__: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them

    total_bytes = 0


class _URL(object):
    # no doc
    @classmethod
    def build(cls, *args, **kwargs): # real signature unknown
        """ Creates and returns a new URL """
        pass

    def human_repr(self): # reliably restored by inspect
        """ Return decoded human readable string for URL representation. """
        pass

    def is_absolute(self): # reliably restored by inspect
        """
        A check for absolute URLs.
        
                Return True for absolute ones (having scheme or starting
                with //), False otherwise.
        """
        pass

    def is_default_port(self): # reliably restored by inspect
        """
        A check for default port.
        
                Return True if port is default for specified scheme,
                e.g. 'http://python.org' or 'http://python.org:80', False
                otherwise.
        """
        pass

    def join(self, url): # reliably restored by inspect
        """
        Join URLs
        
                Construct a full (“absolute”) URL by combining a “base URL”
                (self) with another URL (url).
        
                Informally, this uses components of the base URL, in
                particular the addressing scheme, the network location and
                (part of) the path, to provide missing components in the
                relative URL.
        """
        pass

    def origin(self): # reliably restored by inspect
        """
        Return an URL with scheme, host and port parts only.
        
                user, password, path, query and fragment are removed.
        """
        pass

    def relative(self): # reliably restored by inspect
        """
        Return a relative part of the URL.
        
                scheme, user, password, host and port are removed.
        """
        pass

    def update_query(self, *args, **kwargs): # reliably restored by inspect
        """ Return a new URL with query part updated. """
        pass

    def with_fragment(self, fragment): # reliably restored by inspect
        """
        Return a new URL with fragment replaced.
        
                Autoencode fragment if needed.
        
                Clear fragment to default if None is passed.
        """
        pass

    def with_host(self, host): # reliably restored by inspect
        """
        Return a new URL with host replaced.
        
                Autoencode host if needed.
        
                Changing host for relative URLs is not allowed, use .join()
                instead.
        """
        pass

    def with_name(self, name): # reliably restored by inspect
        """
        Return a new URL with name (last part of path) replaced.
        
                Query and fragment parts are cleaned up.
        
                Name is encoded if needed.
        """
        pass

    def with_password(self, password): # reliably restored by inspect
        """
        Return a new URL with password replaced.
        
                Autoencode password if needed.
        
                Clear password if argument is None.
        """
        pass

# Error generating skeleton for function with_path: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them

    def with_port(self, port): # reliably restored by inspect
        """
        Return a new URL with port replaced.
        
                Clear port to default if None is passed.
        """
        pass

    def with_query(self, *args, **kwargs): # reliably restored by inspect
        """
        Return a new URL with query part replaced.
        
                Accepts any Mapping (e.g. dict, multidict.MultiDict instances)
                or str, autoencode the argument if needed.
        
                A sequence of (key, value) pairs is supported as well.
        
                It also can take an arbitrary number of keyword arguments.
        
                Clear query if None is passed.
        """
        pass

    def with_scheme(self, scheme): # reliably restored by inspect
        """ Return a new URL with scheme replaced. """
        pass

    def with_user(self, user): # reliably restored by inspect
        """
        Return a new URL with user replaced.
        
                Autoencode user if needed.
        
                Clear user/password if user is None.
        """
        pass

    @classmethod
    def _encode_host(cls, *args, **kwargs): # real signature unknown
        pass

    def _FRAGMENT_QUOTER(self, *args, **kwargs): # real signature unknown
        pass

    def _get_str_query(self, *args, **kwargs): # reliably restored by inspect
        # no doc
        pass

    @classmethod
    def _make_netloc(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def _normalize_path(cls, *args, **kwargs): # real signature unknown
        pass

    def _PATH_QUOTER(self, *args, **kwargs): # real signature unknown
        pass

    def _PATH_UNQUOTER(self, *args, **kwargs): # real signature unknown
        pass

    def _QS_UNQUOTER(self, *args, **kwargs): # real signature unknown
        pass

    def _QUERY_PART_QUOTER(self, *args, **kwargs): # real signature unknown
        pass

    def _QUERY_QUOTER(self, *args, **kwargs): # real signature unknown
        pass

    def _query_var(v): # reliably restored by inspect
        # no doc
        pass

    def _QUOTER(self, *args, **kwargs): # real signature unknown
        pass

    def _UNQUOTER(self, *args, **kwargs): # real signature unknown
        pass

    def _validate_authority_uri_abs_path(host, path): # reliably restored by inspect
        """
        Ensure that path in URL with authority starts with a leading slash.
        
                Raise ValueError if not.
        """
        pass

# Error generating skeleton for function __bool__: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them

    def __eq__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __getstate__(self): # reliably restored by inspect
        # no doc
        pass

    def __ge__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __gt__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __hash__(self): # reliably restored by inspect
        # no doc
        pass

    @classmethod
    def __init_subclass__(cls, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __lt__(self, other): # reliably restored by inspect
        # no doc
        pass

    @staticmethod # known case of __new__
# Error generating skeleton for function __new__: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them

    def __repr__(self): # reliably restored by inspect
        # no doc
        pass

    def __setstate__(self, state): # reliably restored by inspect
        # no doc
        pass

    def __str__(self): # reliably restored by inspect
        # no doc
        pass

    def __truediv__(self, name): # reliably restored by inspect
        # no doc
        pass

    explicit_port = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Port part of URL, without scheme-based fallback.

        None for relative URLs or URLs without explicit port.

        """

    port = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Port part of URL, with scheme-based fallback.

        None for relative URLs or URLs without explicit port and
        scheme without default port substitution.

        """

    raw_fragment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Encoded fragment part of URL.

        Empty string if fragment is missing.

        """

    raw_host = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Encoded host part of URL.

        None for relative URLs.

        """

    raw_password = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Encoded password part of URL.

        None if password is missing.

        """

    raw_path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Encoded path of URL.

        / for absolute URLs without path part.

        """

    raw_query_string = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Encoded query part of URL.

        Empty string if query is missing.

        """

    raw_user = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Encoded user part of URL.

        None if user is missing.

        """

    scheme = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Scheme for absolute URLs.

        Empty string for relative URLs or URLs starting with //

        """

    _cache = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _val = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    fragment = None # (!) real value is '<yarl.cached_property object at 0x7fadf47f16d8>'
    host = None # (!) real value is '<yarl.cached_property object at 0x7fadf47d1e10>'
    name = None # (!) real value is '<yarl.cached_property object at 0x7fadf47f1b38>'
    parent = None # (!) real value is '<yarl.cached_property object at 0x7fadf47f1ac8>'
    parts = None # (!) real value is '<yarl.cached_property object at 0x7fadf47f17f0>'
    password = None # (!) real value is '<yarl.cached_property object at 0x7fadf47c24a8>'
    path = None # (!) real value is '<yarl.cached_property object at 0x7fadf47d1320>'
    path_qs = None # (!) real value is '<yarl.cached_property object at 0x7fadf47f1240>'
    query = None # (!) real value is '<yarl.cached_property object at 0x7fadf47d1748>'
    query_string = None # (!) real value is '<yarl.cached_property object at 0x7fadf47f1208>'
    raw_name = None # (!) real value is '<yarl.cached_property object at 0x7fadf47f1b00>'
    raw_parts = None # (!) real value is '<yarl.cached_property object at 0x7fadf47f1630>'
    raw_path_qs = None # (!) real value is '<yarl.cached_property object at 0x7fadf47f1710>'
    user = None # (!) real value is '<yarl.cached_property object at 0x7fadf47c2320>'
    __slots__ = (
        '_cache',
        '_val',
    )


# variables with complex values

_EMPTY_PAYLOAD = None # (!) real value is '<aiohttp.streams.EmptyStreamReader object at 0x7fadf4166e48>'

_HttpVersion10 = (
    1,
    0,
)

_HttpVersion11 = (
    1,
    1,
)

__all__ = (
    'HttpRequestParser',
    'HttpResponseParser',
    'RawRequestMessage',
    'RawResponseMessage',
)

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7fadf4179470>'

__spec__ = None # (!) real value is "ModuleSpec(name='aiohttp._http_parser', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7fadf4179470>, origin='/home/deimos/.virtualenvs/algorithms/lib/python3.6/site-packages/aiohttp/_http_parser.cpython-36m-x86_64-linux-gnu.so')"

__test__ = {}

