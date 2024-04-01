import pyxel
import random

# Définition des variables globales
WINDOW_WIDTH = 160
WINDOW_HEIGHT = 120
PLAYER_WIDTH = 7
PLAYER_HEIGHT = 7
OBSTACLE_WIDTH = 7
OBSTACLE_HEIGHT = 7
PLAYER_COLOR = 8
OBSTACLE_COLOR = 9
BACKGROUND_COLOR = 0
SCORE_COLOR = 7
FONT_COLOR = 7
FONT_SIZE = 4
PLAYER_SPEED = 2
OBSTACLE_SPEED = 2
INITIAL_OBSTACLE_INTERVAL = 40
OBSTACLE_INTERVAL_DECREMENT = 2

class Player:
    def __init__(self):
        self.x = WINDOW_WIDTH // 2
        self.y = WINDOW_HEIGHT - PLAYER_HEIGHT
        self.score = 0
        self.is_alive = True

    def update(self):
        if pyxel.btn(pyxel.KEY_LEFT) and self.x > 0:
            self.x -= PLAYER_SPEED
        if pyxel.btn(pyxel.KEY_RIGHT) and self.x < WINDOW_WIDTH - PLAYER_WIDTH:
            self.x += PLAYER_SPEED

    def draw(self):
        pyxel.rect(self.x, self.y, PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_COLOR)

class Obstacle:
    def __init__(self):
        self.x = random.randint(0, WINDOW_WIDTH - OBSTACLE_WIDTH)
        self.y = -OBSTACLE_HEIGHT

    def update(self):
        self.y += OBSTACLE_SPEED

    def draw(self):
        pyxel.rect(self.x, self.y, OBSTACLE_WIDTH, OBSTACLE_HEIGHT, OBSTACLE_COLOR)

class App:
    def __init__(self):
        pyxel.init(WINDOW_WIDTH, WINDOW_HEIGHT, title="Midnight Drive")
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
            if self.obstacle_interval < 10:
                self.obstacle_interval = 10
        for obstacle in self.obstacles:
            obstacle.update()
            if obstacle.y > WINDOW_HEIGHT:
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
