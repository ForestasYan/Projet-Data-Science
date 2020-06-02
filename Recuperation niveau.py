# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 08:25:47 2020

@author: forestay
"""
#taper import csv dans excel

from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

html = urlopen("https://osustats.click/Pizu")
html_soup = BeautifulSoup(html, 'html.parser')
soup_str = str(html_soup)

rows = []
for k in range(len(soup_str)-11):
    if soup_str[k:k+11] == '{"score_id"':
        z = 0
        while soup_str[k+z] != "}":
            z +=1
        rows.append(soup_str[k:k+z+1])
        
print(rows, '\n')

def trouve_separateur(txt, k):
    z = 0
    while txt[k+z]!= "," and txt[k+z]!="}":
        z +=1
    return k+z

def trouve_separateur2(txt, k):
    z = 0
    while txt[k+z]!= ":":
        z +=1
    return k+z

plays = []

for row in rows:
    ind = 1;
    play = {}
    for k in range (13):
        ind1 = trouve_separateur(row, ind)
        ind2 = trouve_separateur2(row,ind)
        if k != 11:
            play[row[ind+1:ind2-1]] = row[ind2+1:ind1]
        ind = ind1+1
        
    plays.append(play)
    
print(plays)



df = pd.DataFrame(plays)
print(df) 


df.to_csv("stat_joueur.csv", sep="\t")
craftcans = pd.read_csv("stat_joueur.csv", sep='\t', encoding="latin1")
craftcans.columns = ["score_id", "beatmap_id", "nb_100", "nb_300", "nb_50", "miss", "date", "mods", "maxcombo", "pp", "rank", "score"]

"""
ibus = craftcans["ibu"]
print(min(ibus))
print(max(ibus))
"""
