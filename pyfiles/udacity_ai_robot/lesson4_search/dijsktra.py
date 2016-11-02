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

delta_name = ['^', '<', 'v', '>']


def search(grid, init, goal, cost):
	start = [0, init[0], init[1]]
	open_list = [start]
	close_list = []
	while open_list:
		open_list.sort()
#		open_list.reverse()
		print 'current ' +str(open_list)
		node = open_list.pop(0)
		print 'expanding '+str(node)
		if (node[2] == goal[1]) and (node[1] == goal[0]):
			print 'found target'
			return node
		successor_list = []
		for move in delta:
			x = node[2] + move[1]
			y = node[1] + move[0]
			if (len(grid[0]) > x >= 0) and (len(grid) > y >= 0):
				if not grid[y][x]:
					for ol in open_list:
						if (x==ol[1]) and (y==ol[2]):
							break
					else:
						successor_list.append([node[0]+cost,y,x])
		for child in successor_list:
			for cl in close_list:
				if (child[1]==cl[1]) and (child[2]==cl[2]):
					break
			else:
				open_list.append(child)

		close_list.append(node)
						

	return 'failed to find path'
	#return path

if __name__ == '__main__':
	result = search(grid,init,goal,cost)
	print result
	#return [g-value,x,y] 
