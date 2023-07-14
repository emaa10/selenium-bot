import time
import random
import pyautogui

votes = 10000

i = 0;

# Screen Coords
x_1 = 316 # Jetzt abstimmen
y_1 = 328

x_2 = 259  # Zustimmung, um Inhalte von Friendly Captcha anzuzeigen
y_2 = 382

x_3 = 259  # Anti-Roboter-Verifizierung
y_3 = 313

x_4 = 307  # Stimme abgeben
y_4 = 308

x_5 = 135   # Tor Menü
y_5 = 98

x_6 = 212   # Neuer Kanal für diese Seite
y_6 = 384

x_7 = 40  # Lesezeichen aufrufen
y_7 = 130

while True:
#for x in range(0, votes):
    i += 1
    pyautogui.click(x_1, y_1)
    time.sleep(1.5)

    pyautogui.click(x_2, y_2)
    time.sleep(2)

    pyautogui.click(x_3, y_3)
    time.sleep(12)

    pyautogui.click(x_4, y_4)
    time.sleep(1)

    pyautogui.click(x_5, y_5)
    time.sleep(1)

    pyautogui.click(x_6, y_6)
    time.sleep(3)

    pyautogui.click(x_7, y_7)
    time.sleep(5)

    time.sleep(random.randint(1, 8))   # random time to fix detections

    print(str(i) + " mal abgestimmt.")

    # pyautogui.hotkey('command', 'shift', '3')
    # time.sleep(0.5)
    # pyautogui.keyUp('command')
    # pyautogui.keyUp('shift')
    # pyautogui.keyUp('3')
    # time.sleep(1)
