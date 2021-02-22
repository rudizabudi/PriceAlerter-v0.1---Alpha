set Path="C:\Users\fruhd\OneDrive\CloudDesktop\Python\Price Alert v2\ui"
for /f "tokens=*" %%a in ('dir /A:-D /B /O:-D /S %Path%') do set NEW=%%a
for %%F in ("%NEW%") do set NEW=%%~nxF
call "C:\Users\fruhd\OneDrive\CloudDesktop\Python\Price Alert v2\vEnv\Scripts\activate.bat"
cd "C:\Users\fruhd\OneDrive\CloudDesktop\Python\Price Alert v2\ui"
pyuic5 -x %NEW% -o qtgui.py
MOVE "qtgui.py" "C:\Users\fruhd\OneDrive\CloudDesktop\Python\Price Alert v2"

pyrcc5 "C:\Users\fruhd\OneDrive\CloudDesktop\Python\Price Alert v2\res\resources.qrc" -o resources_rc.py
MOVE "resources_rc.py" "C:\Users\fruhd\OneDrive\CloudDesktop\Python\Price Alert v2"
pause