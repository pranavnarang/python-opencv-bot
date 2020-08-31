from pynput.mouse import Button, Controller
import time
import random

mouse = Controller()

#1560, 300
#1065, 320

def move_pointer(xLoc, yLoc, randomLow, randomHigh):
    mouse.position = (xLoc + random.uniform(randomLow, randomHigh), yLoc + random.uniform(randomLow, randomHigh))

def click():
    time.sleep(random.uniform(0.3,0.8))
    mouse.press(Button.left)
    mouse.release(Button.left)

def click_splash():
    move_pointer(1560, 300, -3, 3)
    click()

def click_man():
    move_pointer(1065, 320, -5, 5)
    click()
    time.sleep(random.uniform(1.9, 2.4))

for i in range(20):
    click_splash()
    click_man()

move_pointer(1620, 70, 0, 0) 
move_pointer(1530, 490, 0, 0)