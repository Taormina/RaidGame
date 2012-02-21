import pygame, socket

class Tile(object):
	def __init__(self, x_idx, y_idx, color, TILESIZE):
		self.rect = pygame.Rect(y_idx*TILESIZE, x_idx*TILESIZE, TILESIZE, TILESIZE)
		self.color = pygame.Color(color)
	def __str__(self):
		return "Player <" + self.rect.__str__() + " " +  self.color.__str__() + ">"

def draw_tile(surf, tile):
	return pygame.draw.rect(surf, tile.color, tile.rect)

pygame.init()
TILESIZE = 20
WORLDWIDTH = 4000
WORLDHEIGHT = 3000

world = pygame.Surface((WORLDWIDTH, WORLDHEIGHT))
#world = world.convert()
BACKGROUND = []
test = []

for x in range(WORLDHEIGHT/TILESIZE):
	bx = []
	for y in range(WORLDWIDTH/TILESIZE):
		bx.append(Tile(x, y, "blue", TILESIZE))
		draw_tile(world, bx[-1])
		test.append(bx[-1].rect)
	BACKGROUND.append(bx)

