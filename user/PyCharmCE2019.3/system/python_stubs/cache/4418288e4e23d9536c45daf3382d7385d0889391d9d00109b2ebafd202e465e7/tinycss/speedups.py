# encoding: utf-8
# module tinycss.speedups
# from /usr/lib/python3/dist-packages/tinycss/speedups.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
"""
tinycss.speedups
    ----------------

    Cython module for speeding up inner loops.

    Right now only :func:`tokenize_flat` has a second implementation.

    :copyright: (c) 2010 by Simon Sapin.
    :license: BSD, see LICENSE for more details.
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

# functions

def FIND_NEWLINES(*args, **kwargs): # real signature unknown
    """
    Return an iterator over all non-overlapping matches for the RE pattern in string.
    
    For each match, the iterator returns a match object.
    """
    pass

def NEWLINE_UNESCAPE(*args, **kwargs): # real signature unknown
    """
    partial(func, *args, **keywords) - new function with partial application
        of the given arguments and keywords.
    """
    pass

def SIMPLE_UNESCAPE(*args, **kwargs): # real signature unknown
    """
    partial(func, *args, **keywords) - new function with partial application
        of the given arguments and keywords.
    """
    pass

def tokenize_flat(*args, **kwargs): # real signature unknown
    """
    :param css_source:
            CSS as an unicode string
        :param ignore_comments:
            if true (the default) comments will not be included in the
            return value
        :return:
            An iterator of :class:`Token`
    """
    pass

def UNICODE_UNESCAPE(*args, **kwargs): # real signature unknown
    """
    partial(func, *args, **keywords) - new function with partial application
        of the given arguments and keywords.
    """
    pass

# classes

class CToken(object):
    """
    A token built by the Cython speedups. Identical to
        :class:`~.token_data.Token`.
    """
    def as_css(self, *args, **kwargs): # real signature unknown
        """
        Return as an Unicode string the CSS representation of the token,
                as parsed in the source.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    column = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    line = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _as_css = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    is_container = False


# variables with complex values

COMPILED_TOKEN_INDEXES = {
    '(': 19,
    ')': 20,
    ':': 15,
    ';': 16,
    'ATKEYWORD': 6,
    'BAD_COMMENT': 14,
    'BAD_STRING': 12,
    'BAD_URI': 2,
    'CDC': 24,
    'CDO': 23,
    'COMMENT': 13,
    'DIMENSION': 8,
    'FUNCTION': 3,
    'HASH': 7,
    'IDENT': 5,
    'NUMBER': 10,
    'PERCENTAGE': 9,
    'S': 0,
    'STRING': 11,
    'UNICODE-RANGE': 4,
    'URI': 1,
    '[': 21,
    ']': 22,
    '{': 17,
    '}': 18,
}

