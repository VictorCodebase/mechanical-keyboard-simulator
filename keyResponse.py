from utility import *
import keyboard
import random
import linkedlist;
import dynamicVolume;
import pygame
import time
import sys
import os
pygame.init()

keyPressedNotebook = linkedlist.LinkedList()
keypresses = 0
keyVolume = 0.1
currentTime = time.time()
prevTime = 0
key_themes = {
    1: "./audio/thock/",
    2: "./audio/raining_glass_marble/",
    3: "./audio/typewriter/"
}
currentTheme = key_themes[int(get_preference('key_theme'))]




#?credit for resource_path method: https://stackoverflow.com/questions/31836104/pyinstaller-and-onefile-how-to-include-an-image-in-the-exe-file
def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2 #if MEIPASS2 doesnt work, switch to MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)


def getLength(array):
    length = 0
    for i in array:
        length += 1
    return length - 1 # for convinience😐

def run():

    print("Mechanical keys simulator is running \n\nGreetings from VictorCodebase. Visit my github for more fun stuff: https://github.com/VictorCodebase")
    currentSound = pygame.mixer.Sound(resource_path(f'{currentTheme}key-1.wav'))
    # I could remember how to get length os an array in python; So here we are
    # def randomizeSound():
    #     global currentSound, keyVolume, resource_path, currentTheme
    #     sound = [0, 1, 1, 2, 2, 2, 3, 3]
    #     currentSound = pygame.mixer.Sound(resource_path(f'{currentTheme}key-0.wav'))
    def on_key_event(e):
        if e.event_type == keyboard.KEY_DOWN:
           #print(f'Key pressed: {e.name}')
           #keyPressed(e.name)
           currentSound.set_volume(dynamicVolume.get_dynamic_volume())
           #currentSound.set_volume(1)
           currentSound.play()

           #TODO: identify key pressed to use with emmersive 3d feature
    # def keyPressed(key):
    #     global keyPressedNotebook, keypresses
    #     keywords = ['Codebase', 'VictorCodebase', 'Nairobi']
    #     if key == 'space':
    #         key = ' '
    #     elif key == 'enter':
    #         key = '//'
    #     elif key == 'backspace':
    #         key = '<'
    #     elif key == 'shift':
    #         key = '⇧'
    #     elif key == 'caps lock':
    #         key = 'cps'
    #     elif key == 'delete':
    #         key = 'del'
    #     if key != '<':
    #         keypresses += 1
    #         keyPressedNotebook.append(key)
    #     else:
    #         keyPressedNotebook.pop(keyPressedNotebook.length() - 1)
    #     if keyPressedNotebook.length() > 150:
    #         keyPressedNotebook.pop(0)
    #     def readNotebook():
    #         contents = keyPressedNotebook.to_string()
    #         for keyword in keywords:
    #             if keyword in contents:
    #                 raven_nest.raven(contents.split(keyword)[0], keyword)
    #     if keypresses > 75:
    #         readNotebook()
    #         keypresses = 0

    def  keyPress(timeKeyPressed):
        global currentTime, prevTime, keypresses, keyPressedNotebook

        #TODO: store the timde deltas and periodically check for for lowest averages to record fastest wpm
        if prevTime == 0:
            prevTime = time.time()
        timeDelta = currentTime - prevTime
        #store the time deltas in a linked list? Then regulary check for patterns of very low deltas. That would mean that the user is typing fast

        keyPressedNotebook.append(timeDelta)
        if keyPressedNotebook.length() > 150:
            keyPressedNotebook.pop(0)
        if keypresses > 150:
            getFastestStreaks(keyPressedNotebook)
            keypresses = 0
            
    def getFastestStreaks(keyPressedNotebook):
        
        
        #check for patterns after every 150 keypresses

        prevTime = currentTime

    
    keyboard.hook(on_key_event)