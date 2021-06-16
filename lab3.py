d={}
class Employee:
    def salary(self,name,address,pan,basic,deduct):
        self.name=name
        self.address=address
        self.pan=pan
        self.basic=basic
        self.da=basic*5
        self.hra=basic*25
        self.tdf=500
        self.deduct=deduct
        netsal=basic+self.da+self.hra-(self.tdf+deduct)
        return(netsal)
    def accept(self):
        name=input("name")
        address=input("address")
        pan=int(input("pan"))
        basic=int(input("basic"))
        deduct=int(input("deduct"))
        self.netsal=self.salary(name,address,pan,basic,deduct)
    def display(self):
        print(self.name)
        print(self.address)
        print(self.netsal)
    def search(name):
        for k,v in d.items():
            if k==name:
                v.display()
while True:
    print("1.employee details \n2.display \n3.update \n4.search")
    ch=int(input("enter ur choice"))
    if ch==1:
        e=Employee()
        print(e)
        e.accept()
    elif ch==2:
        e.display()
    elif ch==3:
        d.update({e.name:e})
    elif ch==4:
        Name=input("enter a name")
        Employee.search(Name) 
           
