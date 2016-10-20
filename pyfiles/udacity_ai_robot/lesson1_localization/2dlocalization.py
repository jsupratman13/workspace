'''
colors = [['green', 'green', 'green'],
          ['green', 'red', 'red'],
          ['green', 'green', 'green']]

measurements=['red','red']

motions=[[0,0],[0,1]]
'''

colors = [['R', 'G', 'G', 'R', 'R'],
          ['R', 'R', 'G', 'R', 'R'],
          ['R', 'R', 'G', 'G', 'G'],
          ['R', 'R', 'R', 'R', 'R']]

measurements = ['G', 'G', 'G', 'G', 'G']

motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]

def UniformDist(world):
	q = []
	n = len(world) * len(world[0])
	for i in range(len(world)):
		r = []
		for j in range(len(world[0])):
			r.append(1./n)
		q.append(r)
	return q
#sense
def BayesRule(p,measurement, colors, sensor_right):
	q=[]
	s=0
	
	##accuracy
	pHit = sensor_right
	pMiss = 1.0 - pHit
	
	#measured probability * prior
	for i in range(len(p)):
		r=[]
		for j in range(len(p[i])):
			hit = (measurement == colors[i][j])
			r.append(p[i][j] * (hit*pHit + (1-hit)*pMiss))
		s += sum(r)
		q.append(r)
		
	#normalize
	for k in range(len(p)):
		for l in range(len(p[k])):
			q[k][l] /= s
	return q
#move
def TotalProb(p,U,pExact):
	q=[]

	#accuracy
	pUndershoot = 1.0 - pExact

	#probability of movement in each cell
	for i in range(len(p)):
		r=[]
		for j in range(len(p[i])):
			s = (pExact * p[(i-U[0])%len(p)][(j-U[1])%len(p[i])]) + (pUndershoot*p[i][j])
			r.append(s) 
		q.append(r)
	return q

def localize(colors, measurements, motions,sensor_right=1.0,p_move=1.0):
	p = UniformDist(colors)
	for i in range(len(motions)):
		p = TotalProb(p, motions[i],p_move)
		p = BayesRule(p, measurements[i], colors, sensor_right)
	return p

def show(p):
	for i in range(len(p)):
		print p[i]

if __name__ == '__main__':
	if len(measurements) != len(motions):
		assert False, 'size of measurements and motions does not match'
	p = localize(colors, measurements, motions, sensor_right=0.7,p_move=0.8)
	show(p)

