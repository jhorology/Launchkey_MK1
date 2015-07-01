# 2015.06.30 20:10:51 JST
# Embedded file name: /Users/versonator/Jenkins/live/output/mac_64_static/Release/midi-remote-scripts/Launchkey_MK2/__init__.py
from _Framework.Capabilities import controller_id, inport, outport, CONTROLLER_ID_KEY, PORTS_KEY, NOTES_CC, SCRIPT
from .Launchkey_MK1 import Launchkey_MK1

def get_capabilities():
    return {CONTROLLER_ID_KEY: controller_id(vendor_id=4661, product_ids=[48], model_name='Launchkey 25'),
     PORTS_KEY: [inport(props=[NOTES_CC]),
                 inport(props=[NOTES_CC, SCRIPT]),
                 outport(props=[NOTES_CC]),
                 outport(props=[NOTES_CC, SCRIPT])]}

def create_instance(c_instance):
    return Launchkey_MK1(c_instance)
# okay decompyling /Applications/Ableton Live 9 Suite.app/Contents/App-Resources/MIDI Remote Scripts/Launchkey_MK2/__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.06.30 20:10:51 JST
