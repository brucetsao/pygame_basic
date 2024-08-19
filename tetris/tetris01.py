# 代码说明
# 游戏初始化：
#
# 初始化Pygame，设置屏幕尺寸和标题。
# 定义一些常量，如屏幕尺寸、网格尺寸和颜色。
# Tetrimino类：
#
# 负责创建和旋转俄罗斯方块形状。
# 辅助函数：
#
# create_grid：创建游戏网格。
# draw_grid：绘制网格。
# draw_tetrimino：绘制当前的俄罗斯方块。
# valid_space：检查当前的方块是否在有效位置。
# clear_rows：清除已填满的行并返回清除的行数。
# 主游戏循环：
#
# 处理游戏逻辑，包括下降、移动和旋转方块。
# 检查并处理游戏结束条件。
# 将此代码复制到你的Python文件中运行即可开始游戏。游戏的操作方式如下：
#
# 使用箭头键左、右移动方块。
# 使用箭头键上旋转方块。
# 使用箭头键下加速方块下落。
#
#
import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
GRID_SIZE = 30
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)

# Tetrimino shapes
SHAPES = [
    [[1, 1, 1],
     [0, 1, 0]],

    [[0, 1, 1],
     [1, 1, 0]],

    [[1, 1, 0],
     [0, 1, 1]],

    [[1, 1, 1, 1]],

    [[1, 1],
     [1, 1]],

    [[1, 1, 1],
     [1, 0, 0]],

    [[1, 1, 1],
     [0, 0, 1]]
]

# Assign colors to shapes
SHAPE_COLORS = [CYAN, BLUE, ORANGE, YELLOW, GREEN, RED, MAGENTA]

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")

# Clock for controlling the frame rate
clock = pygame.time.Clock()


class Tetrimino:
    def __init__(self):
        self.shape = random.choice(SHAPES)
        self.color = SHAPE_COLORS[SHAPES.index(self.shape)]
        self.x = GRID_WIDTH // 2 - len(self.shape[0]) // 2
        self.y = 0
        self.rotation = 0

    def rotate(self):
        self.shape = list(zip(*self.shape[::-1]))


def create_grid(locked_positions={}):
    grid = [[BLACK for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            if (x, y) in locked_positions:
                grid[y][x] = locked_positions[(x, y)]
    return grid


def draw_grid(grid):
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            pygame.draw.rect(screen, grid[y][x], (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))
    for x in range(GRID_WIDTH):
        pygame.draw.line(screen, WHITE, (x * GRID_SIZE, 0), (x * GRID_SIZE, SCREEN_HEIGHT))
    for y in range(GRID_HEIGHT):
        pygame.draw.line(screen, WHITE, (0, y * GRID_SIZE), (SCREEN_WIDTH, y * GRID_SIZE))


def draw_tetrimino(tetrimino):
    for y, row in enumerate(tetrimino.shape):
        for x, cell in enumerate(row):
            if cell:
                pygame.draw.rect(screen, tetrimino.color,
                                 ((tetrimino.x + x) * GRID_SIZE, (tetrimino.y + y) * GRID_SIZE, GRID_SIZE, GRID_SIZE))


def valid_space(tetrimino, grid):
    for y, row in enumerate(tetrimino.shape):
        for x, cell in enumerate(row):
            if cell:
                if x + tetrimino.x < 0 or x + tetrimino.x >= GRID_WIDTH or y + tetrimino.y >= GRID_HEIGHT:
                    return False
                if grid[y + tetrimino.y][x + tetrimino.x] != BLACK:
                    return False
    return True


def clear_rows(grid, locked):
    cleared_rows = 0
    for y in range(GRID_HEIGHT - 1, -1, -1):
        if BLACK not in grid[y]:
            cleared_rows += 1
            del locked[y]
            for x in range(GRID_WIDTH):
                del locked[(x, y)]
            for i in range(y, 0, -1):
                for x in range(GRID_WIDTH):
                    if (x, i) in locked:
                        locked[(x, i + 1)] = locked.pop((x, i))
    return cleared_rows


def main():
    locked_positions = {}
    grid = create_grid(locked_positions)
    change_tetrimino = False
    current_tetrimino = Tetrimino()
    next_tetrimino = Tetrimino()
    fall_time = 0
    level_time = 0
    fall_speed = 0.27
    score = 0

    running = True
    while running:
        grid = create_grid(locked_positions)
        fall_time += clock.get_rawtime()
        level_time += clock.get_rawtime()
        clock.tick()

        if level_time / 1000 > 5:
            level_time = 0
            if fall_speed > 0.12:
                fall_speed -= 0.005

        if fall_time / 1000 >= fall_speed:
            fall_time = 0
            current_tetrimino.y += 1
            if not valid_space(current_tetrimino, grid) and current_tetrimino.y > 0:
                current_tetrimino.y -= 1
                change_tetrimino = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_tetrimino.x -= 1
                    if not valid_space(current_tetrimino, grid):
                        current_tetrimino.x += 1
                if event.key == pygame.K_RIGHT:
                    current_tetrimino.x += 1
                    if not valid_space(current_tetrimino, grid):
                        current_tetrimino.x -= 1
                if event.key == pygame.K_DOWN:
                    current_tetrimino.y += 1
                    if not valid_space(current_tetrimino, grid):
                        current_tetrimino.y -= 1
                if event.key == pygame.K_UP:
                    current_tetrimino.rotate()
                    if not valid_space(current_tetrimino, grid):
                        for _ in range(3):
                            current_tetrimino.rotate()

        shape_pos = [(current_tetrimino.x + x, current_tetrimino.y + y) for y, row in enumerate(current_tetrimino.shape)
                     for x, cell in enumerate(row) if cell]
        for x, y in shape_pos:
            if y > -1:
                grid[y][x] = current_tetrimino.color

        if change_tetrimino:
            for x, y in shape_pos:
                locked_positions[(x, y)] = current_tetrimino.color
            current_tetrimino = next_tetrimino
            next_tetrimino = Tetrimino()
            change_tetrimino = False
            score += clear_rows(grid, locked_positions) * 10

        screen.fill(BLACK)
        draw_grid(grid)
        draw_tetrimino(current_tetrimino)
        pygame.display.flip()

        if any(y < 1 for x, y in locked_positions):
            running = False

    pygame.quit()


if __name__ == "__main__":
    main()
