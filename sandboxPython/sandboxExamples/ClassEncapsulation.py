class Person:

	def __init__(self, name):
		self.myVarPublic = name
		
	#Encapsulation - method can only be accesed within class. Also called a "private method".
	def __classSecret(self):
		self.myVarPrivate = "Encapsulation Success!"

	def talk(self):
		self.__classSecret()
		print ("I [" + self.myVarPublic + "] speak therefore I am!" + " " + self.myVarPrivate)

eric = Person("Eric")
eric.talk()
