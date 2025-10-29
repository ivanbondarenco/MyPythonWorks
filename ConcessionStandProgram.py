concessions = {"Pizza" : 3.00,
               "Nachos" : 4.50,
               "Popcorn" : 6.00,
               "Fries" : 2.50,
               "Chips" : 1.00,
               "Pretzel" : 3.50,
               "Soda" : 3.00,
               "Lemonade" : 4.25}
print(help(concessions))
still_buying = ""
buy = []
total = 0
x = 0
while still_buying != "Q" or still_buying != "q":
    print("-------------------------")
    print("   SELECT A CONCESSION   ")
    print("-------------------------")
    for item, price in concessions.items():
        print(f"{item} ${price}")
    itembuy = input("Which item do you want to buy? ")
    if itembuy not in concessions:
        print("Sorry, we don't sell that item")
    else:
        buy.append(itembuy)
        total += concessions.get(itembuy)
    still_buying = str(input("Enter Y if you want to still buy or Q if you want to quit: "))
    if(still_buying == "Q" or still_buying == "q"):
        break
print("--------------------------")
print("        YOUR CHART        ")
print("--------------------------")
for item in buy:
    print(f"{item} ${concessions.get(item)}")
print(f"Your total is: ${total}")
print("Thanks for shopping!")