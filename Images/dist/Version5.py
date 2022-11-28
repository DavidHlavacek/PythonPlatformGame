import pygame
import random
from pygame.locals import *
from os import path
import os

def load_image(name):
	image = pygame.image.load(name)
	return image

clock = pygame.time.Clock()

WIDTH = 1270
HEIGHT = 720
FPS = 60
HS_FILE = "highscore.txt"



WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0,0,0)
RED = (255, 0, 0)
SPECIALRED = (255, 111, 97)
CHILLIPEPPER = (155, 27, 48)
gravity = 0.8


pygame.init()
pygame.mixer.init()
#flags = FULLSCREEN | DOUBLEBUF
flags = DOUBLEBUF
screen = pygame.display.set_mode((WIDTH, HEIGHT), flags, 32)
pygame.display.set_caption("SAVANA RUMBLE")
clock = pygame.time.Clock()
screen.set_alpha(None)


player_hearth_img = pygame.image.load(os.path.join("Images/pixelheart.png")).convert_alpha()
player_hearth_img = pygame.transform.scale(player_hearth_img, (63,63))
font_name = pygame.font.match_font('arial')




def load_data(self):

	self.dir = path.dirname(__dirname__)
	with open(path.join(self.dir, HS_FILE), 'w') as f:

		try:


			self.highscore = int(f.read())



		except:


			self.highscore = 0



def draw_text(surf, text, size, x, y):

	font = pygame.font.Font(font_name, size)
	text_surface = font.render(text, True, SPECIALRED)
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x, y)
	surf.blit(text_surface, text_rect)

def draw_text2(surf, text, size, x, y):

	font = pygame.font.Font(font_name, size)
	text_surface = font.render(text, True, WHITE)
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x, y)
	surf.blit(text_surface, text_rect)


def draw_text3(surf, text, size, x, y):

	font = pygame.font.Font(font_name, size)
	text_surface = font.render(text, True, CHILLIPEPPER)
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x, y)
	surf.blit(text_surface, text_rect)




def newmob():

	m = Mob()
	all_sprites.add(m)
	mobs.add(m)
	m2 = Mob2()
	all_sprites.add(m2)
	mobs.add(m2)


		

def draw_shield_bar(surf, x,y, pct):

	if pct < 0:
		pct = 0

	BAR_LENGTH = 250
	BAR_HEIGHT = 25
	fill = (pct / 100) * BAR_LENGTH
	outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
	fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
	pygame.draw.rect(surf, RED, fill_rect)
	pygame.draw.rect(surf, WHITE, outline_rect, 2)
	
			

def draw_lives(surf, x, y, lives, img):


	for i in range(lives):

		img_rect = img.get_rect()
		img_rect.x = x + 50 * i
		img_rect.y = y
		surf.blit(img, img_rect)




class Player(pygame.sprite.Sprite):

	def __init__(self):

		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("Images/spriteHITBOX.png").convert_alpha()
		self.image = pygame.transform.scale(self.image, (115,144))

		#self.rect = pygame.Rect(90, 10, 75, 230)
		self.rect = self.image.get_rect()
		
		self.radius = pygame.draw.rect(self.image, GREEN, self.rect, 2)
		self.rect.x = WIDTH /2
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


		
		#self.shooting = False

	

		



	def update(self):

		self.keysstop = False

		if self.hidden and pygame.time.get_ticks() - self.hide_timer >= 1000:

			self.hidden = False
			self.rect.x = WIDTH /2 
			self.rect.y = 553
			self.keysstop = True
			
		self.keysstop = False

		self.image = pygame.image.load("Images/spriteSTILL.png").convert_alpha()
		self.image = pygame.transform.scale(self.image, (115,144))
		#self.radius = pygame.draw.rect(self.image, GREEN, self.image.get_rect(), 2)
		
		self.speedx = 0 

		keys = pygame.key.get_pressed()

		if keys[K_a] and self.rect.x > 10 and self.keysstop == False:
			self.image = pygame.image.load("Images/spriteLEFT.png").convert_alpha()
			self.image = pygame.transform.scale(self.image, (86,152))
			#self.radius = pygame.draw.rect(self.image, GREEN, self.image.get_rect(), 2)
			self.speedx -= self.velocity

		if keys[K_d] and self.rect.x < 1150 and self.keysstop == False:
			self.image = pygame.image.load("Images/spriteRIGHT.png").convert_alpha()
			self.image = pygame.transform.scale(self.image, (87,152))
			#self.radius = pygame.draw.rect(self.image, GREEN, self.image.get_rect(), 2)
			self.speedx += self.velocity
		
				
		if keys[pygame.K_SPACE] and self.keysstop == False:


			self.jumping = True



		if self.jumping == True and self.keysstop == False:



			if self.jumpCount >= -10:
				self.rect.y -= (self.jumpCount * abs(self.jumpCount)) * 0.4
				self.jumpCount -= 0.6
 
			else:
				self.jumping = False
				self.jumpCount = 10
				self.rect.y = 553
				


		self.mask = pygame.mask.from_surface(self.image)



		self.rect.x += self.speedx

		#if self.rect.right > WIDTH:
			#self.rect.right = WIDTH
		#if self.rect.left < 0:
		#	self.rect.left = -50





	def hide(self):


		self.hidden = True
		self.keysstop = True
		self.hide_timer = pygame.time.get_ticks()
		self.rect.center = (50000, 5000)
			


