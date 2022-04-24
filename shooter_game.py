#Создай собственный Шутер!

from pygame import *
from random import *
from time import time as timer
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
window = display.set_mode((700, 500))
display.set_caption('Лабиринт')
blacground = transform.scale(image.load('galaxy.jpg'),(700, 500))
clock = time.Clock()
FPS = 60
mixer.init()
mixer.music.load('space.ogg', )
mixer.music.play()





game = True

bullets = sprite.Group()
class Player(GameSprite):
    def apdate(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_d]:
            self.rect.x += 10
        if keys_pressed[K_a]:
            self.rect.x -= 10
    def fire(self):
        bullet = Bullet('3.png',self.rect.centerx, self.rect.top, 20, 25, 30 )
        bullets.add(bullet)
    def fireу(self):
        bullet1 = Bullet('1.png',self.rect.centerx, self.rect.top, 20, 70, 70 )
        bullets.add(bullet1)    
lost = 0
toto = 0
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y == 450:
            self.rect.y = 0
            self.rect.x = randint(0, 600)
            self.speed = randint(1, 3)
            lost = lost + 1





class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        global toto
        if self.rect.y < 0:
            self.kill()


asret1 = Enemy('asteroid.png', 350, 430, 2 , 60, 60)
asret2 = Enemy('asteroid.png', 300, 430, 2 , 60, 60)
asret3 = Enemy('asteroid.png', 300, 430, 2 , 60, 60)
asteroids = sprite.Group()
asteroids.add(asret1)
asteroids.add(asret2)
asteroids.add(asret3)

hero = Player('rocket.png', 200, 400, 1, 60, 60)
enemi = Enemy('ufo.png', 300, 50, 1, 60, 60)
enemi2 = Enemy('ufo.png', 50, 50, 1, 60, 60)
enemi3 = Enemy('ufo.png', 500, 50, 1, 60, 60)
enemi4 = Enemy('ufo.png', 250, 50, 1, 60, 60)
enemi5 = Enemy('ufo.png', 0, 50, 1, 60, 60)

monsters = sprite.Group()
monsters.add(enemi)
monsters.add(enemi2)
monsters.add(enemi3)
monsters.add(enemi4)
monsters.add(enemi5)
nam_pul = 0
toto_plis = False
font.init()
font = font.SysFont('Arial', 36)
lous = font.render('ТЫ ПРОИГРАЛ!!!!!!!!', True, (255, 215, 0))
win = font.render('ХОРОШ!!!!!!!!', True, (255, 215, 0))
finih = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if   e.key == K_SPACE:
                if nam_pul < 5 and toto_plis == False:
                    nam_pul = nam_pul + 1
                    hero.fire()

                if nam_pul >= 5 and toto_plis == False:
                    lost_time = timer()
                    toto_plis = True

                
                







    

    if finih != True:
        window.blit(blacground, (0,0))

   
        hero.apdate()
        hero.reset()
        text_lost = font.render('Пропущено:' + str(lost), 1, (225, 0, 0))
        text_lost2 = font.render('Очки:' + str(toto), 1, (0, 225, 225))
        monsters.draw(window)
        asteroids.draw(window)
        asteroids.update()
        window.blit(text_lost, (0, 0))
        window.blit(text_lost2, (0, 30))
        monsters.update()
        bullets.draw(window)
        bullets.update()

        if toto_plis == True:
            now_time = timer()
            if now_time - lost_time < 3:
                row = font.render('ПЕРЕЗАРЕЖАЮСЬ!!', True, (255, 215, 0))
                window.blit(row, (250, 200))
            else:
                nam_pul = 0
                toto_plis = False






        
        if sprite.groupcollide(monsters, bullets, True, True):
            toto = toto + 1
            monster = Enemy('ufo.png', randint(0, 600), 0, randint(1, 3), 60, 60)
            monsters.add(monster)
        if sprite.spritecollide(hero, monsters, asteroids, False):
            finih = True
            window.blit(lous, (250, 200))
        if sprite.spritecollide(hero, asteroids, False):
            finih = True
            window.blit(lous, (250, 200))
        if toto == 10:
            window.blit(win, (250, 200))
            finih = True



    display.update()
    clock.tick(FPS)



    
    