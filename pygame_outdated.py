import pygame
import random
import sys

# Initialisation de Pygame
pygame.init()

# Définition des variables globales
WIDTH, HEIGHT = 800, 600 # Valeur de la taille (hauteur, largeur) de la fenêtre
PLAYER_SIZE = 50 # Taille du joueur
PLAYER_COLOR = (255, 0, 0) # Couleur du joueur en RVB
BACKGROUND_COLOR = (0, 0, 0) # Couleur du fond du jeu
SCORE_COLOR = (255, 255, 255) # Couleur du score
OBSTACLE_WIDTH = 50 # Largeur des blocs ennemis
OBSTACLE_HEIGHT = 50 # Longueur des blocs ennemis
OBSTACLE_COLOR = (0, 255, 0) # Couleur des blocs ennemis
ACCELERATION = 0.001 # Vitesse d'apparition des blocs ennemis ~~
INITIAL_SPEED = 5 # Vitesse ~~
FONT_SIZE = 30 # Taille de l'écriture

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

# Chargement de la musique de fond
# def load_background_music():
    # pygame.mixer.music.load("666.mp4") # Insertion de la musique en arrière-plan
    # pygame.mixer.music.play(-1)  # Joue en boucle infinie

# /!\Il faut mettre la musique et ce fichier dans le même dossier sinon la musique ne fonctionnera pas et le code aussi


# Création de la fenêtre de jeu
window = pygame.display.set_mode((WIDTH, HEIGHT)) # Paramètre de la fenêtre avec la largeur et la hauteur défini
pygame.display.set_caption("Rouler à minuit") # Paramètre du nom

# Classe pour représenter le joueur
class Player:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT - 2 * PLAYER_SIZE
        self.width = PLAYER_SIZE
        self.height = PLAYER_SIZE
        self.score = 0
        self.velocity = INITIAL_SPEED

    def draw(self):
        pygame.draw.rect(window, PLAYER_COLOR, (self.x, self.y, self.width, self.height))

    def update_score(self):
        self.score += 1

# Classe pour représenter les obstacles
class Obstacle:
    def __init__(self):
        self.x = random.randint(0, WIDTH - OBSTACLE_WIDTH)
        self.y = -OBSTACLE_HEIGHT
        self.width = OBSTACLE_WIDTH
        self.height = OBSTACLE_HEIGHT

    def draw(self):
        pygame.draw.rect(window, OBSTACLE_COLOR, (self.x, self.y, self.width, self.height))

    def move(self, speed):
        self.y += speed

# Fonction pour détecter les collisions entre le joueur et les obstacles
def collision(player, obstacle):
    if (player.x < obstacle.x + obstacle.width and # Verification du côté gauche du joueur
        player.x + player.width > obstacle.x and # Verification du côté droit du joueur
        player.y < obstacle.y + obstacle.height and # Verification du côté haut du joueur
        player.y + player.height > obstacle.y): # Verification du côté bas du joueur
        return True # Continue à jouer
    return False # Arrête le jeu

# Fonction principale du jeu
def main():
    def draw_buttons():

        # Afficher le texte des boutons
        font = pygame.font.SysFont('None', FONT_SIZE)
        

    running = True
    player = Player()
    obstacles = []
    clock = pygame.time.Clock()
    high_score = load_high_score()

    # Chargement de la musique de fond
    # load_background_music()

    while running:
        window.fill(BACKGROUND_COLOR)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Touche R pour rejouer
                    return main()  # Redémarrer le jeu
            if event.type == pygame.MOUSEBUTTONDOWN:
                if quit_button.collidepoint(event.pos) :
                    pygame.quit()
                    sys.exit()
                elif replay_button.collidepoint(event.pos):
                    return main()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.x -= player.velocity #type:ignore
        if keys[pygame.K_RIGHT]:
            player.x += player.velocity #type:ignore

        player.draw()

        # Génération d'obstacles
        if random.randint(0, 100) < 5:
            obstacles.append(Obstacle())

        # Mise à jour et affichage des obstacles
        for obstacle in obstacles:
            obstacle.draw()
            obstacle.move(player.velocity)
            if collision(player, obstacle):
                running = False
            if obstacle.y > HEIGHT: # Condition si un bloc ennemi passe en dessous de la fenêtre
                player.update_score() # Ajout de 1 pour le score 
                obstacles.remove(obstacle) # Destruction du bloc ennemi

        # Augmentation de la vitesse avec le temps
        player.velocity += ACCELERATION  # type:ignore

        # Affichage du score
        font = pygame.font.SysFont('None', FONT_SIZE)
        score_text = font.render("Score: " + str(player.score), True, SCORE_COLOR)
        window.blit(score_text, (10, 10))

        # Affichage du score record
        high_score_text = font.render("High Score: " + str(high_score), True, SCORE_COLOR)
        window.blit(high_score_text, (10, 10 + FONT_SIZE))

        # Définir les coordonnées des boutons
        quit_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2, 200, 50)
        replay_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 100, 200, 50)
        draw_buttons()

        pygame.display.update() # Rafraîchissement de la page
        clock.tick(60) # Valeur du rafrâichissement + c'est haut + le jeu est rapide.

    if player.score > high_score: # Condition pour savoir si le score du joueur est supérieur au score enregistrer dans le fichier de sauvegarde du score
        save_high_score(player.score) # Enregistrer la valeur du nouveau record à l'aide de la fonction save_high_score
        print("New High Score:", player.score) # Afficher sur la console que le joueur a fait un nouveau record et l'afficher

    # Attendre 2 secondes avant de quitter
    pygame.time.wait(1000)
    pygame.quit() # Effacer la fenêtre du jeu

main() # Lancer la fonction pour le jeu
