import math,random

##World has 4 landmarks, inital robot coordinate are somewhere in square
##Landmarks are given in (y,x) coordinate NOT (x,y)

landmarks = [[0.0,100.0], [0.0,0.0], [100.0,0.0], [100.0,100.0]] #landmark position
world_size = 100.0 # NOT cyclic, bot can travel out of bound
max_steering_angle = math.pi/4

class bicycle:
	def __init__(self, length = 10.0):
		self.x = random.random() * world_size #x coordinate of bicycle
		self.y = random.random() * world_size #y coordinate of bicycle
		self.orientation = random.random() * 2*math.pi #theta of bicycle
		self.length = length # length of bicycle, between two wheels
		self.bearing_noise = 0
		self.steering_noise = 0
		self.distance_noise = 0

	def __repr__(self):
		return '[x=%.6s y=%.6s orient=%.6s]' % (str(self.x), str(self.y), str(self.orientation))

	def set(self, initial_x, initial_y, initial_orientation):
		if initial_orientation < 0 or initial_orientation >= 2*math.pi:
			raise ValueError, 'orientation must be between 0 to 2pi'

		self.x = float(initial_x)
		self.y = float(initial_y)
		self.orientation = float(initial_orientation)

	def set_noise(self, b_noise, s_noise, d_noise):
		self.bearing_noise = float(b_noise)
		self.steering_noise = float(s_noise)
		self.distance_noise = float(d_noise)

	def move(self, motion): 
		alpha = motion[0] #steering angle
		distance = motion[1] #target distance
		
		if math.fabs(alpha) > max_steering_angle:
			raise ValueError, 'exceed max steering angle'
		if distance < 0.0:
			raise ValueError, 'backward is not allowed'
		
		length = self.length
		x = self.x
		y = self.y
		theta = self.orientation

		#noise
		steering_noise = random.gauss(alpha, self.steering_noise)
		distance_noise = random.gauss(alpha, self.distance_noise)

		beta = (distance/length) * math.tan(alpha) #angle turn from center
		if math.fabs(beta) < 0.001: #going straight
			self.x = x + (distance * math.cos(theta))
			self.y = y + (distance * math.sin(theta))
			self.orientation = (beta + theta) % (2*math.pi)

		else:
			radius = (distance/beta) #radius of circle
			center_x = x - (radius * math.sin(theta)) #x coordinate of circle
			center_y = y + (radius * math.cos(theta)) #y coordinate of circle
			self.orientation = (beta+theta) % (2*math.pi)
			self.x = center_x + (radius * math.sin(self.orientation))
			self.y = center_y - (radius * math.cos(self.orientation))

		return self

	def sense(self):
		Z = []
		for landmark in landmarks:
			y = landmark[0] - self.y
			x = landmark[1] - self.x
			bearing = math.atan2(y,x) - self.orientation
			if self.steering_noise > 0.0:
				bearing += random.gauss(0.0,self.steering_noise)
			bearing %= 2*math.pi
			Z.append(bearing)
		return Z

def test():
	length = 20.0
	bot = bicycle(length)
	bot.set(30.0,20.0,0.0)
	motions = [[0.0,10.0],[math.pi/6.0,10.0],[0.0,20.0]] #steer angle, distance
	motion_length = len(motions)
	print 'bot: ', bot
	print 'measurement: ',  bot.sense()
	for i in range(motion_length):
		bot = bot.move(motions[i])
		print 'bot: ', bot

if __name__ == '__main__':
	test()

