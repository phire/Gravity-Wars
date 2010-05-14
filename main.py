#!/usr/bin/python

import pyglet
from pyglet.window import key

window = pyglet.window.Window(fullscreen=True)
planet_image = pyglet.resource.image('images/planet.png')
planet = pyglet.sprite.Sprite(planet_image)

@window.event
def on_draw():
	window.clear()
	planet.draw()

@window.event
def on_key_press(symbol, modifiers):
	print symbol, modifiers
	if symbol == key.ESCAPE:
		pyglet.app.exit()

pyglet.app.run()

