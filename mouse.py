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
    dispatcher = {
        'Enter text instantly.': image_click_enter, 'Image autoclicker.': image_click_amount
    }
    dispatcher[pyautogui.confirm(text="Please choose what you want to do:", buttons=['Enter text instantly.', 'Image autoclicker.'])]()

def image_click_enter(retry_counter = 0):
    while True:
        put=pyautogui.prompt(text='Please input your exact image location.',
        title='Enter text instantly.', default='Example:/home/jack/Documents/screenshot.png')
        if put is None:
            os._exit(0)
        tup = pyautogui.prompt(text='Please enter what you want to say. (Notice; After entering the text this prompt will close, however the program will still run.)',
        title='Enter text instantly.', default='Hi mom!')
        if tup is None:
            continue
        else:
            break
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
    enter = pyautogui.prompt(text="Please input the image of what you want your mouse to auto-click.",
     title='Image autoclicker', default='Example:/home/jack/Documents/screenshot.png')
    if enter is None:
        os._exit(0)
    pyautogui.alert(text='After clicking "OK" the autoclicker will begin, to stop it please click "ctrl+alt" at the same time.',
     title='Image autoclicker', button='OK')
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
    ylist = ('Yes')
    nlist = ('No')
    chooseplz = pyautogui.confirm(text="Would you like to use this program?", buttons=[ylist, nlist])
    if chooseplz in ylist:
        return library()
    else:
        pyautogui.alert(text="Ok bye", button='byebye')
        os._exit(0)

select_menu()