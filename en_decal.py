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
PLAYER_WIDTH = 120
PLAYER_HEIGHT = 52
OBSTACLE_WIDTH_1 = 100
OBSTACLE_HEIGHT_1 = 45
OBSTACLE_WIDTH_2 = 150
OBSTACLE_HEIGHT_2 = 45
OBSTACLE_WIDTH_3 = 100
OBSTACLE_HEIGHT_3 = 95
OBSTACLE_WIDTH_4 = 150
OBSTACLE_HEIGHT_4 = 95
BONUS_WIDTH = 50
BONUS_HEIGHT = 50
OBSTACLE_COLOR = 9
BACKGROUND_COLOR = 0
SCORE_COLOR = 7
PLAYER_SPEED = 60
INITIAL_OBSTACLE_INTERVAL = 100
OBSTACLE_INTERVAL_DECREMENT = 2
SCORE_ADD = 1

py.init(WINDOW_WIDTH,WINDOW_HEIGHT, title="Midnight Project")

def initialisation():
    global x_joueur, y_joueur, vivant, game_over, liste_obstacles_1, liste_obstacles_2, liste_obstacles_3, liste_obstacles_4, liste_bonus, obstacle_interval, score, obstacle_genere, vitesse_de_deplacement_ennemi, dash, fusee, tps_fusee, rayon_onde, liste_onde, mode_onde, fusee_ready, fusee_get, calibrage, liste_missiles, longueur_missile, liste_explosion, rayon_explosion, tps_slow, missile_width, missile_height, nb_missiles, shield, liste_nid
    x_joueur = 0 + PLAYER_WIDTH
    y_joueur = WINDOW_HEIGHT // 2 + 2
    vivant = True
    game_over = False
    liste_obstacles_1 =[]
    liste_obstacles_2 =[]
    liste_obstacles_3 =[]
    liste_obstacles_4 =[]
    liste_bonus = []
    obstacle_interval = INITIAL_OBSTACLE_INTERVAL
    score = 0
    obstacle_genere = 0
    vitesse_de_deplacement_ennemi = 10
    dash = 10
    fusee = False
    tps_fusee = 0
    rayon_onde = 0
    liste_onde = []
    mode_onde = False
    fusee_ready = False
    fusee_get = False
    calibrage = True
    liste_missiles = []
    longueur_missile = 50
    liste_explosion = []
    rayon_explosion = 0
    tps_slow = 0
    missile_width = 30
    missile_height = 10
    nb_missiles = 0
    shield = 0
    liste_nid = []

initialisation()

def images():
    py.images[0].load(0,0,"Voiture_joueur.png") #type: ignore
    py.images[1].load(0,0,"fusee.png")  #type: ignore

images()

def deplacement_joueur():
    global y_joueur
    if py.btnp(py.KEY_UP) and y_joueur > 60 :
        y_joueur -= PLAYER_SPEED

    if py.btnp(py.KEY_DOWN) and y_joueur < WINDOW_HEIGHT - 120 :
        y_joueur += PLAYER_SPEED

def Obstacle_1():
    global y_obstacle, x_obstacle, WINDOW_HEIGHT, OBSTACLE_HEIGHT_1, WINDOW_WIDTH, OBSTACLE_WIDTH_1, liste_obstacles_1, obstacle_interval
    y_gen = ra.randint( 0 , 7 )
    if y_gen == 0: 
        y_obstacle = 60
    if y_gen == 1: 
        y_obstacle = 2 * 60
    if y_gen == 2: 
        y_obstacle = 3 * 60
    if y_gen == 3: 
        y_obstacle = 4 * 60
    if y_gen == 4: 
        y_obstacle = 5 * 60
    if y_gen == 5: 
        y_obstacle = 6 * 60
    if y_gen == 6: 
        y_obstacle = 7 * 60
    if y_gen == 7: 
        y_obstacle = 8 * 60
    y_obstacle += 7
    
    x_obstacle = WINDOW_WIDTH + OBSTACLE_WIDTH_1
    
    if py.frame_count % obstacle_interval == 0 and obstacle_genere == 1 :
        liste_obstacles_1.append([x_obstacle , y_obstacle])
        obstacle_interval -= OBSTACLE_INTERVAL_DECREMENT
        if obstacle_interval <= 20 :
            obstacle_interval = 15
            
