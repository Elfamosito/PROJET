import os
chemin_script = os.path.dirname(os.path.abspath(__file__)) # Récupérer le chemin absolu du répertoire contenant le script Python en cours d'exécution
nom_bibliotheque = "librairies" # Nom de la bibliothèque
chemin_bibliotheque = os.path.join(chemin_script, nom_bibliotheque) # Stockage du chemin absolu de la bibliothèque

import sys
sys.path.append(chemin_bibliotheque) # Faire en sorte que les fichiers de chemin_bibliotheque soit lu par l'ordinateur.

import pyxel as py
import random as ra

# Définition des variables globales
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
PLAYER_WIDTH = 60
PLAYER_HEIGHT = 26
OBSTACLE_WIDTH_1 = 50
OBSTACLE_HEIGHT_1 = 23
OBSTACLE_WIDTH_2 = 75
OBSTACLE_HEIGHT_2 = 25
OBSTACLE_WIDTH_3 = 50
OBSTACLE_HEIGHT_3 = 40
OBSTACLE_WIDTH_4 = 75
OBSTACLE_HEIGHT_4 = 40
BONUS_WIDTH = 25
BONUS_HEIGHT = 25
OBSTACLE_COLOR = 9
BACKGROUND_COLOR = 0
SCORE_COLOR = 7
PLAYER_SPEED = 5
INITIAL_OBSTACLE_INTERVAL = 100
OBSTACLE_INTERVAL_DECREMENT = 2
SCORE_ADD = 1

py.init(WINDOW_WIDTH,WINDOW_HEIGHT, title="Midnight Project", quit_key=py.KEY_DELETE, display_scale=2)

# Chargement du score record depuis un fichier
def load_high_score():
    try: # Test pour vérifier l'existence du fichier de sauvegarde du record
        with open("high_score.txt", "r") as file: # Ouverture du fichier avec le record
            return int(file.read()) # Récupération du record
    except FileNotFoundError: # Si le fichier n'existe pas
        return 0 # Ne rien faire

# Sauvegarde du score record dans un fichier
def save_high_score(score): 
    with open("high_score.txt", "w") as file: # Ouverture du fichier ou création du fichier avec le record
        file.write(str(score)) # Insertion du record dans le fichier

def initialisation():
    global menu_active, show_settings, affichage_debut, x_joueur, y_joueur, vivant, game_over, liste_obstacles_1, liste_obstacles_2, liste_obstacles_3, liste_obstacles_4, liste_bonus, obstacle_interval, score, obstacle_genere, vitesse_de_deplacement_ennemi, dash, fusee, tps_fusee, rayon_onde, liste_onde, mode_onde, fusee_ready, fusee_get, calibrage, liste_missiles, liste_explosion, rayon_explosion, rayon_max, tps_slow, missile_width, missile_height, nb_missiles, shield, liste_nid, high_score
    
    menu_active = False
    show_settings = False
    affichage_debut = True
    x_joueur = 0 + PLAYER_WIDTH
    y_joueur = WINDOW_HEIGHT // 2
    vivant = False
    game_over = False
    liste_obstacles_1 =[]
    liste_obstacles_2 =[]
    liste_obstacles_3 =[]
    liste_obstacles_4 =[]
    liste_bonus = []
    obstacle_interval = INITIAL_OBSTACLE_INTERVAL
    score = 0
    obstacle_genere = 0
    vitesse_de_deplacement_ennemi = 5
    dash = 0
    fusee = False
    tps_fusee = 0
    rayon_onde = 0
    liste_onde = []
    mode_onde = False
    fusee_ready = False
    fusee_get = False
    calibrage = True
    liste_missiles = []
    liste_explosion = []
    rayon_explosion = 0
    rayon_max = 25
    tps_slow = 100
    missile_width = 15
    missile_height = 5
    nb_missiles = 0
    shield = 0
    liste_nid = []
    high_score = load_high_score()

initialisation()

def images():
    py.images[0].load(0,0,"Resources/Elements.png") #type: ignore
    py.images[1].load(0,0,"Resources/Commandes.png") #type: ignore

images()


def couleurs_debut():
    global col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,col12,col13,col
    col1=1
    col2=2
    col3=3
    col4=4
    col5=5
    col6=6
    col7=7
    col8=8
    col9=9
    col10=10
    col11=11
    col12=12
    col13=13
    col=0
    
couleurs_debut()

def affichage_debut_jeu():
    global col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,col12,col13,col
    if py.frame_count % 2 == 0:
        col1 += 1
        col2 += 1
        col3 += 1
        col4 += 1
        col5 += 1
        col6 += 1
        col7 += 1
        col8 += 1
        col9 += 1
        col10 += 1
        col11 += 1
        col12 += 1
        col13 += 1
    if col1 == 16 :
        col1 = 1
    elif col2 == 16 :
        col2 = 1
    elif col3 == 16 :
        col3 = 1
    elif col4 == 16 :
        col4 = 1
    elif col5 == 16 :
        col5 = 1
    elif col6 == 16 :
        col6 = 1
    elif col7 == 16 :
        col7 = 1
    elif col8 == 16 :
        col8 = 1
    elif col9 == 16 :
        col9 = 1
    elif col10 == 16 :
        col10 = 1
    elif col11 == 16 :
        col11 = 1
    elif col12 == 16 :
        col12 = 1
    elif col13 == 16 :
        col13 = 1
        
    py.text(240,150,"M",col1)
    py.text(250,150,"I",col2)
    py.text(260,150,"D",col3)
    py.text(270,150,"N",col4)
    py.text(280,150,"I",col5)
    py.text(290,150,"G",col6)
    py.text(300,150,"H",col7)
    py.text(310,150,"T",col8)
    py.text(330,150,"D",col9)
    py.text(340,150,"R",col10)
    py.text(350,150,"I",col11)
    py.text(360,150,"V",col12)
    py.text(370,150,"E",col13)

    if py.frame_count % 30 > 20:
        col = 0
    else:
        col=7

    py.text(260,180,"PRESS ENTER TO START",col)

# Fonctions pour les actions des boutons
def start_game():
    global menu_active, vivant
    
    py.mouse(False)
    menu_active = False
    vivant = True

def quit_game():
    py.quit()

def return_to_menu():
    global show_settings, menu_active
    menu_active = True
    show_settings = False

def update_settings():
    global show_settings
    if show_settings:
        if py.btnp(py.MOUSE_BUTTON_LEFT):
            if 45 <= py.mouse_x <= 95 and 240 <= py.mouse_y <= 260:
                return_to_menu()
        elif py.btnp(py.KEY_ESCAPE):
            return_to_menu()

