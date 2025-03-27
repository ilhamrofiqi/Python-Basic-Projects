# ScreenShot Automation

import time
import pyautogui

def screenshot():
    name = int(round(time.time() * 1000))
    name = 'F:/Data Analyst/Python Basic Project/screenshots data/{}.png'.format(name)
    time.sleep(5)
    img = pyautogui.screenshot(name)
    img.show()


screenshot()