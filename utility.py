import home as home
import settings as settings
import keyResponse as kResponse
import dynamicVolume as dVolume



def global_settings_init():
    dVolume.settingsInit()
    kResponse.settingsInit()
    #settings.settingsInit()
    home.settingsInit()

def partial_settings_init(module):
    if type(module) == str:
        if module == 'home':
            home.settingsInit()
        elif module == 'settings':
            settings.settingsInit()
        elif module == 'keyResponse':
            kResponse.settingsInit()
        elif module == 'dynamicVolume':
            dVolume.settingsInit()
        else:
            print(f"Error: {module} is not a valid module")
    elif type(module) == list:
        for i in module:
            partial_settings_init(i)

