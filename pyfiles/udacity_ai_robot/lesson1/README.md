#Lesson 1 Localization

##Core concept

##uniform distribution

##Normalization

##Exact Movement

##In Exact Movement

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
