import pygame   #匯入PyGame套件
pygame.init()  #啟動PyGame套件
screen = pygame.display.set_mode((800,600))
#screen為視窗變數，來使用建立的視窗
#視窗變數 = pygame.display.set_mode(視窗寬度尺寸:pixels，視窗高度尺寸:pixels)

pygame.display.set_caption("曹建國老師第一個繪圖視窗標題")
#pygame.display.set_caption(視窗標題的內容)

screen.fill((0,0,0))
#視窗變數.fill(RGB變數參數)

bg = pygame.Surface(screen.get_size())
#畫布變數 = pygame.Surface(screen.get_size())
bg = bg.convert()
#畫布變數 = 畫布變數.convert()

pic1 = pygame.image.load('ultimalogo800w.jpg')
#透過pygame套件載入圖片'ultimalogo800w.jpg'，並將圖片轉成繪圖畫布，並儲存在pic1名稱

screen.blit(pic1, (0,0))
#視窗變數.blit(畫布變數, 繪製位置)
#繪製位置 用 (x座標，y座標)來產生

pygame.display.update()
#視窗變數.display.update()

while True:
    a=1
#pygame.display.update()

