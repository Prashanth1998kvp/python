class Operator:
    def __init__(self):
        self.alist=[]
    def getelments(self):
        n=int(input("enter a value"))
        for i in range(0,n):
            self.alist.append(int(input("enter element")))
    def __add__(self,other):
        blist=[]
        for i in range(0,len(self.alist)):
            blist.append(self.alist[i]+other.alist[i])
        return(blist)
    def __mul__(self,other):
        blist=[]
        for i in range(0,len(self.alist)):
            blist.append(self.alist[i]*other.alist[i])
        return(blist)
    def __floordiv__(self,other):
        blist=[]
        for i in range(0,len(self.alist)):
            blist.append(self.alist[i]//other.alist[i])
        return(blist)
    def __sub__(self,other):
        blist=[]
        for i in range(0,len(self.alist)):
            blist.append(self.alist[i]-other.alist[i])
        return(blist)
    
