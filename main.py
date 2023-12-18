import pyautogui
import time

positions = [
    (3610, 57),
    (2994, 535),
    (2885, 602),
    (2952, 652),
    (3183, 436),
]

oldpw = "OldPassword"
newpw = "NewPassword"

time.sleep(3)

for i, pos in enumerate(positions):
    x, y = pos
    pyautogui.click(x, y)
    time.sleep(0.1)

    if i == len(positions) - 1:
        pyautogui.typewrite(oldpw)
        time.sleep(0.1)
pyautogui.click(3137, 497)
time.sleep(0.1)

pyautogui.typewrite(newpw)
time.sleep(0.1)

pyautogui.click(3143, 549)
time.sleep(0.1)
pyautogui.typewrite(newpw)
time.sleep(0.1)

pyautogui.click(2947, 660)
time.sleep(0.1)
