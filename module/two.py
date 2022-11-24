from  one import this_is_one as i
class this_is_two:
    def __init__(self, fname, lname):
        self.fname =fname
        self.lname = lname
    def second(self):
        return (self.fname, self.lname)

x=this_is_two("suba","nandhini")
print(x.second())
y=this_is_two("dhivya","karan")
print(y.second())
z=i("nandhini", 24)
print(z.first())
print(z.second())
print("two",__name__)