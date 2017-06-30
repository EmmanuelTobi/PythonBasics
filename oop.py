#python supports classes and their interactions
#a class can hold anything inside it and also we can make them interact

#the use of class allows Object Oriented programming an any language allowing the creating of a dynamic software

#with no constructor
class Person:
    eyes = "watches"
    ears = "hears"
    mouth = "speaks"
    
    def see(self):
        return "Watching a documentary"
    def eat(self):
        return "need to eat"
    def walk(self):
        return "tired of walking"

python = Person() #class initialization

print (python.ears) #an object to a class
print (python.walk()) #a function to a class, it takes in nothing because we made it (self) but still returns what we want



#using a constructor
class Arithmetic:
    def __init__(self, a, b):       #__init__ helps with the initialization of any variable to be used with a class
        self.a = a                  #self refers to the newly created object; in other class methods,                      
                                    #it refers to the instance whose method was called. 
        self.b = b

    def sum(self):
        c = self.a + self.b   
        return c

    def multiply(self):
        d = self.a * self.b
        return d

task = Arithmetic(157, 3) #initialization, always done after creating a class for easy referencing

print task.sum()
print task.multiply()