class Mob(pygame.sprite.Sprite):

	def __init__(self):
		#"C:/Users/Lenovo/Documents/Python_Game/Images/asteroid111.jpg",
		meteor_images = []
		meteor_list = ["Images/asteroid.png",   
				"Images/asteroid333.png"]

		
		pygame.sprite.Sprite.__init__(self)
		for img in meteor_list:
			meteor_images.append(pygame.image.load(img).convert_alpha())
		self.image_orig = random.choice(meteor_images)
		
		self.image_orig = pygame.transform.scale(self.image_orig, (93,77))

		self.image = self.image_orig.copy()
		self.image = pygame.transform.scale(self.image, (93,77))
		self.rect = pygame.Rect(1, 1, 55, 115)
		self.rect = self.image_orig.get_rect()
		#self.radius = pygame.draw.rect(self.image_orig, GREEN, self.image_orig.get_rect(), 2)

		self.rect.x = random.randrange(WIDTH - self.rect.width)
		self.rect.y = random.randrange(-2000, -300)
		self.speedy = random.randrange(2, 13)
		self.speedx = random.randrange(-5, 5)
		self.rot = 0
		self.rot_speed = random.randrange(-8, 8)
		self.last_update = pygame.time.get_ticks()
		self.damage = 30
		# if self.speedx < 0:
		# 	self.image = pygame.image.load("C:/Users/Lenovo/Documents/Python_Game/Images/Fireball.png")
		# if self.speedx > 0:
		# 	self.image = pygame.image.load("C:/Users/Lenovo/Documents/Python_Game/Images/Fireball.png")
		# if self.speedx == 0:
		# 	self.image = pygame.image.load("C:/Users/Lenovo/Documents/Python_Game/Images/Fireball.png")
	
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

		#self.radius = pygame.draw.rect(self.image, GREEN, self.image.get_rect(), 2)
		
		self.rect.y += self.speedy
		self.rect.x += self.speedx

		now = random.randrange(0, 101)
		
		self.mask = pygame.mask.from_surface(self.image)
		if self.rect.top > HEIGHT + 10 or self.rect.x < -25 or self.rect.x > WIDTH + 20:
			self.rect.x = random.randrange(WIDTH - self.rect.width)
			self.rect.y = random.randrange(-2000, -300)
			self.speedy = random.randrange(2, 8)
			self.speedx = random.randrange(-5, 5)
			
			#plusminus = random.randrange(1,3)
			
			# self.speedxx = random.randrange(0,7)
			# if plusminus == 1:
			# 	self.speedx = -self.speedxx
			# if plusminus == 2:
			# 	self.speedx = +self.speedxx
		


