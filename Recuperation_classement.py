# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 12:43:17 2020

@author: fores
"""

#on peut ignorer caractère 10252 (inclus) d'un page de classement

from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

def Requete_classement(methode, mode, pays, nb_pages):
    if methode!="Rank" and methode!="pp" and methode!="Accuracy" and methode!="Play Count" and methode!="SS count" and methode!="S count"and methode!="A count":
        return "methode de tri non valide"
    players = []
        
    if pays==[]:
        players = Recuperation_classement(methode, mode, None, nb_pages)
    
    else:
        for nation in pays:
            players += Recuperation_classement(methode, mode, nation, nb_pages)
        
    players_sorted = []
    for player in players:
        k = len(players_sorted)
        while k > 0 and float(affichage_comparaison(player[methode])) > float(affichage_comparaison(players_sorted[k-1][methode])):
            k -= 1
        players_sorted = players_sorted[:k] + [player] + players_sorted[k:]    
    
    df = pd.DataFrame(players_sorted)    
    df.to_csv("classement_joueurs.csv", sep="\t")
    classement = pd.read_csv("classement_joueurs.csv", sep='\t', encoding="latin1")
    classement.columns = ["id", "Rank", "Player Name", "Accuracy", "Play Count", "pp", "SS count", "S count", "A count"]


def Recuperation_classement(methode, mode, pays, nb_page):
    players = []
    for num_page in range(nb_page + 1):
        players += Recuperation_page_classement(mode, pays, num_page)

    return players
    


def Recuperation_page_classement(mode, pays, num_page):
    url = "https://old.ppy.sh/p/pp/?m=" + str(mode)
    if pays !=None:
        url += ("&c=" + pays)
    html =  urlopen(url + "&page=" + str(num_page))
    html_soup = BeautifulSoup(html, 'html.parser')

    rows = html_soup.findAll("tr")
    players = []
    
    for k in range(1, len(rows)):
        cells = rows[k].findAll("td")
        player_entry = {
                "Rank": cells[0].text[1:],
                "Player Name": cells[1].text,
                "Accuracy": cells[2].text[:len(cells[2].text)-1],
                "Play Count": cells[3].text,
                "pp": cells[4].text[1:len(cells[4].text)-2],
                "SS count": affichage_comparaison(cells[5].text),
                "S count": affichage_comparaison(cells[6].text),    
                "A count": affichage_comparaison(cells[7].text)
            }
        players.append(player_entry)
    return players
    

    
def affichage_comparaison(txt):
    nv_txt = ""
    bon = True
    for cara in txt:
        if cara == ",":
            pass
        elif cara == "p":
            pass
        elif cara == "(":
            bon = False 
        elif bon == True:
            nv_txt += cara
    return nv_txt
    