from pygame import*

class bullet_class(sprite.Sprite):
    up =0
    down= 0
    left = 0
    right = 0
    def __init__(self,picture,person):
        sprite.Sprite.__init__(self)

        self.picture = transform.scale(image.load(picture), (10,10))

        self.rect = self.picture.get_rect()

        self.rect.x = person.rect.x+50
        self.rect.y = person.rect.y+50

    def update(self,person,win):
        if self.up:
            win.blit(self.picture, (self.rect.x, self.rect.y))
            self.rect.y -= 50
            if self.rect.y<=(-10):
                self.up = False
                self.rect.y = person.rect.y + 50
                self.rect.x = person.rect.x + 50
        if self.down:
            win.blit(self.picture, (self.rect.x, self.rect.y))
            self.rect.y += 50
            if self.rect.y>=(1034):
                self.down = False
                self.rect.y = person.rect.y + 50
                self.rect.x = person.rect.x + 50
        if self.left:
            win.blit(self.picture, (self.rect.x, self.rect.y))
            self.rect.x -= 50
            if self.rect.x<=(-10):
                self.left = False
                self.rect.y = person.rect.y + 50
                self.rect.x = person.rect.x + 50
        if self.right:
            win.blit(self.picture, (self.rect.x, self.rect.y))
            self.rect.x += 50
            if self.rect.x>=(1034):
                self.right = False
                self.rect.y = person.rect.y + 50
                self.rect.x = person.rect.x + 50