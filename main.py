#!/usr/bin/python

import pyglet
from pyglet.window import key
import player
from player import Player, ObjectWithMass
from vector import *

window = pyglet.window.Window(fullscreen=True)
planet_image = pyglet.resource.image('images/planet.png')
planet = ObjectWithMass(pyglet.sprite.Sprite(planet_image), 2.0 * 10**16, Point(0.0,0.0), Vector(0.0, 0.0))
planet.sprite.scale = 0.1

player1 = Player(1)
player2 = Player(2)

player.center = Point(window.width //2, window.height // 2)

@window.event
def on_draw():
	window.clear()
	for object in ObjectWithMass.objects:
		object.draw()

@window.event
def on_key_press(symbol, modifiers):
	if symbol == key.ESCAPE:
		pyglet.app.exit()

def updatePhysics(dt):
	for object in ObjectWithMass.objects:
		object.gravity()
	for object in ObjectWithMass.objects:
		object.physics(dt)

pyglet.clock.schedule_interval(updatePhysics, 0.02)

pyglet.app.run()

