import pygame, sys
from pygame.locals import *

pygame.init()
SCREENWIDTH = 400
SCREENHEIGHT = 300
DISPLAYSURF = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption("Raid Game")
rect = pygame.Rect(200,160,20,20)
pygame.key.set_repeat(1,500)
while True:  # main game loop
	pygame.draw.rect(DISPLAYSURF, pygame.Color("black"), rect)
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == KEYDOWN:
			if event.key == 273 and rect.top: #up
				rect = rect.move(0,-20)
			elif event.key == 274 and rect.bottom != SCREENHEIGHT : #down
				rect = rect.move(0,20)
			elif event.key == 275 and rect.right != SCREENWIDTH: #right
				rect = rect.move(20,0)
			elif event.key == 276 and rect.left: #left
				rect = rect.move(-20,0)
	pygame.draw.rect(DISPLAYSURF, pygame.Color("red"), rect)
	pygame.display.update()


