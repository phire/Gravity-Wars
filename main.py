#!/usr/bin/python

import pyglet
from pyglet.window import key
from player import Player

window = pyglet.window.Window(fullscreen=True)
planet_image = pyglet.resource.image('images/planet.png')
planet = pyglet.sprite.Sprite(planet_image)
planet.scale = 0.1
planet.x = window.width // 2 - planet.width // 2
planet.y = window.height // 2 - planet.height // 2

player1 = Player(1, window.width //2, window.height // 2)
player2 = Player(2, window.width //2, window.height // 2)



@window.event
def on_draw():
	window.clear()
	planet.draw()
	player1.draw()
	player2.draw()

@window.event
def on_key_press(symbol, modifiers):
	print symbol, modifiers
	if symbol == key.ESCAPE:
		pyglet.app.exit()

pyglet.app.run()

