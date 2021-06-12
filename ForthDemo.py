Lorem = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(Lorem)
print("do" in Lorem)
print("does" not in Lorem)
if "do" in Lorem:
  print("Yes, 'do' is present.")
if "does" not in Lorem:
  print("Yes, 'does' is NOT present.")

# Format Strings 
age = 24
txt = "My name is John, and I am {}"
print(txt.format(age))

# Format Strings 
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
# Format Strings 
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

txt = "We are the so-called \"Vikings\" from the north."
print(txt) 
txt = "Hello\nWorld!"
print(txt) 
txt = "Hello\tWorld!"
print(txt) 
#the floor division // rounds the result down to the nearest whole number
x = 15
y = 2
print(x / y)
print(x // y)

#if elif else
a = 200
b = 200
if b > a:
  print("b is greater than a")
elif b < a :
    print("b is less than a")
else:
    print("b and a are equal")
#while else
i = 1
while i < 4:
  print(i)
  i += 1
else:
  print("i is no longer less than 4")
# for
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
# for 0 to 5
for x in range(6) :
  print(x)
print("\n")
# for 1 to 5
for x in range(1,6) :
  print(x)
