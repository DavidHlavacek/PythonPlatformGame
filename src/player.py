import pygame
from pygame.locals import *
from settings import *
from utils import load_image

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("Images/spriteHITBOX.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (115, 144))
        self.rect = self.image.get_rect()
        self.radius = pygame.draw.rect(self.image, GREEN, self.rect, 2)
        self.rect.x = WIDTH / 2
        self.rect.y = 553
        self.speedx = 0
        self.velocity = 10
        self.jumping = False
        self.vel = 0
        self.gravity = 0.8
        self.jumpCount = 10
        self.shield = 100
        self.lives = 3
        self.hidden = False
        self.hide_timer = pygame.time.get_ticks()

    def update(self):
        self.keysstop = False
        if self.hidden and pygame.time.get_ticks() - self.hide_timer >= 1000:
            self.hidden = False
            self.rect.x = WIDTH / 2
            self.rect.y = 553
            self.keysstop = True

        self.keysstop = False
        self.image = load_image("Images/spriteSTILL.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (115, 144))
        self.speedx = 0

        keys = pygame.key.get_pressed()
        if keys[K_a] and self.rect.x > 10 and not self.keysstop:
            self.image = load_image("Images/spriteLEFT.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (86, 152))
            self.speedx -= self.velocity

        if keys[K_d] and self.rect.x < 1150 and not self.keysstop:
            self.image = load_image("Images/spriteRIGHT.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (87, 152))
            self.speedx += self.velocity

        if keys[pygame.K_SPACE] and not self.keysstop:
            self.jumping = True

        if self.jumping and not self.keysstop:
            if self.jumpCount >= -10:
                self.rect.y -= (self.jumpCount * abs(self.jumpCount)) * 0.4
                self.jumpCount -= 0.6
            else:
                self.jumping = False
                self.jumpCount = 10
                self.rect.y = 553

        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x += self.speedx

    def hide(self):
        self.hidden = True
        self.keysstop = True
        self.hide_timer = pygame.time.get_ticks()
        self.rect.center = (50000, 5000)
