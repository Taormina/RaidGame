import pygame, sys
from pygame.locals import *


class Player(object):
	def __init__(self, x_idx, y_idx, color):
		self.rect = pygame.Rect(y_idx, x_idx, TILESIZE, TILESIZE)
		self.color = color
	def __str__(self):
		return "Player <" + self.rect.__str__() + " " + color + ">"

def load_surf():
	SCREENWIDTH = 400
	SCREENHEIGHT = 300
	return pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))

def main():
	pygame.init()
	DISPLAYSURF = load_surf()
	TILESIZE = 20
	WORLDWIDTH = 400
	WORLDHEIGHT = 300
	pygame.display.set_caption("Raid Game")
	BACKGROUND = []
	for x in range(WORLDWIDTH/TILESIZE):
		bx = []
		for y in range(WORLDHEIGHT/TILESIZE):
			bx.append(pygame.Rect(y*TILESIZE,x*TILESIZE,TILESIZE,TILESIZE))
		BACKGROUND.append(bx)
	
	pygame.key.set_repeat(1,500)
	while True:  # main game loop
		changed_rects = []
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == KEYDOWN:
				if event.key == 273 and rect.top: #up
					rect = rect.move(0,-20)
				elif event.key == 274 and rect.bottom != WORLDHEIGHT : #down
					rect = rect.move(0,20)
				elif event.key == 275 and rect.right != WORLDWIDTH: #right
					rect = rect.move(20,0)
				elif event.key == 276 and rect.left: #left
					rect = rect.move(-20,0)
		pygame.draw.rect(DISPLAYSURF, pygame.Color("red"), BACKGROUND[0][0])
		pygame.display.update(changed_rects)
	
main()
