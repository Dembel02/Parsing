import pyautogui

pyautogui.PAUSE = 2
pyautogui.sleep(3)

# pyautogui.moveTo(1100, 600, duration = 2)
# pyautogui.moveTo(300, -200, duration = 2)

pyautogui.click(x=100, y=200, clicks=500, interval=0.1)
pyautogui.doubleClick()
pyautogui.tripleClick()

pyautogui.leftClick()
pyautogui.rightClick()
pyautogui.middleClick()

print(pyautogui.position())
