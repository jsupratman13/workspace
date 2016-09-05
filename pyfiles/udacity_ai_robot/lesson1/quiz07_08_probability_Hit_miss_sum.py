p = [0.2,0.2,0.2,0.2,0.2]
pHit = 0.6
pMiss = 0.2
n = len(p)
for i in range(n):
	if i==1 or i==2:
		p[i] = p[i]*pHit
	else:
		p[i] = p[i]*pMiss
print sum(p)
