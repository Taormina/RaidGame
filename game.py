import pygame, sys
from pygame.locals import *


class Tile(object):
	def __init__(self, x_idx, y_idx, color, TILESIZE):
		self.rect = pygame.Rect(y_idx*TILESIZE, x_idx*TILESIZE, TILESIZE, TILESIZE)
		self.color = pygame.Color(color)
	def __str__(self):
		return "Player <" + self.rect.__str__() + " " +  self.color.__str__() + ">"

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
	test = []
	for x in range(WORLDHEIGHT/TILESIZE):
		bx = []
		for y in range(WORLDWIDTH/TILESIZE):
			bx.append(Tile(x, y, "blue", TILESIZE))
			pygame.draw.rect(DISPLAYSURF, bx[-1].color, bx[-1].rect)
			test.append(bx[-1].rect)
		BACKGROUND.append(bx)
	player = Tile(3, 4, "red", TILESIZE)
	pygame.draw.rect(DISPLAYSURF, player.color, player.rect)
	pygame.display.update()
	pygame.key.set_repeat(1,500)
	prevdir = 275
	hitbox = {	273: (-10, -10, 40, 2), 
			274: (-10, 30, 40,  2), 
			275: (30, -10, 2, 40), 
			276: (-10, -10, 2, 40)}
	while True:  # main game loop
		changed_tiles = []
		changed_rects = []
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == KEYDOWN:
				if event.key == 273 and player.rect.top: #up
					changed_tiles += [player, BACKGROUND[player.rect.top/TILESIZE][player.rect.left/TILESIZE]]
					player.rect.top -= 20
					prevdir = 273
				elif event.key == 274 and player.rect.bottom != WORLDHEIGHT : #down
					changed_tiles += [player, BACKGROUND[player.rect.top/TILESIZE][player.rect.left/TILESIZE]]
					player.rect.top += 20
					prevdir = 274
				elif event.key == 275 and player.rect.right != WORLDWIDTH: #right
					changed_tiles += [player, BACKGROUND[player.rect.top/TILESIZE][player.rect.left/TILESIZE]]
					player.rect.left += 20
					prevdir = 275
				elif event.key == 276 and player.rect.left: #left
					changed_tiles += [player, BACKGROUND[player.rect.top/TILESIZE][player.rect.left/TILESIZE]]
					player.rect.left -= 20
					prevdir = 276
				elif event.key == 32:
					mods = hitbox[prevdir]
					box = pygame.Rect(player.rect.left+mods[0], player.rect.top+mods[1], mods[2], mods[3])
					hits = box.collidelistall(test)
					for index in hits:
						tile = BACKGROUND[index/20][index%20]
						tile.color = pygame.Color("green")
						changed_tiles.append(tile)
		for tile in changed_tiles:
			pygame.draw.rect(DISPLAYSURF, tile.color, tile.rect)
			changed_rects.append(tile.rect)
		pygame.display.update(changed_rects)
	
main()
