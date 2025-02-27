#platform support

#linux
def LINUX_X86():
    ver = int

#win32
def WIN32():
    ver = int

#macos
def MACOS():
    ver = int

import string

LinuxFile_Extension = string = '.UNIX'
Win32File_Extension = string = '.WIN'
MacOsFile_Extension = string = '.MAC'

path = {'C/:/..'}

def LinuxFind():
    if( LINUX_X86 ):
        LinuxFile_Extension.find(path)
        LinuxFile_Extension.format(LinuxFile_Extension)        
        
def WinFind():
    if( WIN32 ):
        Win32File_Extension.find(path)
        Win32File_Extension.format(Win32File_Extension)

def MacFind():
    if( MACOS ):
        MacOsFile_Extension.find(path)
        MacOsFile_Extension.format(MacOsFile_Extension)




