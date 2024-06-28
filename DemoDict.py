"""
    Characteristics of dictionaries
    Unordered: The items in dictionaries are stored without any index value, which is typically a range of numbers. 
        They are stored as Key-Value pairs, and the keys are their index, which will not be in any sequence.
    Unique: As mentioned above, each value has a Key; the Keys in Dictionaries should be unique. 
        If we store any value with a Key that already exists, then the most recent value will replace the old value.
    Mutable: The dictionaries are collections that are changeable, which implies that we can 
        add or remove items after the creation.
    
    d1.pop('b')	Remove the key b from the dictionary.
    md1.popitem()	Remove any random item from a dictionary.


"""
import pandas as pd
import json as json

# create a dictionary named person
person = {"name": "Jessa", "country": "USA", "telephone": 1178}

# access value using key name in []
print(person['name'])
# Output 'Jessa'

#  get key value using key name in get()
print(person.get('telephone'))
# Output 1178


'''
    Creating a Dictionary by a two lists
'''         
# List of strings
listofStrings = ["Hello", "hi", "there", "at", "this"]
    
# List of ints
listofInts = [7, 10, 45, 23, 77]

# Merge the two lists to create a dictionary
wordFrequency = dict( zip(listofStrings,listofInts ))

word_freq = {   "Hello" : 7,
                "hi" : 10,
                "there" : 45,
                "at" : 23,
                "this" : 77 }
# Iterate over the dictionary using for loop
for key in word_freq:
    value = word_freq[key]
    print(key, " :: ", value)

word_freq = {   "Hello" : 7,
                "hi" : 10,
                "there" : 45,
                "at" : 23,
                "this" : 77 }
# Iterate over all key-value pairs of dictionary
for key,value in word_freq.items():
    print(key, " :: ", value)

word_freq = {   "Hello" : 7,
                "hi" : 10,
                "there" : 45,
                "at" : 23,
                "this" : 77 }
[   print(key, ' :: ', value)
    for key, value in word_freq.items() ]

# Dictionary of string and int
word_freq = {
    "Hello": 56,
    "at": 23,
    "test": 43,
    "this": 78
}
key = 'sample'
# check if key exists in dictionary by checking if get() returned None
if word_freq.get(key) is not None:
    print(f"Yes, key: '{key}' exists in dictionary")
else:
    print(f"No, key: '{key}' does not exists in dictionary")

# check if key exists in dictionary by checking if get() returned default value
if word_freq.get(key, -1) != -1:
    print(f"Yes, key: '{key}' exists in dictionary")
else:
    print(f"No, key: '{key}' does not exists in dictionary")
    
if key in word_freq.keys():
    print(f"Yes, key: '{key}' exists in dictionary")
else:
    print(f"No, key: '{key}' does not exists in dictionary")

def check_key_exist(test_dict, key):
    try:
       value = test_dict[key]
       return True
    except KeyError:
        return False

# Dictionary of string and int
word_freq = {
    "Hello": 56,
    "at": 23,
    "test": 43,
    "this": 78
}
key = 'testt'
# check if dictionary has key in python
if check_key_exist(word_freq, key):
    print(f"Yes, key: '{key}' exists in dictionary")
else:
    print(f"No, key: '{key}' does not exists in dictionary")

# Check if key not in dict python
if key not in word_freq:
    print(f"No, key: '{key}' does not exists in dictionary")
else:
    print(f"Yes, key: '{key}' exists in dictionary")

if word_freq['test']:
    print("Yes 'test' key exists in dict")
else:
    print("No 'test' key does not exists in dict")

key_to_be_deleted = 'this'
# As 'this' key is present in dict, so pop() will delete
# its entry and return its value
result = word_freq.pop(key_to_be_deleted, None)
print("Deleted item's value = ", result)
print("Updated Dictionary :", word_freq)

word_freq = {key: value for key, value\
                  in word_freq.items()\
                  if key is not key_to_be_deleted}

# Dictionary of strings and int
word_freq_dict = {"Hello": 56,
                  "at": 23,
                  "test": 43,
                  "this": 43}
