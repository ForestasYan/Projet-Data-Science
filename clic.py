# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 12:10:26 2020

@author: fores
"""


from pynput.mouse import Listener

def on_click(x, y, button, pressed):
    print("clic")

with Listener (on_click=on_click) as listener:
    listener.join()