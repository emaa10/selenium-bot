import time
import random
import pyautogui

votes = 10000

i = 0;

# Screen Coords
x_1 = 1260 # Jetzt abstimmen
y_1 = 574

x_2 = 1125  # Zustimmung, um Inhalte von Friendly Captcha anzuzeigen
y_2 = 698

x_3 = 1136  # Anti-Roboter-Verifizierung
y_3 = 546

x_4 = 1253  # Stimme abgeben
y_4 = 539

x_5 = 169   # Tor Menü
y_5 = 80

x_6 = 273   # Neuer Kanal für diese Seite
y_6 = 422

x_7 = 1128  # Lesezeichen aufrufen
y_7 = 127

for x in range(0, votes):
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
