from tkinter import *
from themes import *


def settings():
    #?word per minute display
    window = Tk()
    window.title("Mechanical Keys Simulator - Settings")
    window.geometry("566x339")
    window.configure(bg=theme.primaryColor())

    #?fastest word per minute display   

    Label(
        window, 
        text="Coming soon in mid October update alongside other mind blowing features✨", 
        bg= theme.primaryColor(), 
        fg=theme.textColor(), 
        font=("Inter", 10)
        ).place(x =15, y = 100)
    Label(
        window, 
        text="See you then!!", 
        bg= theme.primaryColor(), 
        fg=theme.textColor(), 
        font=("Inter", 10)
        ).place(x =15, y = 120)

    #? Change keyboard sound menu

    #Canvas(width=260, height=275 ,bg=theme.secondaryColor(), highlightthickness=0).place(x= 290, y= 36)

    #TODO: minimize to tray, change volume, theme, disengage dynamic and emersive features, vary emersive features intensity



    window.mainloop()



