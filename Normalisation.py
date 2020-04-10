# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 15:11:36 2020

@author: -
"""

def normalisation(emplacement):
    texte = Recuperer_texte(emplacement)
    liste, nb_colonnes = liste_lignes(texte)
    lignes_types = determiner_type_note(liste)
    liste_appuis = creer_apuis(lignes_types, nb_colonnes)
    return liste_appuis, nb_colonnes



def Recuperer_texte(emplacement):
    with open(emplacement,'r') as f:
        texte = f.read()
    return texte

def donner_ligne(texte):
    ligne = ""
    for cara in texte:
        if cara == "\n":
            return ligne
        ligne += cara
        
def liste_lignes(texte):
    HitObject_atteint = False
    liste_lignes = []
    while texte != "":
        ligne = donner_ligne(texte)
        if HitObject_atteint and len(ligne)>10:
            liste_lignes.append(ligne)
        if ligne == "[HitObjects]":
            HitObject_atteint = True
        if len(ligne) >10:
            if ligne[:10] == "CircleSize":
                nb_colonnes = int(ligne[-1])
        texte = texte[len(ligne)+1:]
    return liste_lignes, nb_colonnes
    
def determiner_type_note(liste):
    liste_type =[]
    for ligne in liste:
        nb_deux_points = 0
        for cara in ligne:
            if cara == ":":
                nb_deux_points += 1
        if nb_deux_points == 4:
            liste_type.append(["courte", ligne])
        if nb_deux_points == 5:
            liste_type.append(["longue", ligne])
    return liste_type

def creer_apuis(lignes_types, nb_colonnes):
    appuis =[]
    for ligne in lignes_types:
        if ligne[0] == 'courte':
            val = 0
            while ligne[1][val] != ",":
                val += 1
            val_col = int(ligne[1][:val])
            
            val2 = val + 5
            while ligne[1][val2] != ",":
                val2 += 1
            val_debut = int(ligne[1][val+5:val2])
            #on va appuyer 20ms par note courte
            appuis.append([int((val_col - 512/(2*nb_colonnes))/(512/nb_colonnes)), val_debut, val_debut+25])
        
        else:
            val = 0
            while ligne[1][val] != ",":
                val += 1
            val_col = int(ligne[1][:val])
            
            val2 = val + 5
            while ligne[1][val2] != ",":
                val2 += 1
            val_debut = int(ligne[1][val+5:val2])

            val3 = val2 + 1
            while ligne[1][val3] != ":":
                if ligne[1][val3] == ",":
                    val2 = val3+1
                val3 += 1
            val_fin = int(ligne[1][val2:val3])
            appuis.append([int((val_col - 512/(2*nb_colonnes))/(512/nb_colonnes)), val_debut, val_fin])     
    return appuis
