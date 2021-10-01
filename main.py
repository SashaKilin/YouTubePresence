from win32gui import GetWindowText, GetForegroundWindow
from pypresence import Presence
import time

RPC = Presence(893175364732465202)
RPC.connect()



while True:
	window = str(GetWindowText(GetForegroundWindow()))

	if "YouTube" in window:
		text = window[:-26]
		text = text[6:]

		if text == "":
			text = "Просматривает главную страницу YouTube"
	else:
		text = "В данный момент ничего не смотрит."

	RPC.update(
		state = text,
		large_text = "YouTube Presence by Stullexy (version 0.1)"
	)

	time.sleep(5)