import math
import random

landmarks = [[20.0, 20.0],[80.0,80.0],[20.0,80.0],[80.0,20.0]]
world_size = 100.0

def sense(p):
	Z = []
	for i in range(len(landmarks)):
		dist = math.sqrt((p[0]-landmarks[i][0])**2+(p[1]-landmarks[i][1])**2)
		Z.append(dist)
	return Z

def move(p, turn, forward):
	if forward < 0:
		raise ValueError, 'Robot cant move backward'

	#turn and add randomness to the turning command
	orientation = p[2] + float(turn) # + random.gauss(0.0,self.turn_noise)
	orientation %= 2*math.pi		
		
	#move and add randomness to the motion command
	dist = float(forward) #+ random.gauss(0.0, self.forward_noise)
	x = p[0] + (math.cos(orientation) * dist)
	y = p[1] + (math.sin(orientation) * dist)
	x %= world_size #cyclic truncate
	y %= world_size
	return [x,y,orientation]

def Gaussian(mu, sigma,x):
	return math.exp(-((mu-x)**2)/(sigma**2)/2.0)/math.sqrt(2.0*math.pi*(sigma**2))

def weight_importance(p, measurement):
	prob = 1.0
	for i in range(len(landmarks)):
		dist = math.sqrt((p[0]-landmarks[i][0])**2+(p[1]-landmarks[i][1])**2)
 		prob *= Gaussian(dist, 5.0, measurement[i])
	return prob

#initial
x = random.random() * world_size
y = random.random() * world_size
orientation = random.random() * 2.0 * math.pi
p_initial=[[x,y,orientation]]
p_initial[0] = move(p_initial[0], 0.1,5.0)
Z = sense(p_initial[0])

#Initial particle spread at random
N=1000
p = []
for i in range(N):
	x = random.random() * world_size
	y = random.random() * world_size
	orientation = random.random() * 2.0 * math.pi
	p.append([x,y,orientation])

#Robot moves, add update characterstic to each particle
p2 = []
for i in range(N):
	p2.append(move(p[i],0.1,5.0))
print p

#Importance weight, actual + measurement
w = []
for i in range(N):
	w.append(weight_importance(p[i],Z))
print w
