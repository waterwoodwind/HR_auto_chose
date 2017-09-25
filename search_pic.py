#coding=utf-8
import pyautogui
import time

time.sleep(5)
number_locate = pyautogui.locateCenterOnScreen('query_green.png')
print number_locate
print type(number_locate)
pyautogui.moveTo(number_locate)
pyautogui.click()