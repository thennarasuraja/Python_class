# class MyClass:
#   x = 5

# p1 = MyClass()
# print(p1.x)
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person("John", 36)

# print(p1.name)
# print(p1.age)
import collections_basics
class animal:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

        def printname(self):
            return(self.firstname, self.lastname)


class cat(animal):
    def __init__(self, fname, lname, catcolor):
        super().__init__(fname, lname)
        super().__init__.printname()
        self.catcolor = catcolor

    def printname(self):
        print(self.catcolor, self.firstname, self.lastname)


x = cat("Mike", "Olsen", "white")
x.printname()
