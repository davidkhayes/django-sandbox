@echo off

set TIMESTAMP=%DATE:~-4%%DATE:~4,2%%DATE:~7,2%%time:~0,2%%time:~3,2%%time:~6,2%%time:~9,2%
set "TIMESTAMP=%Timestamp: =0%"

ping -n 10 8.8.8.8 > files\%TIMESTAMP%.TXT

echo ran a task?
