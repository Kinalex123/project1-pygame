import pygame

pygame.init()

size = width, height = 800, 600
screen = pygame.display.set_mode((size))
clock = pygame.time.Clock()
clicks = 0

all_sprite = pygame.sprite.Group()
sprite = pygame.sprite.Sprite()
sprite.image = pygame.image.load('banan.jpg')
sprite.rect = sprite.image.get_rect()
all_sprite.add(sprite)
sprite.rect.x = 100
sprite.rect.y = 100

pygame.font.Font(None, 24)

class Logv:
    def __init__(self, clicks):
        self.clicks = clicks
    
    def click(self):
        if self.clicks == 20:
            pass
        if self.clicks == 50:
            pass
        if self.clicks == 80:
            pass
        if self.clicks == 100:
            pass

running = True
pygame.display.update()
while running:
    clock.tick(60)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
        if i.type == pygame.MOUSEBUTTONUP:
            if sprite.rect.collidepoint(i.pos):
                clicks += 1
                print(clicks)
    screen.fill(pygame.Color("black"))
    all_sprite.draw(screen)
    all_sprite.update()    
    
    pygame.display.update()
    
pygame.quit()