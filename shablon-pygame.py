import pygame

pygame.init()

size = width, height = 600, 400
screen = pygame.display.set_mode((size))
clock = pygame.time.Clock()
BLUE = (64, 128, 255)

r = 50
x = 0 - r
y = height // 2

running = True
while running:
    clock.tick(60)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
    
    pygame.draw.circle(screen, BLUE, (x, y), r)
    if x >= width + r:
        x = 0 - r
    else:
        x += 3
    pygame.display.update()
    
    