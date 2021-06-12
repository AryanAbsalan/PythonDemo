def my_function1():
  print("Hello from a function1")

def my_functionWithParameter(fname):
  print(fname + " printed")

def my_Array():
  cars = ["Ford", "Volvo", "BMW"]
  x = len(cars)
  print(x)
  print(cars)

def my_number(age):
  txt = "I am {} years old."
  print(txt.format(age))

def my_function5(p):
  if type(p) is str :
    print(p)
  else : 
    print("invalid parameter")

my_function1()
my_functionWithParameter("Python")
my_Array()
my_number(22)
my_function5("python")
my_function5(10)

