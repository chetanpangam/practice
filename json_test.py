# json.py
import json

print(type(json.dumps({"name": "John", "age": 30})))
print(json.dumps({"name": "John", "age": 30}))

print(type(json.dumps(["apple", "bananas"])))
print(json.dumps(["apple", "bananas"]))

print(type(json.dumps(("apple", "bananas"))))
print(json.dumps(("apple", "bananas")))

print(type(json.dumps("hello")))
print(json.dumps("hello"))

print(type(json.dumps(42)))
print(json.dumps(42))

print(type(json.dumps(31.76)))
print(json.dumps(31.76))

print(type(json.dumps(True)))
print(json.dumps(True))

print(type(json.dumps(False)))
print(json.dumps(False))

print(type(json.dumps(None)))
print(json.dumps(None))


x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x, indent=4))
new_string = json.dumps(x)
print(new_string)

print(type(json.loads(new_string)))
print(json.loads(new_string))