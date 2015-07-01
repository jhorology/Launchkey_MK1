# -*- coding: utf-8 -*-
from _Framework.ClipSlotComponent import ClipSlotComponent as ClipSlotComponentBase
from .Log import log_message

class ClipSlotComponent(ClipSlotComponentBase):

    def __init__(self, *a, **k):
        super(ClipSlotComponent, self).__init__(*a, **k)
        
    def set_empty_value(self, value):
        self._empty_value = value
        
    def _feedback_value(self):
        value_to_send = super(ClipSlotComponent, self)._feedback_value()
        # log_message("##### in  value_to_send : %s" % str(value_to_send))
        if value_to_send in (None, -1) or value_to_send == 0:
            value_to_send = self._empty_value
        # log_message("##### out value_to_send : %s" % str(value_to_send))
        return value_to_send
