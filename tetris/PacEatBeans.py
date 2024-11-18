import pygame
import sys
from pygame.locals import *

# 初始化 Pygame
pygame.init()

# 定義顏色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

# 設置屏幕大小
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("吃豆人遊戲")

# 設置遊戲更新的時間間隔
CLOCK = pygame.time.Clock()
FPS = 30

# 設置豆子的大小和牆的大小
GRID_SIZE = 20

# 吃豆人的類
class Pacman(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((GRID_SIZE, GRID_SIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = GRID_SIZE  # 每次移動的步長

    def move(self, dx, dy):
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed

        # 邊界限制
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

# 豆子的類
class Pellet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((GRID_SIZE // 2, GRID_SIZE // 2))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

# 牆壁的類
class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((GRID_SIZE, GRID_SIZE))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

# 創建遊戲場景
def create_walls():
    walls = pygame.sprite.Group()
    # 簡單的牆壁布局，可以自行擴展
    wall_coords = [(100, 100), (100, 120), (100, 140), (200, 100), (220, 100), (240, 100)]
    for coord in wall_coords:
        wall = Wall(*coord)
        walls.add(wall)
    return walls

# 創建豆子
def create_pellets():
    pellets = pygame.sprite.Group()
    pellet_coords = [(x * GRID_SIZE + GRID_SIZE // 2, y * GRID_SIZE + GRID_SIZE // 2)
                     for x in range(SCREEN_WIDTH // GRID_SIZE)
                     for y in range(SCREEN_HEIGHT // GRID_SIZE)]
    for coord in pellet_coords:
        pellet = Pellet(*coord)
        pellets.add(pellet)
    return pellets

# 遊戲主循環
def game_loop():
    pacman = Pacman(50, 50)  # 初始化吃豆人的位置
    walls = create_walls()  # 創建牆壁
    pellets = create_pellets()  # 創建豆子
    all_sprites = pygame.sprite.Group(pacman, *walls, *pellets)  # 所有的精靈物件

    # 遊戲循環
    while True:
        SCREEN.fill(BLACK)

        # 處理事件
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # 控制吃豆人的移動
        keys = pygame.key.get_pressed()
        dx, dy = 0, 0
        if keys[K_LEFT]:
            dx = -1
        if keys[K_RIGHT]:
            dx = 1
        if keys[K_UP]:
            dy = -1
        if keys[K_DOWN]:
            dy = 1
        pacman.move(dx, dy)

        # 檢測吃豆人與牆壁的碰撞
        if pygame.sprite.spritecollideany(pacman, walls):
            pacman.move(-dx, -dy)  # 碰到牆壁就後退

        # 檢測吃豆人是否吃到豆子
        pellets_eaten = pygame.sprite.spritecollide(pacman, pellets, True)

        # 更新精靈
        all_sprites.update()

        # 繪製所有元素
        walls.draw(SCREEN)
        pellets.draw(SCREEN)
        SCREEN.blit(pacman.image, pacman.rect)

        pygame.display.update()
        CLOCK.tick(FPS)

# 執行遊戲
if __name__ == "__main__":
    game_loop()
