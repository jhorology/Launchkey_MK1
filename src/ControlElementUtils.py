# -*- coding: utf-8 -*-
# 2015.06.30 20:10:52 JST
# Embedded file name: /Users/versonator/Jenkins/live/output/mac_64_static/Release/midi-remote-scripts/Launchkey_MK2/ControlElementUtils.py
from functools import partial
import Live
from _Framework.Dependency import depends
from _Framework.Resource import PrioritizedResource
from _Framework.InputControlElement import MIDI_CC_TYPE, MIDI_NOTE_TYPE
from _Framework.ButtonMatrixElement import ButtonMatrixElement
from _Framework.ButtonElement import ButtonElement
from _Framework.EncoderElement import EncoderElement
from _Framework.SliderElement import SliderElement
from _Framework.ComboElement import ComboElement
from .consts import STANDARD_CHANNEL

class PadButtonElement(ButtonElement):
    def __init__(self, *a, **k):
        super(PadButtonElement, self).__init__(*a, **k)
        
    def _set_skin_light(self, value):
        color = self._skin[value]
        color.draw(self)
        
    def turn_on(self):
        raise AssertionError, "turn_on()"

    def turn_off(self):
        self._set_skin_light('DefaultButton.Disabled')

    def send_balue(self, value):
        self._set_skin_light('DefaultButton.Disabled')


@depends(skin=None)
def make_button(identifier, msg_type = MIDI_NOTE_TYPE, is_momentary = True, skin = None, is_modifier = False, name = ''):
    return ButtonElement(is_momentary, msg_type, STANDARD_CHANNEL, identifier, skin=skin, name=name, resource_type=PrioritizedResource if is_modifier else None)

def make_pad_button(identifier, msg_type = MIDI_NOTE_TYPE, is_momentary = True, skin = None, is_modifier = False, name = ''):
    return PadButtonElement(is_momentary, msg_type, STANDARD_CHANNEL, identifier, skin=skin, name=name, resource_type=PrioritizedResource if is_modifier else None)

def make_encoder(identifier, name = ''):
    return EncoderElement(MIDI_CC_TYPE, STANDARD_CHANNEL, identifier, Live.MidiMap.MapMode.absolute, name=name)


def make_slider(identifier, name = '', channel = STANDARD_CHANNEL):
    return SliderElement(MIDI_CC_TYPE, channel, identifier, name=name)
# okay decompyling /Applications/Ableton Live 9 Suite.app/Contents/App-Resources/MIDI Remote Scripts/Launchkey_MK2/ControlElementUtils.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.06.30 20:10:52 JST
