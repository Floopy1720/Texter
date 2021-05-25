class Dog:

	def __init__(self, name):
		self.name = name
		print(name)
		pass

	def bark(self):
		print("bark")
		pass

	def meow(self, x):
		return x+1
		pass

d = Dog("floopy")
d.bark()
print(d.meow(8))
print(type(d))