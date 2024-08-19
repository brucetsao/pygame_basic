# 此代碼是一個簡單的飛行射擊遊戲，
# 玩家可以控制綠色飛機移動並射擊子彈，
# 目標是擊中紅色敵機。
# 遊戲的基本功能已經實現，
# 您可以根據需要進一步擴展和完善遊戲。


import pygame
import random

# 初始化Pygame
pygame.init()

# 屏幕尺寸
SCREEN_WIDTH = 800  # 設定屏幕寬度為800像素
SCREEN_HEIGHT = 600  # 設定屏幕高度為600像素

# 顏色定義
BLACK = (0, 0, 0)  # 黑色的RGB值
WHITE = (255, 255, 255)  # 白色的RGB值
GREEN = (0, 255, 0)  # 綠色的RGB值
RED = (255, 0, 0)  # 紅色的RGB值

# 屏幕設置
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # 創建指定尺寸的顯示窗口
pygame.display.set_caption("1943 Airplane Battle")  # 設定窗口的標題

# 用於控制幀速率的時鐘
clock = pygame.time.Clock()

# 玩家飛機設置
player_width = 50  # 玩家飛機的寬度
player_height = 60  # 玩家飛機的高度
player_image = pygame.Surface((player_width, player_height))  # 創建玩家飛機的圖像表面
player_image.fill(GREEN)  # 將玩家飛機填充為綠色
player_x = SCREEN_WIDTH // 2 - player_width // 2  # 初始化玩家飛機的X位置，位於屏幕中間
player_y = SCREEN_HEIGHT - player_height - 10  # 初始化玩家飛機的Y位置，位於屏幕底部
player_speed = 5  # 玩家飛機的移動速度

# 子彈設置
bullet_width = 5  # 子彈的寬度
bullet_height = 10  # 子彈的高度
bullet_speed = 7  # 子彈的移動速度
player_bullets = []  # 存儲玩家發射的所有子彈的列表

# 敵機設置
enemy_width = 50  # 敵機的寬度
enemy_height = 60  # 敵機的高度
enemy_image = pygame.Surface((enemy_width, enemy_height))  # 創建敵機的圖像表面
enemy_image.fill(RED)  # 將敵機填充為紅色
enemy_speed = 3  # 敵機的移動速度
enemies = []  # 存儲所有敵機的列表

# 分數設置
score = 0  # 初始化分數為0
font = pygame.font.SysFont(None, 36)  # 設定字體和大小

def draw_text(text, font, color, surface, x, y):
    """
    在屏幕上繪製文本
    :param text: 要顯示的文本
    :param font: 字體對象
    :param color: 字體顏色
    :param surface: 繪製的目標表面
    :param x: 文本的X座標
    :param y: 文本的Y座標
    """
    text_obj = font.render(text, True, color)  # 渲染文本為字體對象
    text_rect = text_obj.get_rect()  # 獲取文本的邊框
    text_rect.topleft = (x, y)  # 設定文本左上角的座標
    surface.blit(text_obj, text_rect)  # 在目標表面上繪製文本

def move_player(keys):
    """
    根據鍵盤按鍵移動玩家飛機
    :param keys: 按鍵的狀態
    """
    global player_x, player_y
    if keys[pygame.K_LEFT] and player_x - player_speed > 0:  # 如果按下左箭頭鍵且飛機不會超出左邊界
        player_x -= player_speed  # 向左移動飛機
    if keys[pygame.K_RIGHT] and player_x + player_speed + player_width < SCREEN_WIDTH:  # 如果按下右箭頭鍵且飛機不會超出右邊界
        player_x += player_speed  # 向右移動飛機
    if keys[pygame.K_UP] and player_y - player_speed > 0:  # 如果按下上箭頭鍵且飛機不會超出上邊界
        player_y -= player_speed  # 向上移動飛機
    if keys[pygame.K_DOWN] and player_y + player_speed + player_height < SCREEN_HEIGHT:  # 如果按下下箭頭鍵且飛機不會超出下邊界
        player_y += player_speed  # 向下移動飛機

def shoot_bullet():
    """發射子彈"""
    bullet_x = player_x + player_width // 2 - bullet_width // 2  # 設定子彈的X位置，從飛機中間射出
    bullet_y = player_y  # 設定子彈的Y位置，與飛機相同
    player_bullets.append(pygame.Rect(bullet_x, bullet_y, bullet_width, bullet_height))  # 將子彈添加到列表中

def move_bullets():
    """移動子彈"""
    for bullet in player_bullets:  # 遍歷每顆子彈
        bullet.y -= bullet_speed  # 向上移動子彈
        if bullet.y < 0:  # 如果子彈超出屏幕
            player_bullets.remove(bullet)  # 從列表中移除子彈

def create_enemy():
    """創建敵機"""
    enemy_x = random.randint(0, SCREEN_WIDTH - enemy_width)  # 隨機生成敵機的X位置
    enemy_y = -enemy_height  # 設定敵機的Y位置在屏幕外
    enemies.append(pygame.Rect(enemy_x, enemy_y, enemy_width, enemy_height))  # 將敵機添加到列表中

def move_enemies():
    """移動敵機"""
    for enemy in enemies:  # 遍歷每架敵機
        enemy.y += enemy_speed  # 向下移動敵機
        if enemy.y > SCREEN_HEIGHT:  # 如果敵機超出屏幕
            enemies.remove(enemy)  # 從列表中移除敵機

def check_collisions():
    """檢查子彈與敵機的碰撞"""
    global score
    for bullet in player_bullets:  # 遍歷每顆子彈
        for enemy in enemies:  # 遍歷每架敵機
            if bullet.colliderect(enemy):  # 如果子彈與敵機發生碰撞
                player_bullets.remove(bullet)  # 從列表中移除子彈
                enemies.remove(enemy)  # 從列表中移除敵機
                score += 1  # 分數增加1
                break  # 結束當前敵機的迴圈

# 遊戲主循環
running = True  # 設定遊戲循環標誌
while running:
    screen.fill(BLACK)  # 用黑色填充屏幕背景
    keys = pygame.key.get_pressed()  # 獲取按鍵狀態
    move_player(keys)  # 移動玩家飛機

    for event in pygame.event.get():  # 遍歷事件
        if event.type == pygame.QUIT:  # 如果點擊關閉按鈕
            running = False  # 結束遊戲循環
        elif event.type == pygame.KEYDOWN:  # 如果按下鍵盤按鍵
            if event.key == pygame.K_SPACE:  # 如果按下空格鍵
                shoot_bullet()  # 發射子彈

    if random.randint(1, 20) == 1:  # 每20幀有一次機會創建敵機
        create_enemy()  # 創建敵機

    move_bullets()  # 移動所有子彈
    move_enemies()  # 移動所有敵機
    check_collisions()  # 檢查碰撞

    screen.blit(player_image, (player_x, player_y))  # 在屏幕上繪製玩家飛機
    for bullet in player_bullets:  # 繪製所有子彈
        pygame.draw.rect(screen, WHITE, bullet)  # 將子彈繪製為白色矩形
    for enemy in enemies:  # 繪製所有敵機
        screen.blit(enemy_image, enemy.topleft)  # 將敵機圖像繪製在敵機位置

    draw_text(f"Score: {score}", font, WHITE, screen, 10, 10)  # 在屏幕上顯示分數
    pygame.display.flip()  # 更新屏幕顯示
    clock.tick(30)  # 設定遊戲幀率為30FPS

pygame.quit()  # 結束Pygame