def draw_settings():
    py.text(50, 30, "Settings", 7)
    
    py.blt(90 , 100 , 1 , 0 , 193 , 205 , 30) #Config 1
    py.blt(90 , 200 , 1 , 0 , 223 , 207 , 30)  #Config 2
    py.blt(300 , 20 , 1 , 0 , 150 , 150 , 44)#Touches deplacement
    py.blt(470 , 20 , 1 , 150 , 136 , 106 , 49)#touches bonus
    py.blt(315 , 80 , 1 , 0 , 0 , 128 , 78)#touches dp 1 zqsd
    py.blt(315 , 180 , 1 , 128 , 0 , 128 , 80)#touches dp 2 flèches
    py.blt(460 , 82 , 1 , 0 , 78 , 128 , 72)#touches bonus 1 aer
    py.blt(460 , 190 , 1 , 128 , 80 , 128 , 56)#touches bonus 2 :!
    
    retour_color = 7
    if 240 <= py.mouse_y <= 260 and 45 <= py.mouse_x <= 95:
        retour_color = 11  # Change la couleur du bouton "Retour" si la souris le survole
    py.rectb(45, 240, 50, 20, retour_color)
    py.text(50, 250, "Back", retour_color)

# Fonction principale de mise à jour du menu
def update_menu():
    global menu_active, show_settings
    if menu_active:
        if py.btnp(py.MOUSE_BUTTON_LEFT):
            if 75 <= py.mouse_x <= 125:
                if 80 <= py.mouse_y <= 100:
                    start_game()
                elif 110 <= py.mouse_y <= 130:
                    show_settings = True
                    menu_active = False
                elif 140 <= py.mouse_y <= 160:
                    quit_game()

def draw_menu():
    global col1
    
    py.text(50, 30, "MIDNIGHT DRIVE", 7)
    py.text(125, 50, "A game developed by Famoso Engine", 7)
    
    start_color = 7
    quit_color = 7
    settings_color = 7

    if 75 <= py.mouse_x <= 125:
        if 80 <= py.mouse_y <= 100:
            start_color = 11  # Change la couleur du bouton "Démarrer" si la souris le survole
        elif 110 <= py.mouse_y <= 130:
            settings_color = 11  # Change la couleur du bouton "Paramètres" si la souris le survole
        elif 140 <= py.mouse_y <= 160:
            quit_color = 11  # Change la couleur du bouton "Quitter" si la souris le survole

    py.rectb(75, 80, 50, 20, start_color)
    py.text(84, 85, "Drive", start_color)
    py.rectb(75, 110, 50, 20, settings_color)
    py.text(82, 115, "Settings", settings_color)
    py.rectb(75, 140, 50, 20, quit_color)
    py.text(86, 145, "Leave", quit_color)
    
    py.rectb(380, 120, 210, 170, 8)
    py.text(470 , 135 , "NEWS" , 6)
    py.text(390, 155, "- Press ALT + 9 to switch between 3 screen modes", 7)
    py.text(390, 175, "- The game is still in developpment, some bugs",7)
    py.text(390,195,"can still appear.", 7)
    
    py.blt( 200 , 200, 0 , 0 , 0 , 75 , 26, 0)
    
    py.text(500,293,"Actual version: 0.1.1", 7)
    
    if py.frame_count % 2 == 0:
        col1 += 1
    
    if col1 == 16:
        col1 = 1
    
    py.text(75, 250, "High score: {}".format(high_score), col1)
    

def deplacement_joueur():
    global y_joueur
    if (py.btn(py.KEY_UP) and y_joueur > 10) or (py.btn(py.KEY_Z) and y_joueur > 10) :
        y_joueur -= PLAYER_SPEED

    if (py.btn(py.KEY_DOWN) and y_joueur < WINDOW_HEIGHT - PLAYER_HEIGHT) or (py.btn(py.KEY_S) and y_joueur < WINDOW_HEIGHT - PLAYER_HEIGHT) :
        y_joueur += PLAYER_SPEED
    
    if y_joueur < 0 :
        y_joueur = 10
    if y_joueur > WINDOW_HEIGHT - PLAYER_HEIGHT : 
        y_joueur = WINDOW_HEIGHT - PLAYER_HEIGHT

def Obstacle_1():
    global y_obstacle, x_obstacle, WINDOW_HEIGHT, OBSTACLE_HEIGHT_1, WINDOW_WIDTH, OBSTACLE_WIDTH_1, liste_obstacles_1, obstacle_interval

    
    if obstacle_genere == 1 :
        y_obstacle = ra.randint( 10 , WINDOW_HEIGHT - OBSTACLE_HEIGHT_1 )
        x_obstacle = WINDOW_WIDTH + OBSTACLE_WIDTH_1
        liste_obstacles_1.append([x_obstacle , y_obstacle])
        obstacle_interval -= OBSTACLE_INTERVAL_DECREMENT
        if obstacle_interval <= 20 :
            obstacle_interval = 15
            
def Obstacle_2():
    global y_obstacle, x_obstacle, WINDOW_HEIGHT, OBSTACLE_HEIGHT_2, WINDOW_WIDTH, OBSTACLE_WIDTH_2, liste_obstacles_2, obstacle_interval
    
    if obstacle_genere == 2 :
        y_obstacle = ra.randint( 10 , WINDOW_HEIGHT - OBSTACLE_HEIGHT_2 )
        x_obstacle = WINDOW_WIDTH + OBSTACLE_WIDTH_2
        liste_obstacles_2.append([x_obstacle , y_obstacle])
        obstacle_interval -= OBSTACLE_INTERVAL_DECREMENT
        if obstacle_interval <= 20 :
            obstacle_interval = 15
            
def Obstacle_3():
    global y_obstacle, x_obstacle, WINDOW_HEIGHT, OBSTACLE_HEIGHT_3, WINDOW_WIDTH, OBSTACLE_WIDTH_3, liste_obstacles_3, obstacle_interval
    
    if obstacle_genere == 3 :
        y_obstacle = ra.randint( 10 , WINDOW_HEIGHT - OBSTACLE_HEIGHT_3 )
        x_obstacle = WINDOW_WIDTH + OBSTACLE_WIDTH_3
        liste_obstacles_3.append([x_obstacle , y_obstacle])
        obstacle_interval -= OBSTACLE_INTERVAL_DECREMENT
        if obstacle_interval <= 20 :
            obstacle_interval = 15
            
def Obstacle_4():
    global y_obstacle, x_obstacle, WINDOW_HEIGHT, OBSTACLE_HEIGHT_4, WINDOW_WIDTH, OBSTACLE_WIDTH_4, liste_obstacles_4, obstacle_interval
    
    if obstacle_genere == 4 :
        y_obstacle = ra.randint( 10 , WINDOW_HEIGHT - OBSTACLE_HEIGHT_4 )
        x_obstacle = WINDOW_WIDTH + OBSTACLE_WIDTH_4
        liste_obstacles_4.append([x_obstacle , y_obstacle])
        obstacle_interval -= OBSTACLE_INTERVAL_DECREMENT
        if obstacle_interval <= 20 :
            obstacle_interval = 15
            
