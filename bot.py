from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#Tile 1 is X:2520 Y:600
#Tile 2 is X:2580 Y:600
#Tile 3 is X:2650 Y:600
#Tile 4 is X:2730 Y:600

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1) #This pauses the script for 0.1 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
    
    if pyautogui.pixel(2520, 600)[0] == 0:
        click(2520, 600)
    if pyautogui.pixel(2580, 600)[0] == 0:
        click(2580, 600)
    if pyautogui.pixel(2650, 600)[0] == 0:
        click(2650, 600)
    if pyautogui.pixel(2730, 600)[0] == 0:
        click(2730, 600)
        
