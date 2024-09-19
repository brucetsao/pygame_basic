import pygame
pygame.init()
screen = pygame.display.set_mode((400,400))
pygame.display.set_caption("字體顯示")
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0,255,0))

font1 = pygame.font.Font("SetoFont.ttf", 24)
text1 = font1.render("自訂字型", True, (255,0,0), (255,255,255))
background.blit(text1, (20,10))
font2 = pygame.font.SysFont("DFKai-SB", 24)
text2 = font2.render("系統字型", True, (0,0,255),(0,255,0))
background.blit(text2, (20,50))

screen.blit(background, (0, 0))
pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()