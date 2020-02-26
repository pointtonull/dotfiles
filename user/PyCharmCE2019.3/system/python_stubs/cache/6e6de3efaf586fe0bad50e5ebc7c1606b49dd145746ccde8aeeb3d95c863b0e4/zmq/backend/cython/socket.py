# encoding: utf-8
# module zmq.backend.cython.socket
# from /usr/lib/python3/dist-packages/zmq/backend/cython/socket.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
""" 0MQ Socket class. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import copy as copy_mod # /usr/lib/python3.6/copy.py
import time as time # <module 'time' (built-in)>
import sys as sys # <module 'sys' (built-in)>
import random as random # /usr/lib/python3.6/random.py
import struct as struct # /usr/lib/python3.6/struct.py
import codecs as codecs # /usr/lib/python3.6/codecs.py
import pickle as pickle # /usr/lib/python3.6/pickle.py
import zmq as zmq # /usr/lib/python3/dist-packages/zmq/__init__.py
import zmq.backend.cython.constants as constants # /usr/lib/python3/dist-packages/zmq/backend/cython/constants.cpython-36m-x86_64-linux-gnu.so
import zmq.error as __zmq_error


# Variables with simple values

AFFINITY = 4

BACKLOG = 19

BLOCKY = 70

CLIENT = -9999

CONFLATE = 54

CONNECT_RID = 61
CONNECT_TIMEOUT = 79

cPickle = None

CURVE = 2

CURVE_PUBLICKEY = 48
CURVE_SECRETKEY = 49
CURVE_SERVER = 47
CURVE_SERVERKEY = 50

DEALER = 5

DELAY_ATTACH_ON_CONNECT = 39

DGRAM = -9999

DISH = -9999

DONTWAIT = 1
DOWNSTREAM = -9999

DRAFT_API = 0

EADDRINUSE = 98
EADDRNOTAVAIL = 99
EAFNOSUPPORT = 97
EAGAIN = 11

ECONNABORTED = 103
ECONNREFUSED = 111
ECONNRESET = 104

EFAULT = 14
EFSM = 156384763

EHOSTUNREACH = 113

EINPROGRESS = 115
EINVAL = 22

EMSGSIZE = 90
EMTHREAD = 156384766

ENETDOWN = 100
ENETRESET = 102
ENETUNREACH = 101
ENOBUFS = 105
ENOCOMPATPROTO = 156384764
ENODEV = 19
ENOMEM = 12
ENOTCONN = 107
ENOTSOCK = 88
ENOTSUP = 95

EPROTONOSUPPORT = 93

ETERM = 156384765
ETIMEDOUT = 110

EVENTS = 15

EVENT_ACCEPTED = 32

EVENT_ACCEPT_FAILED = 64

EVENT_ALL = 65535

EVENT_BIND_FAILED = 16

EVENT_CLOSED = 128

EVENT_CLOSE_FAILED = 256

EVENT_CONNECTED = 1

EVENT_CONNECT_DELAYED = 2
EVENT_CONNECT_RETRIED = 4

EVENT_DISCONNECTED = 512
EVENT_LISTENING = 8

EVENT_MONITOR_STOPPED = 1024

FAIL_UNROUTABLE = 33

FD = 14

FORWARDER = 2

GATHER = -9999

GSSAPI = 3

GSSAPI_PLAINTEXT = 65
GSSAPI_PRINCIPAL = 63
GSSAPI_SERVER = 62

GSSAPI_SERVICE_PRINCIPAL = 64

HANDSHAKE_IVL = 66

HAUSNUMERO = 156384712

HEARTBEAT_IVL = 75
HEARTBEAT_TIMEOUT = 77
HEARTBEAT_TTL = 76

HWM = -9999

IDENTITY = 5

IMMEDIATE = 39

INVERT_MATCHING = 74

IO_THREADS = 1

IO_THREADS_DFLT = 1

IPC_FILTER_GID = 60
IPC_FILTER_PID = 58
IPC_FILTER_UID = 59

IPC_PATH_MAX_LEN = 107

IPV4ONLY = 31
IPV6 = 42

LAST_ENDPOINT = 32

LINGER = 17

MAXMSGSIZE = 22

MAX_SOCKETS = 2

MAX_SOCKETS_DFLT = 1023

MCAST_LOOP = -9999

MECHANISM = 43

MORE = 1

MULTICAST_HOPS = 25
MULTICAST_MAXTPDU = 84

NOBLOCK = 1

NULL = 0

PAIR = 0

PLAIN = 1

PLAIN_PASSWORD = 46
PLAIN_SERVER = 44
PLAIN_USERNAME = 45

POLLERR = 4
POLLIN = 1

POLLITEMS_DFLT = 16

POLLOUT = 2
POLLPRI = 8

PROBE_ROUTER = 51

PUB = 1
PULL = 7
PUSH = 8

QUEUE = 3

RADIO = -9999
RATE = 8

RCVBUF = 12
RCVHWM = 24
RCVMORE = 13
RCVTIMEO = 27

RECONNECT_IVL = 18

RECONNECT_IVL_MAX = 21

RECOVERY_IVL = 9

RECOVERY_IVL_MSEC = -9999

REP = 4
REQ = 3

REQ_CORRELATE = 52
REQ_RELAXED = 53

ROUTER = 6

ROUTER_BEHAVIOR = 33
ROUTER_HANDOVER = 56
ROUTER_MANDATORY = 33
ROUTER_RAW = 41

SCATTER = -9999

SERVER = -9999

SHARED = 3

SNDBUF = 11
SNDHWM = 23
SNDMORE = 2
SNDTIMEO = 28

SOCKET_LIMIT = 3

SOCKS_PROXY = 68

SRCFD = 2

STREAM = 11
STREAMER = 1

STREAM_NOTIFY = 73

SUB = 2
SUBSCRIBE = 6

SWAP = -9999

TCP_ACCEPT_FILTER = 38

TCP_KEEPALIVE = 34

TCP_KEEPALIVE_CNT = 35
TCP_KEEPALIVE_IDLE = 36
TCP_KEEPALIVE_INTVL = 37

TCP_MAXRT = 80

THREAD_PRIORITY = 3

THREAD_PRIORITY_DFLT = -1

THREAD_SAFE = 81

THREAD_SCHED_POLICY = 4

THREAD_SCHED_POLICY_DFLT = -1

TOS = 57

TYPE = 16

UNSUBSCRIBE = 7

UPSTREAM = -9999

USE_FD = 89

VERSION = 40201

VERSION_MAJOR = 4
VERSION_MINOR = 2
VERSION_PATCH = 1

VMCI_BUFFER_MAX_SIZE = 87

VMCI_BUFFER_MIN_SIZE = 86

VMCI_BUFFER_SIZE = 85

VMCI_CONNECT_TIMEOUT = 88

XPUB = 9

XPUB_MANUAL = 71
XPUB_NODROP = 69
XPUB_VERBOSE = 40
XPUB_VERBOSER = 78

XPUB_WELCOME_MSG = 72

XREP = 6
XREQ = 5

XSUB = 10

ZAP_DOMAIN = 55

# functions

def _check_version(min_version_info, msg=None): # reliably restored by inspect
    """
    Check for libzmq
        
        raises ZMQVersionError if current zmq version is not at least min_version
        
        min_version_info is a tuple of integers, and will be compared against zmq.zmq_version_info().
    """
    pass

# classes

class bytes(object):
    """
    bytes(iterable_of_ints) -> bytes
    bytes(string, encoding[, errors]) -> bytes
    bytes(bytes_or_buffer) -> immutable copy of bytes_or_buffer
    bytes(int) -> bytes object of size given by the parameter initialized with null bytes
    bytes() -> empty bytes object
    
    Construct an immutable array of bytes from:
      - an iterable yielding integers in range(256)
      - a text string encoded using the specified encoding
      - any object implementing the buffer API.
      - an integer
    """
    def capitalize(self): # real signature unknown; restored from __doc__
        """
        B.capitalize() -> copy of B
        
        Return a copy of B with only its first character capitalized (ASCII)
        and the rest lower-cased.
        """
        pass

    def center(self, width, fillchar=None): # real signature unknown; restored from __doc__
        """
        B.center(width[, fillchar]) -> copy of B
        
        Return B centered in a string of length width.  Padding is
        done using the specified fill character (default is a space).
        """
        pass

    def count(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        B.count(sub[, start[, end]]) -> int
        
        Return the number of non-overlapping occurrences of subsection sub in
        bytes B[start:end].  Optional arguments start and end are interpreted
        as in slice notation.
        """
        return 0

    def decode(self, *args, **kwargs): # real signature unknown
        """
        Decode the bytes using the codec registered for encoding.
        
          encoding
            The encoding with which to decode the bytes.
          errors
            The error handling scheme to use for the handling of decoding errors.
            The default is 'strict' meaning that decoding errors raise a
            UnicodeDecodeError. Other possible values are 'ignore' and 'replace'
            as well as any other name registered with codecs.register_error that
            can handle UnicodeDecodeErrors.
        """
        pass

    def endswith(self, suffix, start=None, end=None): # real signature unknown; restored from __doc__
        """
        B.endswith(suffix[, start[, end]]) -> bool
        
        Return True if B ends with the specified suffix, False otherwise.
        With optional start, test B beginning at that position.
        With optional end, stop comparing B at that position.
        suffix can also be a tuple of bytes to try.
        """
        return False

    def expandtabs(self, tabsize=8): # real signature unknown; restored from __doc__
        """
        B.expandtabs(tabsize=8) -> copy of B
        
        Return a copy of B where all tab characters are expanded using spaces.
        If tabsize is not given, a tab size of 8 characters is assumed.
        """
        pass

    def find(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        B.find(sub[, start[, end]]) -> int
        
        Return the lowest index in B where subsection sub is found,
        such that sub is contained within B[start,end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Return -1 on failure.
        """
        return 0

    @classmethod
    def fromhex(cls, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Create a bytes object from a string of hexadecimal numbers.
        
        Spaces between two numbers are accepted.
        Example: bytes.fromhex('B9 01EF') -> b'\\xb9\\x01\\xef'.
        """
        pass

    def hex(self): # real signature unknown; restored from __doc__
        """
        B.hex() -> string
        
        Create a string of hexadecimal numbers from a bytes object.
        Example: b'\xb9\x01\xef'.hex() -> 'b901ef'.
        """
        return ""

    def index(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        B.index(sub[, start[, end]]) -> int
        
        Return the lowest index in B where subsection sub is found,
        such that sub is contained within B[start,end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Raises ValueError when the subsection is not found.
        """
        return 0

    def isalnum(self): # real signature unknown; restored from __doc__
        """
        B.isalnum() -> bool
        
        Return True if all characters in B are alphanumeric
        and there is at least one character in B, False otherwise.
        """
        return False

    def isalpha(self): # real signature unknown; restored from __doc__
        """
        B.isalpha() -> bool
        
        Return True if all characters in B are alphabetic
        and there is at least one character in B, False otherwise.
        """
        return False

    def isdigit(self): # real signature unknown; restored from __doc__
        """
        B.isdigit() -> bool
        
        Return True if all characters in B are digits
        and there is at least one character in B, False otherwise.
        """
        return False

    def islower(self): # real signature unknown; restored from __doc__
        """
        B.islower() -> bool
        
        Return True if all cased characters in B are lowercase and there is
        at least one cased character in B, False otherwise.
        """
        return False

    def isspace(self): # real signature unknown; restored from __doc__
        """
        B.isspace() -> bool
        
        Return True if all characters in B are whitespace
        and there is at least one character in B, False otherwise.
        """
        return False

    def istitle(self): # real signature unknown; restored from __doc__
        """
        B.istitle() -> bool
        
        Return True if B is a titlecased string and there is at least one
        character in B, i.e. uppercase characters may only follow uncased
        characters and lowercase characters only cased ones. Return False
        otherwise.
        """
        return False

    def isupper(self): # real signature unknown; restored from __doc__
        """
        B.isupper() -> bool
        
        Return True if all cased characters in B are uppercase and there is
        at least one cased character in B, False otherwise.
        """
        return False

    def join(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Concatenate any number of bytes objects.
        
        The bytes whose method is called is inserted in between each pair.
        
        The result is returned as a new bytes object.
        
        Example: b'.'.join([b'ab', b'pq', b'rs']) -> b'ab.pq.rs'.
        """
        pass

    def ljust(self, width, fillchar=None): # real signature unknown; restored from __doc__
        """
        B.ljust(width[, fillchar]) -> copy of B
        
        Return B left justified in a string of length width. Padding is
        done using the specified fill character (default is a space).
        """
        pass

    def lower(self): # real signature unknown; restored from __doc__
        """
        B.lower() -> copy of B
        
        Return a copy of B with all ASCII characters converted to lowercase.
        """
        pass

    def lstrip(self, *args, **kwargs): # real signature unknown
        """
        Strip leading bytes contained in the argument.
        
        If the argument is omitted or None, strip leading  ASCII whitespace.
        """
        pass

    def maketrans(self, *args, **kwargs): # real signature unknown
        """
        Return a translation table useable for the bytes or bytearray translate method.
        
        The returned table will be one where each byte in frm is mapped to the byte at
        the same position in to.
        
        The bytes objects frm and to must be of the same length.
        """
        pass

    def partition(self, *args, **kwargs): # real signature unknown
        """
        Partition the bytes into three parts using the given separator.
        
        This will search for the separator sep in the bytes. If the separator is found,
        returns a 3-tuple containing the part before the separator, the separator
        itself, and the part after it.
        
        If the separator is not found, returns a 3-tuple containing the original bytes
        object and two empty bytes objects.
        """
        pass

    def replace(self, *args, **kwargs): # real signature unknown
        """
        Return a copy with all occurrences of substring old replaced by new.
        
          count
            Maximum number of occurrences to replace.
            -1 (the default value) means replace all occurrences.
        
        If the optional argument count is given, only the first count occurrences are
        replaced.
        """
        pass

    def rfind(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        B.rfind(sub[, start[, end]]) -> int
        
        Return the highest index in B where subsection sub is found,
        such that sub is contained within B[start,end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Return -1 on failure.
        """
        return 0

    def rindex(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        B.rindex(sub[, start[, end]]) -> int
        
        Return the highest index in B where subsection sub is found,
        such that sub is contained within B[start,end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Raise ValueError when the subsection is not found.
        """
        return 0

    def rjust(self, width, fillchar=None): # real signature unknown; restored from __doc__
        """
        B.rjust(width[, fillchar]) -> copy of B
        
        Return B right justified in a string of length width. Padding is
        done using the specified fill character (default is a space)
        """
        pass

    def rpartition(self, *args, **kwargs): # real signature unknown
        """
        Partition the bytes into three parts using the given separator.
        
        This will search for the separator sep in the bytes, starting at the end. If
        the separator is found, returns a 3-tuple containing the part before the
        separator, the separator itself, and the part after it.
        
        If the separator is not found, returns a 3-tuple containing two empty bytes
        objects and the original bytes object.
        """
        pass

    def rsplit(self, *args, **kwargs): # real signature unknown
        """
        Return a list of the sections in the bytes, using sep as the delimiter.
        
          sep
            The delimiter according which to split the bytes.
            None (the default value) means split on ASCII whitespace characters
            (space, tab, return, newline, formfeed, vertical tab).
          maxsplit
            Maximum number of splits to do.
            -1 (the default value) means no limit.
        
        Splitting is done starting at the end of the bytes and working to the front.
        """
        pass

    def rstrip(self, *args, **kwargs): # real signature unknown
        """
        Strip trailing bytes contained in the argument.
        
        If the argument is omitted or None, strip trailing ASCII whitespace.
        """
        pass

    def split(self, *args, **kwargs): # real signature unknown
        """
        Return a list of the sections in the bytes, using sep as the delimiter.
        
          sep
            The delimiter according which to split the bytes.
            None (the default value) means split on ASCII whitespace characters
            (space, tab, return, newline, formfeed, vertical tab).
          maxsplit
            Maximum number of splits to do.
            -1 (the default value) means no limit.
        """
        pass

    def splitlines(self, *args, **kwargs): # real signature unknown
        """
        Return a list of the lines in the bytes, breaking at line boundaries.
        
        Line breaks are not included in the resulting list unless keepends is given and
        true.
        """
        pass

    def startswith(self, prefix, start=None, end=None): # real signature unknown; restored from __doc__
        """
        B.startswith(prefix[, start[, end]]) -> bool
        
        Return True if B starts with the specified prefix, False otherwise.
        With optional start, test B beginning at that position.
        With optional end, stop comparing B at that position.
        prefix can also be a tuple of bytes to try.
        """
        return False

    def strip(self, *args, **kwargs): # real signature unknown
        """
        Strip leading and trailing bytes contained in the argument.
        
        If the argument is omitted or None, strip leading and trailing ASCII whitespace.
        """
        pass

    def swapcase(self): # real signature unknown; restored from __doc__
        """
        B.swapcase() -> copy of B
        
        Return a copy of B with uppercase ASCII characters converted
        to lowercase ASCII and vice versa.
        """
        pass

    def title(self): # real signature unknown; restored from __doc__
        """
        B.title() -> copy of B
        
        Return a titlecased version of B, i.e. ASCII words start with uppercase
        characters, all remaining cased characters have lowercase.
        """
        pass

    def translate(self, *args, **kwargs): # real signature unknown
        """
        Return a copy with each character mapped by the given translation table.
        
          table
            Translation table, which must be a bytes object of length 256.
        
        All characters occurring in the optional argument delete are removed.
        The remaining characters are mapped through the given translation table.
        """
        pass

    def upper(self): # real signature unknown; restored from __doc__
        """
        B.upper() -> copy of B
        
        Return a copy of B with all ASCII characters converted to uppercase.
        """
        pass

    def zfill(self, width): # real signature unknown; restored from __doc__
        """
        B.zfill(width) -> copy of B
        
        Pad a numeric string B with zeros on the left, to fill a field
        of the specified width.  B is never truncated.
        """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Return key in self. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __getnewargs__(self, *args, **kwargs): # real signature unknown
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, iterable_of_ints): # real signature unknown; restored from __doc__
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mod__(self, *args, **kwargs): # real signature unknown
        """ Return self%value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass


class ZMQError(__zmq_error.ZMQBaseError):
    """
    Wrap an errno style error.
    
        Parameters
        ----------
        errno : int
            The ZMQ errno or None.  If None, then ``zmq_errno()`` is called and
            used.
        msg : string
            Description of the error or None.
    """
    def __init__(self, errno=None, msg=None): # reliably restored by inspect
        """
        Wrap an errno style error.
        
                Parameters
                ----------
                errno : int
                    The ZMQ errno or None.  If None, then ``zmq_errno()`` is called and
                    used.
                msg : string
                    Description of the error or None.
        """
        pass

    def __repr__(self): # reliably restored by inspect
        # no doc
        pass

    def __str__(self): # reliably restored by inspect
        # no doc
        pass

    errno = None


class InterruptedSystemCall(__zmq_error.ZMQError, InterruptedError):
    """
    Wrapper for EINTR
        
        This exception should be caught internally in pyzmq
        to retry system calls, and not propagate to the user.
        
        .. versionadded:: 14.7
    """
    def __init__(self, errno=None, msg=None): # reliably restored by inspect
        # no doc
        pass

    def __str__(self): # reliably restored by inspect
        # no doc
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class Socket(object):
    """
    Socket(context, socket_type)
    
        A 0MQ socket.
    
        These objects will generally be constructed via the socket() method of a Context object.
        
        Note: 0MQ Sockets are *not* threadsafe. **DO NOT** share them across threads.
        
        Parameters
        ----------
        context : Context
            The 0MQ Context this Socket belongs to.
        socket_type : int
            The socket type, which can be any of the 0MQ socket types: 
            REQ, REP, PUB, SUB, PAIR, DEALER, ROUTER, PULL, PUSH, XPUB, XSUB.
        
        See Also
        --------
        .Context.socket : method for creating a socket bound to a Context.
    """
    def bind(self, addr): # real signature unknown; restored from __doc__
        """
        s.bind(addr)
        
                Bind the socket to an address.
        
                This causes the socket to listen on a network port. Sockets on the
                other side of this connection will use ``Socket.connect(addr)`` to
                connect to this socket.
        
                Parameters
                ----------
                addr : str
                    The address string. This has the form 'protocol://interface:port',
                    for example 'tcp://127.0.0.1:5555'. Protocols supported include
                    tcp, udp, pgm, epgm, inproc and ipc. If the address is unicode, it is
                    encoded to utf-8 first.
        """
        pass

    def close(self, linger=None): # real signature unknown; restored from __doc__
        """
        s.close(linger=None)
        
                Close the socket.
                
                If linger is specified, LINGER sockopt will be set prior to closing.
        
                This can be called to close the socket by hand. If this is not
                called, the socket will automatically be closed when it is
                garbage collected.
        """
        pass

    def connect(self, addr): # real signature unknown; restored from __doc__
        """
        s.connect(addr)
        
                Connect to a remote 0MQ socket.
        
                Parameters
                ----------
                addr : str
                    The address string. This has the form 'protocol://interface:port',
                    for example 'tcp://127.0.0.1:5555'. Protocols supported are
                    tcp, upd, pgm, inproc and ipc. If the address is unicode, it is
                    encoded to utf-8 first.
        """
        pass

    def disconnect(self, addr): # real signature unknown; restored from __doc__
        """
        s.disconnect(addr)
        
                Disconnect from a remote 0MQ socket (undoes a call to connect).
                
                .. versionadded:: libzmq-3.2
                .. versionadded:: 13.0
        
                Parameters
                ----------
                addr : str
                    The address string. This has the form 'protocol://interface:port',
                    for example 'tcp://127.0.0.1:5555'. Protocols supported are
                    tcp, upd, pgm, inproc and ipc. If the address is unicode, it is
                    encoded to utf-8 first.
        """
        pass

    def get(self, option): # real signature unknown; restored from __doc__
        """
        s.get(option)
        
                Get the value of a socket option.
        
                See the 0MQ API documentation for details on specific options.
        
                Parameters
                ----------
                option : int
                    The option to get.  Available values will depend on your
                    version of libzmq.  Examples include::
                    
                        zmq.IDENTITY, HWM, LINGER, FD, EVENTS
        
                Returns
                -------
                optval : int or bytes
                    The value of the option as a bytestring or int.
        """
        pass

    def monitor(self, addr, flags): # real signature unknown; restored from __doc__
        """
        s.monitor(addr, flags)
        
                Start publishing socket events on inproc.
                See libzmq docs for zmq_monitor for details.
                
                While this function is available from libzmq 3.2,
                pyzmq cannot parse monitor messages from libzmq prior to 4.0.
                
                .. versionadded: libzmq-3.2
                .. versionadded: 14.0
                
                Parameters
                ----------
                addr : str
                    The inproc url used for monitoring. Passing None as
                    the addr will cause an existing socket monitor to be
                    deregistered.
                events : int [default: zmq.EVENT_ALL]
                    The zmq event bitmask for which events will be sent to the monitor.
        """
        pass

    def recv(self, flags=0, copy=True, track=False): # real signature unknown; restored from __doc__
        """
        s.recv(flags=0, copy=True, track=False)
        
                Receive a message.
        
                Parameters
                ----------
                flags : int
                    Any supported flag: NOBLOCK. If NOBLOCK is set, this method
                    will raise a ZMQError with EAGAIN if a message is not ready.
                    If NOBLOCK is not set, then this method will block until a
                    message arrives.
                copy : bool
                    Should the message be received in a copying or non-copying manner?
                    If False a Frame object is returned, if True a string copy of
                    message is returned.
                track : bool
                    Should the message be tracked for notification that ZMQ has
                    finished with it? (ignored if copy=True)
        
                Returns
                -------
                msg : bytes, Frame
                    The received message frame.  If `copy` is False, then it will be a Frame,
                    otherwise it will be bytes.
                    
                Raises
                ------
                ZMQError
                    for any of the reasons zmq_msg_recv might fail.
        """
        pass

    def send(self, data, flags=0, copy=True, track=False): # real signature unknown; restored from __doc__
        """
        s.send(data, flags=0, copy=True, track=False)
        
                Send a message on this socket.
        
                This queues the message to be sent by the IO thread at a later time.
        
                Parameters
                ----------
                data : object, str, Frame
                    The content of the message.
                flags : int
                    Any supported flag: NOBLOCK, SNDMORE.
                copy : bool
                    Should the message be sent in a copying or non-copying manner.
                track : bool
                    Should the message be tracked for notification that ZMQ has
                    finished with it? (ignored if copy=True)
        
                Returns
                -------
                None : if `copy` or not track
                    None if message was sent, raises an exception otherwise.
                MessageTracker : if track and not copy
                    a MessageTracker object, whose `pending` property will
                    be True until the send is completed.
                
                Raises
                ------
                TypeError
                    If a unicode object is passed
                ValueError
                    If `track=True`, but an untracked Frame is passed.
                ZMQError
                    If the send does not succeed for any reason.
        """
        pass

    def set(self, option, optval): # real signature unknown; restored from __doc__
        """
        s.set(option, optval)
        
                Set socket options.
        
                See the 0MQ API documentation for details on specific options.
        
                Parameters
                ----------
                option : int
                    The option to set.  Available values will depend on your
                    version of libzmq.  Examples include::
                    
                        zmq.SUBSCRIBE, UNSUBSCRIBE, IDENTITY, HWM, LINGER, FD
                
                optval : int or bytes
                    The value of the option to set.
        
                Notes
                -----
                .. warning::
        
                    All options other than zmq.SUBSCRIBE, zmq.UNSUBSCRIBE and
                    zmq.LINGER only take effect for subsequent socket bind/connects.
        """
        pass

    def unbind(self, addr): # real signature unknown; restored from __doc__
        """
        s.unbind(addr)
                
                Unbind from an address (undoes a call to bind).
                
                .. versionadded:: libzmq-3.2
                .. versionadded:: 13.0
        
                Parameters
                ----------
                addr : str
                    The address string. This has the form 'protocol://interface:port',
                    for example 'tcp://127.0.0.1:5555'. Protocols supported are
                    tcp, upd, pgm, inproc and ipc. If the address is unicode, it is
                    encoded to utf-8 first.
        """
        pass

    def __init__(self, context, socket_type): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    closed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    context = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    underlying = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The address of the underlying libzmq socket"""

    _closed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7f339412ef90>'


class unicode(object):
    """
    str(object='') -> str
    str(bytes_or_buffer[, encoding[, errors]]) -> str
    
    Create a new string object from the given object. If encoding or
    errors is specified, then the object must expose a data buffer
    that will be decoded using the given encoding and error handler.
    Otherwise, returns the result of object.__str__() (if defined)
    or repr(object).
    encoding defaults to sys.getdefaultencoding().
    errors defaults to 'strict'.
    """
    def capitalize(self): # real signature unknown; restored from __doc__
        """
        S.capitalize() -> str
        
        Return a capitalized version of S, i.e. make the first character
        have upper case and the rest lower case.
        """
        return ""

    def casefold(self): # real signature unknown; restored from __doc__
        """
        S.casefold() -> str
        
        Return a version of S suitable for caseless comparisons.
        """
        return ""

    def center(self, width, fillchar=None): # real signature unknown; restored from __doc__
        """
        S.center(width[, fillchar]) -> str
        
        Return S centered in a string of length width. Padding is
        done using the specified fill character (default is a space)
        """
        return ""

    def count(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.count(sub[, start[, end]]) -> int
        
        Return the number of non-overlapping occurrences of substring sub in
        string S[start:end].  Optional arguments start and end are
        interpreted as in slice notation.
        """
        return 0

    def encode(self, encoding='utf-8', errors='strict'): # real signature unknown; restored from __doc__
        """
        S.encode(encoding='utf-8', errors='strict') -> bytes
        
        Encode S using the codec registered for encoding. Default encoding
        is 'utf-8'. errors may be given to set a different error
        handling scheme. Default is 'strict' meaning that encoding errors raise
        a UnicodeEncodeError. Other possible values are 'ignore', 'replace' and
        'xmlcharrefreplace' as well as any other name registered with
        codecs.register_error that can handle UnicodeEncodeErrors.
        """
        return b""

    def endswith(self, suffix, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.endswith(suffix[, start[, end]]) -> bool
        
        Return True if S ends with the specified suffix, False otherwise.
        With optional start, test S beginning at that position.
        With optional end, stop comparing S at that position.
        suffix can also be a tuple of strings to try.
        """
        return False

    def expandtabs(self, tabsize=8): # real signature unknown; restored from __doc__
        """
        S.expandtabs(tabsize=8) -> str
        
        Return a copy of S where all tab characters are expanded using spaces.
        If tabsize is not given, a tab size of 8 characters is assumed.
        """
        return ""

    def find(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.find(sub[, start[, end]]) -> int
        
        Return the lowest index in S where substring sub is found,
        such that sub is contained within S[start:end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Return -1 on failure.
        """
        return 0

    def format(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        S.format(*args, **kwargs) -> str
        
        Return a formatted version of S, using substitutions from args and kwargs.
        The substitutions are identified by braces ('{' and '}').
        """
        return ""

    def format_map(self, mapping): # real signature unknown; restored from __doc__
        """
        S.format_map(mapping) -> str
        
        Return a formatted version of S, using substitutions from mapping.
        The substitutions are identified by braces ('{' and '}').
        """
        return ""

    def index(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.index(sub[, start[, end]]) -> int
        
        Return the lowest index in S where substring sub is found, 
        such that sub is contained within S[start:end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Raises ValueError when the substring is not found.
        """
        return 0

    def isalnum(self): # real signature unknown; restored from __doc__
        """
        S.isalnum() -> bool
        
        Return True if all characters in S are alphanumeric
        and there is at least one character in S, False otherwise.
        """
        return False

    def isalpha(self): # real signature unknown; restored from __doc__
        """
        S.isalpha() -> bool
        
        Return True if all characters in S are alphabetic
        and there is at least one character in S, False otherwise.
        """
        return False

    def isdecimal(self): # real signature unknown; restored from __doc__
        """
        S.isdecimal() -> bool
        
        Return True if there are only decimal characters in S,
        False otherwise.
        """
        return False

    def isdigit(self): # real signature unknown; restored from __doc__
        """
        S.isdigit() -> bool
        
        Return True if all characters in S are digits
        and there is at least one character in S, False otherwise.
        """
        return False

    def isidentifier(self): # real signature unknown; restored from __doc__
        """
        S.isidentifier() -> bool
        
        Return True if S is a valid identifier according
        to the language definition.
        
        Use keyword.iskeyword() to test for reserved identifiers
        such as "def" and "class".
        """
        return False

    def islower(self): # real signature unknown; restored from __doc__
        """
        S.islower() -> bool
        
        Return True if all cased characters in S are lowercase and there is
        at least one cased character in S, False otherwise.
        """
        return False

    def isnumeric(self): # real signature unknown; restored from __doc__
        """
        S.isnumeric() -> bool
        
        Return True if there are only numeric characters in S,
        False otherwise.
        """
        return False

    def isprintable(self): # real signature unknown; restored from __doc__
        """
        S.isprintable() -> bool
        
        Return True if all characters in S are considered
        printable in repr() or S is empty, False otherwise.
        """
        return False

    def isspace(self): # real signature unknown; restored from __doc__
        """
        S.isspace() -> bool
        
        Return True if all characters in S are whitespace
        and there is at least one character in S, False otherwise.
        """
        return False

    def istitle(self): # real signature unknown; restored from __doc__
        """
        S.istitle() -> bool
        
        Return True if S is a titlecased string and there is at least one
        character in S, i.e. upper- and titlecase characters may only
        follow uncased characters and lowercase characters only cased ones.
        Return False otherwise.
        """
        return False

    def isupper(self): # real signature unknown; restored from __doc__
        """
        S.isupper() -> bool
        
        Return True if all cased characters in S are uppercase and there is
        at least one cased character in S, False otherwise.
        """
        return False

    def join(self, iterable): # real signature unknown; restored from __doc__
        """
        S.join(iterable) -> str
        
        Return a string which is the concatenation of the strings in the
        iterable.  The separator between elements is S.
        """
        return ""

    def ljust(self, width, fillchar=None): # real signature unknown; restored from __doc__
        """
        S.ljust(width[, fillchar]) -> str
        
        Return S left-justified in a Unicode string of length width. Padding is
        done using the specified fill character (default is a space).
        """
        return ""

    def lower(self): # real signature unknown; restored from __doc__
        """
        S.lower() -> str
        
        Return a copy of the string S converted to lowercase.
        """
        return ""

    def lstrip(self, chars=None): # real signature unknown; restored from __doc__
        """
        S.lstrip([chars]) -> str
        
        Return a copy of the string S with leading whitespace removed.
        If chars is given and not None, remove characters in chars instead.
        """
        return ""

    def maketrans(self, *args, **kwargs): # real signature unknown
        """
        Return a translation table usable for str.translate().
        
        If there is only one argument, it must be a dictionary mapping Unicode
        ordinals (integers) or characters to Unicode ordinals, strings or None.
        Character keys will be then converted to ordinals.
        If there are two arguments, they must be strings of equal length, and
        in the resulting dictionary, each character in x will be mapped to the
        character at the same position in y. If there is a third argument, it
        must be a string, whose characters will be mapped to None in the result.
        """
        pass

    def partition(self, sep): # real signature unknown; restored from __doc__
        """
        S.partition(sep) -> (head, sep, tail)
        
        Search for the separator sep in S, and return the part before it,
        the separator itself, and the part after it.  If the separator is not
        found, return S and two empty strings.
        """
        pass

    def replace(self, old, new, count=None): # real signature unknown; restored from __doc__
        """
        S.replace(old, new[, count]) -> str
        
        Return a copy of S with all occurrences of substring
        old replaced by new.  If the optional argument count is
        given, only the first count occurrences are replaced.
        """
        return ""

    def rfind(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.rfind(sub[, start[, end]]) -> int
        
        Return the highest index in S where substring sub is found,
        such that sub is contained within S[start:end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Return -1 on failure.
        """
        return 0

    def rindex(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.rindex(sub[, start[, end]]) -> int
        
        Return the highest index in S where substring sub is found,
        such that sub is contained within S[start:end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Raises ValueError when the substring is not found.
        """
        return 0

    def rjust(self, width, fillchar=None): # real signature unknown; restored from __doc__
        """
        S.rjust(width[, fillchar]) -> str
        
        Return S right-justified in a string of length width. Padding is
        done using the specified fill character (default is a space).
        """
        return ""

    def rpartition(self, sep): # real signature unknown; restored from __doc__
        """
        S.rpartition(sep) -> (head, sep, tail)
        
        Search for the separator sep in S, starting at the end of S, and return
        the part before it, the separator itself, and the part after it.  If the
        separator is not found, return two empty strings and S.
        """
        pass

    def rsplit(self, sep=None, maxsplit=-1): # real signature unknown; restored from __doc__
        """
        S.rsplit(sep=None, maxsplit=-1) -> list of strings
        
        Return a list of the words in S, using sep as the
        delimiter string, starting at the end of the string and
        working to the front.  If maxsplit is given, at most maxsplit
        splits are done. If sep is not specified, any whitespace string
        is a separator.
        """
        return []

    def rstrip(self, chars=None): # real signature unknown; restored from __doc__
        """
        S.rstrip([chars]) -> str
        
        Return a copy of the string S with trailing whitespace removed.
        If chars is given and not None, remove characters in chars instead.
        """
        return ""

    def split(self, sep=None, maxsplit=-1): # real signature unknown; restored from __doc__
        """
        S.split(sep=None, maxsplit=-1) -> list of strings
        
        Return a list of the words in S, using sep as the
        delimiter string.  If maxsplit is given, at most maxsplit
        splits are done. If sep is not specified or is None, any
        whitespace string is a separator and empty strings are
        removed from the result.
        """
        return []

    def splitlines(self, keepends=None): # real signature unknown; restored from __doc__
        """
        S.splitlines([keepends]) -> list of strings
        
        Return a list of the lines in S, breaking at line boundaries.
        Line breaks are not included in the resulting list unless keepends
        is given and true.
        """
        return []

    def startswith(self, prefix, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.startswith(prefix[, start[, end]]) -> bool
        
        Return True if S starts with the specified prefix, False otherwise.
        With optional start, test S beginning at that position.
        With optional end, stop comparing S at that position.
        prefix can also be a tuple of strings to try.
        """
        return False

    def strip(self, chars=None): # real signature unknown; restored from __doc__
        """
        S.strip([chars]) -> str
        
        Return a copy of the string S with leading and trailing
        whitespace removed.
        If chars is given and not None, remove characters in chars instead.
        """
        return ""

    def swapcase(self): # real signature unknown; restored from __doc__
        """
        S.swapcase() -> str
        
        Return a copy of S with uppercase characters converted to lowercase
        and vice versa.
        """
        return ""

    def title(self): # real signature unknown; restored from __doc__
        """
        S.title() -> str
        
        Return a titlecased version of S, i.e. words start with title case
        characters, all remaining cased characters have lower case.
        """
        return ""

    def translate(self, table): # real signature unknown; restored from __doc__
        """
        S.translate(table) -> str
        
        Return a copy of the string S in which each character has been mapped
        through the given translation table. The table must implement
        lookup/indexing via __getitem__, for instance a dictionary or list,
        mapping Unicode ordinals to Unicode ordinals, strings, or None. If
        this operation raises LookupError, the character is left untouched.
        Characters mapped to None are deleted.
        """
        return ""

    def upper(self): # real signature unknown; restored from __doc__
        """
        S.upper() -> str
        
        Return a copy of S converted to uppercase.
        """
        return ""

    def zfill(self, width): # real signature unknown; restored from __doc__
        """
        S.zfill(width) -> str
        
        Pad a numeric string S with zeros on the left, to fill a field
        of the specified width. The string S is never truncated.
        """
        return ""

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Return key in self. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __format__(self, format_spec): # real signature unknown; restored from __doc__
        """
        S.__format__(format_spec) -> str
        
        Return a formatted version of S as described by format_spec.
        """
        return ""

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __getnewargs__(self, *args, **kwargs): # real signature unknown
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mod__(self, *args, **kwargs): # real signature unknown
        """ Return self%value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __sizeof__(self): # real signature unknown; restored from __doc__
        """ S.__sizeof__() -> size of S in memory, in bytes """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass


class ZMQBindError(__zmq_error.ZMQBaseError):
    """
    An error for ``Socket.bind_to_random_port()``.
        
        See Also
        --------
        .Socket.bind_to_random_port
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


# variables with complex values

basestring = (
    bytes,
    str,
)

__all__ = [
    'Socket',
    'IPC_PATH_MAX_LEN',
]

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f3390fbfeb8>'

__spec__ = None # (!) real value is "ModuleSpec(name='zmq.backend.cython.socket', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f3390fbfeb8>, origin='/usr/lib/python3/dist-packages/zmq/backend/cython/socket.cpython-36m-x86_64-linux-gnu.so')"

__test__ = {}

