# 代码说明
# 游戏初始化：
#
# 初始化Pygame，设置屏幕尺寸和标题。
# 定义颜色和屏幕尺寸的常量。
# Sprite类定义：
#
# Player类：表示玩家的飞机，具有移动和射击功能。
# Bullet类：表示子弹，具有移动功能。
# Enemy类：表示敌机，具有移动功能。
# 主游戏循环：
#
# 处理用户输入（方向键移动玩家飞机，空格键射击子弹）。
# 创建敌机并更新其位置。
# 检查子弹是否与敌机碰撞。
# 检查敌机是否与玩家碰撞。
# 绘制所有游戏元素（玩家飞机、子弹、敌机）。
# 显示分数。
# 操作说明
# 使用箭头键左、右、上、下移动玩家飞机。
# 使用空格键射击子弹。
# 运行此代码后，你会看到一个更简洁的飞行射击游戏，其中玩家可以控制绿色飞机移动并射击子弹，目标是击中红色敌机。游戏的核心逻辑已经实现，你可以根据需要进一步扩展和完善游戏。
#
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

# 定義玩家飛機的Sprite類
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()  # 初始化父類
        self.image = pygame.Surface((50, 60))  # 創建玩家飛機的圖像表面
        self.image.fill(GREEN)  # 將玩家飛機填充為綠色
        self.rect = self.image.get_rect()  # 獲取玩家飛機的邊框
        self.rect.centerx = SCREEN_WIDTH // 2  # 初始化玩家飛機的X位置，位於屏幕中間
        self.rect.bottom = SCREEN_HEIGHT - 10  # 初始化玩家飛機的Y位置，位於屏幕底部
        self.speed = 5  # 玩家飛機的移動速度

    def update(self):
        """更新玩家飛機的位置"""
        keys = pygame.key.get_pressed()  # 獲取按鍵狀態
        if keys[pygame.K_LEFT] and self.rect.left > 0:  # 如果按下左箭頭鍵且飛機不會超出左邊界
            self.rect.x -= self.speed  # 向左移動飛機
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:  # 如果按下右箭頭鍵且飛機不會超出右邊界
            self.rect.x += self.speed  # 向右移動飛機
        if keys[pygame.K_UP] and self.rect.top > 0:  # 如果按下上箭頭鍵且飛機不會超出上邊界
            self.rect.y -= self.speed  # 向上移動飛機
        if keys[pygame.K_DOWN] and self.rect.bottom < SCREEN_HEIGHT:  # 如果按下下箭頭鍵且飛機不會超出下邊界
            self.rect.y += self.speed  # 向下移動飛機

    def shoot(self):
        """玩家發射子彈"""
        bullet = Bullet(self.rect.centerx, self.rect.top)  # 創建子彈對象，從飛機中間射出
        all_sprites.add(bullet)  # 將子彈添加到所有精靈的組中
        bullets.add(bullet)  # 將子彈添加到子彈的組中

# 定義子彈的Sprite類
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()  # 初始化父類
        self.image = pygame.Surface((5, 10))  # 創建子彈的圖像表面
        self.image.fill(WHITE)  # 將子彈填充為白色
        self.rect = self.image.get_rect()  # 獲取子彈的邊框
        self.rect.centerx = x  # 設定子彈的X位置
        self.rect.bottom = y  # 設定子彈的Y位置
        self.speed = 7  # 子彈的移動速度

    def update(self):
        """更新子彈的位置"""
        self.rect.y -= self.speed  # 向上移動子彈
        if self.rect.bottom < 0:  # 如果子彈超出屏幕
            self.kill()  # 從所有精靈組中刪除子彈

# 定義敵機的Sprite類
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()  # 初始化父類
        self.image = pygame.Surface((50, 60))  # 創建敵機的圖像表面
        self.image.fill(RED)  # 將敵機填充為紅色
        self.rect = self.image.get_rect()  # 獲取敵機的邊框
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)  # 隨機生成敵機的X位置
        self.rect.y = random.randint(-100, -40)  # 隨機生成敵機的Y位置
        self.speed = 3  # 敵機的移動速度

    def update(self):
        """更新敵機的位置"""
        self.rect.y += self.speed  # 向下移動敵機
        if self.rect.top > SCREEN_HEIGHT:  # 如果敵機超出屏幕
            self.kill()  # 從所有精靈組中刪除敵機

# 創建精靈組
all_sprites = pygame.sprite.Group()  # 所有精靈的組
bullets = pygame.sprite.Group()  # 子彈的組
enemies = pygame.sprite.Group()  # 敵機的組

# 創建玩家飛機並添加到精靈組
player = Player()
all_sprites.add(player)

def create_enemy():
    """創建敵機"""
    enemy = Enemy()  # 創建敵機對象
    all_sprites.add(enemy)  # 將敵機添加到所有精靈的組中
    enemies.add(enemy)  # 將敵機添加到敵機的組中

# 遊戲主循環
running = True  # 設定遊戲循環標誌
while running:
    for event in pygame.event.get():  # 遍歷事件
        if event.type == pygame.QUIT:  # 如果點擊關閉按鈕
            running = False  # 結束遊戲循環
        elif event.type == pygame.KEYDOWN:  # 如果按下鍵盤按鍵
            if event.key == pygame.K_SPACE:  # 如果按下空格鍵
                player.shoot()  # 玩家發射子彈

    all_sprites.update()  # 更新所有精靈

    if random.randint(1, 20) == 1:  # 每20幀有一次機會創建敵機
        create_enemy()  # 創建敵機

    hits = pygame.sprite.groupcollide(enemies, bullets, True, True)  # 檢查子彈與敵機的碰撞
    score += len(hits)  # 每次碰撞將敵機和子彈從組中移除，並增加分數

    hits = pygame.sprite.spritecollide(player, enemies, False)  # 檢查敵機與玩家的碰撞
    if hits:  # 如果發生碰撞
        running = False  # 結束遊戲

    screen.fill(BLACK)  # 用黑色填充屏幕背景
    all_sprites.draw(screen)  # 繪製所有精靈
    draw_text(f"Score: {score}", font, WHITE, screen, 10, 10)  # 在屏幕上顯示分數
    pygame.display.flip()  # 更新屏幕顯示
    clock.tick(30)  # 設定遊戲幀率為30FPS

pygame.quit()  # 結束Pygame
