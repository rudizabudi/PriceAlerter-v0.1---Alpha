call "C:\Users\fruhd\OneDrive\CloudDesktop\Python\Price Alert v2\vEnv\Scripts\activate.bat"

cd "C:\Users\fruhd\OneDrive\CloudDesktop\Python\Price Alert v2\ui"

pyuic5 -x root.ui -o qtgui.py
MOVE "qtgui.py" "C:\Users\fruhd\OneDrive\CloudDesktop\Python\Price Alert v2\windows\gui"

pyuic5 -x add_alertlist_popup.ui -o add_alertlist_popup.py
MOVE "add_alertlist_popup.py" "C:\Users\fruhd\OneDrive\CloudDesktop\Python\Price Alert v2\windows\popups"

pyuic5 -x add_alert_popup_first.ui -o add_alert_popup_first.py
MOVE "add_alert_popup_first.py" "C:\Users\fruhd\OneDrive\CloudDesktop\Python\Price Alert v2\windows\popups"

pyuic5 -x add_type_selection.ui -o add_type_selection.py
MOVE "add_type_selection.py" "C:\Users\fruhd\OneDrive\CloudDesktop\Python\Price Alert v2\windows\popups"

pyuic5 -x add_alert_popup_second.ui -o add_alert_popup_second.py
MOVE "add_alert_popup_second.py" "C:\Users\fruhd\OneDrive\CloudDesktop\Python\Price Alert v2\windows\popups"

pyrcc5 "C:\Users\fruhd\OneDrive\CloudDesktop\Python\Price Alert v2\res\resources.qrc" -o resources_rc.py
MOVE "resources_rc.py" "C:\Users\fruhd\OneDrive\CloudDesktop\Python\Price Alert v2"
