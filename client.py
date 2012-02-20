import pygame, sys, socket
from pygame.locals import *


class Tile(object):
	def __init__(self, x_idx, y_idx, color, TILESIZE):
		self.rect = pygame.Rect(y_idx*TILESIZE, x_idx*TILESIZE, TILESIZE, TILESIZE)
		self.color = pygame.Color(color)
	def __str__(self):
		return "Player <" + self.rect.__str__() + " " +  self.color.__str__() + ">"

def draw_tile(surf, tile):
	return pygame.draw.rect(surf, tile.color, tile.rect)

def mouse_dir(tile, x, y):
	coord = pygame.mouse.get_pos()
	coord = [coord[0]-x, coord[1]-y]
	if coord[0] < tile.rect.left:
		dr = 1
	elif coord[0] > tile.rect.right:
		dr = 3
	else:
		dr = 2
	if coord[1] < tile.rect.top:
		dr += 0
	elif coord[1] > tile.rect.bottom:
		dr += 6
	else:
		dr += 3
	return dr

def main():
	pygame.init()
	SCREENWIDTH = 400
	SCREENHEIGHT = 300
	TILESIZE = 20
	WORLDWIDTH = 4000
	WORLDHEIGHT = 3000
	map_x = 0
	map_y = 0
	DISPLAYSURF = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
	pygame.display.set_caption("Raid Game")
	world = pygame.Surface((WORLDWIDTH, WORLDHEIGHT))
	world = world.convert()
	BACKGROUND = []
	test = []

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(("",3496))
	s.shutdown(socket.SHUT_RDWR)
	s.close()

	for x in range(WORLDHEIGHT/TILESIZE):
		bx = []
		for y in range(WORLDWIDTH/TILESIZE):
			bx.append(Tile(x, y, "blue", TILESIZE))
			draw_tile(world, bx[-1])
			test.append(bx[-1].rect)
		BACKGROUND.append(bx)
	player = Tile(3, 4, "red", TILESIZE)
	BACKGROUND[5][10].color = pygame.Color("black")
	draw_tile(world, BACKGROUND[5][10])
	draw_tile(world, player)
	DISPLAYSURF.blit(world, (map_x, map_y, SCREENWIDTH, SCREENHEIGHT))
	pygame.display.flip()
	pygame.key.set_repeat(1,100)
	hitbox = {	2: (-TILESIZE/2, -TILESIZE/2, TILESIZE*2, 2),      #up 
			8: (-TILESIZE/2, 1.5*TILESIZE, TILESIZE*2,  2),    #down
			6: (1.5*TILESIZE, -TILESIZE/2, 2, TILESIZE*2),     #right
			4: (-TILESIZE/2, -TILESIZE/2, 2, TILESIZE*2),      #left
			1: (-TILESIZE/2, -TILESIZE/2, TILESIZE, TILESIZE), #up/left
			7: (-TILESIZE/2, TILESIZE/2, TILESIZE, TILESIZE),  #up/right
			3: (TILESIZE/2, -TILESIZE/2, TILESIZE, TILESIZE),  #down/left
			9: (TILESIZE/2, TILESIZE/2, TILESIZE, TILESIZE) }  #down/right 
	while True:  # main game loop
		changed_tiles = []
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == KEYDOWN:
				if (event.key == 273 or event.key == 119) and player.rect.top: #up
					changed_tiles += [player, BACKGROUND[player.rect.top/TILESIZE][player.rect.left/TILESIZE]]
					player.rect.top -= TILESIZE
					map_y += TILESIZE
				elif (event.key == 274 or event.key == 115) and player.rect.bottom != WORLDHEIGHT : #down
					changed_tiles += [player, BACKGROUND[player.rect.top/TILESIZE][player.rect.left/TILESIZE]]
					player.rect.top += TILESIZE
					map_y -= TILESIZE
				elif (event.key == 275 or event.key == 100) and player.rect.right != WORLDWIDTH: #right
					changed_tiles += [player, BACKGROUND[player.rect.top/TILESIZE][player.rect.left/TILESIZE]]
					player.rect.left += TILESIZE
					map_x -= TILESIZE
				elif (event.key == 276 or event.key == 97) and player.rect.left: #left
					changed_tiles += [player, BACKGROUND[player.rect.top/TILESIZE][player.rect.left/TILESIZE]]
					player.rect.left -= TILESIZE
					map_x += TILESIZE
			elif  event.type == MOUSEBUTTONDOWN:
				if event.button == 1: #left click
					dr = mouse_dir(player, map_x, map_y)
					if dr != 5:
						mods = hitbox[dr]
						box = pygame.Rect(player.rect.left+mods[0], player.rect.top+mods[1], mods[2], mods[3])
					#	pygame.draw.rect(world, pygame.Color("pink"), box) # this is the line that makes hitboxes visible
						hits = box.collidelistall(test)
						for index in hits:
							tile = BACKGROUND[index/(WORLDWIDTH/TILESIZE)][index%(WORLDWIDTH/TILESIZE)]
							if tile.color == pygame.Color("black"):
								tile.color = pygame.Color("green")
								changed_tiles.append(tile)
		for tile in changed_tiles:
			draw_tile(world, tile)
		DISPLAYSURF.blit(world, (map_x, map_y, SCREENWIDTH, SCREENHEIGHT))
		pygame.display.flip()
	
main()
