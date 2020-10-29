*** Settings ***
Library    ExtendedMainframe3270       
Test Setup    Open mainframe connection
Test Teardown    Close mainframe connection


*** Variables ***
${pub400Host}    pub400.com
${sessionFile}    ${CURDIR}\\..\\resources\\pub400.wc3270


*** Keywords ***
Open mainframe connection
    Open Connection    host=${pub400Host}    isSessionFile=${False}

Close mainframe connection
    Close Connection


*** Test Cases ***
Open std host connection
    Sleep    2s
    
Open session connection
    [Setup]    NONE
    [Teardown]    NONE
    Open Connection    host=${sessionFile}    isSessionFile=${True}
    Sleep    2s
    Close Connection
    
Do a mainframe screenshot
    Sleep    2s
    Set Screenshot Folder    ${CURDIR}\\..\\Results\\
    Take Screenshot    format=jpg
    
Check If return value for found string
    @{server_name}    Read Value For Given String    Server name . . . :\ \ \ \     6    
    Should Be Equal As Strings    "${server_name}[0]"    "PUB400"
