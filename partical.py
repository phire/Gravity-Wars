import objects
import pyglet

pixel = pyglet.resource.image('images/partical.png')

def destroy(dt, partical):
	partical.destroy()

class Partical(objects.ObjectWithMass):
	def __init__(self, colour, life, pos, v):
		sprite = pyglet.sprite.Sprite(pixel)
		sprite.color = colour # damm americans 
		super(Partical, self).__init__(sprite, 0.1, pos, v, 1, False)
		if life > 0.0:
			pyglet.clock.schedule_once(destroy, life, self)

	def collision(self, other):
		self.delete()
	
	def draw(self):
		if self.pos.x > 1000 or self.pos.y > 800 or self.pos.x < -1000 or self.pos.y < -800:
			self.delete()
		else:
			super(Partical, self).draw()
	
	def destroy(self):
		self.delete()

