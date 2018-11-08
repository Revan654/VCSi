import re, os, sys
from MediaInfoDLL3 import *

def MediaInput():
    Input=sys.argv[1]    
    return(Input)

MediaRead = MediaInput()

MI = MediaInfo()
############################
#Function Call For Template
############################

def VideoFormatCodec():
    MI.Open(MediaRead)
    MI.Option_Static("Inform", "Video;%Format%")
    Codec=MI.Inform()
    MI.Close()
    return(Codec)

def VideoEncoder():
    MI.Open(MediaRead)
    MI.Option_Static("Inform", "Video;%Format%")
    Encoder=MI.Inform()
    if Encoder == "AVC":
        EncoderFile="x264"
        MI.Close()
        return(EncoderFile)
    elif Encoder == "HEVC":
        EncoderFile="x265"
        MI.Close()
        return(EncoderFile)

def VideoContainer():
    MI.Open(MediaRead)
    MI.Option_Static("Inform", "General;%FileExtension%")
    VideoContainerFile=MI.Inform()
    MI.Close()
    return(VideoContainerFile)

def VideoLength():
    MI.Open(MediaRead)
    MI.Option_Static("Inform", "General;%Duration_String4%")
    DurationFile=MI.Inform()
    MI.Close()
    return(DurationFile)

def VideoLengthMod():
    MI.Open(MediaRead)
    MI.Option_Static("Inform", "General;%Duration_String5%")
    DurationFile=MI.Inform()
    MI.Close()
    regex = r"(.*)\:(.*?)\:(.*)\..*"
    matches = re.search(regex, DurationFile, re.DOTALL)
    if matches:
        Hour=matches.group(1)
        Min=matches.group(2)
        Second=matches.group(3)
        Build=Hour+":"+Min+":"+Second
        return(Build)


def VideoLength_Norm():
    MI.Open(MediaRead)
    MI.Option_Static("Inform", "General;%Duration_String2%")
    DurationFile=MI.Inform()
    MI.Close()
    return(DurationFile)
    
def ChromaSubsampling():
    MI.Open(MediaRead)
    MI.Option_Static("Inform", "Video;%ChromaSubsampling_String%")
    Chroma=MI.Inform()
    ExportChroma=Chroma.replace(":", "")
    MI.Close()
    return(ExportChroma)
    
def Matrix():
    MI.Open(MediaRead)
    MI.Option_Static("Inform", "Video;%matrix_coefficients%")
    BT=MI.Inform().lower()
    MI.Close()
    return(BT)  
    
def VideoRange():
    MI.Open(MediaRead)
    MI.Option_Static("Inform", "Video;%colour_range%")
    Range=MI.Inform()
    if Range == "Limited":
        MI.Close()
        return("tv")    
    elif Range == "":
        return("Unknown")
    else:
        MI.Close()
        return("pc")            

def VideoBitRate():
    MI.Open(MediaRead)
    MI.Option_Static("Inform", "General;%OverallBitRate_String%")
    VideoBiteRate=MI.Inform()
    MI.Close()
    return(VideoBiteRate)

def VideoProfile():
    MI.Open(MediaRead)
    MI.Option_Static("Inform", "Video;%Format_Profile%")
    VProfile=MI.Inform()[:4]
    MI.Close()
    return(VProfile)        
    
def VVideoBitRate():
    MI.Open(MediaRead)
    MI.Option_Static("Inform", "Video;%BitRate_String%")
    VideoBiteRateMaxs=MI.Inform()
    MI.Close()
    return(VideoBiteRateMaxs)    

def VideoBitRateMod():
    MI.Open(MediaRead)
    MI.Option_Static("Inform", "General;%OverallBitRate_String%")
    VideoBiteRate=MI.Inform()
    Rate=VideoBiteRate[:5]
    MI.Close()
    return(Rate)