def Bonus_obstacle():
    global y_obstacle, x_obstacle, WINDOW_HEIGHT, BONUS_HEIGHT, WINDOW_WIDTH, BONUS_WIDTH, liste_bonus, obstacle_interval

    if obstacle_genere == 5 :
        y_obstacle = ra.randint( 10 , WINDOW_HEIGHT - BONUS_HEIGHT )
        x_obstacle = WINDOW_WIDTH + BONUS_WIDTH
        type_bonus = ra.randint(0,4)

        liste_bonus.append([x_obstacle , y_obstacle, type_bonus])
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
            if bonus[2] == 0:
                nb_missiles += 5
            elif bonus[2] == 1:
                dash += 4
            elif bonus[2] == 2:
                fusee_get = True
            elif bonus[2] == 3:
                shield += 1
            else:
                tps_slow += 100
            liste_bonus.remove(bonus)
    for obstacle in liste_nid:
        obstacle_hitbox = [obstacle[0] , obstacle[1] , obstacle[0] + 3 * BONUS_WIDTH , obstacle[1] + 3 * BONUS_HEIGHT ]
        if check_hitbox_colision(joueur_hitbox, obstacle_hitbox):
            if shield > 0 :
                shield -= 1
                liste_explosion.append([obstacle[0] + (3 * BONUS_WIDTH) /2 , obstacle[1] + (3 * BONUS_HEIGHT) /2])
                liste_nid.remove(obstacle)
            else:
                vivant = False
                liste_explosion.append([obstacle[0] + (3 * BONUS_WIDTH) /2 , obstacle[1] + (3 * BONUS_HEIGHT) /2])
            break
                


def check_hitbox_colision(hitbox_1, hitbox_2):
    if (hitbox_1[0] < hitbox_2[2] and hitbox_1[2] > hitbox_2[0] and hitbox_1[1] < hitbox_2[3] and hitbox_1[3] > hitbox_2[1]):
        return True
    return False
   
def collision_obstacle_1_1():
    global liste_obstacles_1
    for obstacle_1 in liste_obstacles_1:
        for obstacle_2 in liste_obstacles_1:
            if obstacle_1 != obstacle_2:
                hitbox_obstacle_1 = [obstacle_1[0], obstacle_1[1], obstacle_1[0] + OBSTACLE_WIDTH_1, obstacle_1[1] + OBSTACLE_HEIGHT_1]
                hitbox_obstacle_2 = [obstacle_2[0], obstacle_2[1], obstacle_2[0] + OBSTACLE_WIDTH_1, obstacle_2[1] + OBSTACLE_HEIGHT_1]
                if check_hitbox_colision(hitbox_obstacle_1, hitbox_obstacle_2):
                    liste_explosion.append([ hitbox_obstacle_1[2] - OBSTACLE_WIDTH_1 / 2 , hitbox_obstacle_1[3] - OBSTACLE_HEIGHT_1 / 2 ])
                    liste_explosion.append([ hitbox_obstacle_2[2] - OBSTACLE_WIDTH_1 / 2 , hitbox_obstacle_2[3] - OBSTACLE_HEIGHT_1 / 2 ])
                    if hitbox_obstacle_1[0] - hitbox_obstacle_2[0] > 0 : # Savoir si obstacle_1 est à droite de obstacle_2
                        pos_x = hitbox_obstacle_1[0]
                    else:
                        pos_x = hitbox_obstacle_2[0]
                    pos_y = (hitbox_obstacle_1[1] + hitbox_obstacle_2[3]) / 2
                    liste_nid.append([ pos_x, pos_y ])
                    liste_obstacles_1.remove(obstacle_1)
                    liste_obstacles_1.remove(obstacle_2)
                    
def collision_obstacle_1_2():
    global liste_obstacles_1, liste_obstacles_2
    for obstacle_1 in liste_obstacles_1:
        for obstacle_2 in liste_obstacles_2:
            if obstacle_1 != obstacle_2:
                hitbox_obstacle_1 = [obstacle_1[0], obstacle_1[1], obstacle_1[0] + OBSTACLE_WIDTH_1, obstacle_1[1] + OBSTACLE_HEIGHT_1]
                hitbox_obstacle_2 = [obstacle_2[0], obstacle_2[1], obstacle_2[0] + OBSTACLE_WIDTH_2, obstacle_2[1] + OBSTACLE_HEIGHT_2]
                if check_hitbox_colision(hitbox_obstacle_1, hitbox_obstacle_2):
                    liste_explosion.append([ hitbox_obstacle_1[2] - OBSTACLE_WIDTH_1 / 2 , hitbox_obstacle_1[3] - OBSTACLE_HEIGHT_1 / 2 ])
                    liste_explosion.append([ hitbox_obstacle_2[2] - OBSTACLE_WIDTH_2 / 2 , hitbox_obstacle_2[3] - OBSTACLE_HEIGHT_2 / 2 ])
                    if hitbox_obstacle_1[0] - hitbox_obstacle_2[0] > 0 : # Savoir si obstacle_1 est à droite de obstacle_2
                        pos_x = hitbox_obstacle_1[0]
                    else:
                        pos_x = hitbox_obstacle_2[0]
                    pos_y = (hitbox_obstacle_1[1] + hitbox_obstacle_2[3]) / 2
                    liste_nid.append([ pos_x, pos_y ])
                    liste_obstacles_1.remove(obstacle_1)
                    liste_obstacles_2.remove(obstacle_2)
        
def collision_obstacle_1_3():
    global liste_obstacles_1, liste_obstacles_3
    for obstacle_1 in liste_obstacles_1:
        for obstacle_2 in liste_obstacles_3:
            if obstacle_1 != obstacle_2:
                hitbox_obstacle_1 = [obstacle_1[0], obstacle_1[1], obstacle_1[0] + OBSTACLE_WIDTH_1, obstacle_1[1] + OBSTACLE_HEIGHT_1]
                hitbox_obstacle_2 = [obstacle_2[0], obstacle_2[1], obstacle_2[0] + OBSTACLE_WIDTH_3, obstacle_2[1] + OBSTACLE_HEIGHT_3]
                if check_hitbox_colision(hitbox_obstacle_1, hitbox_obstacle_2):
                    liste_explosion.append([ hitbox_obstacle_1[2] - OBSTACLE_WIDTH_1 / 2 , hitbox_obstacle_1[3] - OBSTACLE_HEIGHT_1 / 2 ])
                    liste_explosion.append([ hitbox_obstacle_2[2] - OBSTACLE_WIDTH_3 / 2 , hitbox_obstacle_2[3] - OBSTACLE_HEIGHT_3 / 2 ])
                    if hitbox_obstacle_1[0] - hitbox_obstacle_2[0] > 0 : # Savoir si obstacle_1 est à droite de obstacle_2
                        pos_x = hitbox_obstacle_1[0]
                    else:
                        pos_x = hitbox_obstacle_2[0]
                    pos_y = (hitbox_obstacle_1[1] + hitbox_obstacle_2[3]) / 2
                    liste_nid.append([ pos_x, pos_y ])
                    liste_obstacles_1.remove(obstacle_1)
                    liste_obstacles_3.remove(obstacle_2)
    
