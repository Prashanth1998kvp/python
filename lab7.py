class Employee:
    raise_amt=1.03
    def __init__(self,name=None,id=None,pay=None):
        self.name=name
        self.id=id
        self.pay=pay
    def accept(self):
        self.name=input("enter ur name")
        self.id=int(input("enter ur id"))
        self.pay=int(input("enter ur pay"))
    def raise_amt(self):
        self.pay=int(self.pay*self.raise_amt)
    def dipslay(self):
        print(self.name)
        print(self.id)
        print(self.pay)
class Manager(Employee):
    raise_amt=2.04
    def raise_amt1(self):
        self.pay=int(self.pay*self.raise_amt)
class Developer(Employee):
    raise_amt=1.64
    def raise_amt2(self):
        self.pay=int(self.pay*self.raise_amt)
while True:
    print("1.create manager \n2.create developer \n3.display manager \n4.display developer \n5.raise manager \n6.raise developer")
    ch=int(input("enter ur choice"))
    if ch==1:
        e1=Manager()
        e1.accept()
    elif ch==2:
        e2=Developer()
        e2.accept()
    elif ch==3:
        e1.dipslay()
    elif ch==4:
        e2.dipslay()
    elif ch==5:
        e1.raise_amt1()
    elif ch==6:
        e2.raise_amt2()