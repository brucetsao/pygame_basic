# 代码说明
# 游戏初始化：
#
# 初始化Pygame，设置屏幕尺寸和标题。
# 定义颜色和网格尺寸的常量。
# 类定义：
#
# Snake 类：表示蛇，具有移动、绘制、变换方向和生长的功能。
# Food 类：表示食物，具有绘制和重生的功能。
# 主游戏循环：
#
# 处理用户输入（方向键移动蛇）。
# 更新蛇的位置。
# 检查蛇是否吃到食物。
# 绘制所有游戏元素（蛇和食物）。
# 控制帧率。
# 操作说明
# 使用箭头键左、右、上、下移动蛇。
# 运行此代码后，你会看到一个简单的贪吃蛇游戏，其中玩家可以控制绿色的蛇移动，目标是吃到红色的食物并尽量增长蛇的长度。游戏的核心逻辑已经实现，你可以根据需要进一步扩展和完善游戏。


import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
GRID_SIZE = 20

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# Clock for controlling the frame rate
clock = pygame.time.Clock()

class Snake(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.segments = [pygame.Rect(100, 100, GRID_SIZE, GRID_SIZE)]
        self.direction = pygame.Vector2(1, 0)
        self.grow = False

    def update(self):
        if not self.grow:
            self.segments.pop(0)
        else:
            self.grow = False

        new_segment = self.segments[-1].copy()
        new_segment.x += self.direction.x * GRID_SIZE
        new_segment.y += self.direction.y * GRID_SIZE
        self.segments.append(new_segment)

        if new_segment.x < 0 or new_segment.x >= SCREEN_WIDTH or new_segment.y < 0 or new_segment.y >= SCREEN_HEIGHT:
            pygame.event.post(pygame.event.Event(pygame.QUIT))

        for segment in self.segments[:-1]:
            if new_segment.colliderect(segment):
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    def draw(self, surface):
        for segment in self.segments:
            pygame.draw.rect(surface, GREEN, segment)

    def change_direction(self, direction):
        if direction.x != -self.direction.x or direction.y != -self.direction.y:
            self.direction = direction

    def grow_snake(self):
        self.grow = True

class Food(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.rect = pygame.Rect(random.randint(0, (SCREEN_WIDTH // GRID_SIZE) - 1) * GRID_SIZE,
                                random.randint(0, (SCREEN_HEIGHT // GRID_SIZE) - 1) * GRID_SIZE,
                                GRID_SIZE, GRID_SIZE)

    def draw(self, surface):
        pygame.draw.rect(surface, RED, self.rect)

    def respawn(self):
        self.rect.x = random.randint(0, (SCREEN_WIDTH // GRID_SIZE) - 1) * GRID_SIZE
        self.rect.y = random.randint(0, (SCREEN_HEIGHT // GRID_SIZE) - 1) * GRID_SIZE

# Create snake and food
snake = Snake()
food = Food()
all_sprites = pygame.sprite.Group()
all_sprites.add(snake)
all_sprites.add(food)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake.change_direction(pygame.Vector2(-1, 0))
            elif event.key == pygame.K_RIGHT:
                snake.change_direction(pygame.Vector2(1, 0))
            elif event.key == pygame.K_UP:
                snake.change_direction(pygame.Vector2(0, -1))
            elif event.key == pygame.K_DOWN:
                snake.change_direction(pygame.Vector2(0, 1))

    snake.update()
    if snake.segments[-1].colliderect(food.rect):
        snake.grow_snake()
        food.respawn()

    screen.fill(BLACK)
    snake.draw(screen)
    food.draw(screen)
    pygame.display.flip()
    clock.tick(10)

pygame.quit()
