import pygame, os
pygame.init()
screen = pygame.display.set_mode((528,447))
pygame.display.set_caption("math.png")
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((255,255,255))

image = pygame.image.load("math.png").convert()
background.blit(image, (0,0))

screen.blit(background, (0,0))
pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()