# 2015.06.30 20:10:53 JST
# Embedded file name: /Users/versonator/Jenkins/live/output/mac_64_static/Release/midi-remote-scripts/Launchkey_MK2/MixerComponent.py
from _Framework.MixerComponent import MixerComponent as MixerComponentBase

class MixerComponent(MixerComponentBase):

    def set_volume_control(self, control):
        self._selected_strip.set_volume_control(control)
# okay decompyling /Applications/Ableton Live 9 Suite.app/Contents/App-Resources/MIDI Remote Scripts/Launchkey_MK2/MixerComponent.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.06.30 20:10:53 JST