def collision_obstacle_1_4():
    global liste_obstacles_1, liste_obstacles_4
    for obstacle_1 in liste_obstacles_1:
        for obstacle_2 in liste_obstacles_4:
            if obstacle_1 != obstacle_2:
                hitbox_obstacle_1 = [obstacle_1[0], obstacle_1[1], obstacle_1[0] + OBSTACLE_WIDTH_1, obstacle_1[1] + OBSTACLE_HEIGHT_1]
                hitbox_obstacle_2 = [obstacle_2[0], obstacle_2[1], obstacle_2[0] + OBSTACLE_WIDTH_4, obstacle_2[1] + OBSTACLE_HEIGHT_4]
                if check_hitbox_colision(hitbox_obstacle_1, hitbox_obstacle_2):
                    liste_explosion.append([ hitbox_obstacle_1[2] - OBSTACLE_WIDTH_1 / 2 , hitbox_obstacle_1[3] - OBSTACLE_HEIGHT_1 / 2 ])
                    liste_explosion.append([ hitbox_obstacle_2[2] - OBSTACLE_WIDTH_4 / 2 , hitbox_obstacle_2[3] - OBSTACLE_HEIGHT_4 / 2 ])
                    if hitbox_obstacle_1[0] - hitbox_obstacle_2[0] > 0 : # Savoir si obstacle_1 est à droite de obstacle_2
                        pos_x = hitbox_obstacle_1[0]
                    else:
                        pos_x = hitbox_obstacle_2[0]
                    pos_y = (hitbox_obstacle_1[1] + hitbox_obstacle_2[3]) / 2
                    liste_nid.append([ pos_x, pos_y ])
                    liste_obstacles_1.remove(obstacle_1)
                    liste_obstacles_4.remove(obstacle_2)
                    
def collision_obstacle_1_nid():
    global liste_obstacles_1, liste_nid
    for obstacle_1 in liste_obstacles_1:
        for obstacle_2 in liste_nid:
            if obstacle_1 != obstacle_2:
                hitbox_obstacle_1 = [obstacle_2[0], obstacle_2[1], obstacle_2[0] + OBSTACLE_WIDTH_1, obstacle_2[1] + OBSTACLE_HEIGHT_1]
                hitbox_obstacle_2 = [obstacle_1[0], obstacle_1[1], obstacle_1[0] + 2 * BONUS_WIDTH, obstacle_1[1] + 2 * BONUS_HEIGHT]
                if check_hitbox_colision(hitbox_obstacle_1, hitbox_obstacle_2):
                    liste_explosion.append([ hitbox_obstacle_1[2] - OBSTACLE_WIDTH_1 / 2 , hitbox_obstacle_1[3] - OBSTACLE_HEIGHT_1 / 2 ])

                    liste_obstacles_1.remove(obstacle_1)
    
def collision_obstacle_1():
    collision_obstacle_1_1()
    collision_obstacle_1_2()
    collision_obstacle_1_3()
    collision_obstacle_1_4()
    collision_obstacle_1_nid()
    
def collision_obstacle_2_2():
    global liste_obstacles_2
    for obstacle_1 in liste_obstacles_2:
        for obstacle_2 in liste_obstacles_2:
            if obstacle_1 != obstacle_2:
                hitbox_obstacle_1 = [obstacle_1[0], obstacle_1[1], obstacle_1[0] + OBSTACLE_WIDTH_2, obstacle_1[1] + OBSTACLE_HEIGHT_2]
                hitbox_obstacle_2 = [obstacle_2[0], obstacle_2[1], obstacle_2[0] + OBSTACLE_WIDTH_2, obstacle_2[1] + OBSTACLE_HEIGHT_2]
                if check_hitbox_colision(hitbox_obstacle_1, hitbox_obstacle_2):
                    liste_explosion.append([ hitbox_obstacle_1[2] - OBSTACLE_WIDTH_2 / 2 , hitbox_obstacle_1[3] - OBSTACLE_HEIGHT_2 / 2 ])
                    liste_explosion.append([ hitbox_obstacle_2[2] - OBSTACLE_WIDTH_2 / 2 , hitbox_obstacle_2[3] - OBSTACLE_HEIGHT_2 / 2 ])
                    if hitbox_obstacle_1[0] - hitbox_obstacle_2[0] > 0 : # Savoir si obstacle_1 est à droite de obstacle_2
                        pos_x = hitbox_obstacle_1[0]
                    else:
                        pos_x = hitbox_obstacle_2[0]
                    pos_y = (hitbox_obstacle_1[1] + hitbox_obstacle_2[3]) / 2
                    liste_nid.append([ pos_x, pos_y ])
                    liste_obstacles_2.remove(obstacle_2)
                    liste_obstacles_2.remove(obstacle_2)

def collision_obstacle_2_3():
    global liste_obstacles_2, liste_obstacles_3
    for obstacle_1 in liste_obstacles_2:
        for obstacle_2 in liste_obstacles_3:
            if obstacle_1 != obstacle_2:
                hitbox_obstacle_1 = [obstacle_1[0], obstacle_1[1], obstacle_1[0] + OBSTACLE_WIDTH_2, obstacle_1[1] + OBSTACLE_HEIGHT_2]
                hitbox_obstacle_2 = [obstacle_2[0], obstacle_2[1], obstacle_2[0] + OBSTACLE_WIDTH_3, obstacle_2[1] + OBSTACLE_HEIGHT_3]
                if check_hitbox_colision(hitbox_obstacle_1, hitbox_obstacle_2):
                    liste_explosion.append([ hitbox_obstacle_1[2] - OBSTACLE_WIDTH_2 / 2 , hitbox_obstacle_1[3] - OBSTACLE_HEIGHT_2 / 2 ])
                    liste_explosion.append([ hitbox_obstacle_2[2] - OBSTACLE_WIDTH_3 / 2 , hitbox_obstacle_2[3] - OBSTACLE_HEIGHT_3 / 2 ])
                    if hitbox_obstacle_1[0] - hitbox_obstacle_2[0] > 0 : # Savoir si obstacle_1 est à droite de obstacle_2
                        pos_x = hitbox_obstacle_1[0]
                    else:
                        pos_x = hitbox_obstacle_2[0]
                    pos_y = (hitbox_obstacle_1[1] + hitbox_obstacle_2[3]) / 2
                    liste_nid.append([ pos_x, pos_y ])
                    liste_obstacles_2.remove(obstacle_1)
                    liste_obstacles_3.remove(obstacle_2)
    
