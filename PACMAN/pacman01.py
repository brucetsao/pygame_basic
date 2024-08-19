# 代码说明
# 游戏初始化：
#
# 初始化Pygame，设置屏幕尺寸和标题。
# 定义一些常量，如屏幕尺寸、网格尺寸和颜色。
# 主游戏循环：
#
# 处理用户输入（方向键移动Pac-Man）。
# 更新Pac-Man和幽灵的位置。
# 检查Pac-Man是否吃到食物或与幽灵碰撞。
# 绘制游戏元素（网格、Pac-Man、幽灵和食物）。
# 控制帧率。
# 操作说明
# 使用箭头键左、右、上、下移动Pac-Man。
# 运行此代码后，你会看到一个简单的Pac-Man游戏，其中Pac-Man可以通过箭头键移动，吃到绿色的食物增加分数，避免与红色幽灵碰撞。

import pygame
import random

# 初始化 Pygame
pygame.init()

# 設置屏幕的寬度和高度
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
# 設置網格的大小（用於畫格子）
GRID_SIZE = 20

# 顏色定義
BLACK = (0, 0, 0)     # 黑色
WHITE = (255, 255, 255) # 白色
YELLOW = (255, 255, 0) # 黃色
BLUE = (0, 0, 255)    # 藍色
RED = (255, 0, 0)     # 紅色
GREEN = (0, 255, 0)   # 綠色

# 設置顯示窗口
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pac-Man") # 設置窗口標題為 "Pac-Man"

# 設置時鐘用於控制幀率
clock = pygame.time.Clock()

# Pac-Man 的初始位置
pacman_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
# Pac-Man 的移動方向
pacman_dir = [0, 0]

# 幽靈的初始位置（隨機生成）
ghost_pos = [random.randint(0, (SCREEN_WIDTH // GRID_SIZE) - 1) * GRID_SIZE,
             random.randint(0, (SCREEN_HEIGHT // GRID_SIZE) - 1) * GRID_SIZE]

# 食物的初始位置（隨機生成）
food_pos = [random.randint(0, (SCREEN_WIDTH // GRID_SIZE) - 1) * GRID_SIZE,
            random.randint(0, (SCREEN_HEIGHT // GRID_SIZE) - 1) * GRID_SIZE]

# 初始分數
score = 0

def draw_grid():
    """
    畫網格，方便視覺化遊戲區域
    """
    # 繪製垂直線
    for x in range(0, SCREEN_WIDTH, GRID_SIZE):
        pygame.draw.line(screen, WHITE, (x, 0), (x, SCREEN_HEIGHT))
    # 繪製水平線
    for y in range(0, SCREEN_HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, WHITE, (0, y), (SCREEN_WIDTH, y))

def draw_pacman(position):
    """
    繪製 Pac-Man
    :param position: Pac-Man 的位置 [x, y]
    """
    pygame.draw.circle(screen, YELLOW, (position[0] + GRID_SIZE // 2, position[1] + GRID_SIZE // 2), GRID_SIZE // 2)

def draw_ghost(position):
    """
    繪製幽靈
    :param position: 幽靈的位置 [x, y]
    """
    pygame.draw.rect(screen, RED, (position[0], position[1], GRID_SIZE, GRID_SIZE))

def draw_food(position):
    """
    繪製食物
    :param position: 食物的位置 [x, y]
    """
    pygame.draw.circle(screen, GREEN, (position[0] + GRID_SIZE // 2, position[1] + GRID_SIZE // 2), GRID_SIZE // 4)

def move_pacman(direction):
    """
    移動 Pac-Man
    :param direction: 移動方向 [x, y]
    """
    global pacman_pos
    pacman_pos[0] += direction[0] * GRID_SIZE
    pacman_pos[1] += direction[1] * GRID_SIZE
    # 確保 Pac-Man 繼續在屏幕內部（循環邊界）
    pacman_pos[0] %= SCREEN_WIDTH
    pacman_pos[1] %= SCREEN_HEIGHT

def check_collision(pos1, pos2):
    """
    檢查兩個位置是否碰撞
    :param pos1: 位置 1 [x, y]
    :param pos2: 位置 2 [x, y]
    :return: 是否碰撞 (布林值)
    """
    return pos1 == pos2

def move_ghost():
    """
    隨機移動幽靈
    """
    directions = [[0, -1], [0, 1], [-1, 0], [1, 0]] # 上、下、左、右四個方向
    ghost_pos[0] += random.choice(directions)[0] * GRID_SIZE
    ghost_pos[1] += random.choice(directions)[1] * GRID_SIZE
    # 確保幽靈繼續在屏幕內部（循環邊界）
    ghost_pos[0] %= SCREEN_WIDTH
    ghost_pos[1] %= SCREEN_HEIGHT

# 遊戲主循環
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # 如果接收到退出事件，終止遊戲
            running = False
        elif event.type == pygame.KEYDOWN:
            # 根據鍵盤按鍵更新 Pac-Man 的移動方向
            if event.key == pygame.K_LEFT:
                pacman_dir = [-1, 0]
            elif event.key == pygame.K_RIGHT:
                pacman_dir = [1, 0]
            elif event.key == pygame.K_UP:
                pacman_dir = [0, -1]
            elif event.key == pygame.K_DOWN:
                pacman_dir = [0, 1]

    # 移動 Pac-Man 和幽靈
    move_pacman(pacman_dir)
    move_ghost()

    # 檢查 Pac-Man 是否吃到食物
    if check_collision(pacman_pos, food_pos):
        score += 1
        # 隨機生成新的食物位置
        food_pos = [random.randint(0, (SCREEN_WIDTH // GRID_SIZE) - 1) * GRID_SIZE,
                    random.randint(0, (SCREEN_HEIGHT // GRID_SIZE) - 1) * GRID_SIZE]

    # 檢查 Pac-Man 是否與幽靈碰撞
    if check_collision(pacman_pos, ghost_pos):
        running = False

    # 清空屏幕，填充背景顏色
    screen.fill(BLACK)
    # 畫網格、Pac-Man、幽靈和食物
    draw_grid()
    draw_pacman(pacman_pos)
    draw_ghost(ghost_pos)
    draw_food(food_pos)

    # 更新顯示
    pygame.display.flip()
    # 控制遊戲循環的幀率（每秒 10 幀）
    clock.tick(10)

# 結束 Pygame
pygame.quit()
