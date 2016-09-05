from collections import deque
p=[0,1,0,0,0]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
pHit=0.6
pMiss=0.2
pExact = 0.8
pOvershoot =0.1
pUndershoot=0.1

def sense(p,Z):
	q=[]
	for i in range(len(p)):
		hit = (Z == world[i]) #if true or false 
		q.append(p[i] * (hit*pHit + (1-hit)*pMiss)) #1-hit = 1-true = false
	s = sum(q)
	for i in range(len(q)):
		q[i] = q[i]/s
	return q

#shift by U, if U=0, p is same as q
def move(p,U):
	#deque version
	#q=deque(p)
	#q.rotate(U)
	q = []
	for i in range(len(p)):
		s = pExact * p[(i-U)%len(p)]
		s = s + pOvershoot * p[(i-U-1)%len(p)]
		s = s + pUndershoot * p[(i-U+1)%len(p)]
		q.append(s)
	return q
	
for k in range(1000):
	p = move(p,1)
print p
