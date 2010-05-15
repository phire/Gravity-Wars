from math import sqrt, cos, sin, radians

class Point():
	def __init__(self, x, y=None):
		if y == None:
			self.x = x[0]
			self.y = x[1]
		else:
			self.x = x
			self.y = y
	
	def __sub__(self, other):
		if isinstance(other, Point):
			return Vector(self.x - other.x, self.y - other.y)
		elif isInstance(other, Vector):
			return Point(self.x - other.dx, self.y - other.dy)
		else:
			return NotImplemented

	def __add__(self, other):
		if isinstance(other, Vector):
			return Point(self.x + other.dx, self.y + other.dy)
		else:
			return NotImplemented
	
class Vector():
	def __init__(self, x, y=None):
		if y == None:
			self.dx = x[0]
			self.dy = x[0]
		else:
			self.dx = x
			self.dy = y

	def dot(self, other):
		return self.dx*other.dx + self.dy * other.dy

	def __mul__(self, scale):
		return Vector(scale*self.dx, scale* self.dy)

	def __div__(self, scale):
		return self.__mul__(1.0/scale)

	def __add__(self, other):
		return Vector(self.dx + other.dx, self.dy + other.dy)


def length(v):
	return sqrt(v.dot(v))

def unit(v):
	return v / length(v)

def vectorFromAngle(a):
	a = radians(a)
	return Vector(sin(a), cos(a))
