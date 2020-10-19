*** Settings ***
Library    ExtendedMainframe3270

*** Variables ***
${pub400Host}    pub400.com
${sessionFile}    ${CURDIR}\\..\\resources\\pub400.wc3270


*** Test Cases ***
Open std host connection
    Open Connection    host=${pub400Host}    isSessionFile=${False}
    Sleep    2s
    Close Connection
    
Open session connection
    Open Connection    host=${sessionFile}    isSessionFile=${True}
    Sleep    2s
    Close Connection