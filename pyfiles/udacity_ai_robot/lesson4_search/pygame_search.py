import pygame
import sys
from random import randint

class Grid(object):
	def __init__(self):
		self.BLACK = (0,0,0)
		self.WHITE = (255,255,255)
		self.GREEN = (0,255,0)
		self.RED = (255,0,0)
		self.BLUE = (0,255,255)
		self.YELLOW = (255,255,0)

		self.MARGIN = 5
		self.WIDTH = 73
		self.HEIGHT = 73
		self.WINDOW_SIZE = []
		self.grid_map = []

	def up(self,column,row):
		x = self.coordinateX(column)
		y = self.coordinateY(row)
		pygame.draw.line(screen,self.RED,[x,y+self.HEIGHT],[x+(self.WIDTH/2),y], 2)
		pygame.draw.line(screen,self.RED,[x+(self.WIDTH/2),y],[x+self.WIDTH,y+self.HEIGHT], 2)
	
	def down(self, column, row):
		x = self.coordinateX(column)
		y = self.coordinateY(row)
		pygame.draw.line(screen,self.RED,[x,y],[x+(self.WIDTH/2),y+self.HEIGHT], 2)
		pygame.draw.line(screen,self.RED,[x+(self.WIDTH/2),y+self.HEIGHT],[x+self.WIDTH,y], 2)

	def left(self, column, row):
		x = self.coordinateX(column)
		y = self.coordinateY(row)
		pygame.draw.line(screen,self.RED,[x,y],[x+self.WIDTH,y+(self.HEIGHT/2)], 2)
		pygame.draw.line(screen,self.RED,[x+self.WIDTH,y+(self.HEIGHT/2)],[x,y+self.HEIGHT], 2)

	def right(self, column, row):
		x = self.coordinateX(column)
		y = self.coordinateY(row)
		pygame.draw.line(screen,self.RED,[x+self.WIDTH,y],[x,y+(self.HEIGHT/2)], 2)
		pygame.draw.line(screen,self.RED,[x,y+(self.HEIGHT/2)],[x+self.WIDTH,y+self.HEIGHT], 2)

	def coordinateX(self, column):
		return (self.MARGIN+self.WIDTH)*column+self.MARGIN

	def coordinateY(self,row):
		return (self.MARGIN+self.HEIGHT)*row+self.MARGIN

	def draw_grid(self,grid=None):
		if grid:
			self.grid_map = grid
		for row in range(len(self.grid_map)):
			for column in range(len(self.grid_map[0])):
				color = self.grid_map[row][column]
				pygame.draw.rect(screen,color, pygame.Rect([self.coordinateX(column),self.coordinateY(row),self.WIDTH,self.HEIGHT]))

	def draw_path(self,path):
		for row in range(len(path)):
			for column in range(len(path[0])):
				color = self.grid_map[row][column]
				direction = path[row][column]
				pygame.draw.rect(screen,color, pygame.Rect([self.coordinateX(column),self.coordinateY(row),self.WIDTH,self.HEIGHT]))
				if direction == '^':
					self.up(column,row)
				elif direction == 'V':
					self.down(column,row)
				elif direction == '<':
					self.right(column,row)
				elif direction == '>':
					self.left(column,row)

	def use_grid(self):
		W = self.WHITE
		Y = self.YELLOW
		B = self.BLACK
		
		grid_map = [[W,W,W,W,W,W],
					[W,W,W,W,W,W], 
					[W,W,W,W,W,W],
					[W,W,W,W,W,W],
					[W,W,W,W,W,Y]]
		self.grid_map = grid_map
		return grid_map
	
	def fit_window_to_grid(self):
		WIDTH = self.WIDTH
		HEIGHT = self.HEIGHT
		MARGIN = self.MARGIN
		self.WINDOW_SIZE = [len(grid_map[0])*(WIDTH+MARGIN)+MARGIN, len(grid_map)*(HEIGHT+MARGIN)+MARGIN]
		return self.WINDOW_SIZE

