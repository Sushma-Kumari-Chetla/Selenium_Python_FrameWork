#!/bin/bash
pytest -s -v -m "sanity" --html=./Reports/markerreport_chrome.html --browser=chrome testCases/
pytest -s -v -m "sanity" --html=./Reports/markerreport_firefox.html --browser=firefox testCases/
