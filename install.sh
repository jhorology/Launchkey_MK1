#!/bin/sh

TARGET_DIR='/Applications/Ableton Live 9 Suite.app/Contents/App-Resources/MIDI Remote Scripts/Launchkey_MK1'

cd `dirname $0`

if [ -d "$TARGET_DIR" ]; then
    rm -rf "$TARGET_DIR"
fi
mkdir "$TARGET_DIR"
cp ./src/*.py "$TARGET_DIR"
ls -al "$TARGET_DIR"
