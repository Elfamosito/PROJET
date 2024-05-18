"""
Reste à faire : 

Faire le reste

Plus smooth

Faire aussi la sauvegarde du meilleur score et son affichage au début.
"""

"""
- start bouton
- Quite bouton
- Nom du jeu en grand en haut au milieu
- Settings bouton -> Les touches 
- Mettre la voiture a l'opposé des boutons
- Fond ?
- Affichage du meilleur score.

"""

import os
chemin_script = os.path.dirname(os.path.abspath(__file__)) # Récupérer le chemin absolu du répertoire contenant le script Python en cours d'exécution
nom_bibliotheque = "librairies" # Nom de la bibliothèque
chemin_bibliotheque = os.path.join(chemin_script, nom_bibliotheque) # Stockage du chemin absolu de la bibliothèque

import sys
sys.path.append(chemin_bibliotheque) # Faire en sorte que les fichiers de chemin_bibliotheque soit lu par l'ordinateur.

import pyxel as py

py.init(300,300,title='C')

def update():
    py.colors[0] = 0x000000
    py.colors[1] = 0x2b335f
    py.colors[2] = 0x7e2072
    py.colors[3] = 0x19959c
    py.colors[4] = 0x8b4852
    py.colors[5] = 0x395c98
    py.colors[6] = 0xa9c1ff
    py.colors[7] = 0xeeeeee
    py.colors[8] = 0xd4186c
    py.colors[9] = 0xd38441
    py.colors[10] = 0xe9c35b
    py.colors[11] = 0X70c6a9
    py.colors[12] = 0x7696de
    py.colors[13] = 0xa3a3a3
    py.colors[14] = 0xff9798
    py.colors[15] = 0xedc7b0

def draw():
    for i in range(16):
        py.rect(10+i*10,100,10,10,i)

py.run(update,draw)