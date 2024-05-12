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

pyxel.init(600, 300, title="Menu de jeu", quit_key=pyxel.KEY_DELETE, display_scale=2)

# Variables globales pour garder une trace de l'état du menu
menu_active = True
show_settings = False

# Fonctions pour les actions des boutons
def start_game():
    global menu_active
    menu_active = False
    vivant = True

def quit_game():
    pyxel.quit()

def toggle_settings():
    global show_settings, menu_active
    menu_active = False
    show_settings = True

# Fonction principale de dessin du menu
def draw_menu():
    pyxel.cls(0)
    pyxel.text(50, 30, "Nom du Jeu", 7)
    
    start_color = 7
    quit_color = 7
    settings_color = 7

    if 75 <= pyxel.mouse_x <= 125:
        if 80 <= pyxel.mouse_y <= 100:
            start_color = 11  # Change la couleur du bouton "Démarrer" si la souris le survole
        elif 110 <= pyxel.mouse_y <= 130:
            quit_color = 11  # Change la couleur du bouton "Quitter" si la souris le survole
        elif 140 <= pyxel.mouse_y <= 160:
            settings_color = 11  # Change la couleur du bouton "Paramètres" si la souris le survole

    pyxel.rectb(75, 80, 50, 20, start_color)
    pyxel.text(80, 85, "Démarrer", start_color)
    pyxel.rectb(75, 110, 50, 20, quit_color)
    pyxel.text(85, 115, "Quitter", quit_color)
    pyxel.rectb(75, 140, 50, 20, settings_color)
    pyxel.text(80, 145, "Paramètres", settings_color)

def return_to_menu():
    global show_settings, menu_active
    menu_active = True
    show_settings = False

def update_settings():
    global show_settings
    if show_settings:
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            if 75 <= pyxel.mouse_x <= 125 and 140 <= pyxel.mouse_y <= 160:
                return_to_menu()

def draw_settings():
    pyxel.cls(0)
    pyxel.text(50, 30, "Paramètres", 7)
    retour_color = 7
    if 140 <= pyxel.mouse_y <= 160:
        retour_color = 11  # Change la couleur du bouton "Retour" si la souris le survole
    pyxel.rectb(75, 140, 50, 20, retour_color)
    pyxel.text(80, 145, "Retour", retour_color)

# Fonction principale de mise à jour du menu
def update_menu():
    global menu_active, show_settings
    if menu_active:
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            if 75 <= pyxel.mouse_x <= 125:
                if 80 <= pyxel.mouse_y <= 100:
                    start_game()
                elif 110 <= pyxel.mouse_y <= 130:
                    quit_game()
                elif 140 <= pyxel.mouse_y <= 160:
                    toggle_settings()

def update():
    if menu_active:
        update_menu()
        pyxel.mouse(True)
    if show_settings:
        update_settings()
        pyxel.mouse(True)
    
def draw():
    if menu_active:
        draw_menu()
    if show_settings:
        draw_settings()
    
    
pyxel.run(update,draw)