import classes
print(classes.animal.printname("lion", "king"))
list1 = ["apple", "banana", "apple", "cherry"]
list1[0]="change"
list1.append("Dates")  #changable
list1.remove("apple")  # ordered
list1.append("apple")  # duplicate
print(list1)
print(dir(list1))
print(type(list1))
print("###############################")
'''
List is a collection which is ordered and changeable. Allows duplicate members.

'''
list2 = ("apple", "banana",  "cherry",  "cherry", "apple", "cherry")


print(dir(list2))   # unchangable

print(type(list2))   # duplicate

print(list2)         # ordered
'''

Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
'''

list2 = {"apple1", "banana",  "cherry1",  "cherry2", "apple2", "cherry3"}
list2.add("Grapes") 
'''
{'apple1'}
"apple1", "banana"
"apple1", "banana",  "cherry1"
"apple1", "banana",  "cherry2"
"banana",  "cherry2", "apple2"
"banana",   "apple2", "cherry3"
"banana",   "apple2", "cherry3" ,'Grapes'

{'banana', 'apple', 'cherry', 'Grapes'}  # unordered  noduplicate unindexed
'''
print(dir(list2))    # unchangeable
print(type(list2))   
print(list2)         # ordered
'''
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
'''
list2 = {"fruit1":"banana",  "fruit2":"Grapes", "fruit3": "cherry3"}
list2.update({"fruit4": "apple"})
list2.update({"fruit3": "Melon"})
print(list(list2.values())[3])   #changable   nokeyduplicate ordered

if "apple" in list(list2.values()):
  print("Yes, 'apple' is in the fruits list")


print(dir(list2))

print(type(list2))   
print(list2)
'''

Dictionary is a collection which is ordered** and changeable. No duplicate members.
'''


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

print(thislist[-4:-1])
print(thislist[1])
print(thislist[-1])
print(thislist[2:5])
print(thislist[:4])
print(thislist[2:])
print(thislist[:])
thislist[1:4] = ["blackcurrant", "watermelon"]
thislist[1:2] = ["blackcurrant", "watermelon"]
thislist.insert(2, "watermelon")
thislist.append("orange")
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

thislist = ["apple", "banana", "cherry"]
thistuple = {"kiwi": "orange"}

thislist.extend(thistuple.keys())
#['apple', 'banana', 'cherry', 'kiwi']
thislist.extend(thistuple.values())
#['apple', 'banana', 'cherry', 'orange']
thislist.extend(thistuple.items())
#['apple', 'banana', 'cherry', ('kiwi','orange')]

print(thislist) 

thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
#['apple', 'banana', 'cherry', 'kiwi', 'orange']

thislist.remove("banana")
thislist.pop(1)
del thislist[0]
thislist.clear()
del thislist
print(thislist) #this will cause an error because you have succsesfully deleted "thislist".
thislist = ["apple", "banana", "cherry","graPES","mango"]
for i in range(0,len(thislist),2):
  print(thislist[i])

print(thislist)

## "abc" = ["a","b","c"]