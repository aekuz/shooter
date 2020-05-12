from pygame import *
from bullets_def import *

class cowboysprite(sprite.Sprite):

    picture_list = []

    up = ''
    left = ''
    right = ''
    down = ''

    def __init__(self,x,y):
        sprite.Sprite.__init__(self)

        self.picture = transform.scale(image.load(self.picture_list[0]), (100,100))

        self.rect = self.picture.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self,cowboy,wall_horisontal1,wall_vertical1,wall_horisontal2,wall_vertical2,wall_horisontal3,wall_vertical3,wall_horisontal4,wall_vertical4):
        keys = key.get_pressed()

        if keys[K_d]:
            self.rect.x += 20
            self.up = False
            self.right = True
            self.down = False
            self.left = False
            if sprite.collide_rect(cowboy, wall_horisontal1) or sprite.collide_rect(cowboy, wall_horisontal2) or sprite.collide_rect(cowboy,wall_horisontal3) or sprite.collide_rect(cowboy, wall_horisontal4) or sprite.collide_rect(cowboy, wall_vertical1) or sprite.collide_rect(cowboy, wall_vertical2) or sprite.collide_rect(cowboy,wall_vertical3) or sprite.collide_rect(cowboy,wall_vertical4):

                if cowboy.right:
                    cowboy.rect.x -= 20

        if keys[K_a]:
            self.rect.x -= 20
            self.up = False

            self.right = False
            self.down = False
            self.left = True
            if sprite.collide_rect(cowboy, wall_horisontal1) or sprite.collide_rect(cowboy,
                                                                                    wall_horisontal2) or sprite.collide_rect(
                    cowboy, wall_horisontal3) or sprite.collide_rect(cowboy, wall_horisontal4) or sprite.collide_rect(
                    cowboy, wall_vertical1) or sprite.collide_rect(cowboy, wall_vertical2) or sprite.collide_rect(
                    cowboy, wall_vertical3) or sprite.collide_rect(cowboy, wall_vertical4):
                if cowboy.left:
                    cowboy.rect.x += 20

        if keys[K_w]:
            self.rect.y -= 20
            self.up = True
            self.right = False
            self.down = False
            self.left = False
            if sprite.collide_rect(cowboy, wall_horisontal1) or sprite.collide_rect(cowboy, wall_horisontal2) or sprite.collide_rect(cowboy,wall_horisontal3) or sprite.collide_rect(cowboy, wall_horisontal4) or sprite.collide_rect(cowboy, wall_vertical1) or sprite.collide_rect(cowboy, wall_vertical2) or sprite.collide_rect(cowboy,wall_vertical3) or sprite.collide_rect(cowboy,wall_vertical4):
                if cowboy.up:
                    cowboy.rect.y += 20

        if keys[K_s]:
            self.rect.y += 20
            self.up = False
            self.right = False
            self.down = True
            self.left = False
            if sprite.collide_rect(cowboy, wall_horisontal1) or sprite.collide_rect(cowboy, wall_horisontal2) or sprite.collide_rect(cowboy,wall_horisontal3) or sprite.collide_rect(cowboy, wall_horisontal4) or sprite.collide_rect(cowboy, wall_vertical1) or sprite.collide_rect(cowboy, wall_vertical2) or sprite.collide_rect(cowboy,wall_vertical3) or sprite.collide_rect(cowboy,wall_vertical4):
                if cowboy.down:
                    cowboy.rect.y -= 20


    def draw(self,win):
        if not(self.up) and not(self.down) and not(self.left) and not(self.right):
            win.blit(transform.scale(image.load(self.picture_list[0]), (100,100)),(self.rect.x, self.rect.y))

        if self.up:

            win.blit(transform.scale(image.load(self.picture_list[0]), (100,100)),(self.rect.x, self.rect.y))
        elif self.down:

            win.blit(transform.scale(image.load(self.picture_list[1]), (100, 100)), (self.rect.x, self.rect.y))
        elif self.left:

            win.blit(transform.scale(image.load(self.picture_list[2]), (100,100)),(self.rect.x, self.rect.y))
        elif self.right:

            win.blit(transform.scale(image.load(self.picture_list[3]), (100, 100)), (self.rect.x, self.rect.y))

    recoil_time = 5
    recoil = recoil_time
    start_recoil = True

    shot_made = False

    def shoot(self,cowboy,shots):

        keys = key.get_pressed()

        if self.start_recoil:
            if self.recoil != self.recoil_time:
                self.recoil += 1
            else:
                self.start_recoil = False
                self.recoil = 0
                self.shot_made = False
        else:
            if keys[K_UP] and not(self.shot_made):
                bullet_up = bullet_class('bullet.png', cowboy)
                bullet_up.up = True
                bullet_up.down = False
                bullet_up.left = False
                bullet_up.right = False
                shots.add(bullet_up)
                self.shot_made = True
                self.start_recoil = True

            if keys[K_DOWN]and not(self.shot_made):
                bullet_down = bullet_class('bullet.png', cowboy)
                bullet_down.up = False
                bullet_down.down = True
                bullet_down.left = False
                bullet_down.right = False
                shots.add(bullet_down)
                self.shot_made = True
                self.start_recoil = True

            if keys[K_LEFT]and not(self.shot_made):
                bullet_left = bullet_class('bullet.png', cowboy)
                bullet_left.up = False
                bullet_left.down = False
                bullet_left.left = True
                bullet_left.right = False

                shots.add(bullet_left)
                self.shot_made = True
                self.start_recoil = True

            if keys[K_RIGHT]and not(self.shot_made):
                bullet_right = bullet_class('bullet.png', cowboy)
                bullet_right.up = False
                bullet_right.down = False
                bullet_right.left = False
                bullet_right.right = True

                shots.add(bullet_right)
                self.shot_made = True
                self.start_recoil = True
