from pygame import *
from main_hero import *
from enemy_def import *
from walls_def import *


win = display.set_mode((1024, 1024))
display.set_caption('Trouble shooter')
win.blit(transform.scale(image.load('background.jpg'), (1024,1024)),(0,0))


class winning(sprite.Sprite):
    def __init__(self,picture, x,y, width,height):
        self.picture = transform.scale(image.load(picture),(width,height))
        self.rect = self.picture.get_rect()
        self.rect.x = x
        self.rect.y = y
    def place(self):
        win.blit(self.picture, (self.rect.x, self.rect.y))

run = True
x = 0
y = 0
spawn_timer = 100


cowboysprite.picture_list = ['cowboy_back.png','cowboy_front.png','cowboy_left.png','cowboy_right.png']

enemysprite.picture_list = ['bandit_back.png','bandit_front.png','bandit_left.png','bandit_right.png']

cowboy = cowboysprite(500,500)
wall_horisontal1 = wall('wall_side.png',0,0,350,75)
wall_vertical1 = wall('wall_up.png',0,0,75,350)
wall_horisontal2 = wall('wall_side.png',674,0,350,75)
wall_vertical2 = wall ('wall_up.png',949,0,75,350)
wall_horisontal3 = wall('wall_side.png',0,949,350,75)
wall_vertical3 = wall('wall_up.png',0,674,75,350)
wall_horisontal4 = wall('wall_side.png',674,949,350,75)
wall_vertical4 = wall('wall_up.png',949,674,75,350)

bullet = bullet_class('bullet.png',cowboy)

#enemy = enemysprite('bandit_left.png', 200,200)
prize = winning('award.png',900,0,100,100)

shots = sprite.Group()
bandits = sprite.Group()

def losing(cowboy):
    win.blit(transform.scale(image.load('lose.png'), (1024, 1024)), (0, 0))
    display.update()
    restart = True
    while restart:
        for events in event.get():
            if events.type == QUIT:
                restart = False
                return (False)
            if events.type == KEYDOWN:
                if events.key == K_r:
                    restart = False
                    cowboy.rect.x = 0
                    cowboy.rect.y = 0

def winning(cowboy):
    win.blit(transform.scale(image.load('win.png'), (1024, 1024)), (0, 0))
    display.update()
    restart = True
    while restart:
        for events in event.get():
            if events.type == QUIT:
                restart = False
                return (False)
            if events.type == KEYDOWN:
                if events.key == K_r:
                    restart = False
                    cowboy.rect.x = 0
                    cowboy.rect.y = 0

while run:

    time.delay(50)

    for events in event.get():
        if events.type == KEYDOWN:
            if events.key == K_t:
                run = False
        if events.type == QUIT:
            run = False
    win.blit(transform.scale(image.load('background.jpg'), (1024, 1024)), (0, 0))
    cowboy.update(cowboy,wall_horisontal1,wall_vertical1,wall_horisontal2,wall_vertical2,wall_horisontal3,wall_vertical3,wall_horisontal4,wall_vertical4)
    cowboy.draw(win)

    if cowboy.rect.x < -10:
        cowboy.rect.x+=20
    elif cowboy.rect.x >934:
        cowboy.rect.x-=20
    elif cowboy.rect.y <-10:
        cowboy.rect.y+=20
    elif cowboy.rect.y >934:
        cowboy.rect.y-=20

    wall_vertical1.place(win)
    wall_horisontal1.place(win)
    wall_vertical2.place(win)
    wall_horisontal2.place(win)
    wall_vertical3.place(win)
    wall_horisontal3.place(win)
    wall_vertical4.place(win)
    wall_horisontal4.place(win)

    cowboy.shoot(cowboy,shots)

    shots.update(cowboy,win)

    bandits.update(cowboy,wall_horisontal1,wall_vertical1,wall_horisontal2,wall_vertical2,wall_horisontal3,wall_vertical3,wall_horisontal4,wall_vertical4)
    bandits.draw(win)
    spawn(spawn_timer, bandits)

    sprite.groupcollide(shots,bandits,True,True)

    collides = sprite.groupcollide(bandits, bandits, False,False)

    #enemy.update(cowboy,wall_horisontal1,wall_vertical1,wall_horisontal2,wall_vertical2,wall_horisontal3,wall_vertical3,wall_horisontal4,wall_vertical4)
    #enemy.draw(win)
    if sprite.spritecollideany(cowboy, bandits):
        run = False

    '''if sprite.collide_rect(cowboy,enemy):

        if losing(cowboy) == False:
            break
    if sprite.collide_rect(cowboy,prize):
        if winning(cowboy) == False:
            break'''

    display.update()

time.delay(1)