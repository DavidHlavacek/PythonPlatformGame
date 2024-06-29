import pygame
import random
from settings import *
from utils import load_image

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        meteor_images = []
        meteor_list = ["Images/asteroid.png", "Images/asteroid333.png"]
        pygame.sprite.Sprite.__init__(self)
        for img in meteor_list:
            meteor_images.append(load_image(img).convert_alpha())
        self.image_orig = random.choice(meteor_images)
        self.image_orig = pygame.transform.scale(self.image_orig, (93, 77))
        self.image = self.image_orig.copy()
        self.rect = self.image_orig.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-2000, -300)
        self.speedy = random.randrange(2, 13)
        self.speedx = random.randrange(-5, 5)
        self.rot = 0
        self.rot_speed = random.randrange(-8, 8)
        self.last_update = pygame.time.get_ticks()
        self.damage = 30

    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360
            new_image = pygame.transform.rotate(self.image_orig, self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center

    def update(self):
        self.rotate()
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        self.mask = pygame.mask.from_surface(self.image)
        if self.rect.top > HEIGHT + 10 or self.rect.x < -25 or self.rect.x > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-2000, -300)
            self.speedy = random.randrange(2, 8)
            self.speedx = random.randrange(-5, 5)

class Mob2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("Images/projectileee.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (80, 30))
        self.rect = self.image.get_rect()
        self.position = 0
        self.rect.x = random.randrange(-2500, -1000)
        self.rect.y = random.randrange(450, 656)
        if self.rect.y >= 605:
            self.position = 1
            self.positionUP = random.randrange(520, 580)
        elif self.rect.y <= 500:
            self.position = 2
            self.positionDOWN = random.randrange(590, 640)
        self.speedy = random.randrange(-3, 3)
        self.speedx = 5
        self.damage = 20

    def update(self):
        self.mask = pygame.mask.from_surface(self.image)
        if 449 <= self.rect.y <= 656 and self.rect.x >= 0:
            if self.position == 1:
                if self.rect.y >= self.positionUP:
                    self.rect.y += random.randrange(-3, 0)
                else:
                    self.rect.y += 0
                if self.rect.y <= 500:
                    self.position = 2
            if self.position == 2:
                if self.rect.y <= self.positionDOWN:
                    self.rect.y += random.randrange(0, 3)
                else:
                    self.rect.y += 0
                if self.rect.y >= 645:
                    self.position = 1
        self.rect.x += self.speedx
        if self.rect.x > WIDTH + 20 or self.rect.top > HEIGHT + 10:
            self.rect.x = random.randrange(-10000, -2000)
            self.rect.y = random.randrange(450, 656)
            if self.rect.y >= 605:
                self.position = 1
                self.positionUP = random.randrange(520, 580)
            elif self.rect.y <= 500:
                self.position = 2
                self.positionDOWN = random.randrange(590, 680)
            self.speedy = random.randrange(-3, 3)
            self.speedx = 5

class Mob3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.images.append(load_image("Images/whitespikefinalhalf.png").convert_alpha())
        self.images.append(load_image("Images/piques.png").convert_alpha())
        self.index = 0
        self.image = self.images[self.index]
        self.counter = 0
        self.limit = 0
        self.spike = False

    def update(self):
        global spike
        self.limit += 1
        if self.limit <= 45:
            self.counter += 1
            if self.counter >= 10:
                self.counter = 0
                self.index += 1
            if self.index >= 2:
                self.index = 0
            self.image = self.images[self.index]
            self.image = pygame.transform.scale(self.image, (1282, 25))
            self.rect = self.image.get_rect()
            self.rect.x = -5
            self.rect.y = 672
            spike = False
        else:
            self.rect.x = -1000
            self.rect.y = -1000
            spike = True
            self.kill()

class Mob4(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("Images/whitespikefinal22.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (1282, 38))
        self.rect = self.image.get_rect()
        self.rect.x = -1000
        self.rect.y = -1000
        self.stop = 0
        self.stop2 = 0
        self.damage = 10

    def update(self):
        self.mask = pygame.mask.from_surface(self.image)
        if spike:
            self.stop += 1
            if self.stop <= 14:
                self.rect.x = -5
                self.rect.y = 660
            else:
                self.stop2 += 1
                self.image = load_image("Images/whitespikefinalhalf.png").convert_alpha()
                self.image = pygame.transform.scale(self.image, (1282, 25))
                self.rect.x = -5
                self.rect.y = 672
                if self.stop2 > 2:
                    self.rect.x = -1000
                    self.rect.y = -1000
                    self.kill()
