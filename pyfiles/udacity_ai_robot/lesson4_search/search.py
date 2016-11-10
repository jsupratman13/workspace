#  0 1 2 3 4 5
# |-|-|-|-|-|-|
#0|s| |#| | | |
# |-|-|-|-|-|-|
#1| | |#| | | |
# |-|-|-|-|-|-|
#2| | | | |#| |
# |-|-|-|-|-|-|
#3| | |#|#|#| |
# |-|-|-|-|-|-|
#4| | | | |#|g|
# |-|-|-|-|-|-|

#Grid formt: 
#	0 = Navigable Space
#	1 = Occupied Space

grid = [[0, 0, 1, 0, 0, 0],
	[0, 0, 1, 0, 0, 0],
	[0, 0, 0, 0, 1, 0],
	[0, 0, 1, 1, 1, 0],
	[0, 0, 0, 0, 1, 0]]

init = [0,0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], #go up
	 [ 0,-1], #go left
	 [ 1, 0], #go down
	 [ 0, 1]] #go right

delta_name = ['^', '<', 'V', '>']


def search(grid, init, goal, cost):
	#open list elements are of type [g,x,y]

	expand = [[-1 for row in range(len(grid[0]))]for col in range(len(grid))]
	index = 0
	#get closed grid to prevent node from being checked again, 0 for open, 1 for closed
	closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
	closed[init[0]][init[1]] = 1
	#path
	path = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]

	x = init[0]
	y = init[1]
	g = 0

	open = [[g,x,y]]
	
	found = False #flag is set when search complete
	resign = False #flag when we cant find expand

	#print 'initial open list:'
	#for i in range(len(open)):
		#print '	', open[i]
	#print '--------'

	while found is False and resign is False:
		#check if we still have elements on the open list
		if len(open) == 0:
			resign = True
			print 'fail'
		
		else:
			#remove node from list
			open.sort()
			open.reverse()
			next = open.pop()
			#print 'take list item'
			#print next
			x = next[1]
			y = next[2]
			g = next[0]
	
			#check what areas are searched
			expand[x][y] = index
			index += 1
		
			#check if we are done
			if x == goal[0] and y == goal[1]:
				found = True
				path[x][y] = '*'
				print next
			else:
				# expand winning element and add to new open list
				for i in range(len(delta)):
					x2 = x + delta[i][0]
					y2 = y + delta[i][1]
					if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]):
						if closed[x2][y2] == 0 and grid [x2][y2] == 0:
							g2 = g + cost
							open.append([g2,x2,y2])
							#print 'append list item"
							#print [g2,x2,y2]
							closed[x2][y2] = 1
							path[x][y] = delta_name[i]

	x=0
	y=0
	goal = path[x][y]
	memory = [[x,y]]
	while goal!= '*':
		for i in range(len(delta_name)):
			if goal == delta_name[i]:
				x = x + delta[i][0]
				y = y + delta[i][1]
				memory.append([x,y])
			if goal == ' ' and x < 0 and x >= len(grid) and y < 0 and y >= len(grid[0]):
				return False
		goal = path[x][y]
	for y in range(len(grid[0])):
		for x in range(len(grid)):
			if [x,y] not in memory:
				path[x][y] = ' '

	return expand, path

if __name__ == '__main__':
	expand,path = search(grid,init,goal,cost)
	for row in expand:
		print row
	for row in path:
		print row
