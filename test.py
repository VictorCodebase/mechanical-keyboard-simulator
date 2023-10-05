# from ctypes import cast, POINTER
# from comtypes import CLSCTX_ALL
# from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# def get_sound_volume():
#   # Get the speakers device
#   devices = AudioUtilities.GetSpeakers()
#   # Activate the device interface
#   interface = devices.Activate(
#       IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
#   # Get the volume object
#   volume = cast(interface, POINTER(IAudioEndpointVolume))
#   # Get the master volume level as a scalar (0.0 to 1.0)
#   vol = volume.GetMasterVolumeLevelScalar()
#   # Convert the volume level to a percentage
#   vol = vol * 100
#   # Format the volume level as a string
#   vol_str = f"{vol:.0f}%"
#   # Print the volume level
#   print(f"The sound volume is {vol_str}")
# get_sound_volume()

# #! test successful

def split(string, delimeter):
    delimeter_found = False
    response = ''
    for i in string:
        if delimeter_found:
            response += i
        elif delimeter_found is not True and i == len(string):
            response = False
        if i == delimeter:
            delimeter_found = True
    return response        
            

def preferences(preference):
    with open('user_preferences.txt', 'r') as file:
        raw = file.readlines()
    for i in raw:
        j = 0
        while j < len(preference):
            if i[j] == preference[j]:
                j += 1
            else:
                j = len(preference)
            if i[j] == ":":
                return(split(i, ":"))
    return(0)
              

    #I think I must be setting a record for the worst runtime or something of sorts
    
        
        

#print(preferences("key_theme"))
