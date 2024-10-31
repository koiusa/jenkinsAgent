for /f "tokens=1,* delims==" %%a in (setting.ini) do (
    set %%a=%%b
)

curl.exe -sO %url%/jnlpJars/agent.jar
java -jar agent.jar -url %url% -secret %secret% -name %name% -workDir %workdir%

