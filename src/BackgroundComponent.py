# 2015.06.30 20:10:51 JST
# Embedded file name: /Users/versonator/Jenkins/live/output/mac_64_static/Release/midi-remote-scripts/Launchkey_MK2/BackgroundComponent.py
from _Framework.BackgroundComponent import BackgroundComponent as BackgroundComponentBase

class BackgroundComponent(BackgroundComponentBase):

    def _clear_control(self, name, control):
        super(BackgroundComponent, self)._clear_control(name, control)
        if control:
            control.add_value_listener(self._on_value_listener)

    def _on_value_listener(self, *a, **k):
        pass
# okay decompyling /Applications/Ableton Live 9 Suite.app/Contents/App-Resources/MIDI Remote Scripts/Launchkey_MK2/BackgroundComponent.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.06.30 20:10:51 JST
