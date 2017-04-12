import math

#gaussian function
def f(mu,sigma2,x):
        return 1/math.sqrt(2.0*math.pi*sigma2) * math.exp(-0.5*(x-mu)**2/sigma2)

#mean and variance of two combined gaussian function(measurement update)
def update(mean1, var1, mean2, var2):
        new_mean = (mean1*var2 + mean2*var1)/(var1 + var2)
        new_var = 1/(1/var1 + 1/var2)
        return [new_mean, new_var]

#mean and variance of gaussian and movement(motion update
def predict(mean1, var1, mean2, var2):
        new_mean = mean1 + mean2
        new_var = var1 + var2
        return [new_mean, new_var]

print f(10.0,4.0,8.0)
print update(10.0,8.0,13.0,2.0)
print predict(10.0,4.0,12.0,4.0)
