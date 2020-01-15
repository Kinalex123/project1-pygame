import pygame

pygame.init()

size = width, height = 600, 400
screen = pygame.display.set_mode((size))
clock = pygame.time.Clock()

running = True
while ruuning:
    clock.tick(60)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
    pygame.display.update()
    
    