class Mob2(pygame.sprite.Sprite):

	def __init__(self):
		
		
		
		
		
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("Images/projectileee.png").convert_alpha()
		self.image = pygame.transform.scale(self.image, (80,30))
		self.rect = self.image.get_rect()
		# self.radius = pygame.draw.rect(self.image, GREEN, self.image.get_rect(), 2)
		self.position = 0
		self.rect.x = random.randrange(-2500, -1000)
		self.rect.y =  random.randrange(450,656)
		if self.rect.y >= 605:
			self.position = 1
			self.positionUP = random.randrange(520,580)
		elif self.rect.y <= 500:
			self.position = 2
			self.positionDOWN = random.randrange(590,640)
		
		self.speedy = random.randrange(-3, 3)
		self.speedx = 5
		self.damage = 20

	def update(self):
		
		self.mask = pygame.mask.from_surface(self.image)
		
		# test = 1
		
		if 449 <= self.rect.y <= 656 and self.rect.x >= 0:

			

			
		# 	self.rect.y += self.speedy
				

			if self.position == 1:

				
				if self.rect.y >= self.positionUP:

					self.rect.y += random.randrange(-3, 0)

				else:

					self.rect.y += 0

				

				if self.rect.y <= 500:

					

					self.position == 2



				# position = random.randrange(525, 599)

				# if self.rect.y == position:
				# 	self.rect.y += 0
				test = 1

			
			if self.position == 2:

				if self.rect.y <= self.positionDOWN:

					self.rect.y += random.randrange(0, 3)

				else:

					self.rect.y += 0

				

				if self.rect.y >= 645:

					

					self.position == 1

			position2 = random.randrange(525, 599)

			if self.rect.y == position2:
				self.rect.y += 0
				test = 1

				

		self.rect.x += self.speedx

		if self.rect.x > WIDTH + 20 or self.rect.top > HEIGHT + 10:
			self.rect.x = random.randrange(-10000,-2000 )
			self.rect.y =  random.randrange(450,656)
			if self.rect.y >= 605:
				self.position = 1
				self.positionUP = random.randrange(520,580)
			elif self.rect.y <= 500:
				self.position = 2
				self.positionDOWN = random.randrange(590,680)
			
			self.speedy = random.randrange(-3, 3)
			self.speedx = 5


		

			
			
				

class Mob3(pygame.sprite.Sprite):

	def __init__(self):

	
		pygame.sprite.Sprite.__init__(self)
		self.images = []
		self.images.append(load_image("Images/whitespikefinalhalf.png").convert_alpha())
		self.images.append(load_image("Images/piques.png").convert_alpha())
		#self.image = pygame.image.load("C:/Users/Lenovo/Documents/Python_Game/Images/whitespikefinalhalf.png")
		#self.image = pygame.transform.scale(self.image, (1282, 227))
		#self.image = pygame.transform.scale(self.image, (1282, 25))
		#self.rect = self.image.get_rect()
		#self.radius = pygame.draw.rect(self.image, GREEN, self.image.get_rect(), 2)

		
		
		self.index = 0
		self.image = self.images[self.index]
		self.counter = 0
		self.limit = 0
		self.spike = False
		
		
		#self.rect = pygame.Rect(5, 5, 1282, 25)

	def update(self):

		
		global spike
		norepeat = False
		

		self.limit += 1
		if self.limit <= 45:
			self.counter +=1
			if self.counter >= 10:
				self.counter = 0
				self.index += 1
			if self.index >= 2:
				self.index = 0
			self.image = self.images[self.index]
			self.image = pygame.transform.scale(self.image, (1282, 25))
			#self.radius = pygame.draw.rect(self.image, GREEN, self.image.get_rect(), 2)	
			self.rect = self.image.get_rect()	
			self.rect.x = -5
			self.rect.y = 672
			spike = False
			
			
			
		else:
			self.rect.x = -1000
			self.rect.y = -1000
			spike = True
			self.kill()
			
		

		

		
			
			
		




		

spike = Mob3()

