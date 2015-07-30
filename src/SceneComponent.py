# -*- coding: utf-8 -*-
from _Framework.SceneComponent import SceneComponent as SceneComponentBase
from .ClipSlotComponent import ClipSlotComponent

class SceneComponent(SceneComponentBase):
    clip_slot_component_type = ClipSlotComponent
    
    def __init__(self, *a, **k):
        super(SceneComponent, self).__init__(*a, **k)

        
