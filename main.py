
# ttkthemes
import pygame
import tkinter as tk
from linkedlist import *
import themes
import home
import utility as util
import settings as settings
import keyResponse as kResponse
import dynamicVolume as dVolume
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
window = tk.Tk()
window.title("Mechanical Keys Simulator")
window.geometry("566x339")
window.configure(bg=themes.theme.primaryColor())

#window.iconbitmap(resource_path("Logo.ico"))
window.resizable(False, False)


util.global_settings_init()

home.home(window)
kResponse.run()

window.mainloop()


