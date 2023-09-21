from winreg import ConnectRegistry, OpenKey, QueryValueEx, HKEY_CURRENT_USER
import sys


themes = {
    "light": "#FFFFFF",
    "lightSecondary": "#F0F0F0",
    "lightText": "#1E1E1E",
    
    "dark": "#1E1E1E",
    "darkSecondary": "#545454",
    "darkText": "#F0F0F0"
}
    
class theme:

    def get_sys_theme():
        default = True
        try:
            aReg = OpenKey(ConnectRegistry(None,HKEY_CURRENT_USER), r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize")
            value, _=QueryValueEx(aReg, "AppsUseLightTheme")
            return value == 1
            #return defualt
        except:
            print(f"Error: {sys.exc_info()[0]}")
            return default
    
    def primaryColor():
        global themes
        if theme.get_sys_theme():
            return themes["light"]
        else:
            return themes["dark"]
        
    def secondaryColor():
        global themes
        if theme.get_sys_theme():
            return themes["lightSecondary"]
        else:
            return themes["darkSecondary"]
    
    def textColor():
        global themes
        if theme.get_sys_theme():
            return themes["lightText"]
        else:
            return themes["darkText"]
