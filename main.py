#!/usr/bin/python

import pyglet
from pyglet.window import key
import objects
from objects import *
from vector import *

window = pyglet.window.Window(fullscreen=True)
planet_image = pyglet.resource.image('images/planet3.png')
planet_image.anchor_x = planet_image.width // 2
planet_image.anchor_y = planet_image.height // 2
planet = ObjectWithMass(pyglet.sprite.Sprite(planet_image), 2.0 * 10**16, Point(0.0,0.0), Vector(0.0, 0.0), 60)
planet.sprite.scale = 0.66

stars = pyglet.resource.image('images/background.png')

#moon = ObjectWithMass(pyglet.sprite.Sprite(planet_image), 1.0 * 10**14, Point(150.0, 150.0), Vector(-50.0, 50.0))
#moon.sprite.scale = 0.15

player1 = Player(1)
player2 = Player(2)

objects.center = Point(window.width //2, window.height // 2)

@window.event
def on_draw():
	window.clear()
	stars.blit(0, 0)
	planet.sprite.rotation += 0.1
	for object in ObjectWithMass.objects:
		object.draw()

@window.event
def on_key_press(sym, mod):
	if sym == key.ESCAPE:
		pyglet.app.exit()
	player1.on_press(sym, mod)
	player2.on_press(sym, mod)

@window.event
def on_key_release(sym, mod):
	player1.on_release(sym,mod)
	player2.on_release(sym,mod)

def updatePhysics(dt):
	for object in ObjectWithMass.objects:
		object.gravity()
	for object in ObjectWithMass.objects:
		object.physics(dt)
	collisions = []
	for obj1 in ObjectWithMass.objects:
		otherObjects = ObjectWithMass.objects[:]
		otherObjects.remove(obj1)
		for obj2 in otherObjects:
			if obj1.isColliding(obj2):
				if not collisions.__contains__((obj2, obj1)):
					collisions += [(obj1, obj2)]
	for c in collisions:
		c[0].collision(c[1])
		c[1].collision(c[0])


pyglet.clock.schedule_interval(updatePhysics, 0.02)

pyglet.app.run()