def Obstacle_2():
    global y_obstacle, x_obstacle, WINDOW_HEIGHT, OBSTACLE_HEIGHT_2, WINDOW_WIDTH, OBSTACLE_WIDTH_2, liste_obstacles_2, obstacle_interval
    y_gen = ra.randint( 0 , 7 )
    if y_gen == 0: 
        y_obstacle = 60
    if y_gen == 1: 
        y_obstacle = 2 * 60
    if y_gen == 2: 
        y_obstacle = 3 * 60
    if y_gen == 3: 
        y_obstacle = 4 * 60
    if y_gen == 4: 
        y_obstacle = 5 * 60
    if y_gen == 5: 
        y_obstacle = 6 * 60
    if y_gen == 6: 
        y_obstacle = 7 * 60
    if y_gen == 7: 
        y_obstacle = 8 * 60
    y_obstacle += 7
        
    x_obstacle = WINDOW_WIDTH + OBSTACLE_WIDTH_2
    
    if py.frame_count % obstacle_interval == 0 and obstacle_genere == 2 :
        liste_obstacles_2.append([x_obstacle , y_obstacle])
        obstacle_interval -= OBSTACLE_INTERVAL_DECREMENT
        if obstacle_interval <= 20 :
            obstacle_interval = 15
            
def Obstacle_3():
    global y_obstacle, x_obstacle, WINDOW_HEIGHT, OBSTACLE_HEIGHT_3, WINDOW_WIDTH, OBSTACLE_WIDTH_3, liste_obstacles_3, obstacle_interval
    y_gen = ra.randint( 0 , 6 )
    if y_gen == 0: 
        y_obstacle = 60
    if y_gen == 1: 
        y_obstacle = 2 * 60
    if y_gen == 2: 
        y_obstacle = 3 * 60
    if y_gen == 3: 
        y_obstacle = 4 * 60
    if y_gen == 4: 
        y_obstacle = 5 * 60
    if y_gen == 5: 
        y_obstacle = 6 * 60
    if y_gen == 6: 
        y_obstacle = 7 * 60
    y_obstacle += 14
    
    x_obstacle = WINDOW_WIDTH + OBSTACLE_WIDTH_3
    
    if py.frame_count % obstacle_interval == 0 and obstacle_genere == 3 :
        liste_obstacles_3.append([x_obstacle , y_obstacle])
        obstacle_interval -= OBSTACLE_INTERVAL_DECREMENT
        if obstacle_interval <= 20 :
            obstacle_interval = 15
            
def Obstacle_4():
    global y_obstacle, x_obstacle, WINDOW_HEIGHT, OBSTACLE_HEIGHT_4, WINDOW_WIDTH, OBSTACLE_WIDTH_4, liste_obstacles_4, obstacle_interval
    y_gen = ra.randint( 0 , 7 )
    if y_gen == 0: 
        y_obstacle = 60
    if y_gen == 1: 
        y_obstacle = 2 * 60
    if y_gen == 2: 
        y_obstacle = 3 * 60
    if y_gen == 3: 
        y_obstacle = 4 * 60
    if y_gen == 4: 
        y_obstacle = 5 * 60
    if y_gen == 5: 
        y_obstacle = 6 * 60
    if y_gen == 6: 
        y_obstacle = 7 * 60
    y_obstacle += 14
    
    x_obstacle = WINDOW_WIDTH + OBSTACLE_WIDTH_4
    
    if py.frame_count % obstacle_interval == 0 and obstacle_genere == 4 :
        liste_obstacles_4.append([x_obstacle , y_obstacle])
        obstacle_interval -= OBSTACLE_INTERVAL_DECREMENT
        if obstacle_interval <= 20 :
            obstacle_interval = 15
            
def Bonus_obstacle():
    global y_obstacle, x_obstacle, WINDOW_HEIGHT, BONUS_HEIGHT, WINDOW_WIDTH, BONUS_WIDTH, liste_bonus, obstacle_interval
    y_gen = ra.randint( 0 , 7 )
    if y_gen == 0: 
        y_obstacle = 60
    if y_gen == 1: 
        y_obstacle = 2 * 60
    if y_gen == 2: 
        y_obstacle = 3 * 60
    if y_gen == 3: 
        y_obstacle = 4 * 60
    if y_gen == 4: 
        y_obstacle = 5 * 60
    if y_gen == 5: 
        y_obstacle = 6 * 60
    if y_gen == 6: 
        y_obstacle = 7 * 60
    if y_gen == 7: 
        y_obstacle = 8 * 60
    y_obstacle += 6
    
    x_obstacle = WINDOW_WIDTH + BONUS_WIDTH
    
    if py.frame_count % obstacle_interval == 0 and obstacle_genere == 5 :
        liste_bonus.append([x_obstacle , y_obstacle])
        obstacle_interval -= OBSTACLE_INTERVAL_DECREMENT
        if obstacle_interval <= 20 :
            obstacle_interval = 15
        
