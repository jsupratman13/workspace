import pygame
import sys
from random import randint


class Grid(object):
	def __init__(self):
		self.BLACK = (0,0,0)
		self.WHITE = (255,255,255)
		self.GREEN = (0,255,0)
		self.RED = (255,0,0)
		self.BLUE = (0,0,255)
		self.YELLOW = (255,255,0)

		self.MARGIN = 5
		self.WIDTH = 73
		self.HEIGHT = 73
		self.WINDOW_SIZE = []
		self.grid_map = []

	def coordinateX(self, column):
		return (self.MARGIN+self.WIDTH)*column+self.MARGIN

	def coordinateY(self,row):
		return (self.MARGIN+self.HEIGHT)*row+self.MARGIN

	def get_color(self,x,y):
		for row in range(len(grid_map)):
			for column in range(len(grid_map[0])):
				cell = pygame.Rect([self.coordinateX(column),self.coordinateY(row), self.WIDTH, self.HEIGHT])
				if cell.collidepoint(x,y):
					return grid_map[row][column]

	def draw_grid(self):
		for row in range(len(grid_map)):
			for column in range(len(grid_map[0])):
				color = grid_map[row][column]
				pygame.draw.rect(screen,color, pygame.Rect([self.coordinateX(column),self.coordinateY(row),self.WIDTH,self.HEIGHT]))

	def use_grid(self):
		W = self.WHITE
		Y = self.YELLOW
		B = self.BLACK
		
		grid_map = [[W,B,W,W,W,W],
                            [W,B,W,W,W,W],
                            [W,B,W,W,W,W],
                            [W,B,W,W,W,W],
			    [W,W,W,W,B,Y]]
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
		#search area
		self.expand = grid
		self.frontier = 0

		#close list to prevent node from being searched again open:0, close:1
		self.closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
		self.closed[0][0] = 1

		#show decided path
		self.action = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]

		#initial
		self.g = 0
		self.x = 0
		self.y = 0

		#goal
		for y in range(len(grid[0])):
			for x in range(len(grid)):
				if grid[x][y] == (255,255,0):
					self.goal = [x,y]

		#movement
		self.motions = [[-1,0],#up
		                [0,-1],#left
				[1, 0],#down
				[0, 1]]#right

	def dijkstra(self):
		g = self.g
		x = self.x
		y = self.y
		open_list = [[g,x,y]]
		found = False
		resing = False
		while found is False and resign is False:
			if open_list:
				open_list.sort()
				node = open_list.pop(0)
				g = node[0]
				x = node[1]
				y = node[2]

				self.expand[x][y] = (0,255,255)
				if x == self.goal[0] and y == self.goal[y]:
					found = True
				else:
					for i in range(len(self.motions)):
						x = x + self.motions[i][0]
						y = y + self.motions[i][1]
						if x >= 0 and x < len(self.expand) and y >= 0 and y < len(self.expand[0]):
							if self.closed[x][y] == 0 and self.expand != (0,0,0):
								g = g+1
								open_list.append([g,x,y])
								self.closed[x][y] = 1
								self.action[x][y] = i
			else:
				print 'no plan found'
				resign = True
		return self.expand
	
	def greedy(self):
		pass

	def astar(self):
		pass


if __name__ == '__main__':
	grid = Grid()
	
	BLACK = grid.BLACK
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

	search = Search(grid_map)

	while True:
		pygame.display.update()
		clock.tick(60)
		screen.fill(BLACK)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				update_flag = True
				if event.key == pygame.K_ESCAPE:
					pygame.quit()
					sys.exit()
				if event.key == pygame.K_LEFT: rect.move_ip(-WIDTH-MARGIN,0); motion = [0,-1]
				elif event.key == pygame.K_RIGHT: rect.move_ip(WIDTH+MARGIN,0); motion = [0, 1]
				elif event.key == pygame.K_UP: rect.move_ip(0,-HEIGHT-MARGIN); motion = [-1, 0]
				elif event.key == pygame.K_DOWN: rect.move_ip(0,HEIGHT+MARGIN); motion = [1, 0]
				else: motion = [0,0]
		grid.draw_grid()

		if rect.centerx > WINDOW_SIZE[0]: rect.centerx = (grid.coordinateX(0)+WIDTH/2)
		if rect.centerx < 0: rect.centerx = (grid.coordinateX(len(grid_map[0])-1)+WIDTH/2)
		if rect.centery > WINDOW_SIZE[1]: rect.centery = (grid.coordinateY(0)+HEIGHT/2)
		if rect.centery < 0: rect.centery = (grid.coordinateY(len(grid_map)-1)+HEIGHT/2)
		screen.blit(im,rect)

		update_flag = False



