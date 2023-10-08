import utility as util
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

#TODO: next feature: 3d audio. Stereo keysound responsive to where the key is in the keyboard.

default_volume = 1.5
current_volume = default_volume

def settingsInit():
    global current_volume
    current_volume = float(util.get_preference('key_volume'))


def get_dynamic_volume():
    system_volume = get_sys_vol()

    #TODO: allow users to set base volume. probably use a txt file to store basic settings?
    if system_volume is not None:
        scaling_factor = 1.0 - (system_volume / 100.0)
        key_volume = current_volume + (scaling_factor / 2.0) #! alter to change volume
        return float('{:.2f}'.format(key_volume))

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
