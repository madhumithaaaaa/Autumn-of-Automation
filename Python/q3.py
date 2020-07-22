class Complex:

	def __init__(self, re=0, im=0):
		self.re = re
		self.im = im

	def display(self):
		print("{} {} {}i".format(self.re, '+' if self.im>=0 else '-', abs(self.im)))

	def add(self, other):
		return Complex(self.re + other.re, self.im + other.im)

	def subtract(self, other):
		return Complex(self.re - other.re, self.im - other.im)

	def conjugate(self):
		return Complex(self.re, -self.im)

	def multiply(self, other):
		re = self.re * other.re - self.im * other.im
		im = self.im * other.re + self.re * other.im
		return Complex(re, im)

	def modulus(self):
		return sqrt((self.re)**2 + (self.im)**2)

	def inverse(self):
		return conjugate(self)/modulus(self)

'''a = Complex(1,2)
a.display()

b = Complex(2,-3)
c = b.add(a)

c.display()
c.conjugate().display()'''
