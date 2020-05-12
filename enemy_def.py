from pygame import *
from random import *

class enemysprite(sprite.Sprite):

    picture_list = ['bandit_back.png','bandit_front.png','bandit_left.png','bandit_right.png']

    image = transform.scale(image.load('bandit_front.png'), (100,100))

    up = False
    down = False
    right = False
    left = False

    def __init__(self,x,y):
        sprite.Sprite.__init__(self)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        '''if not(self.up) and not(self.down) and not(self.left) and not(self.right):
            self.image = transform.scale(image.load('bandit_front.png'), (100,100))

        if self.up:

            self.image = transform.scale(image.load('bandit_front.png'), (100, 100))
        elif self.down:

            self.image = transform.scale(image.load('bandit_right.png'), (100, 100))
        elif self.left:

            self.image = transform.scale(image.load('bandit_left.png'), (100, 100))
        elif self.right:

            self.image = transform.scale(image.load('bandit_back.png'), (100, 100))'''

    def update(self,cowboy,wall_horisontal1,wall_vertical1,wall_horisontal2,wall_vertical2,wall_horisontal3,wall_vertical3,wall_horisontal4,wall_vertical4):

        one_step = 0

        if self.rect.x> cowboy.rect.x:
            self.rect.x -=10
            one_step = True

            self.up = False
            self.down = False
            self.left = True
            self.right = False

            if sprite.collide_rect(self, wall_horisontal1) or sprite.collide_rect(self, wall_horisontal2) or sprite.collide_rect(self,wall_horisontal3) or sprite.collide_rect(self, wall_horisontal4) or sprite.collide_rect(self, wall_vertical1) or sprite.collide_rect(self, wall_vertical2) or sprite.collide_rect(self,wall_vertical3) or sprite.collide_rect(self,wall_vertical4):

                if self.left:
                    self.rect.x += 20


        if (self.rect.x <cowboy.rect.x) and not(one_step):
            self.rect.x+=10
            one_step=True

            self.up = False
            self.down = False
            self.left = False
            self.right = True

            if sprite.collide_rect(self, wall_horisontal1) or sprite.collide_rect(self, wall_horisontal2) or sprite.collide_rect(self,wall_horisontal3) or sprite.collide_rect(self, wall_horisontal4) or sprite.collide_rect(self, wall_vertical1) or sprite.collide_rect(self, wall_vertical2) or sprite.collide_rect(self,wall_vertical3) or sprite.collide_rect(self,wall_vertical4):

                if self.right:
                    self.rect.x -= 20

        if (self.rect.y>cowboy.rect.y) and not(one_step):
            self.rect.y -=10
            one_step=True

            self.up = True
            self.down = False
            self.left = False
            self.right = False

        if (self.rect.y<cowboy.rect.y) and not(one_step):
            self.rect.y +=10
            self.up = False
            self.down = True
            self.left = False
            self.right = False

        '''if not(self.up) and not(self.down) and not(self.left) and not(self.right):
            self.image = transform.scale(image.load('bandit_front.png'), (100,100))

        if self.up:

            self.image = transform.scale(image.load('bandit_back.png'), (100, 100))
        elif self.down:

            self.image = transform.scale(image.load('bandit_front.png'), (100, 100))
        elif self.left:

            self.image = transform.scale(image.load('bandit_left.png'), (100, 100))
        elif self.right:

            self.image = transform.scale(image.load('bandit_right.png'), (100, 100))
        #win.blit(self.picture, (self.rect.x,self.rect.y))'''


def spawn(spawn_timer,bandits):
    if spawn_timer == 100:

        variety = randint(1,10)


        if variety == 1:
            direction = randint(1,4)
            if direction == 1:
                spawn_x = 500
                spawn_y = 0

                for i in range(1):
                    enemy = enemysprite(spawn_x, spawn_y)

                    bandits.add(enemy)

            elif direction == 2:
                pass

            elif direction == 3:
                pass

            elif direction == 4:
                pass


        elif variety == 2:
            pass

        elif variety == 6:
            pass

    else:
        spawn_timer+=1