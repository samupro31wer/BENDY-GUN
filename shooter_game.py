# ¡Crea tu propio juego de disparos!
from random import randint
from pygame import *

init()
SteamOS  = display.set_mode((700,500))
display.set_caption('bendy gun ')
fondito = transform.scale(image.load("fondo.png"),(700,500))
fondito2 = transform.scale(image.load("fondo2.jpg"),(700,500))
SteamOS.blit(fondito,(0,0))


mixer.init()
mixer.music.load('cancion_fondito.ogg')
mixer.music.play()
# clase padre para otros objetos
class GameSprite(sprite.Sprite):
    # constructor de clase
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # llamamos al constructor de la clase (Sprite):
        sprite.Sprite.__init__(self)

        # cada objeto debe almacenar una propiedad image
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        # cada objeto debe almacenar la propiedad rect en la cual está inscrito
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    # método que dibuja al personaje en la ventana
    def reset(self):
        SteamOS.blit(self.image, (self.rect.x, self.rect.y))


# clase del jugador principal
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT]:
            self.rect.x -= self.speed
        if keys[K_RIGHT]:
            self.rect.x += self.speed
    def fireball(self):
        una_bala = bala('bala.png',self.rect.centerx,self.rect.top,15,20,15)
        balas.add(una_bala)
class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a]:
            self.rect.x -= self.speed
        if keys[K_d]:
            self.rect.x += self.speed
    def fireball(self):
        una_bala = bala('bala.png',self.rect.centerx,self.rect.top,15,20,15)
        balas.add(una_bala)

class bala(GameSprite):
    def update(self):
        self.rect.y -=self.speed
        if self.rect.y <0:
            self.kill()
class enemy(GameSprite):
    def update(self):
        self.rect.y +=self.speed
        if self.rect.y >500:
            self.kill()


balas = sprite.Group()
enemigos = sprite.Group()

for i in range(10):
    malo= enemy('ovni_de_tinta.png',randint(5,650),1,50,30,6)
    enemigos.add(malo)
Bendy = Player('bendy.png',20,400,60,100,20)
Boris = Player2('boris.png',15,400,60,100,20)

btn_jugar = GameSprite("start.jpg",250,300,200,70,0)

run = True
gameover = False 
in_game = True

while in_game and run:
    for e in event.get():
        if e.type == QUIT:
            run= False
            in_game = False

        if e.type == MOUSEBUTTONDOWN:
            in_game = False
            mixer.music.play()
    
    SteamOS.blit(fondito2, (0, 0)) #dibuja el fondo en la pantalla

    display.update()






while run:
    SteamOS.blit(fondito,(0,0))
    for e in event.get():
        if e.type == QUIT:
            run= False
        if e.type == KEYDOWN:
            if e.key == K_UP:
                Bendy.fireball()
            if e.key == K_w:
                Boris.fireball()
    if not gameover:
        sprite.groupcollide(enemigos,balas,True,True)
        Bendy.update()
        Bendy.reset()
        Boris.update()
        Boris.reset()
        enemigos.update()
        enemigos.draw(SteamOS)

        balas.update()
        balas.draw(SteamOS)
        
        if sprite.spritecollide(Bendy,enemigos,False):
            gameover = True
            mixer.music.stop()
    display.update()
    time.delay(100)
