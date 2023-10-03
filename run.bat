@REM Chrome

pytest -s -v -m "sanity" --html=./Reports/markerreport_chrome.html testCases/ --browser chrome

@REM pytest -s -v -m "sanity and regression" --html=./Reports/markerreport.html testCases/ --browser chrome

@REM pytest -s -v -m " sanity or regression " --html=./Reports/markerreport.html testCases/ --browser chrome

:: pytest -s -v -m "regression" --html=./Reports/markerreport.html testCases/ --browser chrome

::  - "::" is comment; @REM is also comment (cmd+/) At a time we can run only one command and comment rest.

@REM firefox
pytest -s -v -m "sanity" --html=./Reports/markerreport_forefox.html testCases/ --browser firefox

@REM pytest -s -v -m "sanity and regression" --html=./Reports/markerreport.html testCases/ --browser chrome

@REM pytest -s -v -m " sanity or regression " --html=./Reports/markerreport.html testCases/ --browser chrome

:: pytest -s -v -m "regression" --html=./Reports/markerreport.html testCases/ --browser chrome
