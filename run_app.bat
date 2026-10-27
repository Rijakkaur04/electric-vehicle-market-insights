@echo off
echo ====================================================================
echo Starting Electric Vehicle Market Performance ^& Insights Web App
echo ====================================================================
echo Launching Flask web server on http://localhost:5000 ...
echo Press Ctrl+C to stop the server at any time.
echo ====================================================================

cd /d "%~dp0\web_app"
python app.py
pause

