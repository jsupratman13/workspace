def update(mean1, var1, mean2, var2):
        new_mean = (mean1*var2 + mean2*var1)/(var1 + var2)
        new_var = 1/(1/var1 + 1/var2)
        return [new_mean, new_var]

def predict(mean1, var1, mean2, var2):
        new_mean = mean1 + mean2
        new_var = var1 + var2
        return [new_mean, new_var]

#sequence
measurements = [5,6,7,9,10]
motions = [1,1,2,1,1]

#uncertainty constant
measurement_sig = 4.
motion_sig = 2. 

#initial
mu = 0.
sig = 10000.

for measurement,motion in zip(measurements,motions):
        mu,sig = update(mu,sig,measurement,measurement_sig)
        print 'update: ', [mu,sig]
        mu,sig = predict(mu,sig,motion,motion_sig)
        print 'predict: ', [mu,sig]

print [mu,sig]
