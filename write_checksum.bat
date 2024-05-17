set arg1=%1
python %~dp0\write_checksum.py -e %arg1%
echo %ERRORLEVEL%