def check_colision_joueur_obstacle():
    global game_over, vivant, shield, nb_missiles, fusee_get, tps_slow, dash
    joueur_hitbox = [x_joueur , y_joueur , x_joueur + PLAYER_WIDTH , y_joueur + PLAYER_HEIGHT]
    for obstacle in liste_obstacles_1:
        obstacle_hitbox = [obstacle[0] , obstacle[1] , obstacle[0] + OBSTACLE_WIDTH_1 , obstacle[1] + OBSTACLE_HEIGHT_1 ]
        if check_hitbox_colision(joueur_hitbox, obstacle_hitbox):
            if shield > 0 :
                shield -= 1
                liste_explosion.append([obstacle[0] + OBSTACLE_WIDTH_1/2 , obstacle[1] + OBSTACLE_HEIGHT_1/2])
                liste_obstacles_1.remove(obstacle)
            else:
                vivant = False
                liste_explosion.append([obstacle[0] + OBSTACLE_WIDTH_1/2 , obstacle[1] + OBSTACLE_HEIGHT_1/2])
            break
    for obstacle in liste_obstacles_2:
        obstacle_hitbox = [obstacle[0] , obstacle[1] , obstacle[0] + OBSTACLE_WIDTH_2 , obstacle[1] + OBSTACLE_HEIGHT_2 ]
        if check_hitbox_colision(joueur_hitbox, obstacle_hitbox):
            if shield > 0 :
                shield -= 1
                liste_explosion.append([obstacle[0] + OBSTACLE_WIDTH_2/2 , obstacle[1] + OBSTACLE_HEIGHT_2/2])
                liste_obstacles_2.remove(obstacle)
            else:
                vivant = False
                liste_explosion.append([obstacle[0] + OBSTACLE_WIDTH_2/2 , obstacle[1] + OBSTACLE_HEIGHT_2/2])
            break
    for obstacle in liste_obstacles_3:
        obstacle_hitbox = [obstacle[0] , obstacle[1] , obstacle[0] + OBSTACLE_WIDTH_3 , obstacle[1] + OBSTACLE_HEIGHT_3 ]
        if check_hitbox_colision(joueur_hitbox, obstacle_hitbox):
            if shield > 0 :
                shield -= 1
                liste_explosion.append([obstacle[0] + OBSTACLE_WIDTH_3/2 , obstacle[1] + OBSTACLE_HEIGHT_3/2])
                liste_obstacles_3.remove(obstacle)
            else:
                vivant = False
                liste_explosion.append([obstacle[0] + OBSTACLE_WIDTH_3/2 , obstacle[1] + OBSTACLE_HEIGHT_3/2])
            break
    for obstacle in liste_obstacles_4:
        obstacle_hitbox = [obstacle[0] , obstacle[1] , obstacle[0] + OBSTACLE_WIDTH_4 , obstacle[1] + OBSTACLE_HEIGHT_4 ]
        if check_hitbox_colision(joueur_hitbox, obstacle_hitbox):
            if shield > 0 :
                shield -= 1
                liste_explosion.append([obstacle[0] + OBSTACLE_WIDTH_4/2 , obstacle[1] + OBSTACLE_HEIGHT_4/2])
                liste_obstacles_4.remove(obstacle)
            else:
                vivant = False
                liste_explosion.append([obstacle[0] + OBSTACLE_WIDTH_4/2 , obstacle[1] + OBSTACLE_HEIGHT_4/2])
            break
    for bonus in liste_bonus:
        bonus_hitbox = [bonus[0] , bonus[1] , bonus[0] + BONUS_WIDTH , bonus[1] + BONUS_HEIGHT ]
        if check_hitbox_colision(joueur_hitbox, bonus_hitbox):
            type_bonus = ra.randint(0,3)
            liste_bonus.remove(bonus)
            if type_bonus == 0:
                nb_missiles += 10
            elif type_bonus == 1:
                fusee_get = True
            elif type_bonus == 2:
                tps_slow += 200
            else:
                dash += 5

