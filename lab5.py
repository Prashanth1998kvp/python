class Student:
    def __init__(self,name=None,usn=None,age=None):
        self.name=name
        self.usn=usn
        self.age=age
    def accept(self):
        self.name=input("enter name")
        self.usn=int(input("enter usn"))
        self.age=int(input("enter age"))
    def display(self):
        print(self.name)
        print(self.usn)
        print(self.age)
class Ug(Student):
    def __init__(self,sem=None,fee=None,stipend=None):
        super().__init__()
        self.sem=sem
        self.fee=fee
        self.stipend=stipend
    def Ugaccept(self):
        self.sem=int(input("enter sem"))
        self.fee=int(input("enter fee"))
        self.stipend=int(input("enter stipend"))
    def Ugdisplay(self):
        print(self.sem)
        print(self.fee)
        print(self.stipend) 
class Pg(Student):
    def __init__(self,sem=None,fee=None,stipend=None):
        super().__init__()
        self.sem=sem
        self.fee=fee
        self.stipend=stipend
    def Pgaccept(self):
        self.sem=int(input("enter sem"))
        self.fee=int(input("enter fee"))
        self.stipend=int(input("enter stipend"))
    def Pgdisplay(self):
        print(self.sem)
        print(self.fee)
        print(self.stipend)         
while True:
    print("1.ug \n2.pg \n3.display ug \n4.display pg")
    ch=int(input("enter ur choice"))
    if ch==1:
        a1=Ug()
        a1.accept()
    elif ch==2:
        a2=Pg()
        a2.accept()
    elif ch==3:
        a1.display()
    elif ch==4:
        a2.display()

