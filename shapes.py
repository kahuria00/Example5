class  Circle:
	def __init__(self,radius):

		self.radius=radius
				
	def c_area(self):
		circle_area=22/7*self.radius
		print(circle_area)
		

	def circumfrence(self):
	    circle_cir=2*(22/7*self.radius)
	    print(circle_cir)
	    
class  Square:
	def __init__(self,side_a):
		self.side_a=side_a
	
	def s_area(self):
		square_area=self.side_a*self.side_a*self.side_a*self.side_a
		print(square_area)
	
	def s_perimeter(self):
		perimeter=self.side_a+self.side_a+self.side_a+self.side_a
		print(perimeter)

class  Rectangle:
	def __init__(self,length,width):
		self.length=length
		self.width=width

	def rec_area (self):
		rectangle_area=self.length*self.width
		print(rectangle_area)

	def rec_perimeter(self):
		rectangle_perimeter=2*(self.length+self.width)
		print(rectangle_perimeter)

class  Sphere:
	def __init__ (self,radius):
		self.radius=radius
	def SA(self):
		surface_area=4*(22/7*self.radius*self.radius)
		print(surface_area)

	def volume(self):
		sphere_vol=4/3*(22/7*self.radius*self.radius*self.radius)
		print(sphere_vol)






