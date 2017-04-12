#Dynamic Programming with stochastic motion and policy
#In reality, robot motion have probility of failing to move to 
#intended target. This is stochastic motion
#Our value (cost) change when we consider stochastic motion,
#and our policy also changes depending on our stochastic motion 

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>'] 

def stochastic_value(grid,goal,cost_step,collision_cost,success_prob):
    failure_prob = (1.0 - success_prob)/2.0 # Probability(stepping left) = prob(stepping right) = failure_prob
    value = [[collision_cost for col in range(len(grid[0]))] for row in range(len(grid))]
    policy = [[' ' for col in range(len(grid[0]))] for row in range(len(grid))]
    change = True
    while change:
        change = False
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if goal[0] == x and goal[1] == y:
                    if value[x][y] > 0:
                        value[x][y] = 0
                        policy[x][y] = '*'
                        change = True
                elif grid[x][y] == 0:
                    for i in range(len(delta)):
                        v2 = cost_step
                        for m in [-1,0,1]:
                            i2 = (i+m)%len(delta)
                            x2 = x + delta[i2][0]
                            y2 = y + delta[i2][1]

                            p2 = success_prob if m == 0 else failure_prob

                            if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]) and grid[x2][y2] == 0:
                                v2 += p2 * value[x2][y2]
                            else:
                                v2 += p2 * collision_cost
                        
                        if v2 < value[x][y]:
                            change = True
                            value[x][y] = v2
                            policy[x][y] = delta_name[i]
    return value, policy

if __name__ == '__main__':
    grid = [[0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 1, 1, 0]]
    goal = [0, len(grid[0])-1] # Goal is in top right corner
    cost_step = 1
    collision_cost = 100
    success_prob = 0.5
    
    value,policy = stochastic_value(grid,goal,cost_step,collision_cost,success_prob)
    for row in value:
       print row
    for row in policy:
       print row


