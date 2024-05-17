@echo off
set arg1=%1
call activate %arg1%
python start_jupyter_server.py -e %arg1%
call conda deactivate