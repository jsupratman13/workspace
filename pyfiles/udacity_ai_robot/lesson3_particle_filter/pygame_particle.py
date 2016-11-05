import pygame
import sys,time
import random, math

class WorldMap(object):
	def __init__(self):
		self.BLACK = (0,0,0)
		self.WHITE = (255,255,255)
		self.GREEN = (0,255,0)
		self.RED = (255,0,0)
		self.BLUE = (0,0,255)
		self.PURPLE = (255,0,255)
		self.YELLOW = (255,255,0,)

		self.MARGIN = 5
		self.HEIGHT = 350
		self.WIDTH = self.HEIGHT*2
		self.WINDOW_SIZE = []
		self.grid_map = []

		self.x1, self.y1 = random.randint(self.MARGIN+5, self.WIDTH/2-self.MARGIN-5),random.randint(self.MARGIN+5, self.HEIGHT-self.MARGIN-5)
		self.x2, self.y2 = random.randint(self.MARGIN+5, self.WIDTH/2-self.MARGIN-5),random.randint(self.MARGIN+5, self.HEIGHT-self.MARGIN-5)
		self.x3, self.y3 = random.randint(self.MARGIN+5, self.WIDTH/2-self.MARGIN-5),random.randint(self.MARGIN+5, self.HEIGHT-self.MARGIN-5)
		self.landmarks = [[self.x1, self.y1],[self.x2, self.y2],[self.x3, self.y3]]

	def coordinateX(self, column):
		return (self.MARGIN+self.WIDTH)*column+self.MARGIN

	def coordinateY(self,row):
		return (self.MARGIN+self.HEIGHT)*row+self.MARGIN

	def get_landmarks(self,x,y):
		#local coordinate
		green_dist = math.sqrt((x-self.x1)**2 + (y-self.y1)**2)
		yellow_dist = math.sqrt((x-self.x2)**2 + (y-self.y2)**2)
		purple_dist = math.sqrt((x-self.x3)**2 + (y-self.y3)**2)
		return [green_dist,yellow_dist,purple_dist]

	def draw_world(self):
		#WORLD
		pygame.draw.rect(screen,self.RED,pygame.Rect([self.MARGIN, self.MARGIN, self.HEIGHT-self.MARGIN, self.WIDTH/2-self.MARGIN]), 3)
		pygame.draw.rect(screen,self.RED,pygame.Rect([self.WIDTH/2+self.MARGIN, self.MARGIN, self.HEIGHT-self.MARGIN, self.WIDTH/2-self.MARGIN]), 3)
		pygame.draw.circle(screen, self.GREEN, (self.x1,self.y1),5)
		pygame.draw.circle(screen, self.YELLOW, (self.x2,self.y2),5)
		pygame.draw.circle(screen, self.PURPLE, (self.x3,self.y3),5)
		
		#MAP
		pygame.draw.circle(screen, self.GREEN, (self.x1+self.WIDTH/2,self.y1),5)
		pygame.draw.circle(screen, self.YELLOW, (self.x2+self.WIDTH/2,self.y2),5)
		pygame.draw.circle(screen, self.PURPLE, (self.x3+self.WIDTH/2,self.y3),5)


	def fit_window_to_grid(self):
		WIDTH = self.WIDTH
		HEIGHT = self.HEIGHT
		self.WINDOW_SIZE = [WIDTH, HEIGHT]
		return self.WINDOW_SIZE

class Renge(object):
	def __init__(self, landmarks, WORLD_SIZE=350, WIDTH=350):
		self.x = random.random() * WORLD_SIZE
		self.y = random.random() * WORLD_SIZE
		self.movement_noise = 0
		self.sense_noise = 0
		self.landmarks = landmarks
		self.WIDTH = WIDTH

	def print_pos(self):
		pygame.draw.circle(screen, (255,255,255), (int(self.x)+self.WIDTH, int(self.y)),3)

	def set_pos(self, new_x, new_y):
		self.x = float(new_x)
		self.y = float(new_y)

	def set_noise(self, movement_noise, sense_noise):
		self.movement_noise = movement_noise
		self.sense_noise = sense_noise

	def measurement_probability(self, measurement):
		predicted_measurements = self.predicted_sense(False)
		error  = 1.0
		for i in range(len(measurement)):
			error_dist = math.fabs(measurement[i] - predicted_measurements[i])
#			error *= (math.exp(-(error_dist**2)/(self.sense_noise**2)/2.0)/math.sqrt(2.0*math.pi*(self.sense_noise**2)))
			error *= self.Gaussian(measurement[i], self.sense_noise, predicted_measurements[i])
		return error

	def Gaussian(self, mu, sigma, x):
		return math.exp(-((mu-x)**2)/(sigma**2)/2.0)/math.sqrt(2.0*math.pi*(sigma**2))

	def predicted_sense(self, use_noise=False):
		Z = []
		for landmark in self.landmarks:
			x = landmark[0] - self.x
			y = landmark[1] - self.y
			dist = math.sqrt((x**2) + (y**2))
			if use_noise:
				dist += random.gauss(0.0, self.sense_noise)
			Z.append(dist)
		return Z

	def predicted_move(self, motion):
		x_movement = motion[0] + random.gauss(0.0,self.movement_noise)
		y_movement = motion[1] + random.gauss(0.0,self.movement_noise)

		x = self.x + x_movement
		y = self.y + y_movement

		res  = Renge(self.landmarks)
		res.set_noise(self.movement_noise, self.sense_noise)
		res.set_pos(x,y)
		return res

