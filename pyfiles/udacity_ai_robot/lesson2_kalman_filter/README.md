#Lesson 2 Kalman Filter
##Tracking
Technique for estimating the state of a system
* Kalman Filter estimate continuous rate -> Uni-modal distribution
* Monte Carlo Localization chop world into discrete places -> Multi-modal distribution
* Particle Filter estimate continuous and Multi-modal distribution
Both technique are applicable to robot localization and tracking other object/vehicle

##Gaussian
Markov Model(seperate world into spaces like grid) + label probability on each space =
Historgram: representation of probability over spaces
Ex:

Monte Carlo Localization
|0.2|0.1|0.5|0.1|0.2|
Kalman Filter
|
|-| |-|
| |-| |-|-|
-----------

Gaussian is a continous function over the space of locations, 
the area underneath sums up to 1.
* In kalman filters the distribution is given by Gaussian
* Rather than estimate distribution as histogram, 
the task in kalman filter is to maintain a u and o^2 that is the best estimate of the location of object we try to find

1-D Gaussian (u,o^2)
f(x) = (1/sqrt(2*pi*o^2))*exp{-0.5*((x-u)^2)/o^2)}
* first part is constant for normalization
* All gaussian have similar shape (one peak = unimodal function)
* All gaussian are symmetrical
* when u = x gaussian is max
* u = mean, o = variance

###Variance
* Higher variance means wide gaussian vice versa
* sigma-squared covariance is measure of uncertainty, the larger it is, the more uncertain the actual state is 
* Therefore the narrow the gaussian, the more confident its location and thus it is better

##Core concept
Kalman filter iterates two different things: measurement and motion updates(similar to monte carlo except max changes)
* Performing measurement meant updating belief by multiplicative factor (measurement = product) and renormalizing our distribution
* Motion meant keeping track of where all of our probability 'went' when we movedand involves performing convolution (motion = convolution)

Measurement Update (Bayes Rule/product) <-> Prediction (Total Probability/convolution/addition)

###Measurement (Gaussian)
1. Uncertain gaussian (prior)
2. narrow guassian (measurement)
3. new mean is between the two gaussian and closer to measurement. The more certain it is, the more closer to measurement.
4. new gaussian is more certain than the other two, more measurement means greater certainty (we gain information therefore two gaussian together have higher information content than isolated gaussian)

prior : u,o2
measurement : v,r2
posterior(combine) : u'=(r2*u + o2*v)/(r2+o2), o2'=1/((1/r2)+(1/o2))

* If variance is same, new mean is middle
* Posterior variance will always be smaller thus narrow gaussian



