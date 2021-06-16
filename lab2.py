set1={1,2,3,4}
set2={2,4,7}
set3={'kv','maha','spc','mani'}
while True:
    print("1.sizeof \n2.length \n3.insert \n4.pop \n5.intersection \n6.difference \n7.symmetric \n8.contain \n9.clear \n10.delete")
    ch=int(input("enter ur choice"))
    if ch==1:
        print(set1.__sizeof__())
    elif ch==2:
        print(len(set1))
    elif ch==3:
        a=int(input("enter a no"))
        set1.add(a)
    elif ch==4:
        set1.pop()
    elif ch==5:
        print(set1.intersection(set2))
    elif ch==6:
        print(set1-set2)
    elif ch==7:
        print(set1^set2)
    elif ch==8:
        print(set1.__contains__(2))
        print(set1.__contains__(9))
    elif ch==9:
        set1.clear()
        print(set1)
    elif ch==10:
        del set1
        print(set1)
    



