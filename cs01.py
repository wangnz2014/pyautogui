import pyautogui
import time
# 系统准备时间
time.sleep(2)
# 取得帮助菜单位置
help_pos = pyautogui.locateOnScreen('btn_help.png')
goto_pos = pyautogui.center(help_pos)
# 移动鼠标
pyautogui.moveTo(goto_pos, duration=1)
# 点击
pyautogui.click()
# 再移动鼠标
pyautogui.moveRel(None, 650, duration=1)
# 再点击
pyautogui.click()