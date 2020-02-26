# encoding: utf-8
# module _icu
# from /usr/lib/python3/dist-packages/_icu.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
""" PyICU extension module """

# imports
import datetime as __datetime
import icu as __icu


# Variables with simple values

FLOATING_TZNAME = 'World/Floating'

ICU_VERSION = '60.1'

UNICODE_VERSION = '10.0'

USET_ADD_CASE_MAPPINGS = 4

USET_CASE_INSENSITIVE = 2

USET_IGNORE_SPACE = 1

U_COMPARE_CODE_POINT_ORDER = 32768

U_FOLD_CASE_DEFAULT = 0

U_FOLD_CASE_EXCLUDE_SPECIAL_I = 1

VERSION = '1.9.8'

# functions

def _install__doc__(*args, **kwargs): # real signature unknown
    """ install immutable doc strings from python """
    pass

# classes

from .UObject import UObject
from .BreakIterator import BreakIterator
from .Calendar import Calendar
from .CanonicalIterator import CanonicalIterator
from .Char import Char
from .ForwardCharacterIterator import ForwardCharacterIterator
from .CharacterIterator import CharacterIterator
from .CharsetDetector import CharsetDetector
from .CharsetMatch import CharsetMatch
from .Format import Format
from .NumberFormat import NumberFormat
from .ChoiceFormat import ChoiceFormat
from .CollationElementIterator import CollationElementIterator
from .CollationKey import CollationKey
from .Collator import Collator
from .DecimalFormat import DecimalFormat
from .CompactDecimalFormat import CompactDecimalFormat
from .Measure import Measure
from .CurrencyAmount import CurrencyAmount
from .CurrencyPluralInfo import CurrencyPluralInfo
from .MeasureUnit import MeasureUnit
from .CurrencyUnit import CurrencyUnit
from .DateFormat import DateFormat
from .DateFormatSymbols import DateFormatSymbols
from .DateInterval import DateInterval
from .DateIntervalFormat import DateIntervalFormat
from .DateIntervalInfo import DateIntervalInfo
from .DateTimePatternGenerator import DateTimePatternGenerator
from .DecimalFormatSymbols import DecimalFormatSymbols
from .RuleBasedBreakIterator import RuleBasedBreakIterator
from .DictionaryBasedBreakIterator import DictionaryBasedBreakIterator
from .FieldPosition import FieldPosition
from .Normalizer2 import Normalizer2
from .FilteredNormalizer2 import FilteredNormalizer2
from .FloatingTZ import FloatingTZ
from .Formattable import Formattable
from .GregorianCalendar import GregorianCalendar
from .ICUtzinfo import ICUtzinfo
from .IDNA import IDNA
from .IDNAInfo import IDNAInfo
from .ListFormatter import ListFormatter
from .Locale import Locale
from .LocaleData import LocaleData
from .MeasureFormat import MeasureFormat
from .MessageFormat import MessageFormat
from .Normalizer import Normalizer
from .ParsePosition import ParsePosition
from .PluralFormat import PluralFormat
from .PluralRules import PluralRules
from .RegexMatcher import RegexMatcher
from .RegexPattern import RegexPattern
from .RelativeDateTimeFormatter import RelativeDateTimeFormatter
from .Replaceable import Replaceable
from .ResourceBundle import ResourceBundle
from .RuleBasedCollator import RuleBasedCollator
from .RuleBasedNumberFormat import RuleBasedNumberFormat
from .Script import Script
from .SearchIterator import SearchIterator
from .SelectFormat import SelectFormat
from .Shape import Shape
from .SimpleDateFormat import SimpleDateFormat
from .TimeZone import TimeZone
from .SimpleTimeZone import SimpleTimeZone
from .SpoofChecker import SpoofChecker
from .UCharCharacterIterator import UCharCharacterIterator
from .StringCharacterIterator import StringCharacterIterator
from .StringEnumeration import StringEnumeration
from .StringSearch import StringSearch
from .TimeUnitFormat import TimeUnitFormat
from .Transliterator import Transliterator
from .UBlockCode import UBlockCode
from .UCalendarAMPMs import UCalendarAMPMs
from .UCalendarDateFields import UCalendarDateFields
from .UCalendarDaysOfWeek import UCalendarDaysOfWeek
from .UCalendarMonths import UCalendarMonths
from .UCharCategory import UCharCategory
from .UCharDirection import UCharDirection
from .UCharNameChoice import UCharNameChoice
from .UCollationResult import UCollationResult
from .UCollAttribute import UCollAttribute
from .UCollAttributeValue import UCollAttributeValue
from .UCurrencySpacing import UCurrencySpacing
from .UDateAbsoluteUnit import UDateAbsoluteUnit
from .UDateDirection import UDateDirection
from .UDateFormatBooleanAttribute import UDateFormatBooleanAttribute
from .UDateRelativeDateTimeFormatterStyle import UDateRelativeDateTimeFormatterStyle
from .UDateRelativeUnit import UDateRelativeUnit
from .UDateTimePatternConflict import UDateTimePatternConflict
from .UDateTimePatternField import UDateTimePatternField
from .UDateTimePatternMatchOptions import UDateTimePatternMatchOptions
from .UDisplayContext import UDisplayContext
from .UDisplayContextType import UDisplayContextType
from .ULocaleDataDelimiterType import ULocaleDataDelimiterType
from .ULocaleDataExemplarSetType import ULocaleDataExemplarSetType
from .ULocDataLocaleType import ULocDataLocaleType
from .UMatchDegree import UMatchDegree
from .UMeasurementSystem import UMeasurementSystem
from .UnicodeFilter import UnicodeFilter
from .UnicodeFunctor import UnicodeFunctor
from .UnicodeMatcher import UnicodeMatcher
from .UnicodeSet import UnicodeSet
from .UnicodeSetIterator import UnicodeSetIterator
from .UnicodeString import UnicodeString
from .UNormalizationCheckResult import UNormalizationCheckResult
from .UNormalizationMode import UNormalizationMode
from .UNormalizationMode2 import UNormalizationMode2
from .UNumberCompactStyle import UNumberCompactStyle
from .UProperty import UProperty
from .UPropertyNameChoice import UPropertyNameChoice
from .URBNFRuleSetTag import URBNFRuleSetTag
from .URegexpFlag import URegexpFlag
from .URestrictionLevel import URestrictionLevel
from .UResType import UResType
from .UScriptCode import UScriptCode
from .UScriptUsage import UScriptUsage
from .USearchAttribute import USearchAttribute
from .USearchAttributeValue import USearchAttributeValue
from .USetSpanCondition import USetSpanCondition
from .USpoofChecks import USpoofChecks
from .UTimeUnitFormatStyle import UTimeUnitFormatStyle
from .UTransDirection import UTransDirection
from .UTransPosition import UTransPosition
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f339411c7f0>'

