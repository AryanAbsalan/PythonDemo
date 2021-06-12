def my_set():
  # Duplicates Not Allowed
  # Sets cannot have two items with the same value.
  thisset = {"apple", "banana", "cherry", "apple"}
  print(thisset)

def my_setPrint():
  thisset = {"apple", "banana", "cherry", "apple"}
  for x in thisset : 
    print(x)

def my_setAdd():
  thisset = {"apple", "banana", "cherry", "apple"}
  thisset.add("kiwi")
  for x in thisset :
    print(x)

  tropical = {"pineapple", "mango", "papaya"}
  mylist = ["kiwi", "orange"]

  thisset.update(tropical)
  print(thisset)
  thisset.update(mylist) # Duplicates Not Allowed
  print(thisset)


def my_setDelete():
  # Note: If the item to remove does not exist, 
  # remove() will raise an error.
  thisset = {"apple", "banana", "cherry", "apple","banana"}
  thisset.remove("apple") # removes both apples 
  for x in thisset : 
    print(x)

  # Note: If the item to remove does not exist, 
  # discard() will NOT raise an error.
  thisset = {"apple", "banana", "cherry", "apple","banana"}
  thisset.discard("banana") # removes both bananas
  for x in thisset : 
    print(x)

  thisset = {"apple", "banana", "cherry"}
  thisset.clear()
  print(thisset)

def my_setIntersection():
  x = {"apple", "banana", "cherry"}
  y = {"google", "microsoft", "apple"}
  z = x.intersection(y)
  print(z)

def my_setSymmetricDifference():
  x = {"apple", "banana", "cherry"}
  y = {"google", "microsoft", "apple"}
  z = x.symmetric_difference(y)
  print(z)

def my_setUnion():
  x = {"apple", "banana", "cherry"}
  y = {"google", "microsoft", "apple"}
  z = {"a", "b", "c"}
  mylist= ["f", "d", "a"]
  result = x.union(y, z, mylist) # Duplicates are excluded
  print(result)


my_set()
my_setPrint()
my_setAdd()
my_setDelete()
my_setIntersection()
my_setSymmetricDifference()
my_setUnion()




