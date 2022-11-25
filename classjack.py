class jack:
    a=100
    def __init__(self,a,b,c):
        self.name=a
        self.age=b
        self.gender=c

    def th(self):
        return(self.name)
    def ht(self):
        return(self.age)
    def hai(self):
        return(self.gender)      

c=jack("vel",20,"male")
print(c.th())
print(c.ht()) 
print(c.hai()) 
d=jack("thennarasu",20,"male") 
print(d.th())
print(d.ht())       
print(d.hai())
print(jack.a)