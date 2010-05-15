#!/usr/bin/python

import pyglet
from pyglet.window import key
import player
from player import *
from vector import *

window = pyglet.window.Window(fullscreen=True)
planet_image = pyglet.resource.image('images/planet18.png')
planet = ObjectWithMass(pyglet.sprite.Sprite(planet_image), 2.2 * 10**16, Point(0.0,0.0), Vector(0.0, 0.0))
planet.sprite.scale = 0.7

moon = ObjectWithMass(pyglet.sprite.Sprite(planet_image), 1.0 * 10**14, Point(150.0, 150.0), Vector(-50.0, 50.0))
moon.sprite.scale = 0.15

player1 = Player(1)
player2 = Player(2)

player.center = Point(window.width //2, window.height // 2)

@window.event
def on_draw():
	window.clear()
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

pyglet.clock.schedule_interval(updatePhysics, 0.02)

pyglet.app.run()

