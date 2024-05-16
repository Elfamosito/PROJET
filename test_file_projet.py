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

import pyxel

