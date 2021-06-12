import CalculateTaxes

# Fruits list
Fruits = {
    "banana":"0.99",
    "Grapes":"1.99",
    "Tomato":"1.29",
    "Carrot":"1.49",
    "Apple":"2.99",
    "Orange":"2.49"
}
Books = {
    "First":"18.99",
    "Second":"19.99",
    "Third":"29.29",
    "Forth":"30.49",
    "Fifth":"28.99"
}
# price list
print("price list:")
CalculateTaxes.printList(Fruits)

# price list with %17 tax:
print("price list with %17 tax:")
CalculateTaxes.printList17(Fruits)

#price list with %19 tax:
print("price list with %19 tax:")
CalculateTaxes.printList19(Fruits)

#price list with new tax:
print("price list with new tax:")
CalculateTaxes.printListNew(Fruits, 21)

#price list with new tax:
print("price list with new tax:")
CalculateTaxes.printListNew(Fruits, 23)

#price list with new tax:
print("price list with new tax:")
CalculateTaxes.printListNew(Fruits, 25)

#price list with no tax:
print("price list with no tax:")
CalculateTaxes.printListNew(Fruits,0) 

# Book list
print("Book list:")
CalculateTaxes.printBookList(Books)