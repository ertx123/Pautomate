import pyautogui
import time
import cv2

print('Please input your exactly image location after this prompt.')
put = input()

print('Now please enter what you wanna say:')
tup = input()

def image_get(retry_counter = 0):
    while retry_counter < 5:
        try:
            ilocation = (pyautogui.locateOnScreen(put, confidence=0.8))
            print("Success!")
            pyautogui.click(ilocation, button='left')
            if ilocation:
                pyautogui.write(tup)
                pyautogui.press('enter')
            if ilocation:
                time.sleep(1)
                retry_counter = 10
        except pyautogui.ImageNotFoundException:
            time.sleep(1)
            retry_counter += 1
            print('Unsuccessful.')

image_get()