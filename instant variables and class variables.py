class students:
    section="A"#this attribute is same for all the objects of class students

ram=students()      #these are the objects of the class students
shyam=students()    #these are the objects of the class students

ram.marks=100   #instant variables(attributes of an object) 
ram.subjects=["hindi","english","science"]

shyam.marks=95
shyam.subjects=["maths","sst"]

print(ram) #printing objects do not print the values(attributes) of them but print teh location of them
print("*****************")
print(ram.marks,ram.subjects,shyam.marks,shyam.subjects)
print("*****************")

print(ram.section)
print("*****************")
print(shyam.section)
print("*****************")

#changing the values of the attributes of a class
#we cannot change the class varaibles by class objects
ram.section="B"#it wont change the section of class students to B but will create a new instant variable for object ram
print(ram.section)
print("*****************")
print(shyam.section)#for shyam its class would be same as A
print("*****************")

#we can change the class variable by directly pointing thr class name rather than pointing the class objects

students.section="B"#it would be changed for all objects from now

print(ram.section,shyam.section)


#__dict__ function to show all the objects variables. it returns a dictionary. 

print(ram.__dict__)
print(shyam.__dict__)
print(students.__dict__) 