class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area1(self):
        self.a1=self.length*self.width
        print("Area=",self.a1)
    def __lt__(self,a2):
        if self.a1<a2.a1:
            return True
        else:
            return False
l=int(input("Enter the length of 1st rectangle:"))
w=int(input("Enter the width of 1st rectangle:"))
l2=int(input("Enter the length of 2nd rectangle:"))
w2=int(input("Enter the width of 2nd rectangle:"))
obj1=Rectangle(l,w)
obj2=Rectangle(l2,w2)
obj1.area1()
obj2.area1()
if obj1<obj2:
    print("2nd rectangle is large")
elif obj1>obj2:
    print("1st rectangle is large")
else:
    print("Both are equal")
