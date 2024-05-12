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


# import pyxel as py

# py.init(1200,600, title="K")

# liste_boutons =[]
# py.mouse(True)

# def update():
#      if py.btnp(py.MOUSE_BUTTON_LEFT):
#             for bulles in liste_bulles:
#                 dx = bubble[0] - py.mouse_x
#                 dy = bubble[1] - py.mouse_y

#                 if dx * dx + dy * dy < bubble.r * bubble.r:
                        
    
# def draw():
#     py.cls(0)

# py.run(update,draw)

# import pyxel

# class Menu:
#     def __init__(self):
#         pyxel.init(200, 200, title="Menu de jeu")
#         pyxel.mouse(True)
#         # pyxel.load("assets.pyxres")  # Assure-toi d'avoir une image appelée "settings.png" dans le même répertoire que ce script

#         self.start_button = Button(75, 80, 50, 20, "Démarrer", self.start_game)
#         self.quit_button = Button(75, 110, 50, 20, "Quitter", pyxel.quit)
#         self.settings_button = Button(75, 140, 50, 20, "Paramètres", self.show_settings)

#     def run(self):
#         pyxel.run(self.update, self.draw)

#     def update(self):
#         self.start_button.update()
#         self.quit_button.update()
#         self.settings_button.update()

#     def draw(self):
#         pyxel.cls(0)
#         pyxel.text(50, 30, "Nom du Jeu", 7)
#         self.start_button.draw()
#         self.quit_button.draw()
#         self.settings_button.draw()

#     def start_game(self):
#         # Implémenter la logique pour démarrer le jeu
#         pass

#     def show_settings(self):
#         # pyxel.blt(0, 0, 0, 0, 0, 200, 150)
#         print('A')

# class Button:
#     def __init__(self, x, y, width, height, text, action):
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
#         self.text = text
#         self.action = action
#         self.hovered = False

#     def update(self):
#         self.hovered = (
#             self.x <= pyxel.mouse_x <= self.x + self.width
#             and self.y <= pyxel.mouse_y <= self.y + self.height
#         )
#         if self.hovered and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
#             self.action()

#     def draw(self):
#         color = 9 if self.hovered else 7
#         pyxel.rectb(self.x, self.y, self.width, self.height, color)
#         pyxel.text(self.x + 5, self.y + 5, self.text, color)

# menu = Menu()
# menu.run()


import pyxel

pyxel.init(1200, 600, title="Menu de jeu")
pyxel.mouse(True)

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
        retour_color = 11  # Change la couleur du bouton "Paramètres" si la souris le survole
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
    if show_settings:
        update_settings()
    
def draw():
    if menu_active:
        draw_menu()
    if show_settings:
        draw_settings()
    
    
pyxel.run(update,draw)