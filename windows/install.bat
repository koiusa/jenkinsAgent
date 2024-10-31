@echo off

pushd %~dp0\bin\
setlocal

py .\generate-serviceconfig.py

.\jenkins-slave.exe install
.\jenkins-slave.exe start

endlocal
popd

exit /b