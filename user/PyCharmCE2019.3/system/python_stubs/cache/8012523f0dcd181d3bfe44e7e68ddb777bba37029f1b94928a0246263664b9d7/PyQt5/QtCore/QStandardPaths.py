# encoding: utf-8
# module PyQt5.QtCore
# from /usr/lib/python3/dist-packages/PyQt5/QtCore.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc
# no imports

class QStandardPaths(): # skipped bases: <class 'sip.simplewrapper'>
    """ QStandardPaths(QStandardPaths) """
    def displayName(self, QStandardPaths_StandardLocation): # real signature unknown; restored from __doc__
        """ displayName(QStandardPaths.StandardLocation) -> str """
        return ""

    def enableTestMode(self, bool): # real signature unknown; restored from __doc__
        """ enableTestMode(bool) """
        pass

    def findExecutable(self, p_str, paths, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ findExecutable(str, paths: Iterable[str] = []) -> str """
        pass

    def locate(self, QStandardPaths_StandardLocation, p_str, options=None): # real signature unknown; restored from __doc__
        """ locate(QStandardPaths.StandardLocation, str, options: QStandardPaths.LocateOptions = QStandardPaths.LocateFile) -> str """
        return ""

    def locateAll(self, QStandardPaths_StandardLocation, p_str, options=None): # real signature unknown; restored from __doc__
        """ locateAll(QStandardPaths.StandardLocation, str, options: QStandardPaths.LocateOptions = QStandardPaths.LocateFile) -> List[str] """
        return []

    def setTestModeEnabled(self, bool): # real signature unknown; restored from __doc__
        """ setTestModeEnabled(bool) """
        pass

    def standardLocations(self, QStandardPaths_StandardLocation): # real signature unknown; restored from __doc__
        """ standardLocations(QStandardPaths.StandardLocation) -> List[str] """
        return []

    def writableLocation(self, QStandardPaths_StandardLocation): # real signature unknown; restored from __doc__
        """ writableLocation(QStandardPaths.StandardLocation) -> str """
        return ""

    def __init__(self, QStandardPaths): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    AppConfigLocation = 18
    AppDataLocation = 17
    ApplicationsLocation = 3
    AppLocalDataLocation = 9
    CacheLocation = 10
    ConfigLocation = 13
    DataLocation = 9
    DesktopLocation = 0
    DocumentsLocation = 1
    DownloadLocation = 14
    FontsLocation = 2
    GenericCacheLocation = 15
    GenericConfigLocation = 16
    GenericDataLocation = 11
    HomeLocation = 8
    LocateDirectory = 1
    LocateFile = 0
    MoviesLocation = 5
    MusicLocation = 4
    PicturesLocation = 6
    RuntimeLocation = 12
    TempLocation = 7


