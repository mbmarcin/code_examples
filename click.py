import pyautogui
import time

x = [0, 600, 700]
y = [250, 250, 250]  # or whatever

for cx, xy in zip(x, y):
    pyautogui.click(cx, xy)
    print('click')
    time.sleep(5)
