
"""
    The following are the properties of a list.

    Mutable: The elements of the list can be modified. 
    Ordered: The items in the lists are ordered. Each item has a unique index value. The new items will be added to the end of the list.
    Heterogenous: The list can contain different kinds of elements i.e; they can contain elements of string, integer, boolean, or any type.
    Duplicates: The list can contain duplicates.

    remove(item)	To remove the first occurrence of the item from the list.
    pop(index)	Removes and returns the item at the given index from the list.
        Note: It will remove the last time from the list if the index number is not passed.

    clear()	To remove all items from the list. The output will be an empty list.
    del list_name	Delete the entire list.

    listname[start_index : end_index : step]

    The copy method can be used to create a copy of a list. 
    This will create a new list and any changes made in the original list will not reflect in the new list. 
    This is shallow copying.

    mylist = [3, 4, 5, 6, 1]
    print(max(mylist)) #returns the maximum number in the list.
    print(min(mylist)) #returns the minimum number in the list.
    print(sum(mylist)) 
    print(mylist.sort()) 
    print(mylist.reverse()) 
    mylist.clear()

    The all() method, the return value will be true only when all the values inside the list are true.
        In the case of Empty List, it will return true.
    The any() method will return true if there is at least one true value.
        In the case of Empty List, it will return false.
    
    l1 = [10, 20, 30, 40, 50] and l2 = [60, 70, 80, 60]
    x in l1	:       Check if the list l1 contains item x.
    x not in l2:	Check if list l1 does not contain item x.


"""


# if-else in one line – Ternary operator
# value_1 if condition else value_2
x = 20
result = 'High' if x > 10 else 'Low'
result = 10 + (10 if x > 100 else 0)

# While loop with else
x = 1
while x <= 10:
    print(x)
    x = x + 1
else:
    print('printed values from 1 to 10')

# Use for loop to display: numbers in descending order
for i in range(10, 0, -1):
    print('Number: ', i)

# For loop with else block
for elem in 'Sample':
    print('Character: ', elem)
else:
    print('<<<<')
    print('End of Loop')
    print('>>>>')

# List Comprehension
''' 
    Use List Comprehension with range() to initialize a list by 20 elements 0
    It will iterate over the tange from 0 to 20 and for
    each entry, it will add 'Hi' to the list and in the end 
    returns the list to listOfStrings
'''
listOfStrings = ['Hi' for i in range(20)]

# change the value of the first three elements to 10.
list_of_numbers = [9, 10, 11, 12, 13, 14, 15]
list_of_numbers[0:3] = [10, 10, 10]

#creating a list with square values with 2 conditions
inputList = [4,7,11,13,18,20]
squareList = [var**2 for var in inputList if var%2==0 if var>=18]
print(squareList)

'''
 Iterate over the list using List Comprehension
'''
wordList = ['hi', 'hello', 'this', 'that', 'is', 'of']
[print(word) for word in wordList]

# Remove first occurrence of 52 from list
list_of_num = [51, 52, 53, 54, 55, 52, 57, 52, 59]
list_of_num.remove(52)
# list_of_num.remove(70)
# ValueError: list.remove(x): x not in list
elem = 70
if elem in list_of_num:
    list_of_num.remove(elem)

# Remove all occurrences of an element from a list by value
def remove_all_occurrences(list_obj, value):
    while value in list_obj:
        list_of_num.remove(value)

remove_all_occurrences(list_of_num, 52)

# Remove all occurrences of multiple elements from a list by values
def remove_all_by_values(list_obj, values):
    for value in values:
        while value in list_obj:
            list_of_num.remove(value)

list_of_num = [51, 52, 52, 55, 55, 52, 57, 52, 55, 61, 62]
remove_all_by_values(list_of_num, [52, 55, 57])

# Find index position of first occurrence of 'Ok' in the list
list_of_elems = ['Hello', 'Ok', 'is', 'Ok', 'test', 'this', 'is', 'a', 'test', 'Ok']
elem = 'Ok'
index_pos = list_of_elems.index(elem)
print(f'First Index of element "{elem}" in the list : ', index_pos)

