import os
chemin_script = os.path.dirname(os.path.abspath(__file__)) # Récupérer le chemin absolu du répertoire contenant le script Python en cours d'exécution
nom_bibliotheque = "librairies" # Nom de la bibliothèque
chemin_bibliotheque = os.path.join(chemin_script, nom_bibliotheque) # Stockage du chemin absolu de la bibliothèque

import sys
sys.path.append(chemin_bibliotheque) # Faire en sorte que les fichiers de chemin_bibliotheque soit lu par l'ordinateur.

import pyxel as py
import random as ra

# Définition des variables globales
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 600
PLAYER_WIDTH = 115
PLAYER_HEIGHT = 50
OBSTACLE_WIDTH = 100
OBSTACLE_HEIGHT = 45
PLAYER_COLOR = 8
OBSTACLE_COLOR = 9
BACKGROUND_COLOR = 0
SCORE_COLOR = 7
PLAYER_SPEED = 10
OBSTACLE_SPEED = 10
INITIAL_OBSTACLE_INTERVAL = 100
OBSTACLE_INTERVAL_DECREMENT = 2

x_joueur = 0 + PLAYER_WIDTH
y_joueur = WINDOW_HEIGHT // 2
vivant = True
game_over = False
liste_obstacles_1 =[]
liste_obstacles_2 =[]
liste_obstacles_3 =[]
liste_obstacles_4 =[]
obstacle_interval = INITIAL_OBSTACLE_INTERVAL
score = 0
nb_minute = 0
obstacle_genere = 0
vitesse_de_déplacement_ennemi = 10

py.init(WINDOW_WIDTH,WINDOW_HEIGHT, title="Midnight Caca")

def images():
    py.images[0].load(0,0,"Voiture_joueur.png") #type: ignore

images()

def Joueur():
    global y_joueur
    if py.btn(py.KEY_UP) and y_joueur > 0 :
        y_joueur -= PLAYER_SPEED

    if py.btn(py.KEY_DOWN) and y_joueur < WINDOW_HEIGHT - PLAYER_HEIGHT :
        y_joueur += PLAYER_SPEED

def Obstacle_1():
    global y_obstacle, x_obstacle, WINDOW_HEIGHT, OBSTACLE_HEIGHT, WINDOW_WIDTH, OBSTACLE_WIDTH, liste_obstacles_1, obstacle_interval
    y_obstacle = ra.randint( 50 , WINDOW_HEIGHT - OBSTACLE_HEIGHT )
    x_obstacle = WINDOW_WIDTH + OBSTACLE_WIDTH
    
    if py.frame_count % obstacle_interval == 0 and obstacle_genere == 1 :
        liste_obstacles_1.append([x_obstacle , y_obstacle])
        obstacle_interval -= OBSTACLE_INTERVAL_DECREMENT
        if obstacle_interval <= 20 :
            obstacle_interval = 15
            
def Obstacle_2():
    global y_obstacle, x_obstacle, WINDOW_HEIGHT, OBSTACLE_HEIGHT, WINDOW_WIDTH, OBSTACLE_WIDTH, liste_obstacles_2, obstacle_interval
    y_obstacle = ra.randint( 50 , WINDOW_HEIGHT - OBSTACLE_HEIGHT )
    x_obstacle = WINDOW_WIDTH + OBSTACLE_WIDTH
    
    if py.frame_count % obstacle_interval == 0 and obstacle_genere == 2 :
        liste_obstacles_2.append([x_obstacle , y_obstacle])
        obstacle_interval -= OBSTACLE_INTERVAL_DECREMENT
        if obstacle_interval <= 20 :
            obstacle_interval = 15
            
