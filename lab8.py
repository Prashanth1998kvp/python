while True:
    print("1.enter the file name of source and destination \n2.open a file in read and write mode \n3.writing a file \n4.reading a file \n5.copy to new file")
    ch=int(input("enter ur choice"))
    if ch==1:
        sname=input("file name")
        dname=input("file name")
        print("files are created")
    if ch==2:
        try:
            a=open(sname,"r")
            b=open(dname,"w")
        except FileNotFoundError:
            print("file not found")
        else:
            print("open sucessfully")
    if ch==3:
        try:
            a=a.read()
            b.write(a)
        except NameError:
            print("name error")
        else:
            print("copied")
            a.close()
            b.close()
    if ch==4:
            try:
                b.read()
            except ValueError:
                print("value error:open a file first")
            else:
                print("read sucess")
    if ch==5:
        try:
            a=open(sname,"r")
            b=open(dname,"w")
            str1=a.read()
            b.write(str1)
        except IOError:
            print("error cant find")
        else:
            print("copied sucess")
            a.close()
            b.close()   