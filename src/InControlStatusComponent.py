# 2015.06.30 20:10:52 JST
# Embedded file name: /Users/versonator/Jenkins/live/output/mac_64_static/Release/midi-remote-scripts/Launchkey_MK2/InControlStatusComponent.py
from _Framework.SubjectSlot import subject_slot
from _Framework.ControlSurfaceComponent import ControlSurfaceComponent

class InControlStatusComponent(ControlSurfaceComponent):

    def __init__(self, set_is_in_control_on, *a, **k):
        super(InControlStatusComponent, self).__init__(*a, **k)
        self._set_is_in_control_on = set_is_in_control_on

    def set_in_control_status_button(self, button):
        self._on_in_control_value.subject = button

    @subject_slot('value')
    def _on_in_control_value(self, value):
        self._set_is_in_control_on(value >= 8)
# okay decompyling /Applications/Ableton Live 9 Suite.app/Contents/App-Resources/MIDI Remote Scripts/Launchkey_MK2/InControlStatusComponent.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.06.30 20:10:52 JST