def check_hitbox_colision(hitbox_1, hitbox_2):
    if (hitbox_1[0] < hitbox_2[2] and hitbox_1[2] > hitbox_2[0] and hitbox_1[1] < hitbox_2[3] and hitbox_1[3] > hitbox_2[1]):
        return True
    return False
   
def collision_entre_obstacles():
    global liste_obstacles_1, liste_obstacles_2, liste_obstacles_3, liste_obstacles_4

   
def nid_de_poule():
    global liste_nid, score
    for nid in liste_nid : 
        nid[0] -= vitesse_de_deplacement_ennemi
        if nid[0] >=  - 100 :
            liste_nid.remove(nid)
            score += 350
    
    
def random_obstacles():
    global obstacle_genere
    proba_type_obstacle_1 = [1 for n in range(max_1)] 
    proba_type_obstacle_2 = [2 for n in range(min_2)] 
    proba_type_obstacle_3 = [3 for n in range(min_3)]
    proba_type_obstacle_4 = [4 for n in range(min_4)]
    proba_type_bonus = [5 for n in range(chance_bonus)]

    liste_proba_type_obstacle = proba_type_obstacle_1 + proba_type_obstacle_2 + proba_type_obstacle_3 + proba_type_obstacle_4 + proba_type_bonus
    
    indice_obstacle_genere = ra.randint(0 , len(liste_proba_type_obstacle) - 1)
    obstacle_genere = liste_proba_type_obstacle[indice_obstacle_genere]

def change_proba():
    global max_1, min_2, min_3, min_4, min_1, chance_bonus, decrease_1, increase_2, increase_3, increase_4, decrease_5
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

        #Type bonus
        chance_bonus = 1000
        
    elif max_1 > min_1 and score !=0 : # type: ignore
            max_1 -= decrease_1 # type: ignore
            min_2 += increase_2 # type: ignore
            min_3 += increase_3 # type: ignore
            min_4 += increase_4 # type: ignore

        
def explosion():
    global rayon_explosion
    rayon_max = 50
    for explosion in liste_explosion :
        if rayon_explosion <= rayon_max :
            rayon_explosion += 10
            py.circ(explosion[0], explosion[1], rayon_explosion, 10)

        else:
            liste_explosion.remove(explosion)
            rayon_explosion = 0
            
def lancer_missiles():
    global nb_missiles
    if py.btnp(py.KEY_SPACE) and nb_missiles > 0:
        nb_missiles -= 1
        liste_missiles.append([x_joueur + PLAYER_WIDTH, y_joueur + PLAYER_HEIGHT/3])
        liste_missiles.append([x_joueur + PLAYER_WIDTH, y_joueur + (PLAYER_HEIGHT/3)*2])
            
def deplacement_missiles():
    for missile in liste_missiles:
        missile[0] += 20
        if missile[0] > WINDOW_WIDTH:
            liste_missiles.remove(missile)
        else:
                for obstacle in liste_obstacles_1:
                    if  missile[0] >= obstacle[0] and missile[1] >= obstacle[1] and missile[1] <= obstacle[1] + OBSTACLE_HEIGHT_1:
                        liste_explosion.append([missile[0] + OBSTACLE_WIDTH_1/2 , missile[1] + OBSTACLE_HEIGHT_1/2])
                        liste_missiles.remove(missile)
                        liste_obstacles_1.remove(obstacle)
                for obstacle in liste_obstacles_2:
                    if  missile[0] >= obstacle[0] and missile[1] >= obstacle[1] and missile[1] <= obstacle[1] + OBSTACLE_HEIGHT_2:
                        liste_explosion.append([missile[0] + OBSTACLE_WIDTH_2/2 , missile[1] + OBSTACLE_HEIGHT_2/2])
                        liste_missiles.remove(missile)
                        liste_obstacles_2.remove(obstacle)
                for obstacle in liste_obstacles_3:
                    if  missile[0] >= obstacle[0] and missile[1] >= obstacle[1] and missile[1] <= obstacle[1] + OBSTACLE_HEIGHT_3:
                        liste_explosion.append([missile[0] + OBSTACLE_WIDTH_3/2 , missile[1] + OBSTACLE_HEIGHT_3/2])
                        liste_missiles.remove(missile)
                        liste_obstacles_3.remove(obstacle)
                for obstacle in liste_obstacles_4:
                    if  missile[0] >= obstacle[0] and missile[1] >= obstacle[1] and missile[1] <= obstacle[1] + OBSTACLE_HEIGHT_4:
                        liste_explosion.append([missile[0] + OBSTACLE_WIDTH_4/2 , missile[1] + OBSTACLE_HEIGHT_4/2])
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
        if obstacle[0] < -OBSTACLE_WIDTH_1 :
            liste_obstacles_1.remove(obstacle)
            score +=100
    for obstacle in liste_obstacles_2 : 
        obstacle[0] -= 1.5 * vitesse_de_deplacement_ennemi
        if obstacle[0] < -OBSTACLE_WIDTH_2 :
            liste_obstacles_2.remove(obstacle)
            score +=200
    for obstacle in liste_obstacles_3 : 
        obstacle[0] -= vitesse_de_deplacement_ennemi
        if obstacle[0] < -OBSTACLE_WIDTH_3 :
            liste_obstacles_3.remove(obstacle)
            score +=200
    for obstacle in liste_obstacles_4 : 
        obstacle[0] -= 1.5 * vitesse_de_deplacement_ennemi
        if obstacle[0] < -OBSTACLE_WIDTH_4 :
            liste_obstacles_4.remove(obstacle)
            score +=400   

