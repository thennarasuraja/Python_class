class this_is_one:
    a=100
    def __init__(self, name, age, gender):
        self.fullname = name
        self.personage = age
        self.gender=gender

    def first(self):
        return (self.fullname)
    def second(self): 
        return (self.personage, self.gender)
    def third(self):
        return (int(self.personage))
    def fourth(self):
        return (self.gender)

a = {1, 2, 11, 13,14 }
person1 = {
    "name": "John",
    "age": 36,
    "country": "Norway"
}
print("one", __name__)
nandhini=this_is_one("subanandhini", 24, "female")
print(nandhini.first())
print(nandhini.second())
print(nandhini.third())
print(nandhini.fourth())
nandhini2=this_is_one("Nandhini2", 21, "female")
print(nandhini2.first())
print(nandhini2.second())
print(nandhini2.third())
print(nandhini2.fourth())
i=this_is_one("subanandhini", 24, "female")
print(i.first())
# j=this_is_one("dhivyakaran", 20)
# print(j.first())
