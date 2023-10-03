from tkinter import *
from themes import *


def settings():
    #?word per minute display
    window = Tk()
    window.title("Mechanical Keys Simulator")
    window.geometry("566x339")
    window.configure(bg=theme.primaryColor())

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

    #Canvas(width=260, height=275 ,bg=theme.secondaryColor(), highlightthickness=0).place(x= 290, y= 36)


    randomSound = Button(
        window,
        text="Settings",
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


    window.mainloop()



