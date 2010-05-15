import pyglet
from pyglet.window import key
from vector import *
from math import fabs

center = Point(0, 0) 

G = 6.667 * (10 ** -11) # Gravational constant

class ObjectWithMass(object):	
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

class OrbitPredictor(object):
	objects = []
	marks = []

	def __init__(self, obj):
		self.mass = obj.mass
		self.pos = obj.pos
		self.v = obj.v
		OrbitPredictor.objects += [self]
		self.otherObjects = None

	def gravity(self):
		if self.otherObjects == None:
			self.otherObjects = OrbitPredictor.objects[:]
			self.otherObjects.remove(self)
		self.dv = Vector(0.0, 0.0)
		for o in self.otherObjects:
			vec = self.pos - o.pos
			r = length(vec)
			Fg = (G * self.mass * o.mass) / (r ** 2)
			a = Fg / self.mass
			self.dv += unit(vec) * -a
	
	def physics(self, dt):
		self.v += self.v + self.dv * dt
		self.pos += self.v * dt

class Player(ObjectWithMass):
	def __init__(self, player):
		if player == 1:
			self.image = pyglet.resource.image('images/player1.png')
			self.pos = Point(200.0, 0.0)
			self.v = Vector(0.0, 75.0)
			self.dir = 0.0
		elif player == 2:
			self.image = pyglet.resource.image('images/player2.png')
			self.pos = Point(-200.0, 0.0)
			self.v = Vector(0.0, -75.0)
			self.dir = 180.0
		self.sprite = pyglet.sprite.Sprite(self.image)
		self.mass = 50.0
		ObjectWithMass.objects += [self]
		self.dv = Vector(0.0, 0.0)
		self.player = player
		self.engine = False
		self.rot = 0.0
		self.thrust = 25.0

	def draw(self):
		self.sprite.rotation = self.dir
		super(Player, self).draw()


	def physics(self, dt):
		super(Player, self).physics(dt)
		if fabs(self.rot) > 0.1:
			self.dir += self.rot * dt * 100.0
		if self.engine:
			self.v += vectorFromAngle(self.dir) * self.thrust * dt


	def on_press(self, sym, mod):
		if self.player == 1:
			if sym == key.UP:
				self.engine = True
			elif sym == key.LEFT:
				self.rot -= 1.0 
			elif sym == key.RIGHT:
				self.rot += 1.0
		else:
			if sym == key.W:
				self.engine = True
			elif sym == key.A:
				self.rot -= 1.0 
			elif sym == key.D:
				self.rot += 1.0

	def on_release(self, sym, mod):
		if self.player == 1:
			if sym == key.UP:
				self.engine = False
			elif sym == key.LEFT:
				self.rot += 1.0 
			elif sym == key.RIGHT:
				self.rot -= 1.0
		else:
			if sym == key.W:
				self.engine = False
			elif sym == key.A:
				self.rot += 1.0 
			elif sym == key.D:
				self.rot -= 1.0

