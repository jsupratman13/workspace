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
* Motion meant keeping track of where all of our probability 'went' when we moved and involves performing convolution (motion = convolution)

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

###Motion(Gaussian)
* Robot loses information as it moves therefore as the gaussian shift, it will be more wider
u'<-u+U(mean motion. if move 10 m this will be 10)
o2'<-o2+r2(motion uncertainty)
σ²′ ← σ² + r²(motion uncertainty)

##Kalman Filter
* initial variance(uncertainty) should be set high (if low it thinks it is in right position)
* If you do estimation using kalman filter in high dimensional spaces, it not only figures out the x, and y spaces but also the velocity of the object and uses the velocity to make good prediction.
* Sensor only reads object position, kalman filter figures out the velocity and predict future position

###Multivariate gaussians
* High dimensional guassians
* mean = vector, variance=covaraince = matrix DxD
* x,y coordinate are dimensional mean, the lines are uncertainty ex 2d contour line
ex
t = 1 | 2 | 3 | 4
   *   *   *    * <- prediction
gaussian space
x = position
y = velocity
initial: know position unknown velocity -> vertical contour line
as measurement are made contour line becomes smaller(more certain)
* Projecting the gaussian uncertainty into the space of possible locations cannot predict position (because velocity is unknown)
* Projecting the gaussian uncertainty into the space of possible velocity cannot predict velocity (single observation/prediction is insufficient)
* we only known that our location is correlated to the velocity ex faster movent, the further on the right is the location
* more on video

##Big Lesson
* Variable of kalman filter are often called states because they reflect states of the physical role(where other car is, fastest moving etc)
* States seperate to 2 subsets: the observables (momentary locations) and the hidden (velocity)
* 2 subsets interact, subsequent observations of the observable variables (multiple locations) gives information about the hidden variables (how fast is moving) thus it can be estimated

##Designing
2 things required
* For state, need state transition function [x, x_dot]T <- [[1,t],[0,1]]T[x, x_dot]T (linear algebra) t = time
* For measurement, measurement function z <- [1,0][x, x_dot]T
new location = old location + velocity * time
x_prime = x + x_dot * delta_t
measurement = location
z = x
* Matrix function must output the equation above
F = [[1,t],[0,1]] H= [1,0] t = interval (for sensor input)

###Update
x = estimate
P = uncertainty covariance
F = state transition matrix
u = motion matrix
z = measurement
H = measurement function
R = measurement noise
I = identity matrix
####Prediction
x' = Fx + u
P' = F * P * FT (transpose)
####Measurement Update
(aka error) y = z - Hx
(error matrix) S = H * P * HT (transpose) + R
(kalman gain) K = P * HT (transpose) * S-1 (invert)
x' = x + (Ky)
P' = (I - KH)P

##Conclusion
Kalman filter predicts the next state through information of observb variable and hidden variable
* heavytail gaussian cannot be represented the same as gaussian function (area have to be 1)
