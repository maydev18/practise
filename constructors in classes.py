class students:
    #we use __init__() to create a constructor it helps to take arguments in class
    def __init__(self,section,id,marks,stream):
        '''note-we donot have to call __init__() function. its bydefault ,when ever we pass arguments
         in a class it
        automatically calls __init__() function'''
        self.section=section
        self.id=id
        self.marks=marks
        self.stream=stream

mayank=students("A",20190258548,483,"science")
'''student ek class ha jiske andar ham ek object create krre mayank jiske details hmne as a argument enter krdi 
 ha vo sari details by default __init__ function par jati ha jha self argument to object(mayank/preeti) ko 
 leta ha or baki arguments jo ham pass krte ha'''

preeti=students("B",20190258549,500,"commerce")

print(mayank.id)
print(preeti.stream)


class employee:
    def __init__(self,age,department,salary,gender):
        self.age=age
        self.department=department
        self.salary=salary
        self.gender=gender

ravi=employee(27,"IT",30000,"male")

print(ravi.age)
print(ravi.gender)

'''isse yeh fayda hota ha ki hamko bar bar ab apne objects ki details ko specify ni krna pdta like
ravi.age=27, ravi.gender="male" and like that. ab ham ek init function bnakr object ki details wha dal skte ha
or isse objects bnane ma help milti ha'''
