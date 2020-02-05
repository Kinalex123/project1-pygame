# -*- coding: utf-8 -*-
import pygame

pygame.init()
pygame.mixer.init()

size = width, height = 800, 600
screen = pygame.display.set_mode((size))
clock = pygame.time.Clock()
clicks = 0
white = (250, 250, 250)
black = (0, 0, 0)

all_sprite = pygame.sprite.Group()
sprite = pygame.sprite.Sprite()
sprite.image = pygame.image.load('banan.jpg')
sprite.rect = sprite.image.get_rect()
all_sprite.add(sprite)
sprite.rect.x = 100
sprite.rect.y = 100


font = pygame.font.Font(None, 24)
text = font.render("Количество кликов: "+str(clicks),True,white)
screen.blit(text, [0, 0])
text_win = font.render('Поздравляю, ты оформил спонсорскую подписку! ',True,white)

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
                text = font.render("Количество кликов: "+str(clicks),True,white)
                if clicks == 100:
                    pygame.mixer.music.load('ганс оф бул щит.mp3')
                    pygame.mixer.music.play()            
                if clicks == 30:
                    pygame.mixer.music.load('ведьмак из мира шутеров.mp3')
                    pygame.mixer.music.play()   
                if clicks == 50:
                    pygame.mixer.music.load('купи мою подписку.mp3')
                    pygame.mixer.music.play()   
                if clicks == 75:
                    pygame.mixer.music.load('смех банана.mp3')
                    pygame.mixer.music.play() 
                if clicks == 20:
                    pygame.mixer.music.load('супер долби диджитал.mp3')
                    pygame.mixer.music.play()   
                if clicks == 10:
                    pygame.mixer.music.load('это игра.mp3')
                    pygame.mixer.music.play()   
                if clicks == 150:
                    surf_win = pygame.Surface((900, 700))
                    surf_win.blit(text_win, [0, 0])
                    pygame.mixer.music.load('БАНАНЧИК.mp3')
                    pygame.mixer.music.play()   
    screen.fill(pygame.Color("black"))
    all_sprite.draw(screen)
    all_sprite.update()
    screen.blit(text, [0, 0])
    
    pygame.display.update()
    
pygame.quit()