class Search(object):
	def __init__(self, grid):
		self.grid = grid.grid_map
		self.BLACK = grid.BLACK
		self.BLUE = grid.BLUE
		self.reset()

	def reset(self):
		#search area
		self.expand = self.grid
		self.frontier = 0

		#close list to prevent node from being searched again open:0, close:1
		self.closed = [[0 for row in range(len(self.grid[0]))] for col in range(len(self.grid))]
		self.closed[0][0] = 1

		#show decided path
		self.action = [[-1 for row in range(len(self.grid[0]))] for col in range(len(self.grid))]
		self.path = [[' ' for row in range(len(self.grid[0]))] for col in range(len(self.grid))]

		#initial
		self.g = 0
		self.x = 0
		self.y = 0

		#goal
		for y in range(len(self.grid[0])):
			for x in range(len(self.grid)):
				if self.grid[x][y] == (255,255,0):
					self.goal = [x,y]

		#movement
		self.motions = [[-1,0],#up
						[0,-1],#left
						[1, 0],#down
						[0, 1]]#right
		self.motion_name = ['^','<','V','>']

	def dijkstra(self):
		g = self.g
		x = self.x
		y = self.y
		open_list = [[g,x,y]]
		found = False
		resign = False
		while found is False and resign is False:
			if open_list:
				open_list.sort()
				node = open_list.pop(0)
				g = node[0]
				x = node[1]
				y = node[2]
				
				#self.expand[x][y] = self.BLUE
				if x == self.goal[0] and y == self.goal[1]:
					print node
					found = True
				else:
					for i in range(len(self.motions)):
						x2 = x + self.motions[i][0]
						y2 = y + self.motions[i][1]
						if x2 >= 0 and x2 < len(self.expand) and y2 >= 0 and y2 < len(self.expand[0]):
							if self.closed[x2][y2] == 0 and self.expand[x2][y2] != self.BLACK:
								g = g+1
								open_list.append([g,x2,y2])
								self.closed[x2][y2] = 1
								self.action[x2][y2] = i
			else:
				print 'no plan found'
				resign = True
		x = self.goal[0]
		y = self.goal[1]
		self.path[x][y] = '*'
		if found:
			while x != self.x or y != self.y:
				x2 = x - self.motions[self.action[x][y]][0]
				y2 = y - self.motions[self.action[x][y]][1]
				self.path[x2][y2] = self.motion_name[self.action[x][y]]
				x = x2
				y = y2
		return self.expand, self.path
	
if __name__ == '__main__':
	grid = Grid()
	
	BLACK = grid.BLACK
	WHITE = grid.WHITE
	WIDTH = grid.WIDTH
	HEIGHT = grid.HEIGHT
	MARGIN = grid.MARGIN
	
	grid_map = grid.use_grid()

	pygame.init()
	
	WINDOW_SIZE = grid.fit_window_to_grid()
	screen = pygame.display.set_mode(WINDOW_SIZE)
	pygame.display.set_caption("wandering renge")
	clock = pygame.time.Clock()

	im = pygame.image.load('renge.png').convert_alpha()
	rect = im.get_rect()
	init_x = 0#randint(0,len(grid_map[0])-1)
	init_y = 0#randint(0,len(grid_map)-1)
	rect.center = (pygame.Rect(grid.coordinateX(init_x),grid.coordinateY(init_y),WIDTH,HEIGHT)).center

	update_flag = False
	motion = [0,0]

	search = Search(grid)

	while True:
		pygame.display.update()
		clock.tick(60)
		screen.fill(BLACK)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					pygame.quit()
					sys.exit()
				if event.key == pygame.K_d:
					new_grid, path = search.dijkstra()
					search.reset()
					update_flag = True
			elif event.type == pygame.MOUSEBUTTONDOWN:
				pos = pygame.mouse.get_pos()
				column = pos[0] // (WIDTH+MARGIN)
				row = pos[1] // (WIDTH+MARGIN)
				if grid.grid_map[row][column] == BLACK:
					grid.grid_map[row][column] = WHITE
				else:
					grid.grid_map[row][column] = BLACK
				new_grid, path = search.dijkstra()
				search.reset()
				update_flag = True

		if update_flag:
			#grid.draw_grid(new_grid)
			grid.draw_path(path)
		else:
			grid.draw_grid()
		screen.blit(im,rect)