def collision_obstacle_2_4():
    global liste_obstacles_2, liste_obstacles_4
    for obstacle_1 in liste_obstacles_2:
        for obstacle_2 in liste_obstacles_4:
            if obstacle_1 != obstacle_2:
                hitbox_obstacle_1 = [obstacle_1[0], obstacle_1[1], obstacle_1[0] + OBSTACLE_WIDTH_2, obstacle_1[1] + OBSTACLE_HEIGHT_2]
                hitbox_obstacle_2 = [obstacle_2[0], obstacle_2[1], obstacle_2[0] + OBSTACLE_WIDTH_4, obstacle_2[1] + OBSTACLE_HEIGHT_4]
                if check_hitbox_colision(hitbox_obstacle_1, hitbox_obstacle_2):
                    liste_explosion.append([ hitbox_obstacle_1[2] - OBSTACLE_WIDTH_2 / 2 , hitbox_obstacle_1[3] - OBSTACLE_HEIGHT_2 / 2 ])
                    liste_explosion.append([ hitbox_obstacle_2[2] - OBSTACLE_WIDTH_4 / 2 , hitbox_obstacle_2[3] - OBSTACLE_HEIGHT_4 / 2 ])
                    if hitbox_obstacle_1[0] - hitbox_obstacle_2[0] > 0 : # Savoir si obstacle_1 est à droite de obstacle_2
                        pos_x = hitbox_obstacle_1[0]
                    else:
                        pos_x = hitbox_obstacle_2[0]
                    pos_y = (hitbox_obstacle_1[1] + hitbox_obstacle_2[3]) / 2
                    liste_nid.append([ pos_x, pos_y ])
                    liste_obstacles_2.remove(obstacle_1)
                    liste_obstacles_4.remove(obstacle_2)
                    
def collision_obstacle_2_nid():
    global liste_obstacles_2, liste_nid
    for obstacle_1 in liste_obstacles_2:
        for obstacle_2 in liste_nid:
            if obstacle_1 != obstacle_2:
                hitbox_obstacle_1 = [obstacle_2[0], obstacle_2[1], obstacle_2[0] + OBSTACLE_WIDTH_2, obstacle_2[1] + OBSTACLE_HEIGHT_2]
                hitbox_obstacle_2 = [obstacle_1[0], obstacle_1[1], obstacle_1[0] + 2 * BONUS_WIDTH, obstacle_1[1] + 2 * BONUS_HEIGHT]
                if check_hitbox_colision(hitbox_obstacle_1, hitbox_obstacle_2):
                    liste_explosion.append([ hitbox_obstacle_1[2] - OBSTACLE_WIDTH_2 / 2 , hitbox_obstacle_1[3] - OBSTACLE_HEIGHT_2 / 2 ])

                    liste_obstacles_2.remove(obstacle_1)
    
def collision_obstacle_2():
    collision_obstacle_2_2()
    collision_obstacle_2_3()
    collision_obstacle_2_4()
    collision_obstacle_2_nid()
    
def collision_obstacle_3_3():
    global liste_obstacles_3
    for obstacle_1 in liste_obstacles_3:
        for obstacle_2 in liste_obstacles_3:
            if obstacle_1 != obstacle_2:
                hitbox_obstacle_1 = [obstacle_1[0], obstacle_1[1], obstacle_1[0] + OBSTACLE_WIDTH_3, obstacle_1[1] + OBSTACLE_HEIGHT_3]
                hitbox_obstacle_2 = [obstacle_2[0], obstacle_2[1], obstacle_2[0] + OBSTACLE_WIDTH_3, obstacle_2[1] + OBSTACLE_HEIGHT_3]
                if check_hitbox_colision(hitbox_obstacle_1, hitbox_obstacle_2):
                    liste_explosion.append([ hitbox_obstacle_1[2] - OBSTACLE_WIDTH_3 / 2 , hitbox_obstacle_1[3] - OBSTACLE_HEIGHT_3 / 2 ])
                    liste_explosion.append([ hitbox_obstacle_2[2] - OBSTACLE_WIDTH_3 / 2 , hitbox_obstacle_2[3] - OBSTACLE_HEIGHT_3 / 2 ])
                    if hitbox_obstacle_1[0] - hitbox_obstacle_2[0] > 0 : # Savoir si obstacle_1 est à droite de obstacle_2
                        pos_x = hitbox_obstacle_1[0]
                    else:
                        pos_x = hitbox_obstacle_2[0]
                    pos_y = (hitbox_obstacle_1[1] + hitbox_obstacle_2[3]) / 2
                    liste_nid.append([ pos_x, pos_y ])
                    liste_obstacles_3.remove(obstacle_1)
                    liste_obstacles_3.remove(obstacle_2)
    
def collision_obstacle_3_4():
    global liste_obstacles_3, liste_obstacles_4
    for obstacle_1 in liste_obstacles_3:
        for obstacle_2 in liste_obstacles_4:
            if obstacle_1 != obstacle_2:
                hitbox_obstacle_1 = [obstacle_1[0], obstacle_1[1], obstacle_1[0] + OBSTACLE_WIDTH_3, obstacle_1[1] + OBSTACLE_HEIGHT_3]
                hitbox_obstacle_2 = [obstacle_2[0], obstacle_2[1], obstacle_2[0] + OBSTACLE_WIDTH_4, obstacle_2[1] + OBSTACLE_HEIGHT_4]
                if check_hitbox_colision(hitbox_obstacle_1, hitbox_obstacle_2):
                    liste_explosion.append([ hitbox_obstacle_1[2] - OBSTACLE_WIDTH_3 / 2 , hitbox_obstacle_1[3] - OBSTACLE_HEIGHT_3 / 2 ])
                    liste_explosion.append([ hitbox_obstacle_2[2] - OBSTACLE_WIDTH_4 / 2 , hitbox_obstacle_2[3] - OBSTACLE_HEIGHT_4 / 2 ])
                    if hitbox_obstacle_1[0] - hitbox_obstacle_2[0] > 0 : # Savoir si obstacle_1 est à droite de obstacle_2
                        pos_x = hitbox_obstacle_1[0]
                    else:
                        pos_x = hitbox_obstacle_2[0]
                    pos_y = (hitbox_obstacle_1[1] + hitbox_obstacle_2[3]) / 2
                    liste_nid.append([ pos_x, pos_y ])
                    liste_obstacles_3.remove(obstacle_1)
                    liste_obstacles_4.remove(obstacle_2)
    
def collision_obstacle_3_nid():
    global liste_obstacles_3, liste_nid
    for obstacle_1 in liste_obstacles_3:
        for obstacle_2 in liste_nid:
            if obstacle_1 != obstacle_2:
                hitbox_obstacle_1 = [obstacle_2[0], obstacle_2[1], obstacle_2[0] + OBSTACLE_WIDTH_3, obstacle_2[1] + OBSTACLE_HEIGHT_3]
                hitbox_obstacle_2 = [obstacle_1[0], obstacle_1[1], obstacle_1[0] + 2 * BONUS_WIDTH, obstacle_1[1] + 2 * BONUS_HEIGHT]
                if check_hitbox_colision(hitbox_obstacle_1, hitbox_obstacle_2):
                    liste_explosion.append([ hitbox_obstacle_1[2] - OBSTACLE_WIDTH_3 / 2 , hitbox_obstacle_1[3] - OBSTACLE_HEIGHT_3 / 2 ])

                    liste_obstacles_3.remove(obstacle_1)    
    
