class Time:
    sum=0
    def __init__(self,hour,minute,second):
        self.hour = hour
        self.minute = minute
        self.second = second
    def sum(self):
        self.sum = self.hour*60*60+self.minute*60+self.second
    def __add__(self,second):
        return self.sum + second.sum

h1 = int(input("Enter the 1st hour:"))
m1 = int(input("Enter the 1st minute:"))
s1 = int(input("Enter the 1st second:"))
print("Time 1 is = ",h1,":",m1,":",s1,"\n");
h2 = int(input("Enter the 2nd hour:"))
m2 = int(input("Enter the 2nd minute:"))
s2 = int(input("Enter the 2nd second:"))
print("Time 2 is = ",h2,":",m2,":",s2,"\n")    
obj1 = Time(h1,m1,s1)
obj2 = Time(h2,m2,s2)
obj1.sum()
obj2.sum()
s=obj1+obj2
hour = int(s/3600)
mini = int((s%3600)/60)
sec = int((s% 3600)%60)
print("The sum of two time = {0} hours: {1} mins: {2} secs".format(hour,mini,sec))

