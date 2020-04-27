@echo off

set fn=%1
set dir=%2
set var="F:\Documents\Programming Projects%dir%/%fn%"
cd /d %~dp0

If "%1"=="" (
    echo "error"
) else ( 
    if "%2"=="l" (
        python local.py %fn%
        ) else (
            python remote.py %fn% %dir%
            cd %var%
        )
    )