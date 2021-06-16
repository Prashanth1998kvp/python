from lab4 import *
a=Operator()
a.getelments()
b=Operator()
b.getelments()
while True:
    print("1.add \n2.mul \n3.div \n4.sub")
    ch=int(input("enter ur choice"))
    if ch==1:
        print(a+b)
    elif ch==2:
        print(a*b)
    elif ch==3:
        print(a//b)
    elif ch==4:
        print(a-b)
