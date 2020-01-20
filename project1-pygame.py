import pygame

pygame.init()

size = width, height = 600, 400
screen = pygame.display.set_mode((size))
clock = pygame.time.Clock()
BLUE = (64, 128, 255)
clicks = 0

all_sprites = pygame.sprite.Group()
sprite = pygame.sprite.Sprite()
sprite.image = load_image('C:\Users\S1080-s1-210-hp319\Documents\как обычноо\banan.jpg')
sprite.rect = sprite.image.get_rect()
all_sprite.add(sprite)
sprite.rect.x = 150
sprite.rect.y = 250

def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname).convert()
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)

    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image

class Logv(pygame.sprite.Sprite):
    image_banan = load_image('banan.jpg')
    
    def __init__(self, clicks):
        self.clicks = clicks
        super().__init__(all_sprites)
        self.image = Logv.image_banan
        self.rect = self.image.get_rect()
        self.x = 250
        self.y = 250
    
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
            exit()
        if i.tipe == pygame.MOUSEBUTTONUP:
            clicks += 1
    screen.fill(pygame.Color("black"))
    all_sprites.draw(screen)
    all_sprites.update()    
    
    pygame.display.update()