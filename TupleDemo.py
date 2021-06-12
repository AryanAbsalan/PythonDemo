def my_tuple():
  # Duplicates Not Allowed
  # you can convert it into a list,
  # add your item(s), 
  # and convert it back into a tuple.
  thistuple = ("apple", "banana", "cherry")
  y = list(thistuple)
  y.append("orange")
  thistuple = tuple(y)

def my_tupleUnpack():
  fruits = ("apple", "banana", "cherry")
  (green, yellow, red) = fruits
  print(green)
  print(yellow)
  print(red)
  # If the number of variables is less than the number of values,
  # you can add an * to the variable name and 
  # the values will be assigned to the variable as a list
  fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
  (green, yellow, *red) = fruits
  print(green)
  print(yellow)
  print(red)

def my_tuplePrint():
  thistuple = ("apple", "banana", "cherry")
  for x in thistuple:
    print(x)

  for i in range(len(thistuple)):
    print(thistuple[i])

def my_tupleCount():
  thistuple = ("apple", "banana", "cherry",
               "apple", "banana", "cherry",
               "apple", "banana", "cherry",
               "apple", "banana", "cherry",
               "apple", "banana", "cherry")
  apple = thistuple.count("apple")
  print(apple)

def my_tupleIndex():
  thistuple = ("apple", "banana", "cherry",
               "apple", "banana", "cherry")
  appleIndex = thistuple.index("apple")
  print(appleIndex)

  text = "Index of \"apple\":{}" 
  print( text.format( thistuple.index("apple")))

  text = "Index of \"banana\":{}" 
  print( text.format( thistuple.index("banana")))

  text = "Index of \"cherry\":{}" 
  print( text.format( thistuple.index("cherry")))


my_tuple()
my_tupleUnpack()
my_tuplePrint()
my_tupleCount()
my_tupleIndex()
