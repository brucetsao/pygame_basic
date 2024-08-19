# 代码说明
# 游戏初始化：
#
# 初始化Pygame，设置屏幕尺寸和标题。
# 定义一些常量，如屏幕尺寸、坦克和子弹的尺寸以及颜色。
# 类定义：
#
# Tank 类：表示一个坦克，具有绘制、移动和射击功能。
# Bullet 类：表示一个子弹，具有绘制和移动功能。
# 主游戏循环：
#
# 处理用户输入（方向键移动坦克，空格键射击）。
# 更新坦克和子弹的位置。
# 检查子弹是否与敌方坦克碰撞。
# 绘制游戏元素（坦克和子弹）。
# 控制帧率。
# 操作说明
# 使用箭头键左、右、上、下移动坦克。
# 使用空格键射击子弹。
# 运行此代码后，你会看到一个简单的坦克大战游戏，其中玩家可以控制绿色坦克移动并射击子弹，目标是击中红色敌方坦克。游戏的核心逻辑已经实现，你可以根据需要进一步扩展和完善游戏。
#
#
import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Tank dimensions
TANK_WIDTH = 40
TANK_HEIGHT = 60

# Bullet dimensions
BULLET_WIDTH = 5
BULLET_HEIGHT = 10

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tank Battle")

# Clock for controlling the frame rate
clock = pygame.time.Clock()

class Tank:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.speed = 5
        self.direction = 0
        self.bullets = []

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, TANK_WIDTH, TANK_HEIGHT))

    def move(self, dx, dy):
        self.x += dx * self.speed
        self.y += dy * self.speed
        self.x = max(0, min(SCREEN_WIDTH - TANK_WIDTH, self.x))
        self.y = max(0, min(SCREEN_HEIGHT - TANK_HEIGHT, self.y))

    def shoot(self):
        if len(self.bullets) < 5:
            bullet_x = self.x + TANK_WIDTH // 2 - BULLET_WIDTH // 2
            bullet_y = self.y
            self.bullets.append(Bullet(bullet_x, bullet_y, self.direction))

class Bullet:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.speed = 7

    def draw(self):
        pygame.draw.rect(screen, WHITE, (self.x, self.y, BULLET_WIDTH, BULLET_HEIGHT))

    def move(self):
        if self.direction == 0:
            self.y -= self.speed
        elif self.direction == 1:
            self.y += self.speed
        elif self.direction == 2:
            self.x -= self.speed
        elif self.direction == 3:
            self.x += self.speed

def check_collision(rect1, rect2):
    return pygame.Rect(rect1).colliderect(pygame.Rect(rect2))

player_tank = Tank(SCREEN_WIDTH // 2, SCREEN_HEIGHT - TANK_HEIGHT - 10, GREEN)
enemy_tank = Tank(random.randint(0, SCREEN_WIDTH - TANK_WIDTH), 10, RED)

running = True
while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_tank.shoot()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_tank.move(-1, 0)
        player_tank.direction = 2
    if keys[pygame.K_RIGHT]:
        player_tank.move(1, 0)
        player_tank.direction = 3
    if keys[pygame.K_UP]:
        player_tank.move(0, -1)
        player_tank.direction = 0
    if keys[pygame.K_DOWN]:
        player_tank.move(0, 1)
        player_tank.direction = 1

    player_tank.draw()
    enemy_tank.draw()

    for bullet in player_tank.bullets:
        bullet.move()
        bullet.draw()
        if bullet.y < 0 or bullet.y > SCREEN_HEIGHT or bullet.x < 0 or bullet.x > SCREEN_WIDTH:
            player_tank.bullets.remove(bullet)
        elif check_collision((bullet.x, bullet.y, BULLET_WIDTH, BULLET_HEIGHT),
                             (enemy_tank.x, enemy_tank.y, TANK_WIDTH, TANK_HEIGHT)):
            player_tank.bullets.remove(bullet)
            enemy_tank = Tank(random.randint(0, SCREEN_WIDTH - TANK_WIDTH), 10, RED)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
