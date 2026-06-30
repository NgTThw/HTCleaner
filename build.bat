@ECHO OFF
RMDIR /S /Q "./dist/HTParkingCleaner"
python -m PyInstaller HTParkingCleaner.spec
RMDIR /S /Q "./build"
PAUSE