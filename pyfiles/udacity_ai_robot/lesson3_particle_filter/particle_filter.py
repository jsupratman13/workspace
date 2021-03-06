import math
import random

landmarks = [[20.0, 20.0],
             [80.0, 80.0],
             [20.0, 80.0],
             [80.0, 20.0]]
world_size = 100.0

class robot(object):
        def __init__(self):
                self.x = random.random() * world_size
                self.y = random.random() * world_size
                self.orientation = random.random() * 2.0 * math.pi
                self.forward_noise = 0.0
                self.turn_noise    = 0.0
                self.sense_noise   = 0.0

        def set_position(self, new_x, new_y, new_orientation):
                if new_x < 0 or new_x >= world_size:
                        raise ValueError, 'x coordinate out of bound'
                if new_y < 0 or new_y >= world_size:
                        raise ValueError, 'y coordinate out of bound'
                if new_orientation < 0 or new_orientation >= 2*math.pi:
                        raise ValueError, 'Orientation must be in 0 < dir < 2pi'
                self.x = float(new_x)
                self.y = float(new_y)
                self.orientation = float(new_orientation)

        def set_noise(self, new_f_noise, new_t_noise, new_s_noise):
                #makes it possible to change the noise parameters
                #often useful in particle filters
                self.forward_noise = float(new_f_noise)
                self.turn_noise    = float(new_t_noise)
                self.sense_noise   = float(new_s_noise)

        def sense(self):
                Z = []
                for i in range(len(landmarks)):
                        dist = math.sqrt((self.x - landmarks[i][0]) ** 2 + (self.y - landmarks[i][1]) ** 2)
                        dist += random.gauss(0.0, self.sense_noise)
                        Z.append(dist)
                return Z

        def move(self, turn, forward):
                if forward < 0:
                        raise ValueError, 'Robot cant move backward'

                #turn and add randomness to the turning command
                orientation = self.orientation + float(turn) + random.gauss(0.0,self.turn_noise)
                orientation %= 2*math.pi
                
                #move and add randomness to the motion command
                dist = float(forward) + random.gauss(0.0, self.forward_noise)
                x = self.x + (math.cos(orientation) * dist)
                y = self.y + (math.sin(orientation) * dist)
                x %= world_size #cyclic truncate
                y %= world_size

                #set particle
                res = robot()
                res.set_position(x,y,orientation)
                res.set_noise(self.forward_noise, self.turn_noise, self.sense_noise)
                return res

        def Gaussian(self, mu, sigma, x):
                #calculates the probability of x for 1-dim Gaussian with mean mu and var. sigma
                return math.exp(-((mu-x)**2)/(sigma**2)/2.0)/math.sqrt(2.0*math.pi*(sigma**2))

        def measurement_prob(self, measurement):
                #calculate how likely a measurement should be
                prob = 1.0
                for i in range(len(landmarks)):
                        dist = math.sqrt((self.x - landmarks[i][0]) ** 2 + (self.y - landmarks[i][1]) ** 2)
                        prob *= self.Gaussian(dist, self.sense_noise, measurement[i])
                return prob

        def __repr__(self):
                return '[x=%.6s y=%.6s orient=%.6s]' % (str(self.x), str(self.y), str(self.orientation))
def evaluation(r, p):
        sum_eval = 0.0
        for i in range(len(p)): #calculate mean error
                dx = (p[i].x - r.x + (world_size/2.0)) % world_size - (world_size/2.0)
                dy = (p[i].y - r.y + (world_size/2.0)) % world_size - (world_size/2.0)
                err = math.sqrt(dx * dx + dy * dy)
                sum_eval += err
        return sum_eval / float(len(p))


if __name__ == '__main__':
        myrobot = robot()
        
#       myrobot.set_noise(5.0,0.1,5.0)
#       myrobot.set_position(30,50,math.pi/2)
#       myrobot = myrobot.move(-math.pi/2, 15.0)
#       print myrobot.sense()
#       myrobot = myrobot.move(-math.pi/2, 10.0)
#       print myrobot.sense()

        #initial/actual measurement
        myrobot = robot()
        myrobot = myrobot.move(0.1,5.0)
        Z = myrobot.sense()

        #spread particle
        N=1000
        p = []
        for i in range(N):
                x = robot()
                x.set_noise(0.05,0.05,5.0)
                p.append(x)
#       print p
        
        T = 10
        for t in range(T):
                #move and measurent
                myrobot = myrobot.move(0.1,5.0)
                Z = myrobot.sense()

                #move each particle
                p2 = []
                for i in range(N):
                        p2.append(p[i].move(0.1,5.0))
                p = p2

                #Calc importance weight
                w = []
                for i in range(N):
                        w.append(p[i].measurement_prob(Z))
                
                #Resampling (circumference method)
                p3 = []
                beta = 0
                index = int(random.random()*N)
                for i in range(N):
                        beta += random.uniform(0,2*max(w))
                        while w[index] < beta:
                                beta -= w[index]
                                index = (index+1)%1000
                        p3.append(p[index])
                p = p3
        
                #evaluat margin of error in 100 by 100 world
                print evaluation(myrobot, p)


