car = {
  "brand": "Ford",
  "year": 1964,
  "model":None
}

x = car.setdefault("model", "Bronco")

print(car)
