'''
	On this assignment, you should work with a partner. You must submit what you have completed at the end of the class period, but you do not need to complete any leftover problems for homework. 

	For some of these problems you will need to create a class; for others, you will need to use a library. 
	You do NOT need to put all your solutions in this file, however you should keep all your solutions together, clearly labeled with descriptive file names, in one folder. 
'''



''' 1.
	Create a class, Point, that keeps track of two properties: x and y
	When a point is created, values for x and y should be provided.

	The methods for this class are as follows:
	rotate90: rotate the point 90Â° about the origin
	rotate180: rotate the point 180Â° about the origin
	rotaten90: rotate -90Â° about the origin
	translate: given 2 values, translate the point by the given amount.
	flip_horizontally: flip the point on the x-axis
	flip_vertically: flip the point on the y-axis
'''

class Point:
	def __init__(x,y):
		self.x = x
		self.y = y
		self.point = (self.x,self.y)
	def rotate90(self):
		self.x = -1*self.y
		self.y = self.x
		self.point = (self.x,self.y)
	def rotate180(self):
		self.x = -1*self.x
		self.y = -1*self.y
		self.point = (self.x,self.y)
	def rotaten90(self):
		self.x = self.y
		self.y = -1*self.x
		self.point = (self.x,self.y)
	def translate(self,tx,ty):
		self.x += tx
		self.y += ty
		self.point = (self.x,self.y)
	def flip_horizontally(self):
		self.y = -1*self.y
		self.x = self.x
		self.point = (self.x,self.y)
	def flip_vertically(self):
		self.x = -1*self.x
		self.y = self.y
		self.point = (self.x,self.y)

''' 2.
	Create a class, Bicycle, that keeps track of three properties: cadence, gear, speed. 
	When a Bicycle is created, cadence, gear, and speed are accepted as arguments.

	The methods for this class are as follows:
	set_gear: given a value, set the gear to that value
	set_cadence: given a value, set the cadence to that value
	apply_brake: given a value, decrease the speed of the bike by that value
	speed_up: given a value, increase the speed of the bike by that value
'''

class Bicycle:
	def __init__(cadence, gear, speed):
		self.cadence = cadence
		self.gear = gear
		self.speed = speed
	def set_gear(self, value):
		self.gear = value
	def set_cadence(self, value):
		self.cadence = value
	def apply_brake(self, value):
		self.speed -= value
	def speed_up(self, value):
		self.speed += value

''' 3.
	Create a class, student, that keeps track of four properties: energy, hunger, stress, and hours.
	These properties have a range from 0-100, except hours, which has a range from 0-24. 100 energy means they are energetic; 100 hunger means they are very hungry; 100 stress means they are extremely stressed. When you create a new student, assume they have moderate hunger, low stress, a lot of energy, and 24 hours.

	The methods for the student class are as follows:
	study: Given a value (to adjust hours), study for that given length of time. Studying decreases energy and increases hunger based on the length of the study.
	sports: Given a value (to adjust hours), play sports for that given length of time. This decreases energy, increases hunger, and decreases stress based on the length of the sports.
	class: Given a value (to adjust hours), attend classes for a given length of time. This decreases energy, increases hunger, and increases stress based on the length of the class.
	take_test: Given a value (to adjust hours), this increases stress. 
	submit_paper: this decreases stress.
	eat_meal: Given a value (to adjust hours), this decreases stress, decreases hunger, and increases energy.
	sleep: Given a time (to adjust hours), this decreases stress, increases energy, and increases hunger.
	new_day: resets the hours in a day.

	You may not let a student do more than 24 hours worth of activities in a given day. 
'''

class student:
	def __init__ (energy, hunger, stress, hours):
		self.energy = energy
		self.hunger = hunger
		self.stress = stress
		self.hours = hours
		self.energy = 50
		self.hunger = 50
		self.stress = 50
		self.hours = 0

	def study(self,value):
		if self.hours < 24:
			self.energy -= value*2
			self.hunger += value*2
			self.hours += value
		else:
			self.new_day()

	def sports(self,value):
		if self.hours < 24:		
			self.energy -= (value)*4
			self.stress -= (value)*2
			self.hunger += (value)*3
			self.hours += value
		else:
			self.new_day()

	def classs(self,value):
		if self.hours < 24:
			self.energy -= (value)*3
			self.stress += (value)*2
			self.hunger += (value)*3
			self.hours += value
		else:
			self.new_day()

	def take_test(self,value):
		if hours < 24:
			self.stress += (value)*5
			self.hours += value
		else:
			self.new_day()

	def submit_paper(self):
		if self.hours < 24:
			self.stress += 20
		else:
			self.new_day()

	def eat_meal(self,value):
		if self.hours < 24:
			self.energy += (value)*2
			self.stress -= (value)*2
			self.hunger -= (value)*5
			self.hours += value
		else:
			self.new_day()

	def sleep(self,value):
		if self.hours < 24:
			self.energy += (value)*4
			self.stress -= (value)*5
			self.hunger += (value)*2
			self.hours += value
		else:
			self.new_day()

	def new_day(self):
		self.hours = 0




''' 4. 
	Use numpy to create an array of numbers going from 20 to 100 by increments of .25
	Then, multiply all the values in the array by 4. 
	Then. find the sum of all the values.
'''

import numpy as np
array = np.arange(20,100,0.25)
scaled = array * 4
summed = np.sum(scaled)


''' 5.
	Use turtle to draw a star.
'''

import turtle
turt = turtle.Turtle()
for i in range(5):
    turt.forward(300)
    turt.right(144)



''' 6.
	Use SymPy to determine the area of a triangle given points a, b and c.
'''

from sympy import Point, Polygon, pi
t = Polygon(a,b,c)
area = abs(t.area)
print(area)

''' 7. 
	Use VPython to build a 3D snowman.
'''



''' Sources:
	https://docs.oracle.com/javase/tutorial/java/javaOO/classes.html
'''