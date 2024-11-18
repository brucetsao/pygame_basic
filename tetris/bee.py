pip install pygame
import pygame
import random

# 初始化 Pygame
pygame.init()

# 定義遊戲視窗的大小
screen_width = 600
screen_height = 400

# 建立遊戲視窗
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bee Game")

# 定義顏色
white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 0)


# 定義蜜蜂類別
class Bee(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("bee.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = screen_width / 2
        self.rect.y = screen_height / 2
        self.speed_x = 0
        self.speed_y = 0

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # 防止蜜蜂飛出視窗外
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > screen_width - self.rect.width:
            self.rect.x = screen_width - self.rect.width

        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y > screen_height - self.rect.height:
            self.rect.y = screen_height - self.rect.height


# 定義花朵類別
class Flower(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("flower.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screen_width - self.rect.width)
        self.rect.y = random.randint(0, screen_height - self.rect.height)

    def update(self):
        pass


# 創建精靈組
all_sprites = pygame.sprite.Group()

# 創建蜜蜂對象
bee = Bee()
all_sprites.add(bee)

# 創建花朵對象
flower = Flower()
all_sprites.add(flower)

# 遊戲循環
running = True
while running:
    # 事件處理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                bee.speed_x = -5
            elif event.key == pygame.K_RIGHT:
                bee.speed_x = 5
            elif event.key == pygame.K_UP:
                bee.speed_y = -5
            elif event.key == pygame.K_DOWN:
                bee.speed_y = 5
        elif event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                bee.speed_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                bee.speed_y = 0

            # 更新精靈組
        all_sprites.update()

        # 碰撞檢測
        hits = pygame.sprite.spritecollide(bee, all_sprites, False)
        if hits:
            if isinstance(hits[0], Flower):
                flower.rect.x = random.randint(0, screen_width - flower.rect.width)
                flower.rect.y = random.randint(0, screen_height - flower.rect.height)

        # 繪製遊戲場景
        screen.fill(white)
        all_sprites.draw(screen)
        pygame.display.flip()
