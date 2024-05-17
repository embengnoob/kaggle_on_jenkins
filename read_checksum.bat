set arg1=%1
python %~dp0\read_checksum.py -e %arg1%
set STATUS = %ERRORLEVEL%
exit %STATUS%