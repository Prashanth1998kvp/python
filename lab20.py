class Employee:
	raise_amt=1.04
	def __init__(self,firstname=None,lastname=None,id=None,pay=None):
		self.firstname=firstname
		self.lastname=lastname
		self.id=id
		self.pay=pay
	def accept(self):
		self.firstname=input("enter a firstname")
		self.lastname=input("enter a lastname")
		self.id=int(input("ente a id"))
		self.pay=int(input("enter a pay"))
#	def raise_amt(self):
	#	self.pay=int(self.pay*self.raise_amt)
	def display(self):
		print (self.firstname)
		print (self.lastname)
		print (self.id)
		print (self.pay)
class Manager(Employee):
	raise_amt=2.01
	def raise_amt1(self):
		self.pay=int(self.pay*self.raise_amt)
class Developer(Employee):
	raise_amt=2.02
	def raise_amt2(self):
		self.pay=int(self.pay*self.raise_amt)
while True:
	print ("1.create manager \n2.create developer \n3.display manager \n4.display developer \n5.raise manager \n6.raise developer")
	ch=int(input("enter ur choice"))
	if ch==1:
		e1=Manager()
		e1.accept()
	elif ch==2:
		e2=Developer()
		e2.accept()
	elif ch==3:
		e1.display()
	elif ch==4:
		e2.display()
	elif ch==5:
		e1.raise_amt1()
	elif ch==6:
		e2.raise_amt2()

