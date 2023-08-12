from pyautogui import *
import pyautogui
import time
import keyboard
import numpy as np
import random
import win32api, win32con
from PIL import ImageGrab
import tkinter as tk
from tkinter import filedialog, Text
import os
import sys
import threading

#Variables
running = False
#Functions
def start():
    print("Turning on the bot, you have 5 sec to Alt-Tab")
    time.sleep(5)
    global running
    running = True
    click(1782, 979)
    print("[+]Game started")
    time.sleep(np.random.uniform(4.1,6))
    while running or keyboard.is_pressed('q') == False: #Main play loop
        checkIfBattleWon()
        if pyautogui.pixel(436, 75)[2] == 255:
            checkHero(436,75)
        checkIfBattleWon()
        if pyautogui.pixel(559, 78)[2] == 255:
            checkHero(559,78)
        checkIfBattleWon()
        if pyautogui.pixel(678, 76)[2] == 255:
            checkHero(678,76)
        checkIfBattleWon()
        if pyautogui.pixel(438, 220)[2] == 255:
            checkHero(438,220)
        checkIfBattleWon()
        if pyautogui.pixel(557, 221)[2] == 255:
            checkHero(557,221)
        checkIfBattleWon()
        if pyautogui.pixel(676, 221)[2] == 255:
            checkHero(676,221)
        checkIfBattleWon()
        if pyautogui.pixel(439, 363)[2] == 255:
            checkHero(439,363)
        checkIfBattleWon()
        if pyautogui.pixel(553, 363)[2] == 255:
            checkHero(553,363)
        checkIfBattleWon()
        if pyautogui.pixel(675, 363)[2] == 255:
            checkHero(675,363)
        checkIfBattleWon()
        if pyautogui.pixel(680, 497)[2] == 255:
            checkHero(680,497)
        checkIfBattleWon()
        if pyautogui.pixel(201, 721)[2] == 255:
            archerCheck(201,721)
        checkIfBattleWon()
        if pyautogui.pixel(204, 547)[2] == 255:
            archerCheck(204,547)
        checkIfBattleWon()
        if pyautogui.pixel(1020,28)[0] == 0:
            smithCheck(442, 555)
        checkIfBattleWon()

def stop():
    global running
    print("Manual Stop")
    running = False

def click(x,y):
    win32api.SetCursorPos((int(np.random.uniform(x - 2, x + 2)),int(np.random.uniform(y - 2, y + 2))))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(np.random.uniform(0.08,0.17))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def checkHero(x, y):
    print("[+]Activating hero")
    win32api.SetCursorPos((int(np.random.uniform(x - 2, x + 2)),int(np.random.uniform(y, y + 30))))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(np.random.uniform(0.08,0.17))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    if pyautogui.pixel(244,334) [1] == 116 and pyautogui.pixel(244,334) [2] == 121:
        checkIfAdditionalClickNeeded(np.random.uniform(1705,1711),np.random.uniform(718,722))
        
def smithCheck (smithX,smithY):
    print("[+]Using smith")
    win32api.SetCursorPos((int(np.random.uniform(smithX - 2, smithX + 2)),int(np.random.uniform(smithY, smithY + 30))))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(np.random.uniform(0.08,0.17))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def archerCheck (x,y):
    print("[+]Activating archers")
    win32api.SetCursorPos((int(np.random.uniform(x - 2, x + 2)),y + int(np.random.uniform(60,110))))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(np.random.uniform(0.08,0.17))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def checkIfAdditionalClickNeeded(clickX, clickY):
    print("[+]Activating additional click")
    win32api.SetCursorPos((int(np.random.uniform(clickX - 10, clickX + 10)),int(np.random.uniform(clickY - 10, clickY + 10))))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(np.random.uniform(0.08,0.17))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def quickRandomPause():
    time.sleep(np.random.uniform(0.08,0.17))

def checkIfBattleWon ():
    autoChestCollectable()
    if pyautogui.pixel(378, 166)[0] == 45 and pyautogui.pixel(378, 166)[1] == 39 and pyautogui.pixel(378, 166)[2] == 33 or pyautogui.pixel(378, 166)[0] == 16 and pyautogui.pixel(378, 166)[1] == 14 and pyautogui.pixel(378, 166)[2] == 12:
        print("[+] Battle has ended")
        time.sleep(4)
        autoCastle()
        time.sleep(1)
        autoArchers()
        print("Now wait for around 10 seconds for bot to turn the battle again")
        time.sleep(np.random.uniform(9,13))
        print("[+]Starting the game again")
        click(1768, 921)
        time.sleep(np.random.uniform(4.1,6))

def autoCastle ():
    global autoCastleStatus
    if autoCastleStatus % 2 == 1:
        if pyautogui.locateOnScreen("./images/upgradeCastle.png", confidence=0.98) != None:
            castlex, castley = pyautogui.locateCenterOnScreen("./images/upgradeCastle.png", confidence=0.98)
            print("Castle upgrade located. X = ", castlex, " Y = ", castley)
            while(pyautogui.locateOnScreen("./images/noGold.png", confidence=0.98) == None):
                win32api.SetCursorPos((int(np.random.uniform(castlex - 5, castlex + 5)),int(np.random.uniform(castley - 2, castley + 2))))
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
                time.sleep(np.random.uniform(0.08,0.17))
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
            print("[+]No more gold - stopping the auto upgrade")

