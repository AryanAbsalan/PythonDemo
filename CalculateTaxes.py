def printList(Fruits):
    for fruit in Fruits:
        print(f"\t 1 kilo of {fruit} costs {Fruits.get(fruit)}€.")
    print("\n")
def printList17(Fruits):
    for fruit in Fruits:
        price = float(Fruits.get(fruit))
        price += (price *17) / 100
        price = '{:05.2f}'.format(price)                
        print(f"\t 1 kilo of {fruit} costs {price} €.")
    print("\n")
def printList19(Fruits):
    for fruit in Fruits:
        price = float(Fruits.get(fruit))
        price += (price *19) / 100
        price = '{:05.2f}'.format(price)                
        print(f"\t 1 kilo of {fruit} costs {price} €.")
    print("\n")
def printListNew(Fruits, percent):
    for fruit in Fruits:
        price = float(Fruits.get(fruit))
        price += (price *percent) / 100
        price = '{:05.2f}'.format(price)                
        print(f"\t 1 kilo of {fruit} with %{percent} taxes costs {price} €.")
    print("\n")

def printBookList(Books):
    for book in Books:
        print(f"\t Book: \"{book}\" costs {Books.get(book)}€.")
    print("\n")