# encoding: utf-8
# module typed_ast._ast27
# from /usr/local/lib/python3.6/dist-packages/typed_ast/_ast27.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc
# no imports

from .AST import AST

class comprehension(AST):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    _fields = (
        'target',
        'iter',
        'ifs',
    )
    __dict__ = None # (!) real value is "mappingproxy({'_fields': ('target', 'iter', 'ifs'), '__module__': 'typed_ast._ast27', '__dict__': <attribute '__dict__' of 'comprehension' objects>, '__weakref__': <attribute '__weakref__' of 'comprehension' objects>, '__doc__': None})"


