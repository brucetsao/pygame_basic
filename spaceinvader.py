import pygame
import random

# 初始化 Pygame
pygame.init()

# 定義遊戲視窗的大小
screen_width = 800
screen_height = 600

# 建立遊戲視窗
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Invader")

# 載入圖片
player_img = pygame.image.load("player.png").convert_alpha()
enemy_img = pygame.image.load("enemy.png").convert_alpha()
bullet_img = pygame.image.load("bullet.png").convert_alpha()

# 定義顏色
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)


# 定義玩家類別
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.x = screen_width / 2
        self.rect.y = screen_height - self.rect.height - 10
        self.speed = 5

    def update(self):
        # 移動玩家
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        elif keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        # 防止玩家超出邊界
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > screen_width - self.rect.width:
            self.rect.x = screen_width - self.rect.width


# 定義敵人類別
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screen_width - self.rect.width)
        self.rect.y = random.randint(-500, -self.rect.height)
        self.speed = random.randint(1, 3)

    def update(self):
        # 移動敵人
        self.rect.y += self.speed

        # 如果敵人超出邊界，就重置位置和速度
        if self.rect.y > screen_height:
            self.rect.x = random.randint(0, screen_width - self.rect.width)
            self.rect.y = random.randint(-500, -self.rect.height)
            self.speed = random.randint(1, 3)


# 定義子彈類別
class Bullet(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + player.rect.width / 2 - self.rect.width / 2
        self.rect.y = player.rect.y - self.rect.height
        self.speed = 10



#上一個代碼塊中，我們定義了玩家、敵人和子彈的類別，但是還沒有定義它們的 update 方法。現在我們來完成這部分的代碼
    def update(self):
        # 移動子彈
        self.rect.y -= self.speed

        # 如果子彈超出邊界，就刪除它
        if self.rect.y < 0:
            self.kill()


# 創建遊戲物件的群組
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()

# 創建玩家
player = Player()
all_sprites.add(player)

# 創建敵人
for i in range(10):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)

# 設置遊戲時鐘
clock = pygame.time.Clock()

# 設置分數
score = 0

# 遊戲主迴圈
running = True
while running:
    # 設置帧速率
    clock.tick(60)

    # 處理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = Bullet(player)
                all_sprites.add(bullet)
                bullets.add(bullet)

    # 更新遊戲物件
    all_sprites.update()

    # 檢測子彈和敵人的碰撞
    hits = pygame.sprite.groupcollide(enemies, bullets, True, True)
    for hit in hits:
        enemy = Enemy()
        all_sprites.add(enemy)
        enemies.add(enemy)
        score += 1

    # 檢測玩家和敵人的碰撞
    hits = pygame.sprite.spritecollide(player, enemies, False)
    if hits:
        running = False

    # 顯示遊戲畫面
    screen.fill(black)
    all_sprites.draw(screen)
    font = pygame.font.SysFont(None, 30)
    text = font.render("Score: " + str(score), True, white)
    screen.blit(text, (10, 10))
    pygame.display.update()

# 退出 Pygame
pygame.quit()

