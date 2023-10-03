from tkinter import *
from themes import *
from settings import *


def home(window):
    
    def openSettings():
        settings()

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


    Button(
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
    ).place(x=300, y=46)
    Button(
        window,
        text="Sts",
        command=openSettings,
        bg=theme.secondaryColor(),
        width=5,
        fg=theme.textColor(),
        font=("Inter", 15),
        activebackground=theme.primaryColor(),
        activeforeground=theme.textColor(),
        borderwidth=1,
        highlightthickness=1,
        highlightbackground=theme.textColor()  # Specify the outline color here
    ).place(x=480, y=46)




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
            buttons[i].place(x=starting_x, y=starting_y + spacing * i)

    place_buttons(60)
