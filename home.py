import tkinter as tk
from themes import *
from settings import *
from PIL import ImageTk, Image
import sys
import os


def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2 #if MEIPASS2 doesnt work, switch to MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def home(window):
    
    def openSettings():
        settings()
    
    settingsImg = ImageTk.PhotoImage(Image.open(resource_path("settings.png")))

    def doSth(self):
        print("Hello")
    def doSth1(self):
        print("Hello1")
    def doSth2(self):
        print("Hello2")


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

    Canvas(window, width=280, height=360 ,bg=theme.secondaryColor(), highlightthickness=0).place(x= 290, y= 0)


    Label(
        window,
        text="Themes",
        bg=theme.secondaryColor(),
        width=15,
        height=2,
        fg=theme.textColor(),
        font=("Inter", 15),
        activebackground=theme.primaryColor(),
        activeforeground=theme.textColor(),
        borderwidth=1,
        highlightthickness=1,
        highlightbackground=theme.textColor()  # Specify the outline color here
    ).place(x=300, y=36)
    Label(
        window,
        text="Sts",
        bg=theme.secondaryColor(),
        width=5,
        height=2,
        fg=theme.textColor(),
        font=("Inter", 15),
        activebackground=theme.primaryColor(),
        activeforeground=theme.textColor(),
        borderwidth=1,
        highlightthickness=1,
        highlightbackground=theme.textColor()  # Specify the outline color here
    ).place(x=476, y=36)


    # button styling
    button_width = 21
    button_height = 2
    button_spacing = 70
    font_size = 15
    type_face = "Inter"
    border_width = 1
    highlight_thickness = 1
    
    Sound_1 = Label(
        window,
        text="Thock",
        bg=theme.secondaryColor(),
        width=button_width,
        height=button_height,
        fg=theme.textColor(),
        font=(type_face, font_size),
        activebackground=theme.primaryColor(),
        activeforeground=theme.textColor(),
        borderwidth=border_width,
        highlightthickness=highlight_thickness,
        highlightbackground=theme.textColor()  
    )

    Sound_2 = Label(
        window,
        text="Raining glass marble",
        bg=theme.secondaryColor(),
        width=button_width,
        height=button_height,
        fg=theme.textColor(),
        font=(type_face, font_size),
        activebackground=theme.primaryColor(),
        activeforeground=theme.textColor(),
        borderwidth=border_width,
        highlightthickness=highlight_thickness,
        highlightbackground=theme.textColor()  
    )
    Sound_3 = Label(
        window,
        text="Raining glass marble",
        bg=theme.secondaryColor(),
        width=button_width,
        height=button_height,
        fg=theme.textColor(),
        font=(type_face, font_size),
        activebackground=theme.primaryColor(),
        activeforeground=theme.textColor(),
        borderwidth=border_width,
        highlightthickness=highlight_thickness,
        highlightbackground=theme.textColor()  
    )
    


    buttons = [Sound_1, Sound_2, Sound_3]
    def place_buttons(spacing, starting_x=300, starting_y=106):
        for i in range(len(buttons)):
            buttons[i].place(x=starting_x, y=starting_y + spacing * i)

        #! Remember to manually bind funtionality here
        buttons[0].bind("<Button-1>", doSth)
        buttons[1].bind("<Button-1>", doSth1)
        buttons[2].bind("<Button-1>", doSth2)

    place_buttons(button_spacing)
