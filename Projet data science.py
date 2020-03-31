# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 09:20:07 2020

@author: forestay
"""
#pyautogui.KEYBOARD_KEYS


touches_jeu = ['a','z','e','r','t','y','u','i']
from Normalisation import normalisation
import time as time
import pyautogui
import pygame
pyautogui.PAUSE = 0.05


def replay(path):
    touches, nb_colonnes = normalisation(path)
    pygame.init()
    fenetre = pygame.display.set_mode((640, 480))
    touches_enfoncees = []
    for k in range(nb_colonnes):
        touches_enfoncees.append(False)

    while touches != [[]] and not(touches_enfoncee_existe(touches_enfoncees)):
         
        event = pygame.event.get()
        for k in event:
            if k.type == pygame.QUIT:
                pygame.quit()
                break
            
            if k.type == pygame.KEYDOWN:
                print(touches)   
                temps_debut = time.time()
                    
                moment_appuis = []
                for k in range(nb_colonnes):
                    moment_appuis.append(0)
                moment_lachees = []
                for k in range(nb_colonnes):
                    moment_lachees.append(0)
 
                    
                while (touches != [[]] or touches_enfoncee_existe(touches_enfoncees)):
                    recuperer_touches(touches, moment_appuis, moment_lachees, temps_debut)
                    appuyer_touches(touches_enfoncees, moment_appuis, moment_lachees, temps_debut)
                    print(1000*(time.time() - temps_debut))
  
#bon
def recuperer_touches(touches, moment_appuis, moment_lachees, temps_debut):
    touches_a_effacer = []
    for k in range(min(16,len(touches))):
        if 1000*(time.time() - temps_debut) > moment_lachees[touches[k][0]]:
            moment_appuis[touches[k][0]] = touches[k][1]
            moment_lachees[touches[k][0]] = touches[k][2]
            touches_a_effacer.append(k)
            #revoir ca↓
    for k in range(len(touches_a_effacer),-1):
        del touches[k]
        
        
def appuyer_touches(touches_enfoncees, moment_appuis, moment_lachees, temps_debut):
    for k in range(len(touches_enfoncees)):
        if touches_enfoncees[k] == True:
            if 1000*(time.time()-temps_debut) > moment_lachees[k]:
                pyautogui.keyUp(touches_jeu[k])
                touches_enfoncees[k] == False
        if touches_enfoncees[k] == False:
            if 1000*(time.time()-temps_debut) > moment_appuis[k]:
                pyautogui.keyDown(touches_jeu[k])
                touches_enfoncees[k] == True
    
    
def touches_enfoncee_existe(touches_enfoncees):
    for k in touches_enfoncees:
        if touches_enfoncees[k]:
            return True
    return False




"""
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


                        
                    if k.type == pygame.KEYUP:
                        print("UwU ", time.time()-a)
                        pass
                pyautogui.keyUp('a')
                     
print("fini")

"""