class Mob4(pygame.sprite.Sprite):

	def __init__(self):

		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("Images/whitespikefinal22.png").convert_alpha()
		self.image = pygame.transform.scale(self.image, (1282, 38))
		#self.radius = pygame.draw.rect(self.image, GREEN, self.image.get_rect(), 2)
		self.rect = self.image.get_rect()
		self.rect.x = -1000
		self.rect.y = -1000
		self.stop = 0
		self.stop2 = 0
		self.damage = 10
		
	def update(self):

		self.mask = pygame.mask.from_surface(self.image)

		if spike == True:

			

			self.stop += 1

			if self.stop <= 14:


				self.rect.x = -5
				self.rect.y = 660
				
			else:

				self.stop2 += 1
				self.image = pygame.image.load("Images/whitespikefinalhalf.png").convert_alpha()
				self.image = pygame.transform.scale(self.image, (1282, 25))
				self.rect.x = -5
				self.rect.y = 672 

				if self.stop2 > 2:

					self.rect.x = -1000
					self.rect.y = -1000
					self.kill()

					

		





				
# meteor_images = []
# meteor_images_mask = pygame.mask.from_surface(meteor_images)





	




		
	

	
		
		
		
		





#==================================================================

# 		self.image = pygame.image.load("C:/Users/Lenovo/Documents/Python_Game/Images/whitespikefinalhalf.png")
#  		self.image = pygame.transform.scale(self.image, (1282, 25))
#		self.rect.x = -5
#		self.rect.y = 660


#==================================================================




# my_sprite = Mob3()
# my_group = pygame.sprite.Group(my_sprite)




				





	

background = pygame.image.load("Images/background.jpg").convert_alpha()



game_over = True



running = True

xx = 0
m3 = Mob3()
m4 = Mob4()
yy = 0





while running:


	def show_go_screen():

		global start
		keys = pygame.key.get_pressed()
		screen.blit(background, (0,0) )
		draw_text(screen, "SAVANA RUMBLE!", 65, WIDTH / 2, HEIGHT / 4)
		draw_text(screen, "A and D to move, spacebar to jump", 30, 
				  WIDTH/2, HEIGHT/2)
		draw_text2(screen, "Rules: ", 35, 200, 20)
		draw_text2(screen, "- Avoid the comets and the bullets !", 21, 200, 100)
		draw_text2(screen, "- Watchout for the spikes coming from the ground !", 21, 205, 140)
		draw_text2(screen, "(They will flash red before they", 21, 200, 165)
		draw_text2(screen, "can hurt you -- JUMP !)", 21, 200, 190)
		draw_text2(screen, "- The MORE you get hit, the HARDER it gets", 21, 200,230)
		draw_text2(screen, "- Last as long as possible ! HAVE FUN !", 21, 200,270)
		draw_text(screen, "Press  SPACE  to begin", 25, WIDTH/2, HEIGHT*3/4)
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



	
	if game_over:
		show_go_screen()

		game_over = False 
		all_sprites = pygame.sprite.Group()
		mobs = pygame.sprite.Group()

		player = Player()
		all_sprites.add(player)

		for i in range(10):

			m = Mob()
			all_sprites.add(m)
			mobs.add(m)


		for i in range(2):

			m2 = Mob2()
			all_sprites.add(m2)
			mobs.add(m2)


		score = 0

	
	

	yy += 1
	xx += 1
	xxx = random.randrange(50, 250)
	xxxx = random.randrange(50, 150)
	xxxxx = random.randrange(0, 1000)
	xxxxxx = random.randrange(2,5)
	clock.tick(FPS)



	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.KEYDOWN:
			if event.type == pygame.K_w:

				Player().jumping = True

	

	
	# print(Mob3().update())
	# print(Mob4().update())
	
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

	# 	all_sprites.remove(m3)
	# 	all_sprites.remove(m4)
	# 	mobs.remove(m4)

		

		

	# my_group.update()
	# my_group.draw(screen)
	# pygame.display.flip()

	all_sprites.update()

	#Collision => mob hits player

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



		
	screen.blit(background,(0,0))
	all_sprites.draw(screen)
	draw_text2(screen, str((pygame.time.get_ticks() - start)/1000), 50, WIDTH / 2, 10)
	draw_shield_bar(screen, 5, 5, player.shield)
	draw_lives(screen, WIDTH - 162, -1, player.lives, player_hearth_img)
	pygame.display.flip()


pygame.quit()