def collision_obstacle_3():
    collision_obstacle_3_3()
    collision_obstacle_3_4()
    collision_obstacle_3_nid()
    
def collision_obstacle_4_4():
    global liste_obstacles_4
    for obstacle_1 in liste_obstacles_4:
        for obstacle_2 in liste_obstacles_4:
            if obstacle_1 != obstacle_2:
                hitbox_obstacle_1 = [obstacle_1[0], obstacle_1[1], obstacle_1[0] + OBSTACLE_WIDTH_4, obstacle_1[1] + OBSTACLE_HEIGHT_4]
                hitbox_obstacle_2 = [obstacle_2[0], obstacle_2[1], obstacle_2[0] + OBSTACLE_WIDTH_4, obstacle_2[1] + OBSTACLE_HEIGHT_4]
                if check_hitbox_colision(hitbox_obstacle_1, hitbox_obstacle_2):
                    liste_explosion.append([ hitbox_obstacle_1[2] - OBSTACLE_WIDTH_4 / 2 , hitbox_obstacle_1[3] - OBSTACLE_HEIGHT_4 / 2 ])
                    liste_explosion.append([ hitbox_obstacle_2[2] - OBSTACLE_WIDTH_4 / 2 , hitbox_obstacle_2[3] - OBSTACLE_HEIGHT_4 / 2 ])
                    if hitbox_obstacle_1[0] - hitbox_obstacle_2[0] > 0 : # Savoir si obstacle_1 est à droite de obstacle_2
                        pos_x = hitbox_obstacle_1[0]
                    else:
                        pos_x = hitbox_obstacle_2[0]
                    pos_y = (hitbox_obstacle_1[1] + hitbox_obstacle_2[3]) / 2
                    liste_nid.append([ pos_x, pos_y ])
                    liste_obstacles_4.remove(obstacle_1)
                    liste_obstacles_4.remove(obstacle_2)

def collision_obstacle_4_nid():
    global liste_obstacles_4, liste_nid
    for obstacle_1 in liste_obstacles_4:
        for obstacle_2 in liste_nid:
            if obstacle_1 != obstacle_2:
                hitbox_obstacle_1 = [obstacle_2[0], obstacle_2[1], obstacle_2[0] + OBSTACLE_WIDTH_4, obstacle_2[1] + OBSTACLE_HEIGHT_4]
                hitbox_obstacle_2 = [obstacle_1[0], obstacle_1[1], obstacle_1[0] + 2 * BONUS_WIDTH, obstacle_1[1] + 2 * BONUS_HEIGHT]
                if check_hitbox_colision(hitbox_obstacle_1, hitbox_obstacle_2):
                    liste_explosion.append([ hitbox_obstacle_1[2] - OBSTACLE_WIDTH_4 / 2 , hitbox_obstacle_1[3] - OBSTACLE_HEIGHT_4 / 2 ])

                    liste_obstacles_4.remove(obstacle_1)
    
def collision_obstacle_4():
    collision_obstacle_4_4()
    collision_obstacle_4_nid()
   
def collision_entre_obstacles():
    collision_obstacle_1()
    collision_obstacle_2()
    collision_obstacle_3()
    collision_obstacle_4()

   
def nid_de_poule():
    global liste_nid, score
    for nid in liste_nid : 
        nid[0] -= vitesse_de_deplacement_ennemi
        if nid[0] <=  - BONUS_WIDTH :
            liste_nid.remove(nid)
            score += 350
    
    
def random_obstacles():
    global obstacle_genere
    proba_type_obstacle_1 = [1 for n in range(max_1)] 
    proba_type_obstacle_2 = [2 for n in range(min_2)] 
    proba_type_obstacle_3 = [3 for n in range(min_3)]
    proba_type_obstacle_4 = [4 for n in range(min_4)]
    proba_type_bonus = [5 for n in range(proba_bonus)]

    liste_proba_type_obstacle = proba_type_obstacle_1 + proba_type_obstacle_2 + proba_type_obstacle_3 + proba_type_obstacle_4 + proba_type_bonus
    
    indice_obstacle_genere = ra.randint(0 , len(liste_proba_type_obstacle) - 1)
    obstacle_genere = liste_proba_type_obstacle[indice_obstacle_genere]

def change_proba():
    global max_1, min_2, min_3, min_4, min_1, proba_bonus, decrease_1, increase_2, increase_3, increase_4
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
        proba_bonus = 6
        
    elif max_1 > min_1 and score !=0 : # type: ignore
            max_1 -= decrease_1 # type: ignore
            min_2 += increase_2 # type: ignore
            min_3 += increase_3 # type: ignore
            min_4 += increase_4 # type: ignore
        
def explosion():
    global rayon_explosion
    for explosion in liste_explosion :
        if rayon_explosion <= rayon_max :
            rayon_explosion += 5
            py.circ(explosion[0], explosion[1], rayon_explosion, 10)

        else:
            liste_explosion.remove(explosion)
            rayon_explosion = 0
            
def lancer_missiles():
    global nb_missiles
    if py.btnp(py.KEY_SPACE) or py.btnp(py.KEY_E) and nb_missiles > 0:
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
    if py.frame_count % obstacle_interval == 0 :
        random_obstacles()
        Obstacle_1()
        Obstacle_2()
        Obstacle_3()
        Obstacle_4()
        Bonus_obstacle()

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
    
    if (tps_slow > 0 and py.btn(py.KEY_R)) or (tps_slow > 0 and py.btn(py.KEY_COLON )): #type: ignore

        vitesse_de_deplacement_ennemi = 4
        if py.frame_count % 3 == 0:
            tps_slow -= 1
        
    else :
        vitesse_de_deplacement_ennemi = 5

