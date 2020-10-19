# ExtendedMainframe3270 Library

## Introduction

ExtendedMainframe3270 is a fork from original [Altran's library](https://github.com/Altran-PT-GDC/Robot-Framework-Mainframe-3270-Library) used for Robot Framework

## Notes

I've added session file handling so You can use *.wc3270 session file and specify all needed parameters inside.<br>
[wc3270 Resource](http://x3270.bgp.nu/wc3270-man.html#Resources) can be found on official x3270 site

## Example

    *** Settings ***
    Library           ExtendedMainframe3270
    *** Test Cases ***
    Example
        Open Connection    host=resources\\pub400.wc3270    isSessionFile=${True}
        Change Wait Time    0.4
        Change Wait Time After Write    0.4
        Set Screenshot Folder    C:\\Temp\\IMG
        ${value}    Read    3    10    17
        Page Should Contain String    ENTER APPLICATION
        Wait Field Detected
        Write Bare    applicationname
        Send Enter
        Take Screenshot
        Close Connection
