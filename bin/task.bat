@echo off

set "TIMESTAMP=%DATE:~-4%%DATE:~4,2%%DATE:~7,2%%time:~0,2%%time:~3,2%%time:~6,2%%time:~9,2%"
set "TIMESTAMP=%Timestamp: =0%"
set "COUNT=%1"
IF "%COUNT%"=="" SET "COUNT=10"

ping -n %COUNT% 8.8.8.8 > files\%TIMESTAMP%.TXT