COMPILED_TOKEN_REGEXPS = [
    (
        'S',
        None, # (!) real value is '<built-in method match of _sre.SRE_Pattern object at 0x7f33940f2930>'
    ),
    (
        'URI',
        None, # (!) real value is '<built-in method match of _sre.SRE_Pattern object at 0x13b0f00>'
    ),
    (
        'BAD_URI',
        None, # (!) real value is '<built-in method match of _sre.SRE_Pattern object at 0x13b5260>'
    ),
    (
        'FUNCTION',
        None, # (!) real value is '<built-in method match of _sre.SRE_Pattern object at 0x13b48e0>'
    ),
    (
        'UNICODE-RANGE',
        None, # (!) real value is '<built-in method match of _sre.SRE_Pattern object at 0x7f33930c2160>'
    ),
    (
        'IDENT',
        None, # (!) real value is '<built-in method match of _sre.SRE_Pattern object at 0x13b3560>'
    ),
    (
        'ATKEYWORD',
        None, # (!) real value is '<built-in method match of _sre.SRE_Pattern object at 0x13b75e0>'
    ),
    (
        'HASH',
        None, # (!) real value is '<built-in method match of _sre.SRE_Pattern object at 0x13b3ea0>'
    ),
    (
        'DIMENSION',
        None, # (!) real value is '<built-in method match of _sre.SRE_Pattern object at 0x13b6250>'
    ),
    (
        'PERCENTAGE',
        None, # (!) real value is '<built-in method match of _sre.SRE_Pattern object at 0x7f3394457df0>'
    ),
    (
        'NUMBER',
        None, # (!) real value is '<built-in method match of _sre.SRE_Pattern object at 0x7f33930c32e0>'
    ),
    (
        'STRING',
        None, # (!) real value is '<built-in method match of _sre.SRE_Pattern object at 0x13b89a0>'
    ),
    (
        'BAD_STRING',
        None, # (!) real value is '<built-in method match of _sre.SRE_Pattern object at 0x13b7f30>'
    ),
    (
        'COMMENT',
        None, # (!) real value is '<built-in method match of _sre.SRE_Pattern object at 0x7f3393103178>'
    ),
    (
        'BAD_COMMENT',
        None, # (!) real value is '<built-in method match of _sre.SRE_Pattern object at 0x13b3350>'
    ),
    (
        ':',
        None, # (!) real value is '<built-in method match of _sre.SRE_Pattern object at 0x7f33930c15b0>'
    ),
    (
        ';',
        None, # (!) real value is '<built-in method match of _sre.SRE_Pattern object at 0x7f33930c1630>'
    ),
    (
        '{',
        None, # (!) real value is '<built-in method match of _sre.SRE_Pattern object at 0x7f33930c16b0>'
    ),
    (
        '}',
        None, # (!) real value is '<built-in method match of _sre.SRE_Pattern object at 0x7f33930c1730>'
    ),
    (
        '(',
        None, # (!) real value is '<built-in method match of _sre.SRE_Pattern object at 0x7f33930c17b0>'
    ),
    (
        ')',
        None, # (!) real value is '<built-in method match of _sre.SRE_Pattern object at 0x7f33930c1830>'
    ),
    (
        '[',
        None, # (!) real value is '<built-in method match of _sre.SRE_Pattern object at 0x7f33930c18b0>'
    ),
    (
        ']',
        None, # (!) real value is '<built-in method match of _sre.SRE_Pattern object at 0x7f33930c1930>'
    ),
    (
        'CDO',
        None, # (!) real value is '<built-in method match of _sre.SRE_Pattern object at 0x7f3394144588>'
    ),
    (
        'CDC',
        None, # (!) real value is '<built-in method match of _sre.SRE_Pattern object at 0x7f33930d31e0>'
    ),
]

