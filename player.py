import pyglet

class Player():
	def __init__(self, player, x, y):
		self.center = (x, y)
		if player == 1:
			self.image = pyglet.resource.image('images/player1.png')
			self.x = 200.0
		elif player == 2:
			self.image = pyglet.resource.image('images/player2.png')
			self.x = -200.0
		self.y = 0.0
		self.sprite = pyglet.sprite.Sprite(self.image)
	
	def draw(self):
		self.sprite.x = self.center[0] + int(self.x)
		self.sprite.y = self.center[1] + int(self.y)
		self.sprite.draw()
		

