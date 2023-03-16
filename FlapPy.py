import pygame
from sys import exit
import random

pygame.init()

#Window settings:

width = 600
height = 400
screen = pygame.display.set_mode((width, height))
screen.fill((225,235,255))
pygame.display.set_caption('FlapPy')


#Time stuff:

clock = pygame.time.Clock()
framerate = 60;


#Audio
music = pygame.mixer.music.load('jump.wav')
pygame.mixer.music.set_volume(0.2)

#Surface with image:

#Bird
bird_surface = pygame.image.load('bird.png')
#Small intermission to se window image
pygame.display.set_icon(bird_surface)
bird_rect = bird_surface.get_rect(center = (50, 200));

#Top Pipe
pipe_surface_down = pygame.image.load('pipe_down.png').convert_alpha()
pipe_rect_down = pipe_surface_down.get_rect(topleft  = (700, 300))
#Bottom Pipe
pipe_surface_up = pygame.image.load('pipe_up.png').convert_alpha()
pipe_rect_up = pipe_surface_up.get_rect(topleft = (700, -100))

#Top Pipe2
pipe_surface_down2 = pygame.image.load('pipe_down.png').convert_alpha()
pipe_rect_down2 = pipe_surface_down.get_rect(topleft  = (930, 300))
#Bottom Pipe2
pipe_surface_up2 = pygame.image.load('pipe_up.png').convert_alpha()
pipe_rect_up2 = pipe_surface_up.get_rect(topleft = (930, -100))

#Top Pipe3
pipe_surface_down3 = pygame.image.load('pipe_down.png').convert_alpha()
pipe_rect_down3 = pipe_surface_down.get_rect(topleft  = (1160, 300))
#Bottom Pipe3
pipe_surface_up3 = pygame.image.load('pipe_up.png').convert_alpha()
pipe_rect_up3 = pipe_surface_up.get_rect(topleft = (1160, -100))

#Font:
font = pygame.font.Font('font.ttf', 50)
#Text surfaces
score = 0
score_text = font.render(str(score), False, (255,255,255))
score_rect= score_text.get_rect(topleft = (300, 10));

bird_vel = -9;
jump = 9;
grav = 0.4;
lock = 0;
lock2 = 0;
lock3 = 0;
pipe_offset = 0;
pipe_offset2 = 0;
pipe_offset3 = 0;

game_active = False


#Initial Pipe offsets
pipe_offset2 = 0 + random.randrange(-150, 50)
pipe_rect_down2.top = 300 + pipe_offset2
pipe_rect_up2.top = -100 + pipe_offset2

pipe_offset3 = 0 + random.randrange(-150, 50)
pipe_rect_down3.top = 300 + pipe_offset3
pipe_rect_up3.top = -100 + pipe_offset3

#Main Gameplay Loop
while True:
	#Update events:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
		if game_active:
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					bird_vel = -jump;
					pygame.mixer.music.play()
				if event.key == pygame.K_ESCAPE:
					pygame.quit()
					exit()
		else:
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					pipe_rect_down.left = 700
					pipe_rect_up.left = 700
					pipe_rect_down2.left = 930
					pipe_rect_up2.left = 930
					pipe_rect_down3.left = 1160
					pipe_rect_up3.left = 1160
					score = 0
					lock = 0
					bird_vel = 0 - jump
					bird_rect.center = 50, 200
					score_text = font.render(str(score), False, (255,255,255))
					pygame.mixer.music.play()
					game_active = True;
				if event.key == pygame.K_ESCAPE:
					pygame.quit()
					exit()
	
	if game_active:
		#Update game logic
		pipe_rect_down.left -= +4
		pipe_rect_up.left -= +4
		pipe_rect_down2.left -= +4
		pipe_rect_up2.left -= +4
		pipe_rect_down3.left -= +4
		pipe_rect_up3.left -= +4

		bird_vel += grav
		bird_rect.top += bird_vel
			
		if pipe_rect_up.left < -100:
			pipe_rect_up.left = 590
			pipe_rect_down.left = 590
			lock = 0
			pipe_offset = 0 + random.randrange(-150, 50)
			pipe_rect_down.top = 300 + pipe_offset
			pipe_rect_up.top = -100 + pipe_offset

		if pipe_rect_up2.left < -100:
			pipe_rect_up2.left = 590
			pipe_rect_down2.left = 590
			lock2 = 0
			pipe_offset2 = 0 + random.randrange(-150, 50)
			pipe_rect_down2.top = 300 + pipe_offset2
			pipe_rect_up2.top = -100 + pipe_offset2

		if pipe_rect_up3.left < -100:
			pipe_rect_up3.left = 590
			pipe_rect_down3.left = 590
			lock3 = 0
			pipe_offset3 = 0 + random.randrange(-150, 50)
			pipe_rect_down3.top = 300 + pipe_offset3
			pipe_rect_up3.top = -100 + pipe_offset3
		
		if pipe_rect_up.left < 25 and not lock:
			score += 1
			score_text = font.render(str(score), False, (255,255,255))
			lock = 1
		if pipe_rect_up2.left < 25 and not lock2:
			score += 1
			score_text = font.render(str(score), False, (255,255,255))
			lock2 = 1
		if pipe_rect_up3.left < 25 and not lock3:
			score += 1
			score_text = font.render(str(score), False, (255,255,255))
			lock3 = 1


		#Draw eleents
		#Clears screen
		screen.fill((225,235,255))
		#Draw elements
	
		#Pipes
		screen.blit(pipe_surface_down, pipe_rect_down)
		screen.blit(pipe_surface_up, pipe_rect_up)

		#Pipes
		screen.blit(pipe_surface_down2, pipe_rect_down2)
		screen.blit(pipe_surface_up2, pipe_rect_up2)

		#Pipes
		screen.blit(pipe_surface_down3, pipe_rect_down3)
		screen.blit(pipe_surface_up3, pipe_rect_up3)
		#Bird
		screen.blit(bird_surface, bird_rect)

		screen.blit(score_text, score_rect)

		if(bird_rect.colliderect(pipe_rect_up) or bird_rect.colliderect(pipe_rect_down)
			or bird_rect.colliderect(pipe_rect_up2) or bird_rect.colliderect(pipe_rect_down2)
			or bird_rect.colliderect(pipe_rect_up3) or bird_rect.colliderect(pipe_rect_down3)):
			lock = 1;
			game_active = False
		if bird_rect.bottom > 400 or  bird_rect.bottom < 10:
			lock = 1;
			game_active = False

	else:
		screen.blit(bird_surface, bird_rect)
		screen.blit(score_text, score_rect)
		#Clears screen
		screen.fill((225,235,255))
		#Draw elements
		#Pipes
		screen.blit(pipe_surface_down, pipe_rect_down)
		screen.blit(pipe_surface_up, pipe_rect_up)

		#Pipes
		screen.blit(pipe_surface_down2, pipe_rect_down2)
		screen.blit(pipe_surface_up2, pipe_rect_up2)

		#Pipes
		screen.blit(pipe_surface_down3, pipe_rect_down3)
		screen.blit(pipe_surface_up3, pipe_rect_up3)
		screen.blit(bird_surface, bird_rect)
		if lock:
			screen.blit(score_text, score_rect)

	#update elements
	pygame.display.update()

	#Time
	clock.tick(framerate);