class ParticleFilter(object):
	def __init__(self, landmarks, m_noise, s_noise, N=300):
		self.landmarks = landmarks
		self.movement_noise = m_noise
		self.sense_noise = s_noise
		self.N = N

		#make particles
		self.p = []
		for i in range(self.N):
			r = Renge(self.landmarks)
			r.set_noise(m_noise, s_noise)
			self.p.append(r)

#	def update(self,motion_list, measurement_list):
#		for j in range(len(motion_list)):
	def update(self,motion,measurement):
			p2 = []
			for i in range(self.N):
#				p2.append(self.p[i].predicted_move(motion_list[j]))
				p2.append(self.p[i].predicted_move(motion))
			self.p = p2

		#calc importance weight
			w = []
			for i in range(self.N):
#				w.append(self.p[i].measurement_probability(measurement_list[j]))
				w.append(self.p[i].measurement_probability(measurement))
		#resampling
			p3 = []
			beta = 0.0
			index = int(random.random()*self.N)
			max_w = max(w)
			for i in range(self.N):
				beta += random.uniform(0,max_w)
				while beta > w[index]:
					beta -= w[index]
					index = (index+1)%self.N
				p3.append(self.p[index])
			self.p = p3

#		return self.p
			return self.p

	def get_position(self,p):
		x = 0.0
		y = 0.0
		for i in range(len(p)):
			x += p[i].x
			y += p[i].y
		return [x/len(p), y/len(p)]

	def check_output(self,current_pos, estimated_pos):
		tolerance = 15.0
		error_x = math.fabs(current_pos[0]- estimated_pos[0])
		error_y = math.fabs(current_pos[1]- estimated_pos[1])
		return error_x < tolerance and error_y < tolerance

if __name__ == '__main__':
	world = WorldMap()
	
	BLACK = world.BLACK
	WIDTH = world.WIDTH
	HEIGHT = world.HEIGHT
	MARGIN = world.MARGIN
	
	pygame.init()
	
	WINDOW_SIZE = world.fit_window_to_grid()
	screen = pygame.display.set_mode(WINDOW_SIZE)
	pygame.display.set_caption("wandering renge")
	clock = pygame.time.Clock()

	im = pygame.image.load('renge.png').convert_alpha()
	rect = im.get_rect()
	init_x = random.randint(0,WIDTH/2)
	init_y = random.randint(0,HEIGHT)
	rect.center = (init_x,init_y)

	renge = Renge(world.landmarks)
	particle_filter = ParticleFilter(world.landmarks,1.0,0.4)

	particle = None
	update_flag = False
#	motion_list = []
#	measurement_list = []
	while True:
		pygame.display.update()
		clock.tick(60)
		screen.fill(BLACK)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				update_flag = True
				if event.key == pygame.K_ESCAPE:
					pygame.quit()
					sys.exit()

		pressed_key = pygame.key.get_pressed()
		motion = [0,0]
		if pressed_key[pygame.K_LEFT]: rect.move_ip(-1,0); update_flag = True; motion = [-1, 0]
		if pressed_key[pygame.K_RIGHT]: rect.move_ip(1,0); update_flag = True; motion = [1, 0]
		if pressed_key[pygame.K_UP]: rect.move_ip(0, -1); update_flag = True; motion = [ 0, -1]
		if pressed_key[pygame.K_DOWN]: rect.move_ip(0,1); update_flag = True; motion = [ 0, 1]

		world.draw_world()

		measurement = world.get_landmarks(rect.centerx, rect.centery)
#		motion_list.append(motion)
#		measurement_list.append(measurement)

		if update_flag:
#		if len(motion_list) > 100:
#			particle = particle_filter.update(motion_list,measurement_list)
			particle = particle_filter.update(motion, measurement)
			pos = particle_filter.get_position(particle)
			motion_list = []
			measurement_list = []
			print '------------'
			print 'truth: ' + str(rect.centerx) + ' ' + str(rect.centery)
			print 'estim: ' + str(int(pos[0]))  + ' ' + str(int(pos[1]))
			print 'accuracy ' + str(particle_filter.check_output([rect.centerx,rect.centery], pos))

		if rect.centerx > 350-5: rect.centerx = 350-5
		if rect.centerx < 0: rect.centerx = 0
		if rect.centery > WINDOW_SIZE[1]: rect.centery = WINDOW_SIZE[1]
		if rect.centery < 0: rect.centery = 0
		screen.blit(im,rect)
		
		if particle:
			for i in range(len(particle)):
				x = particle[i].x
				y = particle[i].y
				pygame.draw.circle(screen, (255,255,255), (int(x+WIDTH/2),int(y)),2)

		update_flag = False