TOKEN_DISPATCH = [
    [],
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    [
        (
            0,
            'S',
            None, # (!) real value is '<built-in method match of _sre.SRE_Pattern object at 0x7f33940f2930>'
        ),
    ],
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    [
        (
            11,
            'STRING',
            None, # (!) real value is '<built-in method match of _sre.SRE_Pattern object at 0x13b89a0>'
        ),
        (
            12,
            'BAD_STRING',
            None, # (!) real value is '<built-in method match of _sre.SRE_Pattern object at 0x13b7f30>'
        ),
    ],
    [
        (
            7,
            'HASH',
            None, # (!) real value is '<built-in method match of _sre.SRE_Pattern object at 0x13b3ea0>'
        ),
    ],
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    [
        (
            19,
            '(',
            None, # (!) real value is '<built-in method match of _sre.SRE_Pattern object at 0x7f33930c17b0>'
        ),
    ],
    [
        (
            20,
            ')',
            None, # (!) real value is '<built-in method match of _sre.SRE_Pattern object at 0x7f33930c1830>'
        ),
    ],
    '<value is a self-reference, replaced by this string>',
    [
        (
            8,
            'DIMENSION',
            None, # (!) real value is '<built-in method match of _sre.SRE_Pattern object at 0x13b6250>'
        ),
        (
            9,
            'PERCENTAGE',
            None, # (!) real value is '<built-in method match of _sre.SRE_Pattern object at 0x7f3394457df0>'
        ),
        (
            10,
            'NUMBER',
            None, # (!) real value is '<built-in method match of _sre.SRE_Pattern object at 0x7f33930c32e0>'
        ),
    ],
    '<value is a self-reference, replaced by this string>',
    [
        (
            3,
            'FUNCTION',
            None, # (!) real value is '<built-in method match of _sre.SRE_Pattern object at 0x13b48e0>'
        ),
        (
            5,
            'IDENT',
            None, # (!) real value is '<built-in method match of _sre.SRE_Pattern object at 0x13b3560>'
        ),
        '<value is a self-reference, replaced by this string>',
        '<value is a self-reference, replaced by this string>',
        '<value is a self-reference, replaced by this string>',
        (
            24,
            'CDC',
            None, # (!) real value is '<built-in method match of _sre.SRE_Pattern object at 0x7f33930d31e0>'
        ),
    ],
    '<value is a self-reference, replaced by this string>',
    [
        (
            13,
            'COMMENT',
            None, # (!) real value is '<built-in method match of _sre.SRE_Pattern object at 0x7f3393103178>'
        ),
        (
            14,
            'BAD_COMMENT',
            None, # (!) real value is '<built-in method match of _sre.SRE_Pattern object at 0x13b3350>'
        ),
    ],
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    [
        (
            15,
            ':',
            None, # (!) real value is '<built-in method match of _sre.SRE_Pattern object at 0x7f33930c15b0>'
        ),
    ],
    [
        (
            16,
            ';',
            None, # (!) real value is '<built-in method match of _sre.SRE_Pattern object at 0x7f33930c1630>'
        ),
    ],
    [
        (
            23,
            'CDO',
            None, # (!) real value is '<built-in method match of _sre.SRE_Pattern object at 0x7f3394144588>'
        ),
    ],
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    [
        (
            6,
            'ATKEYWORD',
            None, # (!) real value is '<built-in method match of _sre.SRE_Pattern object at 0x13b75e0>'
        ),
    ],
    [
        '<value is a self-reference, replaced by this string>',
        '<value is a self-reference, replaced by this string>',
    ],
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    [
        (
            1,
            'URI',
            None, # (!) real value is '<built-in method match of _sre.SRE_Pattern object at 0x13b0f00>'
        ),
        (
            2,
            'BAD_URI',
            None, # (!) real value is '<built-in method match of _sre.SRE_Pattern object at 0x13b5260>'
        ),
        (
            4,
            'UNICODE-RANGE',
            None, # (!) real value is '<built-in method match of _sre.SRE_Pattern object at 0x7f33930c2160>'
        ),
        '<value is a self-reference, replaced by this string>',
        '<value is a self-reference, replaced by this string>',
    ],
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    [
        (
            21,
            '[',
            None, # (!) real value is '<built-in method match of _sre.SRE_Pattern object at 0x7f33930c18b0>'
        ),
    ],
    '<value is a self-reference, replaced by this string>',
    [
        (
            22,
            ']',
            None, # (!) real value is '<built-in method match of _sre.SRE_Pattern object at 0x7f33930c1930>'
        ),
    ],
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    [
        (
            17,
            '{',
            None, # (!) real value is '<built-in method match of _sre.SRE_Pattern object at 0x7f33930c16b0>'
        ),
    ],
    '<value is a self-reference, replaced by this string>',
    [
        (
            18,
            '}',
            None, # (!) real value is '<built-in method match of _sre.SRE_Pattern object at 0x7f33930c1730>'
        ),
    ],
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
    '<value is a self-reference, replaced by this string>',
]

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f33930d2748>'

__spec__ = None # (!) real value is "ModuleSpec(name='tinycss.speedups', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f33930d2748>, origin='/usr/lib/python3/dist-packages/tinycss/speedups.cpython-36m-x86_64-linux-gnu.so')"

__test__ = {}

