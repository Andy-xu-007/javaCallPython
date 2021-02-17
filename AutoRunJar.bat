@echo off
echo ------- start --------
echo=
set INTERVAL=5
:Again
java -jar javaCallPythonTask.jar
timeout %INTERVAL%
goto Again