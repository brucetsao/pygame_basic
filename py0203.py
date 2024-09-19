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

font1 = pygame.font.Font("SetoFont.ttf", 24)
#字體變數 = pygame.font.Font(路徑+字體名稱, 字體尺寸)

text1 = font1.render("這是曹建國老師寫的字", True, (255,0,0)) #繪製紅色文字，但文字背景不繪製
#文字變數(背景透明) = 字體變數.render(文字內容, 平滑值, 文字顯示顏色之RGB變數)

screen.blit(text1, (20,10))
#將"這是曹建國老師寫的字"繪製在(x=20,y=10)的位置上
screen.blit(text1, (30,100))
#將"這是曹建國老師寫的字"繪製在(x=30,y=100)的位置上

#視窗變數.blit(畫布變數, 繪製位置)
#繪製位置 用 (x座標，y座標)來產生

pygame.display.update()
#視窗變數.display.update()

while True:
    a=1
#pygame.display.update()

