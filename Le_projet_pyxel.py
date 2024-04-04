import pyxel
import random

# Définition des variables globales
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 600
PLAYER_WIDTH = 100
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
OBSTACLE_INTERVAL_DECREMENT = 5

pyxel.init(WINDOW_WIDTH, WINDOW_HEIGHT, title="Midnight Drive", display_scale=1)

pyxel.images[0].load(0,0,"Voiture_joueur.png") #type: ignore

class Player:
    def __init__(self):
        self.y = WINDOW_HEIGHT // 2
        self.x = 0 + PLAYER_WIDTH
        self.score = 0
        self.is_alive = True

    def update(self):
        if pyxel.btn(pyxel.KEY_UP) and self.y > 0:
            self.y -= PLAYER_SPEED
        if pyxel.btn(pyxel.KEY_DOWN) and self.y < WINDOW_HEIGHT - PLAYER_HEIGHT:
            self.y += PLAYER_SPEED

    def draw(self):
        pyxel.blt(self.x, self.y, 0 , 0 , 0 ,150,53)

class Obstacle:
    def __init__(self):
        self.y = random.randint(0, WINDOW_HEIGHT - OBSTACLE_WIDTH)
        self.x = WINDOW_WIDTH + OBSTACLE_WIDTH

    def update(self):
        self.x -= OBSTACLE_SPEED

    def draw(self):
        pyxel.rect(self.x, self.y, OBSTACLE_WIDTH, OBSTACLE_HEIGHT, OBSTACLE_COLOR)

class App:
    def __init__(self):
        
        self.player = Player()
        self.obstacles = []
        self.obstacle_interval = INITIAL_OBSTACLE_INTERVAL
        self.game_over = False
        pyxel.run(self.update, self.draw)

    def update(self):
        if not self.game_over:
            self.player.update()
            self.update_obstacles()
            self.check_collision()

    def draw(self):
        pyxel.cls(BACKGROUND_COLOR)
        if not self.game_over:
            self.player.draw()
            for obstacle in self.obstacles:
                obstacle.draw()
            pyxel.text(4, 4, "Score: {}".format(self.player.score), SCORE_COLOR)
        else:
            pyxel.text(WINDOW_WIDTH // 2 - 20, WINDOW_HEIGHT // 2, "Game Over", SCORE_COLOR)

    def update_obstacles(self):
        if pyxel.frame_count % self.obstacle_interval == 0:
            self.obstacles.append(Obstacle())
            self.obstacle_interval -= OBSTACLE_INTERVAL_DECREMENT
            if self.obstacle_interval <= 20:
                self.obstacle_interval = 15
        for obstacle in self.obstacles:
            obstacle.update()
            if obstacle.x < -OBSTACLE_WIDTH :
                self.obstacles.remove(obstacle)
                self.player.score += 1

    def check_collision(self):
        player_rect = [self.player.x, self.player.y, self.player.x + PLAYER_WIDTH, self.player.y + PLAYER_HEIGHT]
        for obstacle in self.obstacles:
            obstacle_rect = [obstacle.x, obstacle.y, obstacle.x + OBSTACLE_WIDTH, obstacle.y + OBSTACLE_HEIGHT]
            if self.check_rect_collision(player_rect, obstacle_rect):
                self.game_over = True
                break

    def check_rect_collision(self, rect1, rect2):
        if (rect1[0] < rect2[2] and rect1[2] > rect2[0] and rect1[1] < rect2[3] and rect1[3] > rect2[1]):
            return True
        return False

App()