# Element "Why" not found in the list:  'Why' is not in list
list_of_elems = ['Hello', 'Ok', 'is', 'Ok', 'test', 'this', 'is', 'a', 'test', 'Ok']
elem = 'Why'
try:
    index_pos = list_of_elems.index(elem)
    print(f'First Index of element "{elem}" in the list : ', index_pos)
except ValueError as e:
    print(f'Element "{elem}" not found in the list: ', e)


# Get last index of item in list
list_of_elems = ['Hello', 'Ok', 'is', 'Ok', 'test', 'this', 'is', 'a', 'test']
elem = 'Ok'
try:
    # Get last index of item 
    index_pos = len(list_of_elems) - list_of_elems[::-1].index(elem) - 1
    print(f'Last Index of element "{elem}" in the list : ', index_pos)
except ValueError as e:
    print(f'Element "{elem}" not found in the list: ', e)

# Find all indices of an item in list using list.index()
def get_index_positions(list_of_elems, element):
    ''' Returns the indexes of all occurrences of give element in
    the list- listOfElements '''
    index_pos_list = []
    index_pos = 0
    while True:
        try:
            # Search for item in list from indexPos to the end of list
            index_pos = list_of_elems.index(element, index_pos)
            # Add the index position in list
            index_pos_list.append(index_pos)
            index_pos += 1
        except ValueError as e:
            break
    return index_pos_list

list_of_elems = ['Hello', 'Ok', 'is', 'Ok', 'test', 'this', 'is', 'a', 'test', 'Ok']

# Get indexes of all occurrences of 'Ok' in the list
index_pos_list = get_index_positions(list_of_elems, 'Ok')
print('Indexes of all occurrences of "Ok" in the list are : ', index_pos_list)

def get_index_positions_2(list_of_elems, element):
    ''' Returns the indexes of all occurrences of give element in
    the list- listOfElements '''
    index_pos_list = []
    for i in range(len(list_of_elems)):
        if list_of_elems[i] == element:
            index_pos_list.append(i)
    return index_pos_list
list_of_elems = ['Hello', 'Ok', 'is', 'Ok', 'test', 'this', 'is', 'a', 'test', 'Ok']

# Get indexes of all occurrences of 'Ok' in the list
index_pos_list = get_index_positions_2(list_of_elems, 'Ok')
print('Indexes of all occurrences of a "Ok" in the list are : ', index_pos_list)

# Use List Comprehension to find all indexes of an item in list
# Use List Comprehension Get indexes of all occurrences of 'Ok' in the list
index_pos_list = [ i for i in range(len(list_of_elems)) if list_of_elems[i] == 'Ok' ]
print('Indexes of all occurrences of a "Ok" in the list are : ', index_pos_list)

'''
    This function accepts a list of elements and a callback function as arguments. 
    For each element it calls the callback function and if callback() function returns True 
    then it keeps the index of that element in a new list.
    In the end it returns the indexes of items in the list for which callback() returned True.
'''
def get_index_positions_by_condition(list_of_elems, condition):
    ''' Returns the indexes of items in the list that returns True when passed
    to condition() '''
    index_pos_list = []
    for i in range(len(list_of_elems)):
        if condition(list_of_elems[i]) == True:
            index_pos_list.append(i)
    return index_pos_list

list_of_elems = ['Hello', 'Ok', 'is', 'Ok', 'test', 'this', 'is', 'a', 'test', 'Ok']
# get index position of string elements in list whose length are greater than 3
index_pos_list = get_index_positions_by_condition(list_of_elems, lambda x : len(x) < 3)
print('Index positions of the string elements in list with length less than 3 : ', index_pos_list)
# get index position of string elements in list whose value are test
index_pos_list = get_index_positions_by_condition(list_of_elems, lambda x : str(x) =='test')
print('Index positions of the string elements in list with test as value : ', index_pos_list)

#List Of Strings
listOfStrings = ['hi' , 'hello', 'at', 'this', 'there', 'from']
# Sort List of string by Length by using len() as custom key function 
listOfStrings.sort(key=len)

'''    
    check if element exist in list using 'in'
'''
if 'at' in listOfStrings :
    print("Yes, 'at' found in List : " , listOfStrings)

