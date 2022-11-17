from cmath import e
from logging import exception
from warnings import catch_warnings


thislist = ["apple", "banana", "cherry"]
i = 0
try:
  while i < len(thislist):
    print(thislist[i])
    i = i + 1
  catch_warnings(e)
  print("e")
finally:
    print("e")
[print(x) for x in thislist]
