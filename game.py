import pygame, sys
from pygame.locals import *


class Tile(object):
	def __init__(self, x_idx, y_idx, color, TILESIZE):
		self.rect = pygame.Rect(y_idx*TILESIZE, x_idx*TILESIZE, TILESIZE, TILESIZE)
		self.color = pygame.Color(color)
	def __str__(self):
		return rect.__str__()



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
	for x in range(WORLDHEIGHT/TILESIZE):
		bx = []
		for y in range(WORLDWIDTH/TILESIZE):
			bx.append(Tile(x, y, "blue", TILESIZE))
			pygame.draw.rect(DISPLAYSURF, bx[-1].color, bx[-1].rect)
		BACKGROUND.append(bx)
	player = Tile(3, 4, "red", TILESIZE)
	pygame.draw.rect(DISPLAYSURF, player.color, player.rect)
	pygame.display.update()
	pygame.key.set_repeat(1,500)
	while True:  # main game loop
		changed_tiles = []
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == KEYDOWN:
				if event.key == 273 and player.rect.top: #up
					changed_tiles += [player, BACKGROUND[player.rect.top/TILESIZE][player.rect.left/TILESIZE]]
					player.rect.top -= 20
				elif event.key == 274 and player.rect.bottom != WORLDHEIGHT : #down
					changed_tiles += [player, BACKGROUND[player.rect.top/TILESIZE][player.rect.left/TILESIZE]]
					player.rect.top += 20
				elif event.key == 275 and player.rect.right != WORLDWIDTH: #right
					changed_tiles += [player, BACKGROUND[player.rect.top/TILESIZE][player.rect.left/TILESIZE]]
					player.rect.left += 20
				elif event.key == 276 and player.rect.left: #left
					changed_tiles += [player, BACKGROUND[player.rect.top/TILESIZE][player.rect.left/TILESIZE]]
					player.rect.left -= 20
		changed_rects = []
		for tile in changed_tiles:
			pygame.draw.rect(DISPLAYSURF, tile.color, tile.rect)
			changed_rects.append(tile.rect)
		pygame.display.update(changed_rects)
	
main()
