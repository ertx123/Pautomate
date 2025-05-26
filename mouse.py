import pyautogui
import time
import cv2
from pynput import keyboard
import os
import threading

def on_activate():
    print('Exiting.')
    raise os._exit(0)

def for_canonical(f):
    return lambda k: f(listener.canonical(k))

hotkey = keyboard.HotKey(
        keyboard.HotKey.parse('<ctrl>+<alt>'),
        on_activate)

def start_hotkey_listener():
    with keyboard.Listener(
        on_press=for_canonical(hotkey.press),
        on_release=for_canonical(hotkey.release)) as l:
        global listener
        listener = l
        l.join()

listener_thread = threading.Thread(target=start_hotkey_listener, daemon=True)
listener_thread.start()

def library():
    thelist = str(("Enter text instantly.", "Image autoclicker"))
    print("Please choose what you want to do:" + thelist)
    dispatcher = {
        'Enter text instantly': image_click_enter, 'Image autoclicker': image_click_amount
    }
    action = input('Choose: ')
    dispatcher[action]()

def image_click_enter(retry_counter = 0):
    print('Please input your exactly image location after this prompt.')
    put=input()
    print('Now please enter what you want to say.')
    tup = input()
    while retry_counter < 5:
        try:
            alocation = (pyautogui.locateOnScreen(put, confidence=0.8))
            print("Success!")
            pyautogui.click(alocation, button='left')
            if alocation:
                pyautogui.write(tup)
                pyautogui.press('enter')
            if alocation:
                time.sleep(1)
                retry_counter = 10
        except pyautogui.ImageNotFoundException:
            time.sleep(1)
            retry_counter += 1
            print('Unsuccessful trying again.')

def image_click_amount(retry_counter2 = 0):
    print("Please input the image of what you want your mouse to auto-click.")
    enter = input()
    while retry_counter2 < 5:
        try:
            blocation = (pyautogui.locateOnScreen(enter, confidence=0.8))
            print("Success!")
            print("To stop this process, please enter ctrl+alt.")
            while True:
                pyautogui.click(blocation, button='left')
            if blocation:
                time.sleep(1)
                retry_counter2 = 10
        except pyautogui.ImageNotFoundException:
            time.sleep(1)
            retry_counter2 += 1
            print('Unsuccessful trying again.')

def select_menu():
    chooseplz = str(input("Would you like to use this program? (Y/N) "))
    ylist = ("Y", "y","yes", "Yes")
    if chooseplz in ylist:
        return library()
    else:
        print("Ok bye")
        os._exit(0)

select_menu()