#creating the vending machine menu using dictionaries
menu = {'chips': 1.0,
        'oreos': 2.0,
        'strawberry milk': 1.5,
        'chocolate milk': 1.5,
        'soda': 1.0,
        'coffee': 2.0
        }

#dictionary for stock
stock = {'chips': 3,
         'oreos': 5,
         'strawberry milk': 5,
         'chocolate milk': 5,
         'soda': 1,
         'coffee': 5
         }

#creating a variable to store the items the user has chosen
bag = []

#creating a variable to store the total
total = 0

#printing the menu
print("------------ MENU -------------")
for key, value in menu.items():
    print(f"{key}: £{value}")
print("-------------------------------")

#asking the user to insert money
inserted_money = float(input("Please insert desired amount: £"))

#using a while loop to get user input and store it in a variable called "item"
while True:
    item = input("Select an item (press x to confirm selection(s)): ").lower()
    #using if loop we can make the user quit after selecting the items by clicking "x"
    if item == "x":
        break
    #adding the selected items to the list "bag" if the stock is available
    elif menu.get(item) and stock[item] > 0:
        bag.append(item)
        #updates the stock
        stock[item] -= 1
    else:
        print("Out of stock of selection")
print("-------------------------------")

#using a for loop to add the total of all items in "bag" and printing the selected items
for item in bag:
    total = total + menu.get(item) 
    print("Selected item: ", item)

print("-------------------------------")
print(f"Your total to be paid is: £{total}")

print("-------------------------------")

#checks if the insertred money is less than the amount required, if so it prints out a message to insert more funds
if total > inserted_money:
    print("Insufficient funds, please insert more money")
else:
    change = inserted_money - total
    print(f"Your change is: £{change}")
    if change > 0:
        print("Please pick up your change")
    print("-------------------------------")
    #goes through the list and prints a message 
    for item in bag:
        print(f"Dispensing {item}.")
print("-------------------------------")

    