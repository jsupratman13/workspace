import math,random

##World has 4 landmarks, inital robot coordinate are somewhere in square
##Landmarks are given in (y,x) coordinate NOT (x,y)

landmarks = [[0.0,100.0], [0.0,0.0], [100.0,0.0], [100.0,100.0]] #landmark position
world_size = 100.0 # NOT cyclic, bot can travel out of bound
max_steering_angle = math.pi/4
bearing_noise = 0.1
steering_noise = 0.1
distance_noise = 5.0

tolerance_xy = 15.0 #tolerance for localization in the x and y direction
tolerance_orientation = 0.25 #tolerance for orientation

class bicycle(object):
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

	def measurement_probability(self, measurements):
		#calculate correct measurement
		predicted_measurements = self.sense(False)

		#compute error
		error = 1.0
		for i in range(len(measurements)):
			error_bearing = math.fabs(measurements[i] - predicted_measurements[i])
			error_bearing = (error_bearing + math.pi) % (2*math.pi) - math.pi #truncate
			#update gaussian
			error *= (math.exp(-(error_bearing**2)/(self.bearing_noise**2)/2.0)/math.sqrt(2.0*math.pi*(self.bearing_noise**2)))
		return error

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
		alpha = random.gauss(alpha, self.steering_noise)
		distance = random.gauss(distance, self.distance_noise)

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

		result = bicycle(length)
		result.set_noise(self.bearing_noise, self.steering_noise, self.distance_noise)
		result.set(self.x, self.y, self.orientation)
		return result

	def sense(self, use_noise=False):
		Z = []
		for landmark in landmarks:
			y = landmark[0] - self.y
			x = landmark[1] - self.x
			bearing = math.atan2(y,x) - self.orientation
			if use_noise:
				bearing += random.gauss(0.0,self.steering_noise)
			bearing %= 2*math.pi
			Z.append(bearing)
		return Z

def particle_filter(motions, measurements, N=500):
	#make particles
	p=[]
	for i in range(N):
		b = bicycle()
		b.set_noise(bearing_noise, steering_noise, distance_noise)
		p.append(b)
	
	#update particles
	for i in range(len(motions)):
		
		#motion update
		p2 = []
		for j in range(N):
			p2.append(p[j].move(motions[i]))
		p = p2
		
		#measurement update
		w = []
		for j in range(N):
			w.append(p[j].measurement_probability(measurements[i]))

		#resampling
		p3=[]
		index = int(random.random()*N)
		beta=0.0
		max_w = max(w)
		for j in range(N):
			beta += random.random() * 2.0 * max_w
			while beta > w[index]:
				beta -= w[index]
				index = (index+1) % N
			p3.append(p[index])
		p=p3
	
	return get_position(p)

##check if particle filter localizes within tolerance level
def check_output(final_pos, estimated_pos):
	error_x = math.fabs(final_pos.x - estimated_pos[0])
	error_y = math.fabs(final_pos.y - estimated_pos[1])
	error_orientation = math.fabs(final_pos.orientation - estimated_pos[2])
	error_orientation = (error_orientation + math.pi) %(2.0*math.pi) - math.pi
	return error_x < tolerance_xy and error_y < tolerance_xy and error_orientation < tolerance_orientation

##Generate measurement vector
def generate_ground_truth(motions):
	robot = bicycle()
	robot.set_noise(bearing_noise, steering_noise, distance_noise)
	Z = []
	for i in range(len(motions)):
		robot = robot.move(motions[i])
		Z.append(robot.sense())
	return [robot,Z]

##Prints measurements associated with gnerate_ground_truth
def print_measurements(Z):
	T = len(Z)
	print 'measurements = [[%.8s, %.8s, %.8s, %.8s],' % (str(Z[0][0]), str(Z[0][1],), str(Z[0][2]), str(Z[0][3]))
	for i in range(1,T-1):
		print '                [%.8s, %.8s, %.8s, %.8s],' % (str(Z[i][0]),str(Z[i][1]),str(Z[i][2]),str(Z[i][3]))
	print '                [%.8s, %.8s, %.8s, %.8s]]' % (str(Z[T-1][0]), str(Z[T-1][1]), str(Z[T-1][2]), str(Z[T-1][3]))

##extract position from particle set
def get_position(p):
	x = 0.0
	y = 0.0
	orientation = 0.0
	for i in range(len(p)):
		x += p[i].x
		y += p[i].y
		#orientation is tricky because it is cyclic. by normalizing around the first particle we are somewhat more robust to the 0=2pi problem
		orientation += (((p[i].orientation - p[0].orientation + math.pi) % (2*math.pi)) + p[0].orientation - math.pi)

	return [x/len(p), y/len(p), orientation/len(p)]

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

def test2():
	motions = [[2.0*math.pi/10,20.0] for row in range(8)]
	measurements = [[4.746936, 3.859782, 3.045217, 2.045506],
			[3.510067, 2.916300, 2.146394, 1.598332],
			[2.972469, 2.407489, 1.588474, 1.611094],
			[1.906178, 1.193329, 0.619356, 0.807930],
			[1.352825, 0.662233, 0.144927, 0.799090],
			[0.856150, 0.214590, 5.651497, 1.062401],
			[0.194460, 5.660382, 4.761072, 2.471682],
			[5.717342, 4.736780, 3.909599, 2.342536]]
	print particle_filter(motions, measurements)

def test3():
	number_of_iterations = 6
	motions = [[2.0*math.pi/20,12.0] for row in range(number_of_iterations)]
	x = generate_ground_truth(motions)
	final_pos = x[0]
	measurements = x[1]
	estimated_pos = particle_filter(motions, measurements)
	print_measurements(measurements)
	print 'Ground truth:	', final_pos
	print 'Particle filter: ', estimated_pos
	print 'Code check:	', check_output(final_pos, estimated_pos)

if __name__ == '__main__':
	test3()

