import pyglet
from vector import *

center = Point(0, 0) 

G = 6.667 * (10 ** -11) # Gravational constant

class ObjectWithMass():	
	objects = []


	def __init__(self, sprite, mass, initial_pos, initial_v):
		self.sprite = sprite
		self.mass = mass
		self.pos = initial_pos
		self.v = initial_v
		ObjectWithMass.objects += [self]
		self.dv = Vector(0.0, 0.0)
	
	def draw(self):
		self.sprite.x = center.x + int(self.pos.x) - self.sprite.width // 2
		self.sprite.y = center.y + int(self.pos.y) - self.sprite.height // 2
		self.sprite.draw()

	def gravity(self):
		otherObjects = ObjectWithMass.objects[:]
		otherObjects.remove(self)
		self.dv = Vector(0.0, 0.0)
		for o in otherObjects:
			vec = self.pos - o.pos
			r = length(vec)
			Fg = (G * self.mass * o.mass) / (r ** 2)
			a = Fg / self.mass
			self.dv = self.dv + (unit(vec) * -a )


	def physics(self, dt):
		self.v = self.v + self.dv * dt
		self.pos += self.v * dt

class Player(ObjectWithMass):
	def __init__(self, player):
		if player == 1:
			self.image = pyglet.resource.image('images/player1.png')
			self.pos = Point(200.0, 0.0)
			self.v = Vector(0.0, 75.0)
		elif player == 2:
			self.image = pyglet.resource.image('images/player2.png')
			self.pos = Point(-200.0, 0.0)
			self.v = Vector(0.0, -75.0)
		self.sprite = pyglet.sprite.Sprite(self.image)
		self.mass = 50.0
		ObjectWithMass.objects += [self]
		self.dv = Vector(0.0, 0.0)