def fusee_pouvoir():
    global fusee, mode_onde, fusee_get
    
    if (fusee_get and py.btnp(py.KEY_EXCLAIM)) or (fusee_get and py.btnp(py.KEY_A)):
        fusee = True
        mode_onde = True
        fusee_get = False

    
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
                x_joueur += 3.5
                score += 23 * SCORE_ADD
            elif tps_fusee >= 100 and tps_fusee < 110 :
                x_joueur += 3
                score += 22 * SCORE_ADD
            elif tps_fusee >= 110 and tps_fusee < 120 :
                x_joueur += 2.5
                score += 21 * SCORE_ADD
            elif tps_fusee >= 120 and tps_fusee < 130:
                x_joueur += 2
                score += 20 * SCORE_ADD
            elif tps_fusee >= 130 and tps_fusee < 140 :
                x_joueur += 1.5
                score += 19 * SCORE_ADD
            elif tps_fusee >= 140 and tps_fusee < 150 :
                x_joueur += 1
                score += 18 * SCORE_ADD
            elif tps_fusee >= 150 and tps_fusee < 160 :
                x_joueur += 0.5
                score += 17 * SCORE_ADD
            elif tps_fusee >= 160 and tps_fusee < 170 :
                x_joueur += 0
                score += 16 * SCORE_ADD
            elif tps_fusee >= 170 and tps_fusee < 180 :
                x_joueur -= 0
                score += 15 * SCORE_ADD
            elif tps_fusee >= 180 and tps_fusee < 190 :
                x_joueur -= 0.5
                score += 14 * SCORE_ADD
            elif tps_fusee >= 190 and tps_fusee < 200 :
                x_joueur -= 1
                score += 13 * SCORE_ADD
            elif tps_fusee >= 200 and tps_fusee < 210 :
                x_joueur -= 1.5
                score += 12 * SCORE_ADD
            elif tps_fusee >= 210 and tps_fusee < 220 :
                x_joueur -= 2
                score += 11 * SCORE_ADD
            elif tps_fusee >= 220 and tps_fusee < 230 :
                x_joueur -= 2.5
                score += 10 * SCORE_ADD
            elif tps_fusee >= 230 and tps_fusee < 240 :
                x_joueur -= 3
                score += 9 * SCORE_ADD
            elif tps_fusee >= 240 and tps_fusee < 310 :
                x_joueur -= 3.5
                score += 8 * SCORE_ADD
            elif tps_fusee >= 310 and tps_fusee < 320 :
                x_joueur -= 3
                score += 7 * SCORE_ADD
            elif tps_fusee >= 320 and tps_fusee < 330 :
                x_joueur -= 2.5
                score += 6 * SCORE_ADD
            elif tps_fusee >= 330 and tps_fusee < 340:
                x_joueur -= 2
                score += 5 * SCORE_ADD
            elif tps_fusee >= 340 and tps_fusee < 350 :
                x_joueur -= 1.5
                score += 4 * SCORE_ADD
            elif tps_fusee >= 350 and tps_fusee < 360 :
                x_joueur -= 1
                score += 3 * SCORE_ADD
            elif tps_fusee >= 360 and tps_fusee < 370 :
                x_joueur -= 0.5
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
            calibrage = True
    
def onde():
    global rayon_onde, fusee_ready
    for onde in liste_onde :
        if rayon_onde <= WINDOW_WIDTH :
            fusee_ready = False
            rayon_onde += 15
            py.circ(onde[0] + PLAYER_WIDTH/2, onde[1] + PLAYER_HEIGHT/2, rayon_onde, 12)
            py.circ(onde[0] + PLAYER_WIDTH/2, onde[1] + PLAYER_HEIGHT/2, rayon_onde - 30, 0)
        else:
            liste_onde.remove(onde)
            rayon_onde = 0
            fusee_ready = True    

def dash_pouvoir():
    global dash, y_joueur, x_joueur
    
    if dash > 0 :  # Voir en_decal.py pour l'autre type d'activation du dash. Il suffit d'inverser les btnp et les btn de cette fonction.
        if py.btnp(py.KEY_SHIFT, 100, 0) : # Pour utilise le dash il faut d'abord appuyer sur les flèches puis sur shift. #type: ignore
            if py.btn(py.KEY_UP) or py.btn(py.KEY_Z) : 
                y_joueur -= 50
                dash -= 1
                
                if y_joueur <= 0 :
                    y_joueur = 0
                    dash += 1
                    
            elif py.btn(py.KEY_DOWN) or py.btn(py.KEY_S) :
                y_joueur += 50
                dash -= 1

                if y_joueur >= WINDOW_HEIGHT - PLAYER_HEIGHT :
                    y_joueur = WINDOW_HEIGHT - PLAYER_HEIGHT
                    dash += 1
                    
            elif py.btn(py.KEY_RIGHT) or py.btn(py.KEY_D) :
                x_joueur += 150
                dash -= 1
                
                if x_joueur > WINDOW_WIDTH - 3 * PLAYER_WIDTH :
                    x_joueur = WINDOW_WIDTH - 3 * PLAYER_WIDTH
                    dash += 1
                    
            elif py.btn(py.KEY_LEFT) or py.btn(py.KEY_Q) :
                x_joueur -= 150
                dash -= 1
                
                if x_joueur < 0 + PLAYER_WIDTH :
                    x_joueur = 0 + PLAYER_WIDTH
                    dash += 1
                
def deplacement_bonus():
    for bonus in liste_bonus : 
        bonus[0] -= 1.25 * vitesse_de_deplacement_ennemi
        if bonus[0] < -BONUS_WIDTH :
            liste_bonus.remove(bonus)               


def pouvoirs():
    missiles_pouvoir()
    slow_pouvoir()
    fusee_pouvoir()
    dash_pouvoir()

def Jeu():
    global score, fusee_ready, vitesse_de_deplacement_ennemi

    if fusee_ready:
        fusee_ready_mode()
    
    else:
        if score % 500 == 0 : 
            change_proba()
            if tps_slow > 0:
                vitesse_de_deplacement_ennemi += 0.2
            else:
                vitesse_de_deplacement_ennemi += 0.1
            if vitesse_de_deplacement_ennemi > 15 :
                vitesse_de_deplacement_ennemi = 15
        joueur()
        obstacles()
        deplacement_obstacles()

        deplacement_bonus()
        pouvoirs()
        collision_entre_obstacles()
        nid_de_poule()

        if py.frame_count % 2 == 0 :
            score += SCORE_ADD

