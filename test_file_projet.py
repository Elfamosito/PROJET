"""
Ce qu'il reste à faire.
-Bonus:
    - Slow
    - Missiles
    - Fusée
    - Dash
    
Mettre les images des ennemis

Faire la hitbox de départ des ennemis, pour qu'ils ne puissent pas se surperposer.

Faire le fond animé.

Menu principal, début

Faire une fin "potable" -> Recommencer + Retour au menu principal + Credits(bande qui défile).

++
Création d'un choix entre voiture de différentes couleurs.
"""

# Bonus
# Slow
from le_vrai_projet import *

# slow = False
# if slow:
#     vitesse_de_deplacement = 5
# else:
#     vitesse_de_deplacement = 10

#Missile
# liste_missiles = []
# longueur_missile = 50
# liste_explosion = []
# rayon_explosion = 0

# def explosion():
#     global rayon_explosion
#     for explosion in liste_explosion :
#         if rayon_explosion <= OBSTACLE_HEIGHT :
#             rayon_explosion += 10
#             py.circ(explosion[0] + OBSTACLE_WIDTH/2, explosion[1] + OBSTACLE_HEIGHT/2, rayon_explosion, 10)
#             py.circ(explosion[0] + OBSTACLE_WIDTH/2, explosion[1] + OBSTACLE_HEIGHT/2, rayon_explosion - 10, 10)
#         else:
#             liste_explosion.remove(explosion)


# def lancer_missiles():
#     if py.btnp(py.KEY_SPACE, 5 , 10):
#         liste_missiles.append([x_joueur + PLAYER_WIDTH, y_joueur + PLAYER_HEIGHT/3])
#         liste_missiles.append([x_joueur + PLAYER_WIDTH, y_joueur + (PLAYER_HEIGHT/3)*2])

# def deplacement_missiles():
#     for missile in liste_missiles:
#         missile[0] += 20
#         if missile[0] > WINDOW_WIDTH:
#             liste_missiles.remove(missile)
#         else:
#                 for obstacle in liste_obstacles_1:
#                     if  missile[0] >= obstacle[0] and missile[1] >= obstacle[1] and missile[1] <= obstacle[1] + OBSTACLE_HEIGHT:
#                         liste_missiles.remove(missile)
#                         liste_obstacles_1.remove(obstacle)
#                         liste_explosion.append([missile[0], missile[1]])
#                 for obstacle in liste_obstacles_2:
#                     if  missile[0] >= obstacle[0] and missile[1] >= obstacle[1] and missile[1] <= obstacle[1] + OBSTACLE_HEIGHT:
#                         liste_missiles.remove(missile)
#                         liste_obstacles_1.remove(obstacle)
#                         liste_explosion.append([missile[0], missile[1]])
#                 for obstacle in liste_obstacles_3:
#                     if  missile[0] >= obstacle[0] and missile[1] >= obstacle[1] and missile[1] <= obstacle[1] + OBSTACLE_HEIGHT:
#                         liste_missiles.remove(missile)
#                         liste_obstacles_1.remove(obstacle)
#                         liste_explosion.append([missile[0], missile[1]])
#                 for obstacle in liste_obstacles_4:
#                     if  missile[0] >= obstacle[0] and missile[1] >= obstacle[1] and missile[1] <= obstacle[1] + OBSTACLE_HEIGHT:
#                         liste_missiles.remove(missile)
#                         liste_obstacles_1.remove(obstacle)
#                         liste_explosion.append([missile[0], missile[1]])

#Fusée
fusee = False
tps_fusee = 0

if fusee : 
    for obstacle in liste_obstacles_1:
        liste_obstacles_1.remove(obstacle)
    for obstacle in liste_obstacles_2:
        liste_obstacles_2.remove(obstacle)
    for obstacle in liste_obstacles_3:
        liste_obstacles_3.remove(obstacle)
    for obstacle in liste_obstacles_4:
        liste_obstacles_4.remove(obstacle)
    
    '''
    A ajouter dans le draw:
    Ne pas oublier de faire charger l'image de la fusée dans la fonction image et de faire correspondre les nombres ci dessous du py.blt
    '''
    if vivant == True and fusee == False:
        py.blt (x_joueur , y_joueur, / , 0 , 0 , / , /)
        # Ajout d'autres éléments par exemple, traits de vitesse , etc...
    else:
        py.blt( x_joueur , y_joueur , 0 , 0 , 0 , 150 , 53 )
        
    '''
    A ajouter dans le update:
    '''
    if vivant == True and fusee == False :
        //
    if fusee :
        if tps_fusee < 300 :
            tps_fusee += 1
            if tps_fusee > 150 :
                x_joueur -= 4
            else:
                x_joueur += 4
        else: 
            fusee = False
            

#Dash
dash = 1

if dash >=1 :
    if py.btn(py.KEY_SHIFT) and py.btn(py.KEY_UP):
            y_joueur -= 100
            dash -= 1
            print('AAAAAA')
            if y_joueur <= 0 :
                y_joueur = 0
    elif py.btn(py.KEY_DOWN) and py.btn(py.KEY_DOWN):
            y_joueur += 100
            dash -= 1
            if y_joueur >= WINDOW_HEIGHT - PLAYER_HEIGHT :
                y_joueur = WINDOW_HEIGHT - PLAYER_HEIGHT
            

#Hitbox départ