# Deleting an item from dictionary using del
# if the given key is not present in the dictionary then it will throw an error i.e. KeyError.
del word_freq_dict['at']
print(word_freq_dict)

# If key exist in dictionary then delete it using del.
key_to_be_deleted = 'where'
if key_to_be_deleted in word_freq_dict:
    del word_freq_dict["where"]
else:
    print(f'Key {key_to_be_deleted} is not in the dictionary')

try:
    del word_freq_dict[key_to_be_deleted]
except KeyError:
    print(f'Key {key_to_be_deleted} is not in the dictionary')

def append_value(dict_obj, key, value):
    # Check if key exist in dict or not
    if key in dict_obj:
        # Key exist in dict.
        # Check if type of value of key is list or not
        if not isinstance(dict_obj[key], list):
            # If type is not list then make it list
            dict_obj[key] = [dict_obj[key]]
        # Append the value in list
        dict_obj[key].append(value)
    else:
        # As key is not in dict,
        # so, add key-value pair
        dict_obj[key] = value
# Dictionary of strings and ints
word_freq = {"Hello": 56,
             "at": 23,
             "test": 43,
             "this": 43}
append_value(word_freq, 'at', 21) # 'at': [23, 21],
append_value(word_freq, 'at', 22) # 'at': [23, 21, 22],

# Dictionary of strings and ints
word_freq = {"Hello": 56,
             "at": 23,
             "test": 43,
             "this": 43}

# join three dictionaries 
student_dict1 = {'Aadya': 1, 'Arul': 2, }
student_dict2 = {'Harry': 5, 'Olivia': 6}
student_dict3 = {'Nancy': 7, 'Perry': 9}

student_dict = {**student_dict1, **student_dict2, **student_dict3}
# printing the final Merged dictionary
print(student_dict)
# Output {'Aadya': 1, 'Arul': 2, 'Harry': 5, 'Olivia': 6, 'Nancy': 7, 'Perry': 9}


# List of tuples
new_pairs = [ ('where', 4) , ('who', 5) , ('why', 6) , ('before' , 20)]
word_freq.update(new_pairs)
print(word_freq)

word_freq = {"Hello": 56,
             "at": 23,
             "test": 43,
             "this": 43}
word_freq.update({'why': [1,2,3]})
print(word_freq)
word_freq['what'] = [1, 2, 3]
print(word_freq)

# Dictionary of string and int
word_freq = {
    "Hello": 56,
    "at": 23,
    "test": 43,
    "this": 78,
    "why": 89,
    "Hi": 51,
    "How": 79
}
# Convert all keys of dictionary to list
list_of_keys = list(word_freq)
print(list_of_keys)

# List of all keys of a dictionary
list_of_keys = [key 
                for key, value in word_freq.items()]
print(list_of_keys)

# List of all values of a dictionary
list_of_values = [value
                  for key, value in word_freq.items()]
print(list_of_values)

# Convert dictionary keys to list where value is greater than 50
selected_keys =[key 
                for key, value in word_freq.items()
                if value > 50]

# A dictionary of student names and their score
student_score = {   'Ritika': 5,
                    'Sam': 7, 
                    'John': 10, 
                    'Aadi': 8}
# Iterate over the key-value pairs of a dictionary 
# using list comprehension and print them
[print(key,':',value) for key, value in student_score.items()]

# Dictionary of strings and ints
wordsFreqDict = {
    "hello": 56,
    "at" : 23 ,
    "test" : 43,
    "this" : 43
    }

# Create a list of tuples sorted by index 1 i.e. value field     
listofTuples = sorted(wordsFreqDict.items() ,  key=lambda x: x[1])
# Iterate over the sorted sequence
for elem in listofTuples :
    print(elem[0] , " ::" , elem[1] )

# Use List comprehension to print the contents of dictionary , sorted by value
[ print(key , " :: " , value) 
  for (key, value) in sorted(wordsFreqDict.items() ,  key=lambda x: x[1] ) ]

# Create a list of tuples sorted by index 1 i.e. value field     
listofTuples = sorted(wordsFreqDict.items() , reverse=True, key=lambda x: x[1])
# Iterate over the sorted sequence
for elem in listofTuples :
    print(elem[0] , " ::" , elem[1] )    