def Obstacle_3():
    global y_obstacle, x_obstacle, WINDOW_HEIGHT, OBSTACLE_HEIGHT, WINDOW_WIDTH, OBSTACLE_WIDTH, liste_obstacles_3, obstacle_interval
    y_obstacle = ra.randint( 50 , WINDOW_HEIGHT - OBSTACLE_HEIGHT )
    x_obstacle = WINDOW_WIDTH + OBSTACLE_WIDTH
    
    if py.frame_count % obstacle_interval == 0 and obstacle_genere == 3 :
        liste_obstacles_3.append([x_obstacle , y_obstacle])
        obstacle_interval -= OBSTACLE_INTERVAL_DECREMENT
        if obstacle_interval <= 20 :
            obstacle_interval = 15
            
def Obstacle_4():
    global y_obstacle, x_obstacle, WINDOW_HEIGHT, OBSTACLE_HEIGHT, WINDOW_WIDTH, OBSTACLE_WIDTH, liste_obstacles_4, obstacle_interval
    y_obstacle = ra.randint( 50 , WINDOW_HEIGHT - OBSTACLE_HEIGHT )
    x_obstacle = WINDOW_WIDTH + OBSTACLE_WIDTH
    
    if py.frame_count % obstacle_interval == 0 and obstacle_genere == 4 :
        liste_obstacles_4.append([x_obstacle , y_obstacle])
        obstacle_interval -= OBSTACLE_INTERVAL_DECREMENT
        if obstacle_interval <= 20 :
            obstacle_interval = 15
        
def check_colision_joueur_obstacle():
    global game_over, vivant
    joueur_hitbox = [x_joueur , y_joueur , x_joueur + PLAYER_WIDTH , y_joueur + PLAYER_HEIGHT]
    for obstacle in liste_obstacles_1:
        obstacle_hitbox = [obstacle[0] , obstacle[1] , obstacle[0] + OBSTACLE_WIDTH , obstacle[1] + OBSTACLE_HEIGHT ]
        if check_hitbox_colision_joueur_obstacle(joueur_hitbox, obstacle_hitbox):
            vivant = False
            break
    for obstacle in liste_obstacles_2:
        obstacle_hitbox = [obstacle[0] , obstacle[1] , obstacle[0] + OBSTACLE_WIDTH , obstacle[1] + OBSTACLE_HEIGHT ]
        if check_hitbox_colision_joueur_obstacle(joueur_hitbox, obstacle_hitbox):
            vivant = False
            break
    for obstacle in liste_obstacles_3:
        obstacle_hitbox = [obstacle[0] , obstacle[1] , obstacle[0] + OBSTACLE_WIDTH , obstacle[1] + OBSTACLE_HEIGHT ]
        if check_hitbox_colision_joueur_obstacle(joueur_hitbox, obstacle_hitbox):
            vivant = False
            break
    for obstacle in liste_obstacles_4:
        obstacle_hitbox = [obstacle[0] , obstacle[1] , obstacle[0] + OBSTACLE_WIDTH , obstacle[1] + OBSTACLE_HEIGHT ]
        if check_hitbox_colision_joueur_obstacle(joueur_hitbox, obstacle_hitbox):
            vivant = False
            break

def check_hitbox_colision_joueur_obstacle(joueur_hitbox, obstacle_hitbox):
    if (joueur_hitbox[0] < obstacle_hitbox[2] and joueur_hitbox[2] > obstacle_hitbox[0] and joueur_hitbox[1] + 10 < obstacle_hitbox[3] and joueur_hitbox[3] - 10 > obstacle_hitbox[1]):
        return True
    return False
    
def random_obstacles():
    global obstacle_genere
    proba_type_obstacle_1 = [1 for n in range(max_1)] 
    proba_type_obstacle_2 = [2 for n in range(min_2)] 
    proba_type_obstacle_3 = [3 for n in range(min_3)]
    proba_type_obstacle_4 = [4 for n in range(min_4)]

    liste_proba_type_obstacle = proba_type_obstacle_1 + proba_type_obstacle_2 + proba_type_obstacle_3 + proba_type_obstacle_4
    
    indice_obstacle_genere = ra.randint(0 , len(liste_proba_type_obstacle)-1)
    obstacle_genere = liste_proba_type_obstacle[indice_obstacle_genere]

