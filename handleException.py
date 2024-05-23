# handleException.py

try:
	print(x)
except NameError:
	print("Variable not define")
except:
	print("Something else went wrong")
finally:
	print("Try..Except completd")




try:
	print(5*9)
except:
	print("Something else went wrong")
else:
	print("Multiplication completed")


try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")


x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")