# Create a dictionary of string and int
sampleDict = {'Ritika': 5, 'Sam': 27, 'John': 12, 'Sachin': 14, 'Mark': 19, 'Shaun' : 27}

# Find item with Max Value in Dictionary
itemMaxValue = max(sampleDict.items(), key=lambda x: x[1])
print('Maximum Value in Dictionary : ', itemMaxValue[1])
listOfKeys = list()
# Iterate over all the items in dictionary to find keys with max value
for key, value in sampleDict.items():
    if value == itemMaxValue[1]:
        listOfKeys.append(key)
print('Keys with maximum Value in Dictionary : ', listOfKeys)

# Create a dictionary of string and int
sampleDict = {'Ritika': 5, 'Sam': 27, 'John': 12, 'Sachin': 14, 'Mark': 19, 'Shaun' : 27}
# Find item with Max Value in Dictionary
itemMaxValue = max(sampleDict.items(), key=lambda x: x[1])
print('Maximum Value in Dictionary : ', itemMaxValue[1])
maxValuesDict = dict()
# Iterate over all the items in dictionary to find keys with max value
for key, value in sampleDict.items():
    if value == itemMaxValue[1]:
        maxValuesDict.update({key:value})
print('Dictionary Contents : ', maxValuesDict)

# Dictionary of string and int
word_freq = {
    "Hello": 56,
    "at": 23,
    "test": 43,
    "this": 78,
    "why": 89,
    "Hi": 51,
    "How": 79
}
# Convert all values in dictionary to a list
list_of_values = list(word_freq.values())
print(list_of_values)

# Convert specific values of dictionary
selected_values = { key : value 
                    for key, value in word_freq.items()
                    if len(key) >= 4 
                    and key.startswith('H') 
                    and key.endswith('o') 
                    and value >=50 }
print(selected_values)

# Dictionary of string and integers
word_freq = {
    'Hello' : 56,
    'At'    : 23,
    'Test'  : 43,
    'Why'   : 11,
    'This'  : 78,
}
# Iterate over key-value pairs of dictionary
# sorted by values
for key, value in sorted(   word_freq.items(), 
                            key=lambda item: item[1],
                            reverse=True):
    print(key, ' :: ', value)
  
# Nested Dictionary
studentData = { 
0 : {
    'name' : 'Aadi',
    'age' : 16,
    'city' : 'New york'
    },
1 : {
    'name' : 'Jack',
    'age' : 34,
    'city' : 'Sydney'
    },
2 : {
    'name' : 'Riti',
    'age' : 30,
    'city' : 'Delhi'
    }
}
'''
Create dataframe from nested dictionary 
'''
dfObj = pd.DataFrame(studentData) 
# Print Dataframe object on console
print(dfObj)

print("Transpose the dictionary")

# Transpose dataframe object
dfObj = dfObj.transpose()
print(dfObj)

# When we apply ** to this dictionary, it de-serializes the contents of dictionary
# **dict1 is equivalent to,'Ritika': 5, 'Sam': 7, 'John' : 10

# Create first dictionary
dict1 = {  'Ritika': 5, 'Sam': 7, 'John' : 10 }
# Create second dictionary
dict2 = {'Aadi': 8,'Sam': 20,'Mark' : 11 }
# Merge contents of dict2 and dict1 to dict3
dict3 = {**dict1 , **dict2}
print('Dictionary 3 :')
print(dict3)
print('*** Merge 3 dictionaries using ** trick ***')
# Create third dictionary
dict3 = {'Mark': 18,'Rose': 22,'Wong' : 22 }
# Merge contents of dict3, dict2 and dict1 to dict4
dict4 = {**dict1, **dict2, **dict3}
print('Dictionary 4 :')
print(dict4)

