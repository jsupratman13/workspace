#Lesson 3 Particle Filter

Filters|State Space|Belief|Efficiency|in Robotics
-------------------------------------------------
Histogram Filters|Discrete|Multimodal|ExponentialApproximate
Kalman Filters|Continuous|Unimodal|Qudratic|Approximate
Particle Filters|Continuous|Multimodal|Unknown|Approximate

* Unimodal have one peak only, multimodal have multiple peak (more the better, can compare)
* Exponential is good for low dimensional problem like 3d robot localize problem. However, exponential cant represent high dimension grid.
* Quadratic is more efficient than exponential when dealing with high dimension 
* Unknown means depend on world. Certain dimensions can cause exponential while others (tracking domain )is quadratic

Among the three estimation method, particle filter is
* easiest to program (Main Key)
* most flexible
* shouldnt be represented anything more than 4 dimensions

Start with unknown position and map
* global localization => spread a lot(thousands) of particles where robot think they are
Particles: structured as x,y and direction comprise as a single guess (filter is a set of thousands of guess that together comprise an approximate representation for the posterior of the robot)
* as the robot move and sense, particles cluster together at the most likely position

##Robot World
ex localizing_robot.py
m1            m2
--->robot-------
m2         m3
cyclic world

##Steps for particle
* generate N particles with information
* for a movement, generate result for each N particles
* measurement the landmarks = actual measurement
* for each particle the comparison between the predicted and actual measurement gives the weight. The more the weight, the more important it is.
* Resampling: randomly drawing new particles from old particles in proportion to the importance of weight

##Weight importance
use gaussian with mean as predicted and x as actual and sigma as noise.
the higher the more likely it is

##Resampling
* normalize weight
* The new random set of particles will pick the particles with high importance several times
* sometime, higher importance might not be sampled at all
* probability of never sampling p1 = (1-pi)^N where N is number of sampling

