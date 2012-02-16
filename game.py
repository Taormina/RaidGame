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

def draw_tile(display, tile):
	return pygame.draw.rect(display, tile.color, tile.rect)

def main():
	pygame.init()
	DISPLAYSURF = load_surf()
	TILESIZE = 25
	WORLDWIDTH = 400
	WORLDHEIGHT = 300
	pygame.display.set_caption("Raid Game")
	BACKGROUND = []
	test = []
	for x in range(WORLDHEIGHT/TILESIZE):
		bx = []
		for y in range(WORLDWIDTH/TILESIZE):
			bx.append(Tile(x, y, "blue", TILESIZE))
			draw_tile(DISPLAYSURF, bx[-1])
			test.append(bx[-1].rect)
		BACKGROUND.append(bx)
	player = Tile(3, 4, "red", TILESIZE)
	BACKGROUND[5][10].color = pygame.Color("black")
	draw_tile(DISPLAYSURF, BACKGROUND[5][10])
	draw_tile(DISPLAYSURF, player)
	pygame.display.update()
	pygame.key.set_repeat(1,500)
	hitbox = {	2: (-TILESIZE/2, -TILESIZE/2, TILESIZE*2, 2), #up 
			7: (-TILESIZE/2, 1.5*TILESIZE, TILESIZE*2,  2), #down
			4: (1.5*TILESIZE, -TILESIZE/2, 2, TILESIZE*2),  #right
			5: (-TILESIZE/2, -TILESIZE/2, 2, TILESIZE*2)} #left
	prevdir = 5
	while True:  # main game loop
		changed_tiles = []
		changed_rects = []
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == KEYDOWN:
				if (event.key == 273 or event.key == 119) and player.rect.top: #up
					changed_tiles += [player, BACKGROUND[player.rect.top/TILESIZE][player.rect.left/TILESIZE]]
					player.rect.top -= TILESIZE
					prevdir = 2
				elif (event.key == 274 or event.key == 115) and player.rect.bottom != WORLDHEIGHT : #down
					changed_tiles += [player, BACKGROUND[player.rect.top/TILESIZE][player.rect.left/TILESIZE]]
					player.rect.top += TILESIZE
					prevdir = 7
				elif (event.key == 275 or event.key == 100) and player.rect.right != WORLDWIDTH: #right
					changed_tiles += [player, BACKGROUND[player.rect.top/TILESIZE][player.rect.left/TILESIZE]]
					player.rect.left += TILESIZE
					prevdir = 4
				elif (event.key == 276 or event.key == 97) and player.rect.left: #left
					changed_tiles += [player, BACKGROUND[player.rect.top/TILESIZE][player.rect.left/TILESIZE]]
					player.rect.left -= TILESIZE
					prevdir = 5
			elif  event.type == MOUSEBUTTONDOWN:
				if event.button == 1: #left click
					mods = hitbox[prevdir]
					box = pygame.Rect(player.rect.left+mods[0], player.rect.top+mods[1], mods[2], mods[3])
		#			changed_rects.append(box)
		#			pygame.draw.rect(DISPLAYSURF, pygame.Color("pink"), box)
					hits = box.collidelistall(test)
					for index in hits:
						tile = BACKGROUND[index/(WORLDWIDTH/TILESIZE)][index%(WORLDWIDTH/TILESIZE)]
						if tile.color == pygame.Color("black"):
							tile.color = pygame.Color("green")
							changed_tiles.append(tile)
		for tile in changed_tiles:
			draw_tile(DISPLAYSURF, tile)
			changed_rects.append(tile.rect)
		pygame.display.update(changed_rects)
	
main()
