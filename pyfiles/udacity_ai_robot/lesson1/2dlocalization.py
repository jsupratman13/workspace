colors = [['green', 'green', 'green'],
		  ['green', 'red', 'green'],
		  ['green', 'green', 'green']]

measurements=['red','green']

motions=[[0,0],[0,1]]

sensor_right = 1.0 #how accurate sensor value is 1=100%
pHit=0.6
pMiss=0.2

p_move = 1.0 #how accurate motion is
pExact = 1.0
pOvershoot = 0.1
pUndershoot = 0.1

def UniformDist(mat2d):
	q = []
	n = len(mat2d) * len(mat2d[0])
	for i in range(len(mat2d)):
		r = []
		for j in range(len(mat2d[0])):
			r.append(1./n)
		q.append(r)
	return q

#sense
def BayesRule(p,Z):
	q=[]
	s=0
	
	#measured probability * prior
	for i in range(len(p)):
		r=[]
		for j in range(len(p[0])):
			hit = (Z == colors[i][j])
			r.append(p[i][j] * (hit*pHit + (1-hit)*pMiss))
		s += sum(r)
		q.append(r)
		
	#normalize
	for k in range(len(p)):
		for l in range(len(p[0])):
			q[i][j] = q[i][j]/s
	return q
#move
def TotalProb(p,U):
	q=[]
	for i in range(len(p)):
		r=[]
		for j in range(len(p[0])):
			s = pExact * p[(i-U[0])%len(p)][j]
			#s = s + pOvershoot * p[(i-U[0]-1)%len(p)][j]
			#s = s + pUndershoot * p[(i-U[0]+1)%len(p)][j]

			s = s + pExact * p[i][(j-U[1])%len(p[0])]
			#s = s + pOvershoot * p[i][(j-U[1]-1)%len(p[0])]
			#s = s + pUndershoot * p[i][(j-U[1]+1)%len(p[0])]
			r.append(s) 
		q.append(r)
	return q

if __name__ == '__main__':
	p = UniformDist(colors)
	for i in range(len(motions)):
		p = BayesRule(p, measurements[i])
		p = TotalProb(p, motions[i])
	print p	