def VideoHeight():
    MI.Open(MediaRead)
    MI.Option_Static("Inform", "Video;%Height%")
    Height=MI.Inform()
    MI.Close()
    return(Height)

def VideoWidth():
    MI.Open(MediaRead)
    MI.Option_Static("Inform", "Video;%Width%")
    Width=MI.Inform()
    MI.Close()
    return(Width)

def VideoFormat():
    MI.Open(MediaRead)
    MI.Option_Static("Inform", "Video;%Height%")
    Height=MI.Inform()
    MI.Option_Static("Inform", "Video;%Width%")
    Width=MI.Inform()
    if Height == "480":
        Format = "480p"
        MI.Close()
        return(Format)
    elif Width == "1280" and Height == "720":
        Format="720p"
        MI.Close()
        return(Format)
    elif Width == "1920" and Height == "1080":
        Format="1080p"
        MI.Close()
        return(Format)
    elif Width == "2560" and Height == "1440":
        Format="2k"
        MI.Close()
        return(Format)
    elif Width == "3840" and Height == "2160":
        Format="4K"
        MI.Close()
        return(Format)

def VideoFrameRate():
    MI.Open(MediaRead)
    MI.Option_Static("Inform", "General;%FrameRate%")
    VFrameRates=MI.Inform()
    MI.Close()
    return(VFrameRates)
    
def VideoFrameRateFPS():
    MI.Open(MediaRead)
    MI.Option_Static("Inform", "General;%FrameRate_String%")
    VFrameRatesFPS=MI.Inform().lower()
    MI.Close()
    return(VFrameRatesFPS)

def FileSize():
    MI.Open(MediaRead)
    MI.Option_Static("Inform", "General;%FileSize_String2%")
    FileSize=MI.Inform()
    MI.Close()
    return(FileSize)
    
def FileSizeBytes():
    MI.Open(MediaRead)
    MI.Option_Static("Inform", "General;%FileSize%")
    FileSizeByte=MI.Inform()
    MI.Close()
    return(FileSizeByte)

def ColorSpace():
    MI.Open(MediaRead)
    MI.Option_Static("Inform", "Video;%ColorSpace%")
    ColorSpaces=MI.Inform().lower()
    MI.Close()
    return(ColorSpaces)

def BitDepth():
    MI.Open(MediaRead)
    MI.Option_Static("Inform", "Video;%BitDepth%")
    VideoDepth=MI.Inform()
    return(VideoDepth)    
        
def FileName():
    MI.Open(MediaRead)
    MI.Option_Static("Inform", "General;%CompleteName%")
    FileNames=MI.Inform()
    Path=os.path.basename(FileNames)
    return(Path)        

def ScanType():
    MI.Open(MediaRead)
    MI.Option_Static("Inform", "Video;%ScanType%")
    ScanType=MI.Inform()
    MI.Close()
    return(ScanType)    

def AudioCodec():
    MI.Open(MediaRead)
    MI.Option_Static("Inform", "Audio;%Format%")
    AudioFormat=MI.Inform()
    MI.Close()
    return(AudioFormat)

def AudioBitRate():
    MI.Open(MediaRead)
    MI.Option_Static("Inform", "Audio;%BitRate_String%")
    AudioBitRate=MI.Inform()
    MI.Close()
    return(AudioBitRate)

def AudioSampleRate():
    MI.Open(MediaRead)
    MI.Option_Static("Inform", "Audio;%SamplingRate_String%")
    AudioSampleRate=MI.Inform()
    MI.Close()
    return(AudioSampleRate)
    
def Channels():
    MI.Open(MediaRead)
    MI.Option_Static("Inform", "Audio;%Channel(s)%")
    Channel=MI.Inform()
    if Channel == "1":
        MI.Close()
        return("Mono")
    elif Channel == "2":
        MI.Close()
        return("Stereo")
    elif Channel == "5.1":
        MI.Close()
        return("Surround Sound")
    elif Channel == "7.1":
        MI.Close()
        return("Surround Sound")    