def change_proba():
    global nb_minute, max_1, min_2, min_3, min_4, min_1, decrease_1, increase_2, increase_3, increase_4
    if nb_minute == 0:
        # Initialisation des valeurs
        # Type 1 d'obstacle   Type décroissant   
        min_1 = 30
        max_1 = 90
        decrease_1 = 5
        # Type 2 d'obstacle    Type croissant
        min_2 = 5
        max_2 = 25
        increase_2 = 2
        # Type 3 d'obstacle    Type croissant
        min_3 = 5
        max_3 = 25
        increase_3 = 2
        # Type 4 d'obstacle    Type croissant
        min_4 = 0
        max_4 = 20
        increase_4 = 1
        
    elif max_1 > min_1 and nb_minute !=0 : # type: ignore
            max_1 -= decrease_1 # type: ignore
            min_2 += increase_2 # type: ignore
            min_3 += increase_3 # type: ignore
            min_4 += increase_4 # type: ignore
        
            
def update():
    global score, nb_minute, SCORE_COLOR
    
    if py.btnp(py.KEY_Q):
        py.quit()
    
    if vivant :
        Joueur()
        Obstacle_1()
        Obstacle_2()
        Obstacle_3()
        Obstacle_4()
        check_colision_joueur_obstacle()
        for obstacle in liste_obstacles_1 : 
            obstacle[0] -= vitesse_de_déplacement_ennemi
            if obstacle[0] < -OBSTACLE_WIDTH :
                liste_obstacles_1.remove(obstacle)
                score +=1
        for obstacle in liste_obstacles_2 : 
            obstacle[0] -= 1.5 * vitesse_de_déplacement_ennemi
            if obstacle[0] < -OBSTACLE_WIDTH :
                liste_obstacles_2.remove(obstacle)
                score +=2
        for obstacle in liste_obstacles_3 : 
            obstacle[0] -= vitesse_de_déplacement_ennemi
            if obstacle[0] < -OBSTACLE_WIDTH :
                liste_obstacles_3.remove(obstacle)
                score +=2
        for obstacle in liste_obstacles_4 : 
            obstacle[0] -= 1.5 * vitesse_de_déplacement_ennemi
            if obstacle[0] < -OBSTACLE_WIDTH :
                liste_obstacles_4.remove(obstacle)
                score +=4
        
        if score % 15 == 1 or nb_minute == 0 :
            change_proba()
        
        random_obstacles()
        nb_minute += 1
                
    else:
        py.cls(0)
        SCORE_COLOR += 1
        if SCORE_COLOR == 15 :
            SCORE_COLOR = 0
        py.text(WINDOW_WIDTH // 2 - 20, WINDOW_HEIGHT // 2, "Game Over", SCORE_COLOR)
        
    # nb_minute += 1

    
def draw():
    
    if vivant == True :
        py.cls(BACKGROUND_COLOR)
        py.blt( x_joueur , y_joueur , 0 , 0 , 0 , 150 , 53 )
        for obstacle in liste_obstacles_1 :
            py.rect(obstacle[0] , obstacle[1], OBSTACLE_WIDTH, OBSTACLE_HEIGHT, OBSTACLE_COLOR)
        for obstacle in liste_obstacles_2 :
            py.rect(obstacle[0] , obstacle[1], OBSTACLE_WIDTH+50, OBSTACLE_HEIGHT, OBSTACLE_COLOR)
        for obstacle in liste_obstacles_3 :
            py.rect(obstacle[0] , obstacle[1], OBSTACLE_WIDTH, OBSTACLE_HEIGHT+50, OBSTACLE_COLOR)
        for obstacle in liste_obstacles_4 :
            py.rect(obstacle[0] , obstacle[1], OBSTACLE_WIDTH+50, OBSTACLE_HEIGHT+50, OBSTACLE_COLOR)
        py.text(4,4,"Score: {}".format(score), SCORE_COLOR)
        
py.run(update,draw)