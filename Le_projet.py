import pygame
import random
import sys

# Initialisation de Pygame
pygame.init()

# Définition des variables globales
WIDTH, HEIGHT = 800, 600
PLAYER_SIZE = 50
PLAYER_COLOR = (255, 0, 0)
BACKGROUND_COLOR = (0, 0, 0)
SCORE_COLOR = (255, 255, 255)
OBSTACLE_WIDTH = 50
OBSTACLE_HEIGHT = 50
OBSTACLE_COLOR = (0, 255, 0)
ACCELERATION = 0.001
INITIAL_SPEED = 5
FONT_SIZE = 30

# Chargement du score record depuis un fichier
def load_high_score():
    try:
        with open("high_score.txt", "r") as file:
            return int(file.read())
    except FileNotFoundError:
        return 0

# Sauvegarde du score record dans un fichier
def save_high_score(score):
    with open("high_score.txt", "w") as file:
        file.write(str(score))

# Chargement de la musique de fond
# def load_background_music():
    # pygame.mixer.music.load("666.mp4")
    # pygame.mixer.music.play(-1)  # Joue en boucle infinie

# Création de la fenêtre de jeu
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Runner Game")

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
    if (player.x < obstacle.x + obstacle.width and
        player.x + player.width > obstacle.x and
        player.y < obstacle.y + obstacle.height and
        player.y + player.height > obstacle.y):
        return True
    return False

# Fonction principale pour exécuter le jeu
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
            if obstacle.y > HEIGHT:
                player.update_score()
                obstacles.remove(obstacle)

        # Augmentation de la vitesse avec le temps
        player.velocity += ACCELERATION #type:ignore

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

        pygame.display.update()
        clock.tick(60)

    # Vérification du score pour le record
    if player.score > high_score:
        save_high_score(player.score)
        print("New High Score:", player.score)

    # Attendre 2 secondes avant de quitter
    pygame.time.wait(2000)
    pygame.quit()

if __name__ == "__main__":
    main()

