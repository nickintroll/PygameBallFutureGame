import pygame
from stuff import invert

class Object():

	def __init__(self, image, max_speed=3):
		self.image 					= pygame.image.load(image)
		self.rect 					= self.image.get_rect()

		self.vector_vertical 		= 0
		self.vector_horisontal 		= 0
		self.speed 					= [0.0, 0.0]

		# limits
		self.max_speed = max_speed 


	def limit_speed(self):

		speed = []
		for i in self.speed:
			if i > self.max_speed:
				print(self.speed)
				i = self.max_speed
			
			elif invert(self.max_speed) > i:
				print(self.speed)
				i = invert(self.max_speed)
				
			speed.append(i)
		self.speed = speed
	
	def rotate(self):
		self.rect = pygame.transform.scale(self.rect, 2)# rotate(self.rect, 20)

	def update(self, display_size, display=None, dif=0.1):
		# moving horisontal
		if self.vector_horisontal != 0:
			if self.vector_horisontal == 1:
				self.speed[0] += dif
			else:
				self.speed[0] -= dif
		else:
			if self.speed[0] != 0:
				if '-' in str(self.speed[0]):
					self.speed[0] += dif
				else:
					self.speed[0] -= dif

		# moving vertical
		if self.vector_vertical != 0:
			if self.vector_vertical == 1:
				self.speed[1] -= dif
			else:
				self.speed[1] += dif
		else:
			if self.speed[1] != 0:
				if '-' in str(self.speed[1]):
					self.speed[1] += dif
				else:
					self.speed[1] -= dif


		# borders
		old_speed = self.speed 
		if self.rect.left < 0:
			self.speed[0] = 0 - self.rect.left

		if self.rect.right > display_size[0]:
			self.speed[0] = invert(self.rect.right - display_size[0])

		if self.rect.top < 0: 
			self.speed[1] = 0 - self.rect.top
			# self.speed[1] -= invert(old_speed[1])
		if self.rect.bottom > display_size[1]:
			self.speed[1] = invert(self.rect.bottom - display_size[1])
			# self.speed[1] += old_speed[1]

		self.limit_speed()
		self.rect = self.rect.move(self.speed)