# Iterate over a dictionary and remove items with even values
# Dictionary of string and integers
word_freq = {
    'Hello' : 56,
    'at'    : 23,
    'test'  : 43,
    'This'  : 78,
    'Why'   : 11
}
# Delete items from dictionary while iterating
# and based on conditions on values
# Create a copy of dictionary and iterate over that 
# and delete elements from original dictionary while iteration
for key, value in dict(word_freq).items():
    if value % 2 == 0:
        del word_freq[key]
print(word_freq)

# Dictionary of string and integers
word_freq = {
    'Hello' : 56,
    'at'    : 23,
    'test'  : 43,
    'This'  : 78,
    'Why'   : 11
}
# Create a copy of original dictionary and iterate over it
for key in dict(word_freq):
    if word_freq[key] % 2 == 0:
        word_freq.pop(key)
print(word_freq)

# Dictionary of string and integers
word_freq = {
    'Hello' : 56,
    'at'    : 23,
    'test'  : 43,
    'This'  : 78,
    'Why'   : 11
}
# Delete items from dictionary while iterating using comprehension
# and based on conditions on values
word_freq = {   key: value 
                for key, value in word_freq.items()
                if value % 2 != 0}
print(word_freq)

list_of_dict = [
    {'Name': 'Shaun' ,  'Age': 35,  'Marks': 91},
    {'Name': 'Ritika',  'Age': 31,  'Marks': 87},
    {'Name': 'Smriti',  'Age': 33,  'Marks': 78},
    {'Name': 'Jacob' ,  'Age': 23,  'Marks': 93},
]
# Create Dataframe from list of dictionaries
df = pd.DataFrame(list_of_dict,
                  index=['a', 'b', 'c', 'd'],
                  columns=['Name', 'Marks'])
print(df)

# A Nested dictionary i.e. dictionaty of dictionaries
students = {
            'ID 1':    {'Name': 'Shaun', 'Age': 35, 'City': 'Delhi'},
            'ID 2':    {'Name': 'Ritika', 'Age': 31, 'City': 'Mumbai'},
            'ID 3':    {'Name': 'Smriti', 'Age': 33, 'City': 'Sydney'},
            'ID 4':    {'Name': 'Jacob', 'Age': 23, 'City': {'perm': 'Tokyo', 'current': 'London'}},
            }
print(json.dumps(students, indent=4))

# Pretty print nested dictionary as a table
df = pd.DataFrame(students).T
print(df)

# A Nested dictionary i.e. dictionaty of dictionaries
students = {
            'ID 1':    {'Name': 'Shaun', 'Age': 35, 'City': 'Delhi'},
            'ID 2':    {'Name': 'Ritika', 'Age': 31, 'City': 'Mumbai'},
            'ID 3':    {'Name': 'Smriti', 'Age': 33, 'City': 'Sydney'},
            'ID 4':    {'Name': 'Jacob', 'Age': 23, 'City': {'perm': 'Tokyo',
                                                             'current': 'London'}},
            }
def nested_dict_pairs_iterator(dict_obj):
    ''' This function accepts a nested dictionary as argument
        and iterate over all values of nested dictionaries
    '''
    # Iterate over all key-value pairs of dict argument
    for key, value in dict_obj.items():
        # Check if value is of dict type
        if isinstance(value, dict):
            # If value is dict then iterate over all its values
            for pair in  nested_dict_pairs_iterator(value):
                yield (key, *pair)
        else:
            # If value is not dict type then yield the value
            yield (key, value)

#Loop through all key-value pairs of a nested dictionary
for pair in nested_dict_pairs_iterator(students):
    print(pair)

# Check if a value exists in python dictionary using for loop
def check_value_exist(test_dict, value):
    do_exist = False
    for key, val in test_dict.items():
        if val == value:
            do_exist = True
    return do_exist

value = 43
# Iterate over all key, value pairs in dict and check if value exist
if check_value_exist(word_freq, value):
    print(f"Yes, Value: '{value}' exists in dictionary")
else:
    print(f"No, Value: '{value}' does not exists in dictionary")

value = 66
# Check if key exist in dictionary using any()
if any([True 
        for k,v in word_freq.items() 
        if v == value]):
    print(f"Yes, Value: '{value}' exists in dictionary")
else:
    print(f"No, Value: '{value}' does not exists in dictionary")