def missiles_pouvoir():
    lancer_missiles()
    deplacement_missiles()

def slow_pouvoir():
    global vitesse_de_deplacement_ennemi, tps_slow
    
    if tps_slow > 0 :
        vitesse_de_deplacement_ennemi = 5
        tps_slow -= 1
        
    else :
        vitesse_de_deplacement_ennemi = 10    

def fusee_pouvoir():
    global fusee, mode_onde, fusee_get
    
    if fusee_get :
        fusee = True
        mode_onde = True
        fusee_get = False

def mode_fusee():
    global fusee, liste_bonus
    
    if fusee :
        for obstacle in liste_obstacles_1:
            liste_obstacles_1.remove(obstacle)
        for obstacle in liste_obstacles_2:
            liste_obstacles_2.remove(obstacle)
        for obstacle in liste_obstacles_3:
            liste_obstacles_3.remove(obstacle)
        for obstacle in liste_obstacles_4:
            liste_obstacles_4.remove(obstacle)
    
def fusee_ready_mode():
    global fusee, tps_fusee, x_joueur, y_joueur, mode_onde, fusee_ready, score, calibrage
    
    if calibrage :
        if x_joueur > 0 + PLAYER_WIDTH :
            x_joueur -= PLAYER_SPEED // 2
            score += SCORE_ADD
        if x_joueur <= 0 + PLAYER_WIDTH :
            x_joueur = 0 + PLAYER_WIDTH
            calibrage = False
            tps_fusee = -60
    else :

        if y_joueur > WINDOW_HEIGHT // 2 :
            y_joueur -= PLAYER_SPEED // 4
        if y_joueur < WINDOW_HEIGHT // 2 :
            y_joueur += PLAYER_SPEED // 4
        
        score += SCORE_ADD
        
        if tps_fusee < 371 :
            tps_fusee += 1
            if tps_fusee < 100 and tps_fusee >= 0:
                x_joueur += 7
                score += 23 * SCORE_ADD
            elif tps_fusee >= 100 and tps_fusee < 110 :
                x_joueur += 6
                score += 22 * SCORE_ADD
            elif tps_fusee >= 110 and tps_fusee < 120 :
                x_joueur += 5
                score += 21 * SCORE_ADD
            elif tps_fusee >= 120 and tps_fusee < 130:
                x_joueur += 4
                score += 20 * SCORE_ADD
            elif tps_fusee >= 130 and tps_fusee < 140 :
                x_joueur += 3
                score += 19 * SCORE_ADD
            elif tps_fusee >= 140 and tps_fusee < 150 :
                x_joueur += 2
                score += 18 * SCORE_ADD
            elif tps_fusee >= 150 and tps_fusee < 160 :
                x_joueur += 1
                score += 17 * SCORE_ADD
            elif tps_fusee >= 160 and tps_fusee < 170 :
                x_joueur += 0
                score += 16 * SCORE_ADD
            elif tps_fusee >= 170 and tps_fusee < 180 :
                x_joueur -= 0
                score += 15 * SCORE_ADD
            elif tps_fusee >= 180 and tps_fusee < 190 :
                x_joueur -= 1
                score += 14 * SCORE_ADD
            elif tps_fusee >= 190 and tps_fusee < 200 :
                x_joueur -= 2
                score += 13 * SCORE_ADD
            elif tps_fusee >= 200 and tps_fusee < 210 :
                x_joueur -= 3
                score += 12 * SCORE_ADD
            elif tps_fusee >= 210 and tps_fusee < 220 :
                x_joueur -= 4
                score += 11 * SCORE_ADD
            elif tps_fusee >= 220 and tps_fusee < 230 :
                x_joueur -= 5
                score += 10 * SCORE_ADD
            elif tps_fusee >= 230 and tps_fusee < 240 :
                x_joueur -= 6
                score += 9 * SCORE_ADD
            elif tps_fusee >= 240 and tps_fusee < 310 :
                x_joueur -= 7
                score += 8 * SCORE_ADD
            elif tps_fusee >= 310 and tps_fusee < 320 :
                x_joueur -= 6
                score += 7 * SCORE_ADD
            elif tps_fusee >= 320 and tps_fusee < 330 :
                x_joueur -= 5
                score += 6 * SCORE_ADD
            elif tps_fusee >= 330 and tps_fusee < 340:
                x_joueur -= 4
                score += 5 * SCORE_ADD
            elif tps_fusee >= 340 and tps_fusee < 350 :
                x_joueur -= 3
                score += 4 * SCORE_ADD
            elif tps_fusee >= 350 and tps_fusee < 360 :
                x_joueur -= 2
                score += 3 * SCORE_ADD
            elif tps_fusee >= 360 and tps_fusee < 370 :
                x_joueur -= 1
                score += 2 * SCORE_ADD
            elif tps_fusee >= 370 and tps_fusee < 371 :
                x_joueur -= 0
                score += 1 * SCORE_ADD
                mode_onde = True
                x_joueur = 0 + PLAYER_WIDTH   
        elif tps_fusee >= 371 : 
            fusee = False
            fusee_ready = False
            x_joueur = 0 + PLAYER_WIDTH
            tps_fusee = 0
            calibrage = False
    
