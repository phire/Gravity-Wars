#!/usr/bin/python

import pyglet

window = pyglet.window.Window()
planet_image = pyglet.resource.image('images/planet.png')
planet = pyglet.sprite.Sprite(planet_image)

@window.event
def on_draw():
	window.clear()
	planet.draw()

pyglet.app.run()

