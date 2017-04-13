# Motion Planning
* Robot has to device a plan(path) from their own location to their target location
* Planning: the process of finding a pth from a start location to goal location
## Planning Problem
Given:
* Map
* Starting location
* goal location
* cos (ex time it takes to get there)
Goal:
* find minimal cost path

## Search option
* Depth First Search
* Breadth First Search
* Dijkstra Search
* Greedy Search
* Astar search
etc

## Search
* Open List: list that has yet to be searched
* g-Value: the expenditure, how much from start did it get to current?
* expansion: area that search
* path: optimal path (recrusion: during expansion, memorize the path direction, afterward return from goal)

## herustic function
* optimal guess of how far we are from the goal
* optimal guess has to be smaller or equal to the actual goal distance
* doesnt have to be accurate, its function where to search next in case of ties, underestimate or at best equals the true distance from the goal
* h-value

## Astar
* uses heuristic function and ground function
* f = g+h
* same as dijkstra except we find lowest h
* careful not to accumulate h. For next f, g = current g + past g but h is only the current h. F is not carried over to next iteration.

## Dynamic Programming
* in Reality, enviornment is stochastic, outcome of action are non-deteministic (when moving, you might end going to places that are not optimal due to situation)
* instead of astar(only one path to the goal) you need optimal path for any other location (anywhere)
* in grid map, each grid cell have policy: function that maps the grid cell into action
* in policy, each grid cell show which direction agent should take to reach the goal

### Value Function
* associates to each grid cell the length of the shortest path to the goal
ex.
5|4|3|3
-------
6|x|2|1
7|x|1|G

```
f(x,y) = min(f(x'y')) + 1
```
### Stochastic Action
* For path plan, robot usually get shortest path. In case of obstacle, it gets as close as possible to obstacle. This however is dangerous.
* robot may not move as planned, due to noise
* we add clearance or avoid radius
* our value (cost) change when considering stochastic action and thus our policy also changes

## QA
* Global planning -> local planning -> update variable
* heuristic function
  * 3d to 2d mapping 
  * 3d without obstacles
* good Astar heuristic: good ways of cheating and solving the problem by lessening constraint and doing it much faster