def onde():
    global rayon_onde, fusee_ready
    for onde in liste_onde :
        if rayon_onde <= WINDOW_WIDTH :
            fusee_ready = False
            rayon_onde += 30
            py.circ(onde[0] + PLAYER_WIDTH/2, onde[1] + PLAYER_HEIGHT/2, rayon_onde, 12)
            py.circ(onde[0] + PLAYER_WIDTH/2, onde[1] + PLAYER_HEIGHT/2, rayon_onde - 30, 0)
        else:
            liste_onde.remove(onde)
            rayon_onde = 0
            fusee_ready = True    

def dash_pouvoir():
    global dash, y_joueur, x_joueur
    
    if dash > 0 :
        if py.btn(py.KEY_SHIFT) : # Pour utiliser le dash, il faut d'abord appuyer sur shift puis sur la touche de déplacement.
            if py.btnp(py.KEY_UP) :
                y_joueur -= 180
                dash -= 1
                
                if y_joueur <= 62 :
                    y_joueur = 62
                    dash += 1
                    
            elif py.btnp(py.KEY_DOWN) :
                y_joueur += 180
                dash -= 1

                if y_joueur >= WINDOW_HEIGHT - 120 :
                    y_joueur = WINDOW_HEIGHT - 120
                    dash += 1
                    
            elif py.btnp(py.KEY_RIGHT) :
                x_joueur += 300
                dash -= 1
                
                if x_joueur > WINDOW_WIDTH - 3 * PLAYER_WIDTH :
                    x_joueur = WINDOW_WIDTH - 3 * PLAYER_WIDTH
                    dash += 1
                    
            elif py.btnp(py.KEY_LEFT) :
                x_joueur -= 300
                dash -= 1
                
                if x_joueur < 0 + PLAYER_WIDTH :
                    x_joueur = 0 + PLAYER_WIDTH
                    dash += 1
                
def bonus():
    for bonus in liste_bonus : 
        bonus[0] -= vitesse_de_deplacement_ennemi
        if bonus[0] < -BONUS_WIDTH :
            liste_bonus.remove(bonus)               


def pouvoirs():
    missiles_pouvoir()
    slow_pouvoir()
    fusee_pouvoir()
    dash_pouvoir()

