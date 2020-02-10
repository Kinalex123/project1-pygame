import pygame

pygame.init()
pygame.mixer.init()

size = width, height = 800, 600
screen = pygame.display.set_mode((size))
clock = pygame.time.Clock()
clicks = 0
white = (250, 250, 250)
black = (0, 0, 0)

# ������� ��� �������

all_sprite = pygame.sprite.Group()
sprite = pygame.sprite.Sprite()
sprite.image = pygame.image.load('banan.jpg')
sprite.rect = sprite.image.get_rect()
all_sprite.add(sprite)
sprite.rect.x = 100
sprite.rect.y = 100

# ����� ��� ����� ��������

all_sprites = pygame.sprite.Group()
sprites = pygame.sprite.Sprite()
sprites.image = pygame.image.load('��������.bmp')
sprites.rect = sprite.image.get_rect()
all_sprites.add(sprites)
sprites.rect.x = 50
sprites.rect.y = 200

# ������

font = pygame.font.Font(None, 24)
text = font.render("���������� ����� ������: "+str(clicks),True,white)
screen.blit(text, [0, 0])
text_win = font.render('��������� �� ������� ����������� �������� �� �����! ',True,white)

running = True
pygame.display.update()
while running:
    clock.tick(60)
    screen.fill(pygame.Color("black"))
    all_sprite.draw(screen)
    all_sprite.update()
    screen.blit(text, [0, 0])    
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
        if i.type == pygame.MOUSEBUTTONUP:
            if sprite.rect.collidepoint(i.pos):
                clicks += 1
                print(clicks)
                text = font.render("���������� ����� ������: "+str(clicks),True,white)
                if clicks == 100:
                    pygame.mixer.music.load('���� �� ��� ���.mp3')
                    pygame.mixer.music.play()            
                if clicks == 30:
                    pygame.mixer.music.load('������� �� ���� �������.mp3')
                    pygame.mixer.music.play()   
                if clicks == 50:
                    pygame.mixer.music.load('���� ��� ��������.mp3')
                    pygame.mixer.music.play()   
                if clicks == 75:
                    pygame.mixer.music.load('���� ������.mp3')
                    pygame.mixer.music.play() 
                if clicks == 20:
                    pygame.mixer.music.load('����� ����� ��������.mp3')
                    pygame.mixer.music.play()   
                if clicks == 10:
                    pygame.mixer.music.load('��� ����.mp3')
                    pygame.mixer.music.play()   
                if clicks == 5:
                    pygame.mixer.music.load('��������.mp3')
                    pygame.mixer.music.play()
                    running = False
    pygame.display.update()
    
gaming = True
while gaming:
    clock.tick(60)
    pygame.display.update()
    all_sprites.draw(screen)
    all_sprites.update()    
    screen_battle = pygame.display.set_mode((size))
    screen_battle.fill(pygame.Color('white'))    
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            gaming = False    
    
    
pygame.quit()