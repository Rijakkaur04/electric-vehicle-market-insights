@echo off
title Pushing to GitHub
echo ====================================================================
echo  Pushing Electric Vehicle Market Insights to GitHub
echo  Target: https://github.com/Rijakkaur04/electric-vehicle-market-insights
echo ====================================================================
echo.

cd /d "%~dp0"

echo 1. Verifying current branch and status...
git branch -M main

echo 2. Pushing files to GitHub...
echo (If a browser window or login prompt appears, please sign in to authorize)
echo.
git push -u origin main

echo.
echo ====================================================================
echo  Done! Your repository now has all project files.
echo  Visit: https://github.com/Rijakkaur04/electric-vehicle-market-insights
echo ====================================================================
echo.
pause
