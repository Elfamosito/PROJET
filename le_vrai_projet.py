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

py.init(WINDOW_WIDTH,WINDOW_HEIGHT, title="Midnight Project")

def initialisation():
    global x_joueur, y_joueur, vivant, game_over, liste_obstacles_1, liste_obstacles_2, liste_obstacles_3, liste_obstacles_4, obstacle_interval, score, obstacle_genere, vitesse_de_deplacement_ennemi, dash, fusee, tps_fusee, liste_missiles, longueur_missile, liste_explosion, rayon_explosion, slow, missile_width, missile_height, nb_missiles
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
    obstacle_genere = 0
    vitesse_de_deplacement_ennemi = 10
    dash = 0
    fusee = False
    tps_fusee = 0
    liste_missiles = []
    longueur_missile = 50
    liste_explosion = []
    rayon_explosion = 0
    slow = False
    missile_width = 30
    missile_height = 10
    nb_missiles = 0

initialisation()

def images():
    py.images[0].load(0,0,"Voiture_joueur.png") #type: ignore

images()

def deplacement_joueur():
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
    global max_1, min_2, min_3, min_4, min_1, decrease_1, increase_2, increase_3, increase_4
    if score == 0:
        # Initialisation des valeurs
        # Type 1 d'obstacle   Type décroissant   
        min_1 = 30
        max_1 = 100
        decrease_1 = 5
        # Type 2 d'obstacle    Type croissant
        min_2 = 0
        max_2 = 25
        increase_2 = 2
        # Type 3 d'obstacle    Type croissant
        min_3 = 0
        max_3 = 25
        increase_3 = 2
        # Type 4 d'obstacle    Type croissant
        min_4 = 0
        max_4 = 20
        increase_4 = 1
        
        # Il faut que max_1 + max_2 + max_3 + max_4 = 100.
        
    elif max_1 > min_1 and score !=0 : # type: ignore
            max_1 -= decrease_1 # type: ignore
            min_2 += increase_2 # type: ignore
            min_3 += increase_3 # type: ignore
            min_4 += increase_4 # type: ignore
        
def explosion():
    global rayon_explosion
    for explosion in liste_explosion :
        if rayon_explosion <= OBSTACLE_HEIGHT :
            rayon_explosion += 10
            py.circ(explosion[0] + OBSTACLE_WIDTH/2, explosion[1] + OBSTACLE_HEIGHT/2, rayon_explosion, 10)
            py.circ(explosion[0] + OBSTACLE_WIDTH/2, explosion[1] + OBSTACLE_HEIGHT/2, rayon_explosion - 10, 10)
        else:
            liste_explosion.remove(explosion)
            rayon_explosion = 0
            
def lancer_missiles():
    if py.btn(py.KEY_SPACE) and nb_missiles > 0:
        liste_missiles.append([x_joueur + PLAYER_WIDTH, y_joueur + PLAYER_HEIGHT/3])
        liste_missiles.append([x_joueur + PLAYER_WIDTH, y_joueur + (PLAYER_HEIGHT/3)*2])
            
def deplacement_missiles():
    for missile in liste_missiles:
        missile[0] += 20
        if missile[0] > WINDOW_WIDTH:
            liste_missiles.remove(missile)
        else:
                for obstacle in liste_obstacles_1:
                    if  missile[0] >= obstacle[0] and missile[1] >= obstacle[1] and missile[1] <= obstacle[1] + OBSTACLE_HEIGHT:
                        liste_explosion.append([missile[0], missile[1]])
                        liste_missiles.remove(missile)
                        liste_obstacles_1.remove(obstacle)
                for obstacle in liste_obstacles_2:
                    if  missile[0] >= obstacle[0] and missile[1] >= obstacle[1] and missile[1] <= obstacle[1] + OBSTACLE_HEIGHT:
                        liste_explosion.append([missile[0], missile[1]])
                        liste_missiles.remove(missile)
                        liste_obstacles_2.remove(obstacle)
                for obstacle in liste_obstacles_3:
                    if  missile[0] >= obstacle[0] and missile[1] >= obstacle[1] and missile[1] <= obstacle[1] + OBSTACLE_HEIGHT:
                        liste_explosion.append([missile[0], missile[1]])
                        liste_missiles.remove(missile)
                        liste_obstacles_3.remove(obstacle)
                for obstacle in liste_obstacles_4:
                    if  missile[0] >= obstacle[0] and missile[1] >= obstacle[1] and missile[1] <= obstacle[1] + OBSTACLE_HEIGHT:
                        liste_explosion.append([missile[0], missile[1]])
                        liste_missiles.remove(missile)
                        liste_obstacles_4.remove(obstacle)

def joueur():
    deplacement_joueur()
    check_colision_joueur_obstacle()

def obstacles():
    Obstacle_1()
    Obstacle_2()
    Obstacle_3()
    Obstacle_4()    

def deplacement_obstacles():
    global score
    
    for obstacle in liste_obstacles_1 : 
        obstacle[0] -= vitesse_de_deplacement_ennemi
        if obstacle[0] < -OBSTACLE_WIDTH :
            liste_obstacles_1.remove(obstacle)
            score +=1
    for obstacle in liste_obstacles_2 : 
        obstacle[0] -= 1.5 * vitesse_de_deplacement_ennemi
        if obstacle[0] < -OBSTACLE_WIDTH :
            liste_obstacles_2.remove(obstacle)
            score +=2
    for obstacle in liste_obstacles_3 : 
        obstacle[0] -= vitesse_de_deplacement_ennemi
        if obstacle[0] < -OBSTACLE_WIDTH :
            liste_obstacles_3.remove(obstacle)
            score +=2
    for obstacle in liste_obstacles_4 : 
        obstacle[0] -= 1.5 * vitesse_de_deplacement_ennemi
        if obstacle[0] < -OBSTACLE_WIDTH :
            liste_obstacles_4.remove(obstacle)
            score +=4    

def missiles_pouvoir():
    lancer_missiles()
    deplacement_missiles()

def slow_pouvoir():
    global vitesse_de_deplacement_ennemi
    
    if slow :
        vitesse_de_deplacement_ennemi = 5
    else :
        vitesse_de_deplacement_ennemi = 10    

def pouvoirs():
    missiles_pouvoir()
    slow_pouvoir()

def Jeu():
    global score, SCORE_COLOR
    
    if py.btnp(py.KEY_Q):
        py.quit()

    joueur()
    obstacles()
    deplacement_obstacles()

    pouvoirs()
    
    if score % 500 == 0: 
        change_proba()
    
    random_obstacles()

    if py.frame_count % 2 == 0 :
        score += 1

def Fin():
    global SCORE_COLOR
    
    py.cls(0)
    SCORE_COLOR += 1
    
    if SCORE_COLOR == 15 :
        SCORE_COLOR = 0
    
    py.text(WINDOW_WIDTH // 2 - 20, WINDOW_HEIGHT // 2, "Game Over", SCORE_COLOR)
    py.text(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 20 , "Final score: {}".format(score), SCORE_COLOR)

def draw_jeu():
    global SCORE_COLOR
    
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
    for missile in liste_missiles :
        py.rect(missile[0], missile[1], missile_width, missile_height, 10)
    
    explosion()
    
    py.text(4,4,"Score: {}".format(score), SCORE_COLOR)


def update():
    
    if vivant :
        Jeu()
            
    
def draw():
    
    if vivant :
        draw_jeu()   
    else:
        Fin()
        

py.run(update,draw)