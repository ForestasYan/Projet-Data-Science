"""
Created on Thu Mar 12 09:20:07 2020
"""
#sensibilite 3.13
#position y  614

#pyautogui.KEYBOARD_KEYS


touches_jeu = ['a','z','e','r','t','y','u','i']
from Normalisation import normalisation
import time
import pyautogui
import pygame
import pynput
pyautogui.PAUSE = 0.0001


def replay(path):
    time.sleep(1)
    touches, nb_colonnes = normalisation(path)
    pygame.init()
    fenetre = pygame.display.set_mode((640, 480))
    touches_enfoncees = []
    for k in range(nb_colonnes):
        touches_enfoncees.append(False)

    while touches != []:
         
        event = pygame.event.get()
        for k in event:
            if k.type == pygame.QUIT:
                pygame.quit()
                break
            
            if k.type == pygame.KEYDOWN:
                print("debut du programme")
                moment_appuis = []
                for k in range(nb_colonnes):
                    moment_appuis.append(0)
                moment_lachees = []
                for k in range(nb_colonnes):
                    moment_lachees.append(0)
                    
                    
                while pyautogui.position().y != 899:
                    pass
                while pyautogui.position().y >846:
                    pass
                temps_debut = time.time()+0.510
                
                while (touches != [] or reste_a_appuyer(1000*(time.time() - temps_debut), moment_lachees)):
                    recuperer_touches(touches, moment_appuis, moment_lachees, temps_debut)
                    appuyer_touches(touches_enfoncees, moment_appuis, moment_lachees, temps_debut)
                print(time.time()-temps_debut)
                pygame.quit()

def recuperer_touches(touches, moment_appuis, moment_lachees, temps_debut):
    touches_a_effacer = []
    for k in range(min(16,len(touches))):
        if 1000*(time.time() - temps_debut) > moment_lachees[touches[k][0]]:
            moment_appuis[touches[k][0]] = touches[k][1]
            moment_lachees[touches[k][0]] = touches[k][2]
            touches_a_effacer.append(k)
    for k in range(len(touches_a_effacer), 0, -1):
        del touches[k-1]
        
        
def appuyer_touches(touches_enfoncees, moment_appuis, moment_lachees, temps_debut):
    for k in range(len(touches_enfoncees)):
        if touches_enfoncees[k] == True:
            if 1000*(time.time()-temps_debut) > moment_lachees[k]:
                pyautogui.keyUp(touches_jeu[k])
                touches_enfoncees[k] = False
        if touches_enfoncees[k] == False:
            if moment_lachees[k] > 1000*(time.time()-temps_debut) > moment_appuis[k]:
                pyautogui.keyDown(touches_jeu[k])
                touches_enfoncees[k] = True
    
    
def reste_a_appuyer(time, moment_lachees):
    for k in range(len(moment_lachees)):
        if time < moment_lachees[k]:
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