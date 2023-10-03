from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

def get_sound_volume():
  # Get the speakers device
  devices = AudioUtilities.GetSpeakers()
  # Activate the device interface
  interface = devices.Activate(
      IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
  # Get the volume object
  volume = cast(interface, POINTER(IAudioEndpointVolume))
  # Get the master volume level as a scalar (0.0 to 1.0)
  vol = volume.GetMasterVolumeLevelScalar()
  # Convert the volume level to a percentage
  vol = vol * 100
  # Format the volume level as a string
  vol_str = f"{vol:.0f}%"
  # Print the volume level
  print(f"The sound volume is {vol_str}")
get_sound_volume()

#! test successful