import pyautogui
import time

# Warten auf Mausklick
while True:
    x, y = pyautogui.position()
    print("Mausklick an Position: x={}, y={}".format(x, y))
    time.sleep(0.1)
