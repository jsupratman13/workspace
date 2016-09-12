#Lesson 1 Localization
Monte Carlo Localization

##Core concept
2d -> robot -> uniform -> sense -> move -> sense -> convolution

##Uniform Distribution
Uniform Distribution means that the probability of all possilibilty is the same.

For example the probability of 5 cell with uniform(same) distribution is 1/5 or 0.2

##Normalization
The sum of probability must equal to 1. The process of converting the calculated probability to meet this condition is normalization.

For example:
given 5 cells with color red or green
green|red|red|green|green
 0.2  |0.2|0.2|0.2  |0.2
 x1   |x2 |x3 |x4   |x5
say robot saw red
red * 0.6
green * 0.2
 green|red |red |green|green
 0.04 |0.12|0.12|0.04 |0.04
total distribution = 0.36
however distribution needs to add up to 1!
therefore we normalize our distribution by dividing each cell by total distribution
 green|red |red |green|green
 0.11 |0.33|0.33|0.11 |0.11
 1/9  |1/3 |1/3 |1/9  |1/9
total distribution = 0.99
probability of x after observation z = posterior distribution
p(xi|z)

##In Exact Movement
In an ideal situation, exact movement is when robot move precisely as it should. 
However in reality, robot would not completely move exactly as it should do to noise. This is called inexact movement.
For example:
cells
0,1,0,0,0
if U=2
target is
0,0,0,1,0
however robot may overshoot/undershoot target such that
1->0.1
1-->0.8
1--->0.1
probability
therefore if
U=2
p(Xi+2|Xi)=0.8
p(Xi+1|Xi)=0.1
(Xi+3|Xi)=0.1
the distribution is
0|0|0|1|0| to
0|0|0.1|0.8|0.1
if U=2
p(Xi+2|Xi)=0.8
p(Xi+1|Xi)=0.1
p(Xi+3|Xi)=0.1
initial is
 0  |0.5 |0  |0.5 |0
then
0  : |    |0   |0   |0   |
0.5: |    |    |0.05|0.4 |0.05
0  : |0   |    |    |0   |0
0.5: |0.4 |0.05|    |    |0.05
etc.
final:
 0.4|0.05|0.05|0.4|0.1
if uniform distribution, no uncertainty
ex 0.2,0.2,0.2,0.2,0.2
then 0.2,0.2,0.2,0.2,0.2

##Sense Movement
initial belief -> sense
sense <-> move 
* each time robot moves it loses information
* each time robot senses it gains information

Entropy- the measures of information sigma(pXi) logp(xi)
* motion (update step) decrease entropy
* measurement increase entropy

##summarize
Belief = Probabilility
Sense = Product followed by normalization
move = Convolution (=Addition)

##Formal definition
###probability
0 <= P(X) <= 1 probabilities add up to 1
Sum(Px)=1

###measurement
(Bayes Rule)
X = grid cell
Z = measurement
P(Xi|Z) = P(Z|Xi)P(Xi)/P(Z))
       = Measurement Probility(large if correspond with sense) * Prior(past value)/ Normalization Constant(used for normalizing probability)
P(Z) = sum(P(z|xi)P(Xi)

therefore
~p(xi|z) <- p(z|xi)p(xi)
a <- sum(~p(xi|z))
p(xi|z) -< (1/a)~p(xi|z)

this is the same as what we program!!!

ex cancer test
p(C) = 0.001
p(^C) = 0.999
p(pos|c) = 0.8
p(pos|^c)=0.1

what is p(c|pos)=?
hint think of p(c) as robot movement and p(pos|c) as measurement

ans: 0.0079

##Motion: Total probability
t = time, i = grid cell
P(Xt,i) = sumj(P(Xt-1,j)P(xi|xj)
(or)
p(a)=sumb(p(a|b)p(B)
aka convolution

ex coin toss
p(t)=p(h)=0.5
t->accept
h-> flip, accept
p(H)=?

ans 0.25

##Limit Distribuition
for example:
1,0,0,0,0
if U=1 but continously move then
0.2,0.2,0.2,0.2,0.2
the more the robot moves the more uncertain it becomes and finally reaches maximum uncertainty which is uniform distribution
0.7*p(X2)+0.1*p(X1)+0.1*p(X3)=p(X4)

#Conclusion
* Localization
* Markov Localization
* Probabilites
* Bayes Rule
* Total Probability

##Homework make 2d localization
world
|R|R|G|R|R|
|G|G|R|G|G|
|R|R|G|R|R|
Measurement
R,R,G
Motion
[0, 0] -nomove
[0, 1] -right
[0,-1] -left
[1, 0] -down
[-1,0] -up
