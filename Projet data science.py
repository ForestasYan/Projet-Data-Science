"""
Created on Thu Mar 12 09:20:07 2020
"""

""" replay("D://osu!/Songs/349208 Camellia as Bang Riot - Blastix Riotz/Camellia as Bang Riot - Blastix Riotz (Fresh Chicken) [GRAVITY copie].osu")
    replay("D://osu!/Songs/365619 KimuraYP - Kouon Katsuzetsu-chuu Oniki Hayakuchi Test/KimuraYP - Kouon Katsuzetsu-chuu Oniki Hayakuchi Test (Hydria) [copie].osu")
    replay("D://osu!/Songs/404994 noma - Brain Power/noma - Brain Power (Blocko) [Jinjin x Blocko's Overdrive].osu")
    replay("D://osu!/Songs/223370 Team Grimoire - C18H27NO3/Team Grimoire - C18H27NO3 ([Shana Lesus]) [7K NOVICE Lv.9].osu")
    replay("D://osu!/Songs/332673 Collection - Piano Beatmap Set/Collection - Piano Beatmap Set (CircusGalop) [10K HELL CIRCUS].osu")
    replay("D://osu!/Songs/379758 Cardboard Box - The Limit Does Not Exist/Cardboard Box - The Limit Does Not Exist (iJinjin) [Infinity].osu")
    replay("D://osu!/Songs/272871 D(ABE3) - MANIERA/D(ABE3) - MANIERA (iJinjin) [Masterpiece].osu")"""



#sensibilite 3.13
#position y  614

#pyautogui.KEYBOARD_KEYS


touches_jeu = ['a','z','e','r','t','y','u','i','o','p']
from Normalisation import normalisation
from Recuperation_plays import Recuperer_plays
from Recuperation_classement import Requete_classement
from pynput.mouse import Listener
import time
import pyautogui
import pygame
import pynput
pyautogui.PAUSE = 0.0001


def replay(path):
    time.sleep(2)
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
                    
                def on_click(x, y, button, pressed):
                    print("clic")
                    listener.stop()

                    
                with Listener (on_click=on_click) as listener:
                    listener.join()    

                temps_debut = time.time() - (touches[0][1]/1500)
                
                while (touches != [] or reste_a_appuyer(1500*(time.time() - temps_debut), moment_lachees)):
                    recuperer_touches(touches, touches_enfoncees, moment_appuis, moment_lachees, temps_debut)
                    appuyer_touches(touches_enfoncees, moment_appuis, moment_lachees, temps_debut)
                pygame.quit()

def recuperer_touches(touches, touches_enfoncees, moment_appuis, moment_lachees, temps_debut):
    val = 0
    for k in range(min(16,len(touches))):
        if (1500*(time.time() - temps_debut) > moment_lachees[touches[k-val][0]] and touches_enfoncees[touches[k-val][0]] == False):
            moment_appuis[touches[k-val][0]] = touches[k-val][1]
            moment_lachees[touches[k-val][0]] = touches[k-val][2]
            del touches[k-val]
            val += 1
        
        
def appuyer_touches(touches_enfoncees, moment_appuis, moment_lachees, temps_debut):
    for k in range(len(touches_enfoncees)):
        if touches_enfoncees[k] == True:
            if 1500*(time.time()-temps_debut) > moment_lachees[k]:
                pyautogui.keyUp(touches_jeu[k])
                touches_enfoncees[k] = False
        if touches_enfoncees[k] == False:
            if moment_lachees[k] > 1500*(time.time()-temps_debut) > moment_appuis[k]:
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

                while pyautogui.position().y != 899:
                    pass
                while pyautogui.position().y >846:
                    pass

"""