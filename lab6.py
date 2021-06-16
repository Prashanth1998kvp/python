class Person:
    def hello(self,name=None,age=None):
        if name!=None and age!=None:
            print("hello",name,"ur age is",age)
        elif name!=None and age==None:
            print("hello",name)
        else:
            print("hello")
p1=Person()
p1.hello()
p1.hello("kvp")
p1.hello("kvp",23)