__spec__ = None # (!) real value is "ModuleSpec(name='_icu', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f339411c7f0>, origin='/usr/lib/python3/dist-packages/_icu.cpython-36m-x86_64-linux-gnu.so')"

__types__ = {
    'N6icu_607UObjectE': [
        'N6icu_6011ReplaceableE',
        'N6icu_6013UnicodeStringE',
        'N6icu_6011FormattableE',
        'N6icu_6011MeasureUnitE',
        'N6icu_607MeasureE',
        'N6icu_6012CurrencyUnitE',
        'N6icu_6014CurrencyAmountE',
        'N6icu_6017StringEnumerationE',
        'N6icu_606LocaleE',
        'N6icu_6014ResourceBundleE',
        'N6icu_6014TransliteratorE',
        'N6icu_6024ForwardCharacterIteratorE',
        'N6icu_6017CharacterIteratorE',
        'N6icu_6022UCharCharacterIteratorE',
        'N6icu_6023StringCharacterIteratorE',
        'N6icu_6013BreakIteratorE',
        'N6icu_6022RuleBasedBreakIteratorE',
        'N6icu_6022RuleBasedBreakIteratorE',
        'N6icu_6017CanonicalIteratorE',
        'N6icu_6024CollationElementIteratorE',
        'N6icu_6013FieldPositionE',
        'N6icu_6013ParsePositionE',
        'N6icu_606FormatE',
        'N6icu_6013MeasureFormatE',
        'N6icu_6013MessageFormatE',
        'N6icu_6011PluralRulesE',
        'N6icu_6012PluralFormatE',
        'N6icu_6014TimeUnitFormatE',
        'N6icu_6012SelectFormatE',
        'N6icu_6013ListFormatterE',
        'N6icu_6017DateFormatSymbolsE',
        'N6icu_6010DateFormatE',
        'N6icu_6016SimpleDateFormatE',
        'N6icu_6024DateTimePatternGeneratorE',
        'N6icu_6012DateIntervalE',
        'N6icu_6016DateIntervalInfoE',
        'N6icu_6018DateIntervalFormatE',
        'N6icu_6025RelativeDateTimeFormatterE',
        'N6icu_6020DecimalFormatSymbolsE',
        'N6icu_6012NumberFormatE',
        'N6icu_6018CurrencyPluralInfoE',
        'N6icu_6013DecimalFormatE',
        'N6icu_6020CompactDecimalFormatE',
        'N6icu_6021RuleBasedNumberFormatE',
        'N6icu_6012ChoiceFormatE',
        'N6icu_608TimeZoneE',
        'N6icu_6014SimpleTimeZoneE',
        'N6icu_608CalendarE',
        'N6icu_6017GregorianCalendarE',
        'N6icu_6012CollationKeyE',
        'N6icu_608CollatorE',
        'N6icu_6017RuleBasedCollatorE',
        'N6icu_6014UnicodeFunctorE',
        'N6icu_6014UnicodeMatcherE',
        'N6icu_6013UnicodeFilterE',
        'N6icu_6010UnicodeSetE',
        'N6icu_6018UnicodeSetIteratorE',
        'N6icu_6012RegexPatternE',
        'N6icu_6012RegexMatcherE',
        'N6icu_6010NormalizerE',
        'N6icu_6011Normalizer2E',
        'N6icu_6019FilteredNormalizer2E',
        'N6icu_6014SearchIteratorE',
        'N6icu_6012StringSearchE',
    ],
    UObject: 
        'N6icu_607UObjectE'
    ,
    'N6icu_6011ReplaceableE': [
        'N6icu_6013UnicodeStringE',
    ],
    Replaceable: 
        'N6icu_6011ReplaceableE'
    ,
    'N6icu_6013UnicodeStringE': [],
    UnicodeString: 
        'N6icu_6013UnicodeStringE'
    ,
    'N6icu_6011FormattableE': '<value is a self-reference, replaced by this string>',
    Formattable: 
        'N6icu_6011FormattableE'
    ,
    'N6icu_6011MeasureUnitE': [
        'N6icu_6012CurrencyUnitE',
    ],
    MeasureUnit: 
        'N6icu_6011MeasureUnitE'
    ,
    'N6icu_607MeasureE': [
        'N6icu_6014CurrencyAmountE',
    ],
    Measure: 
        'N6icu_607MeasureE'
    ,
    'N6icu_6012CurrencyUnitE': '<value is a self-reference, replaced by this string>',
    CurrencyUnit: 
        'N6icu_6012CurrencyUnitE'
    ,
    'N6icu_6014CurrencyAmountE': '<value is a self-reference, replaced by this string>',
    CurrencyAmount: 
        'N6icu_6014CurrencyAmountE'
    ,
    'N6icu_6017StringEnumerationE': '<value is a self-reference, replaced by this string>',
    StringEnumeration: 
        'N6icu_6017StringEnumerationE'
    ,
    'N6icu_606LocaleE': '<value is a self-reference, replaced by this string>',
    Locale: 
        'N6icu_606LocaleE'
    ,
    'N6icu_6014ResourceBundleE': '<value is a self-reference, replaced by this string>',
    ResourceBundle: 
        'N6icu_6014ResourceBundleE'
    ,
    'N6icu_6014TransliteratorE': '<value is a self-reference, replaced by this string>',
    Transliterator: 
        'N6icu_6014TransliteratorE'
    ,
    'N6icu_6024ForwardCharacterIteratorE': [
        'N6icu_6017CharacterIteratorE',
        'N6icu_6022UCharCharacterIteratorE',
        'N6icu_6023StringCharacterIteratorE',
    ],
    ForwardCharacterIterator: 
        'N6icu_6024ForwardCharacterIteratorE'
    ,
    'N6icu_6017CharacterIteratorE': [
        'N6icu_6022UCharCharacterIteratorE',
        'N6icu_6023StringCharacterIteratorE',
    ],
    CharacterIterator: 
        'N6icu_6017CharacterIteratorE'
    ,
    'N6icu_6022UCharCharacterIteratorE': [
        'N6icu_6023StringCharacterIteratorE',
    ],
    UCharCharacterIterator: 
        'N6icu_6022UCharCharacterIteratorE'
    ,
    'N6icu_6023StringCharacterIteratorE': '<value is a self-reference, replaced by this string>',
    StringCharacterIterator: 
        'N6icu_6023StringCharacterIteratorE'
    ,
    'N6icu_6013BreakIteratorE': [
        'N6icu_6022RuleBasedBreakIteratorE',
        'N6icu_6022RuleBasedBreakIteratorE',
    ],
    BreakIterator: 
        'N6icu_6013BreakIteratorE'
    ,
    'N6icu_6022RuleBasedBreakIteratorE': [
        'N6icu_6022RuleBasedBreakIteratorE',
    ],
    RuleBasedBreakIterator: 
        'N6icu_6022RuleBasedBreakIteratorE'
    ,
    DictionaryBasedBreakIterator: 
        'N6icu_6022RuleBasedBreakIteratorE'
    ,
    'N6icu_6017CanonicalIteratorE': '<value is a self-reference, replaced by this string>',
    CanonicalIterator: 
        'N6icu_6017CanonicalIteratorE'
    ,
    'N6icu_6024CollationElementIteratorE': '<value is a self-reference, replaced by this string>',
    CollationElementIterator: 
        'N6icu_6024CollationElementIteratorE'
    ,
    'N6icu_6013FieldPositionE': '<value is a self-reference, replaced by this string>',
    FieldPosition: 
        'N6icu_6013FieldPositionE'
    ,
    'N6icu_6013ParsePositionE': '<value is a self-reference, replaced by this string>',
    ParsePosition: 
        'N6icu_6013ParsePositionE'
    ,
    'N6icu_606FormatE': [
        'N6icu_6013MeasureFormatE',
        'N6icu_6013MessageFormatE',
        'N6icu_6012PluralFormatE',
        'N6icu_6014TimeUnitFormatE',
        'N6icu_6012SelectFormatE',
        'N6icu_6010DateFormatE',
        'N6icu_6016SimpleDateFormatE',
        'N6icu_6018DateIntervalFormatE',
        'N6icu_6012NumberFormatE',
        'N6icu_6013DecimalFormatE',
        'N6icu_6020CompactDecimalFormatE',
        'N6icu_6021RuleBasedNumberFormatE',
        'N6icu_6012ChoiceFormatE',
    ],
    Format: 
        'N6icu_606FormatE'
    ,
    'N6icu_6013MeasureFormatE': [
        'N6icu_6014TimeUnitFormatE',
    ],
    MeasureFormat: 
        'N6icu_6013MeasureFormatE'
    ,
    'N6icu_6013MessageFormatE': '<value is a self-reference, replaced by this string>',
    MessageFormat: 
        'N6icu_6013MessageFormatE'
    ,
    'N6icu_6011PluralRulesE': '<value is a self-reference, replaced by this string>',
    PluralRules: 
        'N6icu_6011PluralRulesE'
    ,
    'N6icu_6012PluralFormatE': '<value is a self-reference, replaced by this string>',
    PluralFormat: 
        'N6icu_6012PluralFormatE'
    ,
    'N6icu_6014TimeUnitFormatE': '<value is a self-reference, replaced by this string>',
    TimeUnitFormat: 
        'N6icu_6014TimeUnitFormatE'
    ,
    'N6icu_6012SelectFormatE': '<value is a self-reference, replaced by this string>',
    SelectFormat: 
        'N6icu_6012SelectFormatE'
    ,
    'N6icu_6013ListFormatterE': '<value is a self-reference, replaced by this string>',
    ListFormatter: 
        'N6icu_6013ListFormatterE'
    ,
    'N6icu_6017DateFormatSymbolsE': '<value is a self-reference, replaced by this string>',
    DateFormatSymbols: 
        'N6icu_6017DateFormatSymbolsE'
    ,
    'N6icu_6010DateFormatE': [
        'N6icu_6016SimpleDateFormatE',
    ],
    DateFormat: 
        'N6icu_6010DateFormatE'
    ,
    'N6icu_6016SimpleDateFormatE': '<value is a self-reference, replaced by this string>',
    SimpleDateFormat: 
        'N6icu_6016SimpleDateFormatE'
    ,
    'N6icu_6024DateTimePatternGeneratorE': '<value is a self-reference, replaced by this string>',
    DateTimePatternGenerator: 
        'N6icu_6024DateTimePatternGeneratorE'
    ,
    'N6icu_6012DateIntervalE': '<value is a self-reference, replaced by this string>',
    DateInterval: 
        'N6icu_6012DateIntervalE'
    ,
    'N6icu_6016DateIntervalInfoE': '<value is a self-reference, replaced by this string>',
    DateIntervalInfo: 
        'N6icu_6016DateIntervalInfoE'
    ,
    'N6icu_6018DateIntervalFormatE': '<value is a self-reference, replaced by this string>',
    DateIntervalFormat: 
        'N6icu_6018DateIntervalFormatE'
    ,
    'N6icu_6025RelativeDateTimeFormatterE': '<value is a self-reference, replaced by this string>',
    RelativeDateTimeFormatter: 
        'N6icu_6025RelativeDateTimeFormatterE'
    ,
    'N6icu_6020DecimalFormatSymbolsE': '<value is a self-reference, replaced by this string>',
    DecimalFormatSymbols: 
        'N6icu_6020DecimalFormatSymbolsE'
    ,
    'N6icu_6012NumberFormatE': [
        'N6icu_6013DecimalFormatE',
        'N6icu_6020CompactDecimalFormatE',
        'N6icu_6021RuleBasedNumberFormatE',
        'N6icu_6012ChoiceFormatE',
    ],
    NumberFormat: 
        'N6icu_6012NumberFormatE'
    ,
    'N6icu_6018CurrencyPluralInfoE': '<value is a self-reference, replaced by this string>',
    CurrencyPluralInfo: 
        'N6icu_6018CurrencyPluralInfoE'
    ,
    'N6icu_6013DecimalFormatE': [
        'N6icu_6020CompactDecimalFormatE',
    ],
    DecimalFormat: 
        'N6icu_6013DecimalFormatE'
    ,
    'N6icu_6020CompactDecimalFormatE': '<value is a self-reference, replaced by this string>',
    CompactDecimalFormat: 
        'N6icu_6020CompactDecimalFormatE'
    ,
    'N6icu_6021RuleBasedNumberFormatE': '<value is a self-reference, replaced by this string>',
    RuleBasedNumberFormat: 
        'N6icu_6021RuleBasedNumberFormatE'
    ,
    'N6icu_6012ChoiceFormatE': '<value is a self-reference, replaced by this string>',
    ChoiceFormat: 
        'N6icu_6012ChoiceFormatE'
    ,
    'N6icu_608TimeZoneE': [
        'N6icu_6014SimpleTimeZoneE',
    ],
    TimeZone: 
        'N6icu_608TimeZoneE'
    ,
    'N6icu_6014SimpleTimeZoneE': '<value is a self-reference, replaced by this string>',
    SimpleTimeZone: 
        'N6icu_6014SimpleTimeZoneE'
    ,
    'N6icu_608CalendarE': [
        'N6icu_6017GregorianCalendarE',
    ],
    Calendar: 
        'N6icu_608CalendarE'
    ,
    'N6icu_6017GregorianCalendarE': '<value is a self-reference, replaced by this string>',
    GregorianCalendar: 
        'N6icu_6017GregorianCalendarE'
    ,
    'N6icu_6012CollationKeyE': '<value is a self-reference, replaced by this string>',
    CollationKey: 
        'N6icu_6012CollationKeyE'
    ,
    'N6icu_608CollatorE': [
        'N6icu_6017RuleBasedCollatorE',
    ],
    Collator: 
        'N6icu_608CollatorE'
    ,
    'N6icu_6017RuleBasedCollatorE': '<value is a self-reference, replaced by this string>',
    RuleBasedCollator: 
        'N6icu_6017RuleBasedCollatorE'
    ,
    'N6icu_6014UnicodeFunctorE': '<value is a self-reference, replaced by this string>',
    UnicodeFunctor: 
        'N6icu_6014UnicodeFunctorE'
    ,
    'N6icu_6014UnicodeMatcherE': '<value is a self-reference, replaced by this string>',
    UnicodeMatcher: 
        'N6icu_6014UnicodeMatcherE'
    ,
    'N6icu_6013UnicodeFilterE': [
        'N6icu_6010UnicodeSetE',
    ],
    UnicodeFilter: 
        'N6icu_6013UnicodeFilterE'
    ,
    'N6icu_6010UnicodeSetE': '<value is a self-reference, replaced by this string>',
    UnicodeSet: 
        'N6icu_6010UnicodeSetE'
    ,
    'N6icu_6018UnicodeSetIteratorE': '<value is a self-reference, replaced by this string>',
    UnicodeSetIterator: 
        'N6icu_6018UnicodeSetIteratorE'
    ,
    'N6icu_6012RegexPatternE': '<value is a self-reference, replaced by this string>',
    RegexPattern: 
        'N6icu_6012RegexPatternE'
    ,
    'N6icu_6012RegexMatcherE': '<value is a self-reference, replaced by this string>',
    RegexMatcher: 
        'N6icu_6012RegexMatcherE'
    ,
    'N6icu_6010NormalizerE': '<value is a self-reference, replaced by this string>',
    Normalizer: 
        'N6icu_6010NormalizerE'
    ,
    'N6icu_6011Normalizer2E': [
        'N6icu_6019FilteredNormalizer2E',
    ],
    Normalizer2: 
        'N6icu_6011Normalizer2E'
    ,
    'N6icu_6019FilteredNormalizer2E': '<value is a self-reference, replaced by this string>',
    FilteredNormalizer2: 
        'N6icu_6019FilteredNormalizer2E'
    ,
    'N6icu_6014SearchIteratorE': [
        'N6icu_6012StringSearchE',
    ],
    SearchIterator: 
        'N6icu_6014SearchIteratorE'
    ,
    'N6icu_6012StringSearchE': '<value is a self-reference, replaced by this string>',
    StringSearch: 
        'N6icu_6012StringSearchE'
    ,
}

