# https://docs.python.org/3/library/json.html
import json
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
x={"name": "John", "age": 30}
print(type(x))
y=json.dumps(x)
print(y)
print(type(y))
print(json.dumps(x, indent=1))
print(json.dumps(x, indent=4, separators=("+ ", ":")))  #(", ", ": "))
print(json.dumps(x, indent=2, separators=(", ","= "), sort_keys=True))
