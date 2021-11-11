#normally we cannot change the properties of a class by its object. rather it creates a
#new instance for that object.
#we can change the property of a class
# by directly accessing the class but not by directly accessing the object of that class

#class method

class preeti:
    marks=80
    @classmethod #decorator in python
    def changemarks(cls,newmarks):  #cls is just like self but instead of taking objects as a argument
        cls.marks=newmarks          #it takes class of the object as argument

mayank=preeti()
mayank.marks=95
print(mayank.marks)
#changing the marks by accessing the object
mayank.changemarks(96)
print(preeti.marks)
#we changed the marks of our class just by accessing the object of my class