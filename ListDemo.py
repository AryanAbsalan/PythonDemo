def my_list():
  myList = ["Enter","Esc","F1","F5"]
  print(myList)

def my_listConstructor():
   # note the double round-brackets
  mylist = list(("apple", "banana", "cherry"))
  print(mylist)

def my_printList():
  thislist = ["apple", "banana", "cherry", "orange", 
              "kiwi", "melon", "mango"]
  print(thislist[:5])
  print(thislist[2:])
  print(thislist[3:5])
  for x in thislist:
    print(x)
  for x in range(len(thislist)):
     print(x)

def my_changeList():
  thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
  thislist[1:3] = ["blackcurrant", "watermelon","watermelon",
                    "watermelon","watermelon"]
  print(thislist)

def my_insertList():
  thislist = ["apple", "banana", "cherry"]
  thislist.insert(2, "watermelon")
  print(thislist) 

def my_appendList():
  thislist = ["apple", "banana", "cherry"]
  thislist.append("orange")
  print(thislist)

def my_extendList():
  thislist = ["apple", "banana", "cherry"]
  tropical = ["mango", "pineapple", "papaya"]
  thislist.extend(tropical)
  print(thislist)
  # you can add any iterable object 
  # (tuples, sets, dictionaries) to a list
  thislist = ["apple", "banana", "cherry"]
  thistuple = ("kiwi", "orange")
  thislist.extend(thistuple)
  print(thislist)

def my_removeList():
  thislist = ["apple", "banana", "cherry"]
  thislist.remove("banana")
  print(thislist)
  print("######## remove #########")
  thislist = []
  print(thislist)
  fruits = ['apple', 'banana', 'cherry', 'orange']
  fruits.clear()

def my_popList():
  thislist = ["apple", "banana", "cherry"]
  thislist.pop(1)
  print(thislist)
  # If you do not specify the index, 
  # the pop() method removes the last item.
  thislist = ["apple", "banana", "cherry"]
  thislist.pop()
  print(thislist)

def my_deleteList():
  thislist = ["apple", "banana", "cherry"]
  del thislist[0]
  print(thislist)
  # The del keyword can also delete the list completely.
  del thislist

def my_searchList():
  fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
  newlist = []
  for x in fruits:
    if "a" in x:
      newlist.append(x)

  print("new list items:")    
  print(newlist)

def my_sortList():
  thislist = [100, 50, 65, 82, 23]
  thislist.sort()
  print(thislist)

  thislist = [100, 50, 65, 82, 23]
  thislist.sort(reverse = True)
  print(thislist)

  thislist = ["apple", "banana", "cherry", "kiwi", "mango"]
  thislist.sort()
  print(thislist)

  thislist = ["apple", "banana", "cherry", "kiwi", "mango"]
  thislist.sort(reverse = True)
  print(thislist)

  fruits = ['apple', 'banana', 'cherry']
  fruits.reverse()
  print(thislist)

def my_copyList():
  thislist = ["apple", "banana", "cherry", "kiwi", "mango"]
  newList = thislist.copy()
  print(newList)

  thislist = ["apple", "banana", "cherry", "kiwi", "mango"]
  newList = list(thislist)
  print(newList)

def my_joinList():
  firstlist = ["apple", "banana", "cherry", "kiwi", "mango"]
  secondlist = [ "kiwi", "mango"]
  newList = firstlist + secondlist
  print(newList)

  firstlist = ["apple", "banana", "cherry", "kiwi", "mango"]
  secondlist = [ "kiwi", "mango"]
  for x in secondlist:
    firstlist.append(x)
  print(firstlist)

  firstlist = ["apple", "banana", "cherry", "kiwi", "mango"]
  secondlist = [ "kiwi", "mango"]
  firstlist.extend(secondlist)
  print(firstlist)


my_list()
my_listConstructor()
my_printList()
my_changeList()
my_insertList()
my_appendList()
my_extendList()
my_removeList()
my_popList()
my_deleteList()
my_searchList()
my_sortList()
my_copyList()
my_joinList()