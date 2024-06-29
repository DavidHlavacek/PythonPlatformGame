import pygame
import random
from pygame.locals import *
from settings import *
from player import Player
from mob import Mob, Mob2, Mob3, Mob4
from utils import load_image, draw_text, draw_text2, draw_shield_bar, draw_lives

pygame.init()
pygame.mixer.init()
flags = FULLSCREEN | DOUBLEBUF
screen = pygame.display.set_mode((WIDTH, HEIGHT), flags, 32)
pygame.display.set_caption("SAVANA RUMBLE")
clock = pygame.time.Clock()
screen.set_alpha(None)

background = load_image("Images/background.jpg")
player_hearth_img = load_image("Images/pixelheart.png")
player_hearth_img = pygame.transform.scale(player_hearth_img, (63, 63))
font_name = pygame.font.match_font('arial')

def newmob():
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)
    m2 = Mob2()
    all_sprites.add(m2)
    mobs.add(m2)

def show_go_screen():
    global start
    keys = pygame.key.get_pressed()
    screen.blit(background, (0, 0))
    draw_text(screen, "SAVANA RUMBLE!", 65, WIDTH / 2, HEIGHT / 4)
    draw_text(screen, "A and D to move, SPACEBAR to jump", 30, WIDTH / 2, HEIGHT / 2)
    draw_text2(screen, "Rules: ", 35, 200, 20)
    draw_text2(screen, "- Avoid the comets and the bullets!", 21, 200, 100)
    draw_text2(screen, "- Watch out for the spikes coming from the ground!", 21, 205, 140)
    draw_text2(screen, "(They will flash red before they", 21, 200, 165)
    draw_text2(screen, "can hurt you -- JUMP!)", 21, 200, 190)
    draw_text2(screen, "- The MORE you get hit, the HARDER it gets", 21, 200, 230)
    draw_text2(screen, "- Last as long as possible! HAVE FUN!", 21, 200, 270)
    draw_text(screen, "Press SPACE to begin", 25, WIDTH / 2, HEIGHT * 3 / 4)
    pygame.display.flip()
    waiting = True
    while waiting:
        start = pygame.time.get_ticks()
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False

game_over = True
running = True
xx = 0
yy = 0

while running:
    if game_over:
        show_go_screen()
        game_over = False
        all_sprites = pygame.sprite.Group()
        mobs = pygame.sprite.Group()
        player = Player()
        all_sprites.add(player)
        for i in range(10):
            newmob()
        score = 0

    yy += 1
    xx += 1
    xxx = random.randrange(50, 250)
    xxxx = random.randrange(50, 150)
    xxxxx = random.randrange(0, 1000)
    xxxxxx = random.randrange(2, 5)
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.type == pygame.K_w:
                player.jumping = True

    if xx >= (100 + xxx + xxxx + xxxxx) * xxxxxx:
        xx = 0
        m3 = Mob3()
        all_sprites.add(m3)
        m4 = Mob4()
        all_sprites.add(m4)
        mobs.add(m4)

    yy += 1
    if yy >= 500:
        yy = 0

    all_sprites.update()

    hits = pygame.sprite.spritecollide(player, mobs, True, pygame.sprite.collide_mask)
    for hit in hits:
        player.shield -= hit.damage
        newmob()
        if player.shield <= 0:
            player.hide()
            player.lives -= 1
            player.shield = 100

    if player.lives == 0:
        game_over = True

    screen.blit(background, (0, 0))
    all_sprites.draw(screen)
    draw_text2(screen, str((pygame.time.get_ticks() - start) / 1000), 50, WIDTH / 2, 10)
    draw_shield_bar(screen, 5, 5, player.shield)
    draw_lives(screen, WIDTH - 162, -1, player.lives, player_hearth_img)
    pygame.display.flip()

pygame.quit()
