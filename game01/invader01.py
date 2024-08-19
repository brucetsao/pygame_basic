import sys
import random
import pygame
from pygame.locals import QUIT
from Enemy import *  # 敵人
import pygame.mixer as player  # 加入音樂播放器

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WHITE = (255, 255, 255)
FPS = 60
enemy = []

def get_random_position(widow_width, window_height, image_width, image_height):
    random_x = random.randint(image_width, widow_width - image_width)
    random_y = random.randint(image_height, window_height - image_height)

    return random_x, random_y


def initenemy():
    for x in range(0,8):
        enemy.append(Enemy(0+x*100, 10, WINDOW_WIDTH, WINDOW_HEIGHT))
        #x.show(screen)

def showenemy(canvas):
    for x in enemy:
        x.show(canvas)


# 初始化
pygame.init()

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
# 產生一個視窗， 800x600 解析度
# 設置視窗標題為 Bruce Game:)
pygame.display.set_caption('太空大作戰')
# pygame.display.set_icon(icon)

# Background
background = pygame.image.load('./images/background.png')
screen.blit(background, (0, 0))

initenemy()
#ee1 = Enemy(100,100,WINDOW_WIDTH,WINDOW_HEIGHT)
# Game Loop
running = True
while running:
    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))
    # Background Image
    screen.blit(background, (0, 0))
    #showenemy(screen)
    #for x in enemy:
    #    x.show(screen)
    #ee1.show(screen)
    for x in enemy:
        x.show(screen)
    pygame.display.update()
