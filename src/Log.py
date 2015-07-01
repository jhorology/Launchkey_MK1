# -*- coding: utf-8 -*-
def set_log_instance(instance):
    global c_instance
    c_instance = instance

def log_message(message):
    c_instance.log_message(message) 
