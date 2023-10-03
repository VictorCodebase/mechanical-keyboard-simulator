from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

def get_dynamic_volume():
    system_volume = get_sys_vol()

    if system_volume is not None:
        scaling_factor = 1.0 - (system_volume / 100.0)
        key_volume = 0.1 + (scaling_factor / 2.0) #! alter to change volume
        
        print("Scaling factor:", scaling_factor)
        print("System vol:", system_volume)
        print ("Key vol:", key_volume)

        return '{:.2f}'.format(key_volume)

def get_sys_vol():
    try:
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))

        vol = volume.GetMasterVolumeLevelScalar()
        vol *= 100
        return int(vol)


    except Exception as e:
        print(f"Error getting system volume: {str(e)}")
        return None


#print(get_sys_vol())
print(get_dynamic_volume())


