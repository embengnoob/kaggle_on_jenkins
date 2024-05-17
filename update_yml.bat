@echo off
set arg1=%1
call activate %arg1%
conda env export > %~dp0\environment_%arg1%.yml
call conda deactivate 