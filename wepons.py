import pyglet
import objects

mineImage = pyglet.resource.image('images/mine.png')
mineImage.anchor_x = mineImage.width // 2
mineImage.anchor_y = mineImage.height // 2

def activate(dt, mine):
	mine.activate()

class Mine(objects.ObjectWithMass):
	def __init__(self, location, velocity):
		sprite = pyglet.sprite.Sprite(mineImage)
		self.activated = False
		super(Mine, self).__init__(sprite, 1.0, location, velocity, 1.5)
		pyglet.clock.schedule_once(activate, 2.5, self)

	def activate(self):
		self.activated = True
