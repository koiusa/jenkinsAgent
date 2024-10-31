@echo off
pushd %~dp0\bin\
setlocal

.\jenkins-slave.exe stop
.\jenkins-slave.exe uninstall

endlocal
popd
exit /b