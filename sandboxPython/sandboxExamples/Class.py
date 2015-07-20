class Person:

    def __init__(self, name):
        self.myVar = name

    def talk(self):
            print ("I [" + self.myVar + "] speak therefore I am!")

eric = Person("Eric")
eric.talk()
