class Person:

	#Method Overloading - Without/ With Parameter
	def talk(self, name=None):
			if name is None:
				print ("Parameter Value does not Exist")
			else:
				print ("Parameter Value Exists: " + name)

eric = Person()

#Call the method without a parameter
eric.talk()

#Call the method with a parameter
eric.talk("hey!")
