import pyglet
from pyglet.window import key
from vector import *
from math import fabs

center = Point(0, 0) 

G = 6.667 * (10 ** -11) # Gravational constant

class ObjectWithMass(object):	
	objects = []
	heavyObjects = []
	collisionObjects = []

	def __init__(self, sprite, mass, initial_pos, initial_v, radius, collidable=True):
		self.sprite = sprite
		self.mass = mass
		self.pos = initial_pos
		self.v = initial_v
		ObjectWithMass.objects += [self]
		if mass > 10 ** 10: # Lite objects aren't going to have a major effect on gravity
			ObjectWithMass.heavyObjects += [self]
		self.dv = Vector(0.0, 0.0)
		self.radius = radius
		if collidable:
			ObjectWithMass.collisionObjects += [self]
	
	def draw(self):
		self.sprite.x = center.x + int(self.pos.x)
		self.sprite.y = center.y + int(self.pos.y)
		self.sprite.draw()

	def gravity(self):
		self.dv = Vector(0.0, 0.0)
		for o in ObjectWithMass.heavyObjects:
			vec = self.pos - o.pos
			r = length(vec)
			if not r == 0.0: # prevent devide by zero errors
				Fg = (G * self.mass * o.mass) / (r ** 2)
				a = Fg / self.mass
				self.dv = self.dv + (unit(vec) * -a )

	def physics(self, dt):
		self.v = self.v + self.dv * dt
		self.pos += self.v * dt
	
	def isColliding(self, other):
		return length(self.pos - other.pos) < self.radius + other.radius

	def collision(self, other):
		pass

	def delete(self):
		if ObjectWithMass.objects.__contains__(self):
			ObjectWithMass.objects.remove(self)
		if ObjectWithMass.heavyObjects.__contains__(self):
			ObjectWithMass.heavyObjects.remove(self)
		if ObjectWithMass.collisionObjects.__contains__(self):
			ObjectWithMass.collisionObjects.remove(self)

import wepons # This needs to be done after ObjectsWithMass is defined
from partical import Partical
import random

class Player(ObjectWithMass):
	def __init__(self, player):
		if player == 1:
			image = pyglet.resource.image('images/player1.png')
			pos = Point(200.0, 0.0)
			v = Vector(0.0, 75.0)
			self.dir = 0.0
		elif player == 2:
			image = pyglet.resource.image('images/player2.png')
			pos = Point(-200.0, 0.0)
			v = Vector(0.0, -75.0)
			self.dir = 180.0
		image.anchor_x = image.width // 2
		image.anchor_y = image.height // 2

		self.player = player
		self.engine = False
		self.rot = 0.0
		self.thrust = 25.0
		super(Player, self).__init__(pyglet.sprite.Sprite(image), 50.0, pos, v, 4)


	def draw(self):
		self.sprite.rotation = self.dir
		super(Player, self).draw()


	def physics(self, dt):
		super(Player, self).physics(dt)
		if fabs(self.rot) > 0.1:
			self.dir += self.rot * dt * 100.0
		if self.engine:
			self.v += vectorFromAngle(self.dir) * self.thrust * dt

	def collision(self, other):
		if hasattr(other, "activated"):
			if not other.activated:
				return
		if self.player == 1:
			colour = (0, 138, 208)
		else:
			colour = (255, 32, 32)
		for i in range(0, 35):
			v = self.v + Vector(random.gauss(0, 33), random.gauss(0, 33))
			Partical(colour, 0, self.pos, v)
		self.delete()

	def on_press(self, sym, mod):
		if self.player == 1:
			if sym == key.UP:
				self.engine = True
			elif sym == key.LEFT:
				self.rot -= 1.0 
			elif sym == key.RIGHT:
				self.rot += 1.0
			elif sym == key.DOWN:
				wepons.Mine(self.pos, self.v)
		else:
			if sym == key.W:
				self.engine = True
			elif sym == key.A:
				self.rot -= 1.0 
			elif sym == key.D:
				self.rot += 1.0
			elif sym == key.S:
				wepons.Mine(self.pos, self.v)

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

