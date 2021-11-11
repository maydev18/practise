class students:
    def get_details(self):  #self is an argument which will take the value of object
        #self vo object hai jispar get_details waala function lagega
        print(self.id,self.rollno,self.section)

    def get_marks(self):
        print("marks is 100")

mayank=students()
preeti=students()

mayank.id=20190258548
mayank.rollno=44
mayank.section="A"

preeti.id=20190258549
preeti.rollno=45
preeti.section="B"

mayank.get_details()#here the value of self will become mayank
preeti.get_details()#now self will take the object preeti

#mayank or preeti automatic arguments bn jyenge pr self ke pass chle jyenge. ye ek rule ha

#agar ma mayank.get_details(mayank) likhu to ma indirectly 2 arguments send kr rha hu get_details wale function mai jbki vo bs ek argument lega joki self ha or vo hmara object name ha.

mayank.get_marks()
preeti.get_marks()