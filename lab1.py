while True:
    print("1.uppercase \n2.lowercase \n3.concate \n4.length \n5.reverse \n6.slicing \n7. split \n8.member \n9in \n10count")
    ch=int(input("enter ur choice"))
    if ch==1:
        a=input("enter a string")
        print(a.upper())
    elif ch==2:
        a=input("enter a string")
        print(a.lower())
    elif ch==3:
        a=input("enter a string1")
        b=input("enter a string2")
        print(a+b)
    elif ch==4:
        a=input("enter ur string")
        print(len(a))
    elif ch==5:
        a=input("enter a string")
        print(a[::-1])
    elif ch==6:
        a=input("enter a string")
       st=int(input("enter starting part"))
        en=int(input("enter ending part"))
        print(a[st:en]) 
    elif ch==7:
        a=input("enter a string")
        b=a.split()
        print(b)
    elif ch==8:
        a=input("enter a string")
        b=input("enter a string")
        c=a in b
        print(a,"in",b,c)
    elif ch==9:
        a=input("enter a string")
        b=input("enter a string")
        c=a not in b
        print(a,"not in",b,c)
    elif ch==10:
        a=input("enter a string")
        b=input("enter a string")
        print(a.count(b)) 