def Jeu():
    global score, fusee_ready
    
    if py.btnp(py.KEY_Q):
        py.quit()

    if fusee_ready:
        fusee_ready_mode()
    
    else:
        joueur()
        obstacles()
        deplacement_obstacles()
        Bonus_obstacle()
        bonus()
        pouvoirs()
        collision_entre_obstacles()
        nid_de_poule()
                
        if score % 50 == 0: 
            change_proba()
        
        random_obstacles()

        if py.frame_count % 2 == 0 :
            score += SCORE_ADD

def Fin():
    global SCORE_COLOR
    
    py.cls(0)
    SCORE_COLOR += 1
    
    if SCORE_COLOR == 15 :
        SCORE_COLOR = 0
    
    py.text(WINDOW_WIDTH // 2 - 20, WINDOW_HEIGHT // 2, "Game Over", SCORE_COLOR)
    py.text(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 20 , "Final score: {}".format(score), SCORE_COLOR)

def draw_jeu():
    global SCORE_COLOR, mode_onde, tps_slow
    
    py.cls(BACKGROUND_COLOR)
    
    if fusee:
        onde()
        for bonus in liste_bonus:
            liste_bonus.remove(bonus)
        for missile in liste_missiles:
            liste_missiles.remove(missile)
        tps_slow = 0
        if mode_onde :
            liste_onde.append([x_joueur, y_joueur])
            mode_onde = False
        elif fusee_ready == False:
            py.rect(x_joueur, y_joueur, PLAYER_WIDTH, PLAYER_HEIGHT, 7)
        else:
            py.blt (x_joueur , y_joueur, 1 , 0 , 0 , 150, 47, 11)
        
        
    else:
        py.blt( x_joueur , y_joueur + 1, 0 , 0 , 0 , 150 , 53, 0)
    
    py.line(0,60,1200,60,7)
    
    py.line(0,120,1200,120,7)
    
    py.line(0,180,1200,180,7)
    
    py.line(0,240,1200,240,7)
    
    py.line(0,300,1200,300,7)
    
    py.line(0,360,1200,360,7)
    
    py.line(0,420,1200,420,7)
    
    py.line(0,480,1200,480,7)
    
    py.line(0,540,1200,540,7)
    
    for obstacle in liste_obstacles_1 :
        py.rect(obstacle[0] , obstacle[1], OBSTACLE_WIDTH_1, OBSTACLE_HEIGHT_1, OBSTACLE_COLOR)
    for obstacle in liste_obstacles_2 :
        py.rect(obstacle[0] , obstacle[1], OBSTACLE_WIDTH_2, OBSTACLE_HEIGHT_2, OBSTACLE_COLOR)
    for obstacle in liste_obstacles_3 :
        py.rect(obstacle[0] , obstacle[1], OBSTACLE_WIDTH_3, OBSTACLE_HEIGHT_3, OBSTACLE_COLOR)
    for obstacle in liste_obstacles_4 :
        if py.frame_count % 40 > 20 :
            py.rect(obstacle[0] , obstacle[1], OBSTACLE_WIDTH_4, OBSTACLE_HEIGHT_4, OBSTACLE_COLOR)
        else:
            py.rect(obstacle[0] , obstacle[1], OBSTACLE_WIDTH_4, OBSTACLE_HEIGHT_4, 0)
    for bonus in liste_bonus :
        py.rect(bonus[0], bonus[1], BONUS_WIDTH, BONUS_HEIGHT, 12)
    # for nid in liste_nid : 
    #     py.rect(nid[0], nid[1], OBSTACLE_WIDTH, OBSTACLE_HEIGHT, 3)
    for missile in liste_missiles :
        py.rect(missile[0], missile[1], missile_width, missile_height, 10)
    
    explosion()
    
    py.text(4,4,"Score: {}".format(score), SCORE_COLOR)
    py.text(100,4,"DASH: {}".format(dash), SCORE_COLOR)
    py.text(200,4,"SLOW: {}".format(tps_slow), SCORE_COLOR)
    py.text(300,4,"MISSILES: {}".format(nb_missiles), SCORE_COLOR)
    

def update():

    if vivant :
        Jeu()
            
    
def draw():
    
    if vivant :
        draw_jeu()   
    else:
        explosion()
        Fin()
        if py.btnp(py.KEY_Q):
            py.quit()
        

py.run(update,draw)