'''    
    check if element NOT exist in list using 'in'
'''
if 'time' not in listOfStrings :
    print("Yes, 'time' NOT found in List : " , listOfStrings)

'''    
    check if element exist in list using count() function
'''
if listOfStrings.count('at') > 0 :
    print("Yes, 'at' found in List : " , listOfStrings)

'''    
    check if element exist in list based on custom logic
    Check if any string with length 5 exist in List
'''
result = any(len(elem) == 5 for elem in listOfStrings)
if result:
    print("Yes, string element with size 5 found")

# using separate function in any to match the condition
def checkIfMatch(elem):
    if len(elem) == 5:
        return True
    else :
        return False

'''    
    Check if any string that satisfies the condition in checkIfMatch() function  exist in List
'''
result = any(checkIfMatch for elem in listOfStrings)
if result:
    print("Yes, string element with size 5 found")

# List of tuples i.e. word and its frequency count    
'''
By default sort() function will sort the list of tuple by first item in tuple
'''    
wordFreq = [ ('the' , 34) , ('at' , 23), ('should' , 1) , ('from' , 3) ]
wordFreq.sort()
# Key Function 
'''
While sorting a list, all the elements of list will be compared with each other.
But before comparison it will call the key function on each entry, 
to determine what portion of the object will compared.
'''

# Sort List of tuple by 2nd Item of tuple, using Lambda Function as key function
wordFreq.sort(key=lambda elem: elem[1])

# Sort List of tuple by 2nd Item of tuple, using custom function or Comparator
def comparator( tupleElem ) :
    return tupleElem[1]

wordFreq.sort(key=comparator)

# Join / Merge two lists in python using itertools.chain()

import itertools
# List of strings
list_1 = ["This" , "is", "a", "sample", "program"]
# List of ints
list_2 = [10, 2, 45, 3, 5, 7, 8, 10]
# Join two lists
final_list=list(itertools.chain(list_1, list_2))
print('Merged List:')
print(final_list)

# List of lists
listOfElems2D = [ 
                  [1,2,3,45,6,7],
                  [22,33,44,55],
                  [11,13,14,15] 
                ]
# Iterate over the list and add the size of all internal lists 
count = 0
for listElem in listOfElems2D:
    count += len(listElem)                    
print('Total Number of elements : ', count)

# Get the size of list of list using list comprehension & sum() function
count = sum( [ len(listElem) for listElem in listOfElems2D])
print('Total Number of elements : ', count)

# Nested List
def getSizeOfNestedList(listOfElem):
    ''' Get number of elements in a nested list'''
    count = 0
    # Iterate over the list
    for elem in listOfElem:
        # Check if type of element is list
        if type(elem) == list:  
            # Again call this function to get the size of this element
            count += getSizeOfNestedList(elem)
        else:
            count += 1    
    return count

nestedList = [2 ,3, [44,55,66], 66, 
                    [5,6,7, [1,2,3], 6] , 10, 
                    [11, [12, [13, 24]]]
             ] 
count = getSizeOfNestedList(nestedList)
print('Total Number of elements : ', count)
    
''' 
map() Function in python accepts a function and an iterable like list. 
Then applies the given function to each element in the list and appends the result of function in a new list. 
In the end map() returns this new list i.e. list of results.
'''
listOfElems = [11, 22, 33, 45, 66, 77, 88, 99, 101]
# Count odd numbers in the list
count = sum(map(lambda x : x%2 == 1, listOfElems))
print('Count of odd numbers in a list : ', count) # Count of odd numbers in a list :  6
# Count even numbers in the list
count = sum(map(lambda x : x%2 == 0, listOfElems))
print('Count of even numbers in a list : ', count)
# count numbers in the list which are greater than 5
count = sum(map(lambda x : x>5, listOfElems))
print('Count of numbers in a list which are greater than 5: ', count)

# Returns the count of elements in list that satisfies the given condition
def getCount(listOfElems, cond = None):
    if cond:
        count = sum(cond(elem) for elem in listOfElems)
    else:
        count = len(listOfElems)    
    return count   
# count numbers in the list which are greater than 5 but less than 20
count = getCount(listOfElems, lambda x : x>5 and x < 20)
print('Count of numbers in a list which are greater than 5 but less than 20 : ', count)

