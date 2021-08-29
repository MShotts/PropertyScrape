# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 08:26:21 2021

@author: DrShotts
"""

import pyautogui, time, os, shutil, sys

#The following function will be used for all screenshots (other than the Firefox screen)
def clickimage(imagename):
#The search for the provided image continues until found
    Attempt = 1
    while True:
        pos = pyautogui.locateCenterOnScreen("C:/Users/DrShotts/Desktop/Python_WebScraping/Pyautogui_Data Universe/%s.PNG" % imagename, confidence=0.95)
#This adds a note to the console as to what image is being searched for and how many attempts have been made
        print("Current search image:", imagename, ", Attempt:",Attempt)
        print(pos)
        Attempt = Attempt + 1
        if pos is not None:
            break
    pyautogui.click(pos, duration=0.1)
    print("Success!")

clickimage("Mozilla")

time.sleep(1)


Page=1
#while Page < 5:
while Page < 22219:

    #This is where the looped operation should begin
    #This clicks at the start location of the list
    pyautogui.click(x=38, y=276)

    time.sleep(1)

    pyautogui.keyDown('shift')

    time.sleep(1)

    clickimage("EndList")

    time.sleep(1)

    pyautogui.keyUp('shift')

    time.sleep(1)

    pyautogui.hotkey('ctrl', 'c')

    time.sleep(1)

    clickimage("Notepad")

    time.sleep(1)

    pyautogui.hotkey('ctrl', 'v')

    time.sleep(1)

    pyautogui.press('enter')

    time.sleep(1)

    pyautogui.hotkey('ctrl', 's')

    time.sleep(2)

    clickimage("Mozilla")

    time.sleep(1)
    Page = Page + 1
    clickimage("NextPage")


