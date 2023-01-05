class Student:
    college='MTICA'
    course='MCA'
    def __init__(self,name,rollno):
        self.rollno=rollno
        self.name=name
    def DisplayStudent(self):
        print('name: '+self.name+'\nrollno: '\
              +str(self.rollno))
        print('college: '+self.college+'\ncourse : '+self.course)
        
lstobj=[]
for i in range(3):
    name=input()
    rollno=int(input())
    temp='obj'+str(i)
    temp=Student(name,rollno)
    lstobj.append(temp)
for i in lstobj:
    i.DisplayStudent()
    
