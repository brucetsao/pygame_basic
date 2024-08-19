import sys
import random
import pygame
from pygame.locals import QUIT
from Mosquito import *  #加入蚊子類別
import pygame.mixer as player   #加入音樂播放器

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WHITE = (255, 255, 255)
IMAGEWIDTH = 100
IMAGEHEIGHT = 75
FPS = 60

def get_random_position(widow_width, window_height, image_width, image_height):
    random_x = random.randint(image_width, widow_width - image_width)
    random_y = random.randint(image_height, window_height - image_height)

    return random_x, random_y

# 初始化
pygame.init()
window_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
# 產生一個視窗， 800x600 解析度
# 設置視窗標題為 Bruce Game:)
pygame.display.set_caption('Bruce Game')
# 清除畫面並填滿背景色(r,g,b)
window_surface.fill((255, 255, 255))

# 更新畫面，等所有操作完成後一次更新（若沒更新，則元素不會出現）
random_x, random_y = get_random_position(WINDOW_WIDTH, WINDOW_HEIGHT, IMAGEWIDTH, IMAGEHEIGHT)
#產生一個隨機位置 random_x, random_y
mosquito = Mosquito(IMAGEWIDTH, IMAGEHEIGHT, random_x, random_y, WINDOW_WIDTH, WINDOW_HEIGHT)
#產生一個Mosquito 的物件，取名為mosquito
# 渲染物件
window_surface.blit(mosquito.image, mosquito.rect)
#window_surface.blit(text_surface, (10, 0))
player.music.load('./music/cat.mp3')
#載入龍貓音樂mp3(in music目錄下， 名字為cat.mp3
player.music.play(0, 0.0)   #播放音樂
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()