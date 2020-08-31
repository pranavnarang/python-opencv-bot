import cv2
import time
import random
import keyboard
import numpy
from PIL import ImageGrab
from pynput.mouse import Button, Controller

mouse = Controller()


#Load template
tree1 = cv2.imread("tree1.png", 0)
tree2 = cv2.imread('tree2.png', 0)
tree3 = cv2.imread('tree3.png', 0)
tree4 = cv2.imread("tree4.png", 0)
tree5 = cv2.imread('tree5.png', 0)
tree6 = cv2.imread('tree6.png', 0)
tree7 = cv2.imread('tree7.png', 0)
tree8 = cv2.imread('tree8.png', 0)
tree9 = cv2.imread('tree9.png', 0)
tree10 = cv2.imread('tree10.png', 0)

template = [tree1, tree2, tree3, tree4, tree5, tree6, tree7, tree8, tree9, tree10]

# w, h = template.shape[::-1]

#screenshot values
topLeftX = 750
topLeftY = 60
bottomRightX = 1619
bottomRightY = 495

def take_screenshot():
    image = ImageGrab.grab(bbox=(topLeftX*2, topLeftY*2, bottomRightX*2, bottomRightY*2))
    return cv2.cvtColor(numpy.array(image), cv2.COLOR_RGB2GRAY)

def look_for_templates(opencvImage, templates):
    length = -1
    loc = 1
    threshold = 0.55
    for template in templates:
        res = cv2.matchTemplate(opencvImage, template, cv2.TM_CCOEFF_NORMED)
        tmp = numpy.where(res >= threshold)
        if len(tmp[0]) > length:
            loc = tmp
            length = len(tmp[0])
    
    return loc

def look_for_template(opencvImage, template):
    threshold = 0.8
    res = cv2.matchTemplate(opencvImage, template, cv2.TM_CCOEFF_NORMED)
    return numpy.where(res >= threshold)


def rotate_screen():
    keyboard.press('right arrow')
    time.sleep(random.uniform(1,2))
    keyboard.release('right arrow')


def click():
    time.sleep(random.uniform(0.003,0.0098))
    mouse.press(Button.left)
    time.sleep(random.uniform(0.001,0.0002))
    mouse.release(Button.left)

def move_pointer(xLoc, yLoc, randomLow, randomHigh):
    return (topLeftX + xLoc + random.uniform(randomLow, randomHigh), topLeftY + yLoc)

#TODO:
#1. set treeCount to 0 and increment after mouse.press
#2. when treeCount == 28
#3.     clearInventory
#4.     make clearInventory function -> click inventory, (for i=0...27 ), hold shift, click on log, end for, close inventory

def clear_inventory():
    inventory = cv2.imread('logInventory.png', 0)
    #Open inventory
    mouse.position = move_pointer(755, 455, 3, 5)
    click()
    #Take screenshot 
    opencvImage = take_screenshot()
    
    loc = look_for_template(opencvImage, inventory)
    while len(loc[0])>0:
        loc = look_for_template(opencvImage, inventory)
        if len(loc[0]) != 0:
            mouse.position = move_pointer(loc[1][0]/2, loc[0][0]/2, 1, 10)
            keyboard.press('shift')
            click()
            opencvImage = take_screenshot()

    

print('running script')
treeCount = 0
while keyboard.is_pressed('q') == False:
    #Take screenshot 
    opencvImage = take_screenshot()

    #Look for template
    loc = look_for_templates(opencvImage, template)
    print(len(loc[0]))

    while len(loc[0])==0:
        rotate_screen()
        opencvImage = take_screenshot()
        loc = look_for_templates(opencvImage, template)

    #Go to template location and cut
    print('the tree is at:', loc[1][0], loc[0][0])
    mouse.position = move_pointer(loc[1][0]/2, loc[0][0]/2, 30, 50)
    click()
    treeCount = treeCount + 1
    time.sleep(random.uniform(7,10))
    if treeCount == 28:
        clear_inventory()
        treeCount = 0


cv2.waitKey(0)
cv2.destroyAllWindows()

    #Draw rectangles
    # for pt in zip(*loc[::-1]):
        # print(pt)
        # cv2.rectangle(opencvImage, pt, (pt[0] + w, pt[1]+h), (0,0,255), 2)
        # mouse.position = (750 + (pt[0]/2) + 30, 60 + (pt[1]/2) + 30)