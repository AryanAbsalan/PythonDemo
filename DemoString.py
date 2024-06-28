
import re

sampleStr = "Hello, this is a sample string"
print( "Last character in string : " , sampleStr[-1] )
print( "Second Last character in string : " , sampleStr[-2] )
# If string size is n then string[-n] will return the first character of string
print( "First character in string : " , sampleStr[ -len(sampleStr) ] )

'''
Modifying character in string by Index
As strings are immutable so we can modify the contents of string in python
'''
# sampleStr[5] = 's' 
# TypeError: 'str' object does not support item assignment

mainStr = "This is a sample String with sample message."
if "Hello" not in mainStr:
   print ("Sub-string Doesn't exists in main String")
if "sample" in mainStr:
   print ("Sub-string Does exists in main String")

# Check if a String contains any string from a List
mainStr = "This is a sample String with sample message."
listOfStrs = ['Hello', 'here', 'with', 'here', 'who']

def checkIfAny(mainStr, listOfStrs):
   for subStr in listOfStrs:
       if subStr in mainStr:
           return (True, subStr)
   return (False, "")

result = checkIfAny(mainStr, listOfStrs)
if result[0]:
    print('Sub-string Found in main String : ', result[1])
    
# Check if any string from the list exists in given string
result = any(([True if subStr in mainStr else False for subStr in listOfStrs]))
if result:
    print('A string from list Found in main String ')

print('**** Check if a String contains any string from a list ****')
listOfStrs = ['sample', 'String', 'with']
# Check if all strings from the list exists in given string
result = all(([True if subStr in mainStr else False for subStr in listOfStrs]))
if result:
    print('All strings from list Found in main String ')

print('**** Regex : Check if a String contains another string using Python Regex ****')
# Create a pattern to match string 'sample'
patternObj = re.compile("sample")
# search for the pattern in the string and return the match object
matchObj = patternObj.search(mainStr)
# check if match object is not Null
if matchObj:
    print('Sub-string Found')
else:
    print('Sub-string Not Found')

print('**** Python Regex : Check if a String contains another string in Case in sensitive manner | ignore case ****')
# search for the sub-string in string by ignoring case
matchObj =  re.search('SAMple', mainStr, flags=re.IGNORECASE)
if matchObj:
    print('Sub-string Found')
else:
    print('Sub-string Not Found')

# string[start : stop : step size]
# Iterate over the first three elements of string
sampleStr = "Hello!"
for elem in sampleStr[0:3:1] : 
    print(elem)

# Iterate over string in reverse using slice operation   
for elem in sampleStr[ : :-1]:
    print(elem)

i = len(sampleStr) - 1 
while i >= 0 :
    print(sampleStr[i])
    i = i - 1
    

mainStr = 'This is a sample string and a sample code. It is very short.'
# Create a Regex pattern to match the substring
regexPattern = re.compile("sample")
# Get a list of strings that matches the given pattern i.e. substring
listOfMatches = regexPattern.findall(mainStr)
print("'sample' sub string frequency / occurrence count : ", len(listOfMatches))

def frequencyCountAndPositions(mainStr, subStr):
   counter = pos = 0
   indexpos = []
   while(True):
       pos = mainStr.find(subStr , pos)
       if pos > -1:
           indexpos.append(pos)
           counter = counter + 1
           pos = pos + 1
       else:
           break
   return (counter, indexpos)

mainStr = 'This is a sample string and a sample code. It is very Short.'
result = frequencyCountAndPositions(mainStr, 'is')
print(result)
if result[0] >= 2:
    print("Index Positions of 2nd Occurrence of sub-string 'is'  : ", result[1][1])


listOfIps = [ "192.122.78.11", "192.122.78.305" , "192.122.77.111"]
# Create regex pattern
regexPattern = re.compile("192.122.78.*")
# Check if strings in list matches the regex pattern
for ipStr in listOfIps:
    matchObj = regexPattern.fullmatch(ipStr)
    if matchObj:
        print('Contents of string ' ,ipStr , ' matched the pattern')
    else:
        print('Contents of string ' ,ipStr , ' do not matched the pattern')

'''
Replace a set of multiple sub strings with a new string in main string.
'''
def replaceMultiple(mainString, toBeReplaces, newString):
    # Iterate over the strings to be replaced
    for elem in toBeReplaces :
        # Check if string is in the main string
        if elem in mainString :
            # Replace the string
            mainString = mainString.replace(elem, newString)
    
    return  mainString     

mainStr = "Hello, This is a sample string"
# Replace all the occurrences of string in list by AA in the main list 
otherStr = replaceMultiple(mainStr, ['s', 'l', 'a'] , "AA") 
print(otherStr)

mainStr = 'This is a sample string and a sample code. It is very Short.'
# Create a regex pattern to match character 's'
regexPattern = re.compile('s')
# Iterate over all the matches of regex pattern
iteratorOfMatchObs = regexPattern.finditer(mainStr)
indexPositions = []
count = 0
for matchObj in iteratorOfMatchObs:
    indexPositions.append(matchObj.start())
    count = count + 1
print("Occurrence Count of character 's' : ", count)
print("Index Positions of 's' are : ", indexPositions)

mainStr = 'This is a sample string and a sample code. It is very Short.'
# Create a regex pattern to match character 's' or 'a' or 'c'
regexPattern = re.compile('[sac]')
# Iterate over all the matches of regex pattern
iteratorOfMatchObs = regexPattern.finditer(mainStr)
print(iteratorOfMatchObs)
count = 0
indexPositions = {}
for matchObj in iteratorOfMatchObs:
    indexPositions[matchObj.group()] = indexPositions.get(matchObj.group(), []) + [matchObj.start()]
    count = count + 1
print("Total Occurrence Count of characters 's' , 'a' and 'c' are : ", count)
for (key, value) in indexPositions.items():
    print('Index Positions of ', key , ' are : ', indexPositions[key])