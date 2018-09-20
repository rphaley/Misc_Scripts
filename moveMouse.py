import ctypes, time
from random import randint

while True:
	ctypes.windll.user32.SetCursorPos(randint(300,600), randint(300,600))
	ctypes.windll.user32.mouse_event(2, 0, 0, 0,0)
	ctypes.windll.user32.mouse_event(4, 0, 0, 0,0)
	time.sleep(randint(5,300))