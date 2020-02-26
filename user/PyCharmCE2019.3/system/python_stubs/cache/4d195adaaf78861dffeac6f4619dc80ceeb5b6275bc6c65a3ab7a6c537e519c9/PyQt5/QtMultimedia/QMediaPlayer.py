# encoding: utf-8
# module PyQt5.QtMultimedia
# from /usr/lib/python3/dist-packages/PyQt5/QtMultimedia.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore


from .QMediaObject import QMediaObject

class QMediaPlayer(QMediaObject):
    """ QMediaPlayer(parent: QObject = None, flags: Union[QMediaPlayer.Flags, QMediaPlayer.Flag] = 0) """
    def audioAvailableChanged(self, bool): # real signature unknown; restored from __doc__
        """ audioAvailableChanged(self, bool) [signal] """
        pass

    def audioRole(self): # real signature unknown; restored from __doc__
        """ audioRole(self) -> QAudio.Role """
        pass

    def availability(self): # real signature unknown; restored from __doc__
        """ availability(self) -> QMultimedia.AvailabilityStatus """
        pass

    def bind(self, QObject): # real signature unknown; restored from __doc__
        """ bind(self, QObject) -> bool """
        return False

    def bufferStatus(self): # real signature unknown; restored from __doc__
        """ bufferStatus(self) -> int """
        return 0

    def bufferStatusChanged(self, p_int): # real signature unknown; restored from __doc__
        """ bufferStatusChanged(self, int) [signal] """
        pass

    def currentMedia(self): # real signature unknown; restored from __doc__
        """ currentMedia(self) -> QMediaContent """
        return QMediaContent

    def currentMediaChanged(self, QMediaContent): # real signature unknown; restored from __doc__
        """ currentMediaChanged(self, QMediaContent) [signal] """
        pass

    def currentNetworkConfiguration(self): # real signature unknown; restored from __doc__
        """ currentNetworkConfiguration(self) -> QNetworkConfiguration """
        pass

    def duration(self): # real signature unknown; restored from __doc__
        """ duration(self) -> int """
        return 0

    def durationChanged(self, p_int): # real signature unknown; restored from __doc__
        """ durationChanged(self, int) [signal] """
        pass

    def error(self, QMediaPlayer_Error=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        error(self) -> QMediaPlayer.Error
        error(self, QMediaPlayer.Error) [signal]
        """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def hasSupport(self, p_str, codecs, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ hasSupport(str, codecs: Iterable[str] = [], flags: Union[QMediaPlayer.Flags, QMediaPlayer.Flag] = 0) -> QMultimedia.SupportEstimate """
        pass

    def isAudioAvailable(self): # real signature unknown; restored from __doc__
        """ isAudioAvailable(self) -> bool """
        return False

    def isMuted(self): # real signature unknown; restored from __doc__
        """ isMuted(self) -> bool """
        return False

    def isSeekable(self): # real signature unknown; restored from __doc__
        """ isSeekable(self) -> bool """
        return False

    def isVideoAvailable(self): # real signature unknown; restored from __doc__
        """ isVideoAvailable(self) -> bool """
        return False

    def media(self): # real signature unknown; restored from __doc__
        """ media(self) -> QMediaContent """
        return QMediaContent

    def mediaChanged(self, QMediaContent): # real signature unknown; restored from __doc__
        """ mediaChanged(self, QMediaContent) [signal] """
        pass

    def mediaStatus(self): # real signature unknown; restored from __doc__
        """ mediaStatus(self) -> QMediaPlayer.MediaStatus """
        pass

    def mediaStatusChanged(self, QMediaPlayer_MediaStatus): # real signature unknown; restored from __doc__
        """ mediaStatusChanged(self, QMediaPlayer.MediaStatus) [signal] """
        pass

    def mediaStream(self): # real signature unknown; restored from __doc__
        """ mediaStream(self) -> QIODevice """
        pass

    def mutedChanged(self, bool): # real signature unknown; restored from __doc__
        """ mutedChanged(self, bool) [signal] """
        pass

    def networkConfigurationChanged(self, QNetworkConfiguration): # real signature unknown; restored from __doc__
        """ networkConfigurationChanged(self, QNetworkConfiguration) [signal] """
        pass

    def pause(self): # real signature unknown; restored from __doc__
        """ pause(self) """
        pass

    def play(self): # real signature unknown; restored from __doc__
        """ play(self) """
        pass

    def playbackRate(self): # real signature unknown; restored from __doc__
        """ playbackRate(self) -> float """
        return 0.0

    def playbackRateChanged(self, p_float): # real signature unknown; restored from __doc__
        """ playbackRateChanged(self, float) [signal] """
        pass

    def playlist(self): # real signature unknown; restored from __doc__
        """ playlist(self) -> QMediaPlaylist """
        return QMediaPlaylist

    def position(self): # real signature unknown; restored from __doc__
        """ position(self) -> int """
        return 0

    def positionChanged(self, p_int): # real signature unknown; restored from __doc__
        """ positionChanged(self, int) [signal] """
        pass

    def seekableChanged(self, bool): # real signature unknown; restored from __doc__
        """ seekableChanged(self, bool) [signal] """
        pass

    def setAudioRole(self, QAudio_Role): # real signature unknown; restored from __doc__
        """ setAudioRole(self, QAudio.Role) """
        pass

    def setMedia(self, QMediaContent, stream=None): # real signature unknown; restored from __doc__
        """ setMedia(self, QMediaContent, stream: QIODevice = None) """
        pass

    def setMuted(self, bool): # real signature unknown; restored from __doc__
        """ setMuted(self, bool) """
        pass

    def setNetworkConfigurations(self, Iterable, QNetworkConfiguration=None): # real signature unknown; restored from __doc__
        """ setNetworkConfigurations(self, Iterable[QNetworkConfiguration]) """
        pass

    def setPlaybackRate(self, p_float): # real signature unknown; restored from __doc__
        """ setPlaybackRate(self, float) """
        pass

    def setPlaylist(self, QMediaPlaylist): # real signature unknown; restored from __doc__
        """ setPlaylist(self, QMediaPlaylist) """
        pass

    def setPosition(self, p_int): # real signature unknown; restored from __doc__
        """ setPosition(self, int) """
        pass

    def setVideoOutput(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setVideoOutput(self, QVideoWidget)
        setVideoOutput(self, QGraphicsVideoItem)
        setVideoOutput(self, QAbstractVideoSurface)
        """
        pass

    def setVolume(self, p_int): # real signature unknown; restored from __doc__
        """ setVolume(self, int) """
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ state(self) -> QMediaPlayer.State """
        pass

    def stateChanged(self, QMediaPlayer_State): # real signature unknown; restored from __doc__
        """ stateChanged(self, QMediaPlayer.State) [signal] """
        pass

    def stop(self): # real signature unknown; restored from __doc__
        """ stop(self) """
        pass

    def supportedAudioRoles(self): # real signature unknown; restored from __doc__
        """ supportedAudioRoles(self) -> List[QAudio.Role] """
        return []

    def supportedMimeTypes(self, flags, QMediaPlayer_Flags=None, QMediaPlayer_Flag=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ supportedMimeTypes(flags: Union[QMediaPlayer.Flags, QMediaPlayer.Flag] = 0) -> List[str] """
        pass

    def unbind(self, QObject): # real signature unknown; restored from __doc__
        """ unbind(self, QObject) """
        pass

    def videoAvailableChanged(self, bool): # real signature unknown; restored from __doc__
        """ videoAvailableChanged(self, bool) [signal] """
        pass

    def volume(self): # real signature unknown; restored from __doc__
        """ volume(self) -> int """
        return 0

    def volumeChanged(self, p_int): # real signature unknown; restored from __doc__
        """ volumeChanged(self, int) [signal] """
        pass

    def __init__(self, parent=None, flags, QMediaPlayer_Flags=None, QMediaPlayer_Flag=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    AccessDeniedError = 4
    BufferedMedia = 6
    BufferingMedia = 5
    EndOfMedia = 7
    FormatError = 2
    InvalidMedia = 8
    LoadedMedia = 3
    LoadingMedia = 2
    LowLatency = 1
    NetworkError = 3
    NoError = 0
    NoMedia = 1
    PausedState = 2
    PlayingState = 1
    ResourceError = 1
    ServiceMissingError = 5
    StalledMedia = 4
    StoppedState = 0
    StreamPlayback = 2
    UnknownMediaStatus = 0
    VideoSurface = 4


