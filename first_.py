class Point(object):
	""" Point class for representing and manipulating x,y coordinates. """
	def __init__(self,x,y):
		self.x = x
		self.y = y

	def show(self):
		print("x->{} y->{}".format(self.x, self.y))

	def __str__(self):
		return "x->{} y->{} ".format(self.x, self.y)


class D3Point(Point):
	def __init__(self,x,y,z):
		super().__init__(x,y)
		self.z = z
	
	def __str__(self):
		return super().__str__() + "z->{}".format(self.z, self.y)

def change_x(point, x):
	point.x = x

point_1 = Point(2,5)
print(point_1)
change_x(point_1, 56)
point_1.show()

point_3d = D3Point(12,15, 17)
print(point_3d)
