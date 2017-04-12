import numpy as np

def kalman_filter(x,P):
        for measurement in measurements:
                z = np.matrix([[measurement]])
                #measurement update
                y = z - H*x 
                S = H * P * H.getT() + R
                K = P * H.getT() * S.getI()
                x = x + (K*y)
                P = (I - K*H)*P

                #prediction
                x = F*x + u
                P = F*P*F.getT()
        
#               print x
#               print P
        return x,P

### 1 dimension world example x = [position, velocity] 2D
measurements = [1,2,3]

x = np.matrix([[0.0],[0.0]]) #initial state (location and velocity)
P = np.matrix([[1000.0,0.0],[0.0,1000.0]]) # initial uncertainty covariance
u = np.matrix([[0.0],[0.0]]) # external motion of outside force(ex hit car) currently no effect
F = np.matrix([[1.0,1.0],[0.0,1.0]]) # next state function (state transition matrix)
H = np.matrix([[1.0,0.0]]) # measurement function
R = np.matrix([[1.0]]) # measurement uncertainty
I = np.matrix([[1.0,0.0],[0.0,1.0]]) # identity matrix
###

#for 4d
def kalman_filter2(x,P):
        for measurement in measurements:
                #prediction
                x = F*x + u
                P = F*P*F.getT()
                
                z = np.matrix([measurement])
                #measurement update
                y = z.getT() - H*x 
                S = H * P * H.getT() + R
                K = P * H.getT() * S.getI()
                x = x + (K*y)
                P = (I - K*H)*P

        return x,P

### 2 dimension world example x = [pos_x, vel_x, pos_y, vel_y] 4D
measurements = [[5.0,10.0],[6.0,8.0],[7.0,6.0],[8.0,4.0],[9.0,2.0],[10.0,0.0]]
initial_xy = [4.0,12.0]
dt = 0.1

x = np.matrix([[initial_xy[0]], [initial_xy[1]], [0.0], [0.0]]) #initial state (location and velocity)
P = np.matrix([[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,1000.0,0.0],[0.0,0.0,0.0,1000.0]]) # initial uncertainty: 0 for position x,y and 1000 for velocity x,y
u = np.matrix([[0.0],[0.0],[0.0],[0.0]]) # external motion of outside force(ex hit car) currently no effect
F = np.matrix([[1.0,0.0,dt,0.0],[0.0,1.0,0.0,dt],[0.0,0.0,1.0,0.0],[0.0,0.0,0.0,1.0]]) # next state function (state transition matrix)
H = np.matrix([[1.0,0.0,0.0,0.0],[0.0,1.0,0.0,0.0]]) # measurement function
R = np.matrix([[0.1,0.0],[0.0,0.1]]) # measurement uncertainty
I = np.matrix([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]) # identity matrix
###
x,P = kalman_filter2(x,P)
print 'output x,x_dot:'
print x
print 'covariance:'
print P 
