import pyautogui
import time

pyautogui.PAUSE = 0.3

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

time.sleep(3)
pyautogui.click(x=758, y=619)

time.sleep(1)

pyautogui.write("hashtagtreinamentos.com")
pyautogui.press("enter")