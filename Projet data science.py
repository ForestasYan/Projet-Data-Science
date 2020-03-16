# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 09:20:07 2020

@author: forestay
"""
#pyautogui.KEYBOARD_KEYS

import time as time
import pyautogui
import pygame

pygame.init()
fenetre = pygame.display.set_mode((640, 480))
a = time.time()
pyautogui.PAUSE = 0.05
while True:
    event = pygame.event.get()
    for k in event:
        if k.type == pygame.KEYDOWN:
            while True:

                pyautogui.keyDown('a')
                
                event = pygame.event.get()     
                for k in event:
                    
                    if k.type == pygame.QUIT:
                        pygame.quit()
                        break
                    if k.type == pygame.KEYDOWN:
                        if k.key == pygame.K_0:
                            pygame.quit()
                            break

                        
                    if k.type == pygame.KEYUP:
                        print("UwU ", time.time()-a)
                        pass
                pyautogui.keyUp('a')
                
                
                      
                
                
                     
print("fini")


