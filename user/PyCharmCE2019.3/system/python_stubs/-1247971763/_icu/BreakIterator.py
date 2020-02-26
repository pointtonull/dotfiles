# encoding: utf-8
# module _icu
# from /usr/lib/python3/dist-packages/_icu.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
""" PyICU extension module """

# imports
import datetime as __datetime
import icu as __icu


class BreakIterator(__icu.UObject):
    """
    The BreakIterator class implements methods for finding the location of
    boundaries in text.
    
    BreakIterator is an abstract base class. Instances of BreakIterator maintain
    a current position and scan over text returning the index of characters
    where boundaries occur.
    
    Line boundary analysis determines where a text string can be broken when
    line-wrapping. The mechanism correctly handles punctuation and hyphenated
    words.
    
    Sentence boundary analysis allows selection with correct interpretation of
    periods within numbers and abbreviations, and trailing punctuation marks
    such as quotation marks and parentheses.
    
    Word boundary analysis is used by search and replace functions, as well as
    within text editing applications that allow the user to select words with a
    double click. Word selection provides correct interpretation of punctuation
    marks within and following words. Characters that are not part of a word,
    such as symbols or punctuation marks, have word-breaks on both sides.
    
    Character boundary analysis allows users to interact with characters as they
    expect to, for example, when moving the cursor through a text
    string. Character boundary analysis provides correct navigation of through
    character strings, regardless of how the character is stored. For example,
    an accented character might be stored as a base character and a diacritical
    mark. What users consider to be a character can differ between languages.
    
    The text boundary positions are found according to the rules described in
    Unicode Standard Annex #29, Text Boundaries, and Unicode Standard Annex #14,
    Line Breaking Properties. These are available at
    http://www.unicode.org/reports/tr14/ and http://www.unicode.org/reports/tr29/.
    """
    @classmethod
    def createCharacterInstance(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def createLineInstance(cls, *args, **kwargs): # real signature unknown
        """
        Returns an instance of a BreakIterator implementing line breaks. Line breaks
        are logically possible line breaks, actual line breaks are usually
        determined based on display width. LineBreak is useful for word wrapping
        text.
        """
        pass

    @classmethod
    def createSentenceInstance(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def createTitleInstance(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def createWordInstance(cls, *args, **kwargs): # real signature unknown
        pass

    def current(self, *args, **kwargs): # real signature unknown
        pass

    def first(self, *args, **kwargs): # real signature unknown
        pass

    def following(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def getAvailableLocales(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def getDisplayName(cls, *args, **kwargs): # real signature unknown
        pass

    def getLocale(self, *args, **kwargs): # real signature unknown
        pass

    def getLocaleID(self, *args, **kwargs): # real signature unknown
        pass

    def getText(self, *args, **kwargs): # real signature unknown
        """ Return the string over the text being analyzed. """
        pass

    def isBoundary(self, *args, **kwargs): # real signature unknown
        pass

    def last(self, *args, **kwargs): # real signature unknown
        pass

    def nextBoundary(self, *args, **kwargs): # real signature unknown
        pass

    def preceding(self, *args, **kwargs): # real signature unknown
        pass

    def previous(self, *args, **kwargs): # real signature unknown
        pass

    def setText(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __next__(self, *args, **kwargs): # real signature unknown
        """ Implement next(self). """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    DONE = -1
    __hash__ = None