# count numbers in the list which are greater than 5
count = len([elem for elem in listOfElems if elem > 5])
print('Count of numbers in a list which are greater than 5: ', count)

# Get frequency count of duplicate elements in the given list 
def getDuplicatesWithCount(listOfElems):
    dictOfElems = dict()
    # Iterate over each element in list
    for elem in listOfElems:
        # If element exists in dict then increment its value else add it in dict
        if elem in dictOfElems:
            dictOfElems[elem] += 1
        else:
            dictOfElems[elem] = 1    
 
    # Filter key-value pairs in dictionary. Keep pairs whose value is greater than 1 
    # i.e. only duplicate elements from list.
    dictOfElems = { key:value for key, value in dictOfElems.items() if value > 1}
    # Returns a dict of duplicate elements and thier frequency count
    return dictOfElems

# List of strings
listOfElems = ['Hello', 'Ok', 'is', 'Ok', 'test', 'this', 'is', 'a', 'test']
# Get a dictionary containing duplicate elements in list and their frequency count
dictOfElems = getDuplicatesWithCount(listOfElems)     
for key, value in dictOfElems.items():
        print(key , ' :: ', value)

# List of strings
listOfElems = ['Hello', 'Ok', 'is', 'Ok', 'test', 'this', 'is', 'a', 'test']

from collections import Counter
# Create a dictionary of elements & their frequency count
dictOfElems = dict(Counter(listOfElems))
# Remove elements from dictionary whose value is 1, i.e. non duplicate items
dictOfElems = { key:value for key, value in dictOfElems.items() if value > 1}
for key, value in dictOfElems.items():
        print('Element = ' , key , ' :: Repeated Count = ', value)

# Get duplicate element in a list along with thier indices in list and frequency count
def getDuplicatesWithInfo(listOfElems):
    dictOfElems = dict()
    index = 0
    # Iterate over each element in list and keep track of index
    for elem in listOfElems:
        # If element exists in dict then keep its index in list & increment its frequency
        if elem in dictOfElems:
            dictOfElems[elem][0] += 1
            dictOfElems[elem][1].append(index)
        else:
            # Add a new entry in dictionary 
            dictOfElems[elem] = [1, [index]]
        index += 1    
 
    dictOfElems = { key:value for key, value in dictOfElems.items() if value[0] > 1}
    return dictOfElems

# List of strings
listOfElems = ['Hello', 'Ok', 'is', 'Ok', 'test', 'this', 'is', 'a', 'test']
dictOfElems = getDuplicatesWithInfo(listOfElems)
for key, value in dictOfElems.items():
        print('Element = ', key , ' :: Repeated Count = ', value[0] , ' :: Index Positions =  ', value[1])

# Convert list to string with comma as delimiter in python
def convert_list_to_string(org_list, seperator=' '):
    """ Convert list to string, by joining all item in list with given separator.
        Returns the concatenated string """
    return seperator.join(org_list)

list_of_words = ["This", "is", "a", "sample", "program"]
# Join all the strings in list
full_str = convert_list_to_string(list_of_words, ',')
print(full_str)

# Convert list of integers to string in python using join() in python
list_of_num = [1, 2, 3, 4, 5]
# Covert list of integers to a string
full_str = ' '.join([str(elem) for elem in list_of_num])
print(full_str)

# Convert list to string using map() in python
mix_list = ["This", "is", "a", "sample", 44, 55, 66, "program"]
delimiter = ' '
# Convert list of items to a string value
final_str = delimiter.join(map(str, mix_list))
print(final_str)

# List of list
listOfList = [ [1, 2, 3, 4, 5],
                [11, 22, 33, 44, 55],
                [17, 18, 19, 20, 21] ]

# Use list.extend() to convert a list of lists to a flat list
flatList = []
for elem in listOfList:
    flatList.extend(elem)
print('Flat List : ', flatList)

# Use list.append() to convert a list of lists to a flat list
flatList = []
for elem in listOfList:
    for item in elem:
        flatList.append(item)
print('Flat List : ', flatList)  

# Use list comprehension to convert a list of lists to a flat list 
flatList = [ item for elem in listOfList for item in elem]
print('Flat List : ', flatList)   