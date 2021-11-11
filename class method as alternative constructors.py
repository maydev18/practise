class mayank:
    def __init__(self,name,section,school):
        self.name=name
        self.section=section
        self.school=school
    @classmethod
    def makeobject(cls,string):
        list=string.split(" ")
        return mayank(list[0],list[1],list[2])


ravi=mayank("ravi","A","mount")
print(ravi.__dict__)

neha=mayank.makeobject("neha B lc2")
print(neha.__dict__)