def Fin():
    global SCORE_COLOR
    
    SCORE_COLOR += 1
    
    if SCORE_COLOR == 15 :
        SCORE_COLOR = 0
        
    py.text(WINDOW_WIDTH // 2 - 20, WINDOW_HEIGHT // 2, "Game Over", SCORE_COLOR)
    py.text(WINDOW_WIDTH // 2 - 20, WINDOW_HEIGHT // 2 + 20 , "Final score: {}".format(score), SCORE_COLOR)
    
    if score > high_score :
        save_high_score(score)
        py.text(WINDOW_WIDTH // 2 - 20, WINDOW_HEIGHT // 2 + 40 , "You broke your record !", SCORE_COLOR)
        py.text(WINDOW_WIDTH // 2 - 20, WINDOW_HEIGHT // 2 + 50 , "GG", SCORE_COLOR)
    
    if py.frame_count % 30 > 20:
        col = 0
    else:
        col=7

    py.text(WINDOW_WIDTH // 2, WINDOW_HEIGHT - 70, "Press R to restart and M to go to the menu", col)

def draw_jeu():
    global SCORE_COLOR, mode_onde, tps_slow
    
    if fusee:
        onde()
        for bonus in liste_bonus:
            liste_bonus.remove(bonus)
        for obstacle in liste_obstacles_1:
            liste_obstacles_1.remove(obstacle)
        for obstacle in liste_obstacles_2:
            liste_obstacles_2.remove(obstacle)
        for obstacle in liste_obstacles_3:
            liste_obstacles_3.remove(obstacle)
        for obstacle in liste_obstacles_4:
            liste_obstacles_4.remove(obstacle)
        for missile in liste_missiles:
            liste_missiles.remove(missile)
        for nid in liste_nid :
            liste_nid.remove(nid)
        if mode_onde :
            liste_onde.append([x_joueur, y_joueur])
            mode_onde = False
        elif fusee_ready == False:
            py.rect(x_joueur, y_joueur, PLAYER_WIDTH, PLAYER_HEIGHT, 7)
        else:
            py.blt (x_joueur , y_joueur, 0 , 175 , 40 , 75, 24, 11)
 
        
    else:
        py.blt( x_joueur , y_joueur +1, 0 , 0 , 0 , 75 , PLAYER_HEIGHT, 0)
    
    for obstacle in liste_obstacles_1 :
        py.blt(obstacle[0] , obstacle[1], 0 , 75, 0, OBSTACLE_WIDTH_1 , OBSTACLE_HEIGHT_1)
    for obstacle in liste_obstacles_2 :
        py.blt(obstacle[0] , obstacle[1], 0 , 0 , 26 , OBSTACLE_WIDTH_2, OBSTACLE_HEIGHT_2)
    for obstacle in liste_obstacles_3 :
        py.blt(obstacle[0] , obstacle[1], 0 , 125 , 0 , OBSTACLE_WIDTH_3, OBSTACLE_HEIGHT_3)
    for obstacle in liste_obstacles_4 :
        if py.frame_count % 30 < 15 :
            py.blt(obstacle[0] , obstacle[1], 0 , 175 , 0 , OBSTACLE_WIDTH_4, OBSTACLE_HEIGHT_4)

    for bonus in liste_bonus :
        if bonus[2] == 0:
            py.blt(bonus[0], bonus[1], 0 , 0 , 51, 25 , 25)
        elif bonus[2] == 1:
            py.blt(bonus[0], bonus[1], 0 , 25 , 51, 25 , 25)
        elif bonus[2] == 2:
            py.blt(bonus[0], bonus[1], 0 , 50 , 51, 25 , 25)
        elif bonus[2] == 3:
            py.blt(bonus[0], bonus[1], 0 , 75 , 51, 25 , 25)
        else:
            py.blt(bonus[0], bonus[1], 0 , 100 , 51, 25 , 25)
    for nid in liste_nid : 
        py.rect(nid[0], nid[1], 2 * BONUS_WIDTH, 2 * BONUS_HEIGHT, 8)
    for missile in liste_missiles :
        py.rect(missile[0], missile[1], missile_width, missile_height, 10)
    
    explosion()
    
    py.text(4,4,"Score: {}".format(score), SCORE_COLOR)
    py.text(100,4,"DASH: {}".format(dash), SCORE_COLOR)
    py.text(175,4,"SLOW: {}".format(tps_slow), SCORE_COLOR)
    py.text(250,4,"MISSILES: {}".format(nb_missiles), SCORE_COLOR)
    py.text(325,4,"SHIELD: {}".format(shield), SCORE_COLOR)
    if fusee_get :
        py.text(400,4,"ROCKET: ON", SCORE_COLOR)
    else:
        py.text(400,4,"ROCKET: OFF", SCORE_COLOR)
        
    py.text(500,4,"HIGH SCORE: {}".format(high_score), SCORE_COLOR)
    
def recommencer():
    global menu_active, show_settings, affichage_debut, x_joueur, y_joueur, vivant, game_over, liste_obstacles_1, liste_obstacles_2, liste_obstacles_3, liste_obstacles_4, liste_bonus, obstacle_interval, score, obstacle_genere, vitesse_de_deplacement_ennemi, dash, fusee, tps_fusee, rayon_onde, liste_onde, mode_onde, fusee_ready, fusee_get, calibrage, liste_missiles, liste_explosion, rayon_explosion, rayon_max, tps_slow, missile_width, missile_height, nb_missiles, shield, liste_nid, high_score, SCORE_COLOR
    
    menu_active = False
    show_settings = False
    affichage_debut = False
    x_joueur = 0 + PLAYER_WIDTH
    y_joueur = WINDOW_HEIGHT // 2
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
    vitesse_de_deplacement_ennemi = 5
    dash = 0
    fusee = False
    tps_fusee = 0
    rayon_onde = 0
    liste_onde = []
    mode_onde = False
    fusee_ready = False
    fusee_get = False
    calibrage = True
    liste_missiles = []
    liste_explosion = []
    rayon_explosion = 0
    rayon_max = 25
    tps_slow = 0
    missile_width = 15
    missile_height = 5
    nb_missiles = 0
    shield = 0
    liste_nid = []
    high_score = load_high_score()
    SCORE_COLOR = 7
    
def retour_au_menu():
    global menu_active, show_settings, affichage_debut, x_joueur, y_joueur, vivant, game_over, liste_obstacles_1, liste_obstacles_2, liste_obstacles_3, liste_obstacles_4, liste_bonus, obstacle_interval, score, obstacle_genere, vitesse_de_deplacement_ennemi, dash, fusee, tps_fusee, rayon_onde, liste_onde, mode_onde, fusee_ready, fusee_get, calibrage, liste_missiles, liste_explosion, rayon_explosion, rayon_max, tps_slow, missile_width, missile_height, nb_missiles, shield, liste_nid, high_score, SCORE_COLOR
    
    menu_active = True
    show_settings = False
    affichage_debut = False
    x_joueur = 0 + PLAYER_WIDTH
    y_joueur = WINDOW_HEIGHT // 2
    vivant = False
    game_over = False
    liste_obstacles_1 =[]
    liste_obstacles_2 =[]
    liste_obstacles_3 =[]
    liste_obstacles_4 =[]
    liste_bonus = []
    obstacle_interval = INITIAL_OBSTACLE_INTERVAL
    score = 0
    obstacle_genere = 0
    vitesse_de_deplacement_ennemi = 5
    dash = 0
    fusee = False
    tps_fusee = 0
    rayon_onde = 0
    liste_onde = []
    mode_onde = False
    fusee_ready = False
    fusee_get = False
    calibrage = True
    liste_missiles = []
    liste_explosion = []
    rayon_explosion = 0
    rayon_max = 25
    tps_slow = 0
    missile_width = 15
    missile_height = 5
    nb_missiles = 0
    shield = 0
    liste_nid = []
    high_score = load_high_score()
    SCORE_COLOR = 7

def update():
    global vivant
    if menu_active:
        update_menu()
        py.mouse(True)
    elif show_settings:
        update_settings()
        py.mouse(True)
    elif vivant :
        Jeu()
    else:
        if py.btn(py.KEY_R):
            recommencer() 
        elif py.btn(py.KEY_M):
            retour_au_menu() 
    
def draw():
    global affichage_debut, menu_active
    py.cls(BACKGROUND_COLOR)
    
    if affichage_debut:
        affichage_debut_jeu()
        if py.btnp(py.KEY_RETURN) :
            affichage_debut = False
            menu_active = True
    elif menu_active:
        draw_menu()
    elif show_settings:
        draw_settings()
    elif vivant :
        py.mouse(False)
        draw_jeu()   
    else:
        explosion()
        Fin()

py.run(update,draw)