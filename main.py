
# ttkthemes
import pygame
import tkinter as tk
from tkinter import Label
from tkinter import Button
from tkinter import Canvas
from tkinter import Frame
from linkedlist import *
from themes import *
import keyResponse
import sys
import os
pygame.init()


#?credit for resource_path method: https://stackoverflow.com/questions/31836104/pyinstaller-and-onefile-how-to-include-an-image-in-the-exe-file
#remember to use when GUI is included
def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2 #if MEIPASS2 doesnt work, switch to MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

Logo = resource_path("Logo.png")

currentTracks = 3



    
#!color scheme





window = tk.Tk()
window.title("Mechanical Keys Simulator")
window.geometry("566x339")
window.configure(bg=theme.primaryColor())

#window.iconbitmap(resource_path("Logo.ico"))
window.resizable(False, False)

#?word per minute display
Label(
    window, 
    text="23", 
    bg= theme.primaryColor(), 
    fg=theme.textColor(), 
    font=("Inter", 80, 'bold')
    ).place(x =29, y = 53)
Label(
    window, 
    text="Avg", 
    bg= theme.primaryColor(), 
    fg=theme.textColor(), 
    font=("Inter", 20)
    ).place(x =155, y = 90)
Label(
    window, 
    text="WPM", 
    bg= theme.primaryColor(), 
    fg=theme.textColor(), 
    font=("Inter", 20)
    ).place(x =155, y = 127)

#?fastest word per minute display   
Label(
    window, 
    text="96", 
    bg= theme.primaryColor(), 
    fg=theme.textColor(), 
    font=("Inter", 80, 'bold')
    ).place(x =29, y = 180)
Label(
    window, 
    text="Fastest", 
    bg= theme.primaryColor(), 
    fg=theme.textColor(), 
    font=("Inter", 20)
    ).place(x =155, y = 217)
Label(
    window, 
    text="WPM", 
    bg= theme.primaryColor(), 
    fg=theme.textColor(), 
    font=("Inter", 20)
    ).place(x =155, y = 254)

#? Change keyboard sound menu

Canvas(width=260, height=275 ,bg=theme.secondaryColor(), highlightthickness=0).place(x= 290, y= 36)

borderColor = Frame(window, background=theme.textColor())

randomSound = Button(
    window,
    text="Random",
    bg=theme.secondaryColor(),
    width=15,
    fg=theme.textColor(),
    font=("Inter", 15),
    activebackground=theme.primaryColor(),
    activeforeground=theme.textColor(),
    borderwidth=1,
    highlightthickness=1,
    highlightbackground=theme.textColor()  # Specify the outline color here
)
randomSound.place(x=300, y=46)

settings = Button(
    window,
    text="Sts",
    bg=theme.secondaryColor(),
    width=5,
    fg=theme.textColor(),
    font=("Inter", 15),
    activebackground=theme.primaryColor(),
    activeforeground=theme.textColor(),
    borderwidth=1,
    highlightthickness=1,
    highlightbackground=theme.textColor()  # Specify the outline color here
)
settings.place(x=480, y=46)

Sound_1 = Button(
    window,
    text="1980's type Writer",
    bg=theme.secondaryColor(),
    width=21,
    fg=theme.textColor(),
    font=("Inter", 15),
    activebackground=theme.primaryColor(),
    activeforeground=theme.textColor(),
    borderwidth=1,
    highlightthickness=1,
    highlightbackground=theme.textColor()  # Specify the outline color here
)

Sound_2 = Button(
    window,
    text="Modern Keyboard",
    bg=theme.secondaryColor(),
    width=21,
    fg=theme.textColor(),
    font=("Inter", 15),
    activebackground=theme.primaryColor(),
    activeforeground=theme.textColor(),
    borderwidth=1,
    highlightthickness=1,
    highlightbackground=theme.textColor()  # Specify the outline color here
)

Sound_3 = Button(
    window,
    text="Mechanical Keyboard",
    bg=theme.secondaryColor(),
    width=21,
    fg=theme.textColor(),
    font=("Inter", 15),
    activebackground=theme.primaryColor(),
    activeforeground=theme.textColor(),
    borderwidth=1,
    highlightthickness=0,
    highlightbackground=theme.textColor()  # Specify the outline color here
)

buttons = [Sound_1, Sound_2, Sound_3]
def place_buttons(spacing, starting_x=300, starting_y=106):
    for i in range(len(buttons)):
        buttons[i].place(x=300, y=106 + spacing * i)

place_buttons(60)





keyResponse.run()

window.mainloop()


