p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
pHit=0.6
pMiss=0.2

def sense(p,Z):
	q=[]
	for i in range(len(p)):
		hit = (Z == world[i]) #if true or false 
		q.append(p[i] * (hit*pHit + (1-hit)*pMiss)) #1-hit = 1-true = false
	s = sum(q)
	for i in range(len(q)):
		q[i] = q[i]/s
	return q
for k in range(len(measurements)):
	p=sense(p,measurements[k])
print p