def autoArchers ():
    global autoArchersStatus
    if autoArchersStatus % 2 == 1:
        if pyautogui.locateOnScreen("./images/upgradeArchers.png", confidence=0.98) != None:
            archersx, archersy = pyautogui.locateCenterOnScreen("./images/upgradeArchers.png", confidence=0.98)
            print("Archers upgrade located. X = ", archersx, " Y = ", archersy)
            while(pyautogui.locateOnScreen("./images/noGold.png", confidence=0.98) == None):
                win32api.SetCursorPos((int(np.random.uniform(archersx - 5, archersx + 5)),int(np.random.uniform(archersy - 2, archersy + 2))))
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
                time.sleep(np.random.uniform(0.08,0.17))
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
            print("[+]No more gold - stopping the auto upgrade")

def autoChestCollectable():
    global autoChestStatus
    if autoChestStatus % 2 == 1:
        chest_image_path = "./images/chest.png"
        chest_region = (920, 780, 1000, 300)
        confidence_threshold = 0.75

        chest_location = pyautogui.locateCenterOnScreen(chest_image_path, confidence=confidence_threshold, grayscale=True, region=chest_region)
        
        if chest_location is not None:
            chestx, chesty = chest_location
            print(f"Chest collectable located. X = {chestx}, Y = {chesty}")
            
            click_offset_x = np.random.uniform(-2, 2)
            click_offset_y = np.random.uniform(-2, 2)
            win32api.SetCursorPos((int(chestx + click_offset_x), int(chesty + click_offset_y)))
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
            time.sleep(np.random.uniform(0.08, 0.17))
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
            
            print("[+] Chest collected")

def start_bot_thread():
    bot_thread = threading.Thread(target=start)
    bot_thread.start()

autoCastleStatus = 0
def autoCastle_thread():
    global autoCastleStatus
    global autoArchersStatus
    autoCastleStatus += 1
    autoArchersStatus = 0
    print("[+]Auto Castle upgrade toggled, status: ", True)
    print("[+]Auto Archers upgrade toggled, status: ", False)

autoArchersStatus = 0
def autoArchers_thread():
    global autoArchersStatus
    global autoCastleStatus
    autoCastleStatus = 0
    autoArchersStatus += 1
    print("[+]Auto Archers upgrade toggled, status: ", True)
    print("[+]Auto Castle upgrade toggled, status: ", False)

autoChestStatus = 0
def autoChest_thread():
    global autoChestStatus
    autoChestStatus +=1
    print("[+]Auto Chest collect upgrade toggled, status: ", autoChestStatus % 2)


# Application
root = tk.Tk()
root.title("Grow Castle Auto-Bot by Alex-G-R")
icon_path = "./Icon/icon.ico"
root.iconbitmap(icon_path)

# Declare canvas
canvas = tk.Canvas(root, height=500, width=800, bg="#8478F2")
canvas.pack()

# Start the bot button
startBot = tk.Button(root, text="Start the Bot",command=start_bot_thread, padx=10, pady = 5, fg="black", bg="white", height=2, width=50)
canvas.create_window(195, 33, window=startBot)

# Stop the bot button
stopBot = tk.Button(root, text="Stop the Bot (hold Q to stop)",command=stop, padx=10, pady = 5, fg="black", bg="white", height=2, width=50)
canvas.create_window(195, 468, window=stopBot)

# Button Auto Castle upgrade toggle
autoUpgradeCastle = tk.Button(root, text="Auto Castle upgrade", command=autoCastle_thread, fg="black", bg="white", height=2, width=25)
canvas.create_window(100, 415, window=autoUpgradeCastle)

# Button Auto Archers upgrade toggle
autoUpgradeArchers = tk.Button(root, text="Auto Archers upgrade", command=autoArchers_thread, fg="black", bg="white", height=2, width=25)
canvas.create_window(290, 415, window=autoUpgradeArchers)

# Button Auto Chest auto collect toggle
autoChest = tk.Button(root, text="Auto Chest collect", command=autoChest_thread, fg="black", bg="white", height=2, width=52)
canvas.create_window(195, 367, window=autoChest)

# Console window, every print command will appear here as text
output_text = tk.Text(root, height=30, width=50)
canvas.create_window(590, 250, window=output_text)

#Redirect output to the text widet
def redirect_stdout(target_widget):
    class StdoutRedirector:
        def __init__(self, text_widget):
            self.text_widget = text_widget

        def write(self, message):
            self.text_widget.config(state=tk.NORMAL)  # Enable writing
            self.text_widget.insert("end", message)
            self.text_widget.see("end")  # Scroll to the end
            self.text_widget.config(state=tk.DISABLED)  # Disable writing

        def flush(self):
            pass

    sys.stdout = StdoutRedirector(target_widget)

    sys.stdout = StdoutRedirector(target_widget)

redirect_stdout(output_text)
root.mainloop()