# -*- coding: utf-8 -*-
# 2015.06.30 20:10:53 JST
# Embedded file name: /Users/versonator/Jenkins/live/output/mac_64_static/Release/midi-remote-scripts/Launchkey_MK2/Skin.py
from _Framework.Skin import Skin
from .Colors import Rgb

class Colors:

    class Session:
        # stop all clip button
        StopAllOn = Rgb.AMBER_HALF
        StopAllOff = Rgb.BLACK
        # bottom row stop button
        StopClipTriggered = Rgb.GREEN_BLINK
        StopClip = Rgb.AMBER
        # scen start button
        Scene = Rgb.AMBER_HALF
        NoScene = Rgb.BLACK
        SceneTriggered = Rgb.GREEN_BLINK
        # top row clip launch button
        ClipTriggeredPlay = Rgb.GREEN_BLINK
        ClipTriggeredRecord = Rgb.RED_BLINK
        RecordButton = Rgb.RED
        ClipStopped = Rgb.AMBER
        ClipStarted = Rgb.GREEN
        ClipRecording = Rgb.RED
        ClipEmpty = Rgb.BLACK
        # may be unused
        StoppedClip = Rgb.BLACK
        Enabled = Rgb.BLACK

    class Mode:
        DeviceMode = Rgb.AMBER_HALF
        DeviceModeOn = Rgb.AMBER
        PanMode = Rgb.AMBER_HALF
        PanModeOn = Rgb.AMBER
        Send0Mode = Rgb.AMBER_HALF
        Send0ModeOn = Rgb.AMBER
        Send1Mode = Rgb.AMBER_HALF
        Send1ModeOn = Rgb.AMBER
        Send2Mode = Rgb.AMBER_HALF
        Send2ModeOn = Rgb.AMBER
        Send3Mode = Rgb.AMBER_HALF
        Send3ModeOn = Rgb.AMBER
        Send4Mode = Rgb.AMBER_HALF
        Send4ModeOn = Rgb.AMBER
        Send5Mode = Rgb.AMBER_HALF
        Send5ModeOn = Rgb.AMBER
        Disabled = Rgb.BLACK

    class Device:
        Bank = Rgb.AMBER_HALF
        BestOfBank = Rgb.AMBER
        BankSelected = Rgb.GREEN
        BankEmpty = Rgb.BLACK

    class DefaultButton:
        Disabled = Rgb.BLACK
        
def make_skin():
    return Skin(Colors)
# okay decompyling /Applications/Ableton Live 9 Suite.app/Contents/App-Resources/MIDI Remote Scripts/Launchkey_MK2/Skin.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.06.30 20:10:54 JST
