#Motion Planning
* Robot has to device a plan(path) from their own location to their target location
* Planning: the process of finding a pth from a start location to goal location
##Planning Problem
Given:
* Map
* Starting location
* goal location
* cos (ex time it takes to get there)
Goal:
* find minimal cost path

##Seach option
* Depth First Search
* Breadth First Search
* Dijkstra Search
* Greedy Search
* Astar search
etc

##Search
* Open List: list that has yet to be searched
* g-Value: the expenditure, how much from start did it get to current?
* expansion: area that search
* path: optimal path (recrusion: during expansion, memorize the path direction, afterward return from goal)

##herustic function
* optimal guess of how far we are from the goal
* optimal guess has to be smaller or equal to the actual goal distance
* doesnt have to be accurate, its function where to search next in case of ties, underestimate or at best equals the true distance from the goal
* h-value

##Astar
* uses heuristic function and ground function
* f = g+h
* same as dijkstra except we find lowest h
* careful not to accumulate h. For next f, g = current g + past g but h is only the current h. F is not carried over to next iteration.
