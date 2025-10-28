#Collection = single "variable" used to store multiple values
#List = [] ordered and changeable. Duplicates OK
#Set = {} Unordered and immutable, but Add/Remove OK. NO duplicates.
#Tuples = () ordered and unchangeable. Duplicates OK. Faster

foods = []
prices = []
total = 0
food = ""
price = 0
still_shopping = True

while still_shopping:
    food = input("What food do you want to buy? ")
    price = float(input("What is the price of the food you want to buy? $"))
    if(food != "" or price != 0):
        foods.append(food)
        prices.append(price)
        total += price
    elif(food == "" or price == 0):
        print("Please enter a valid food or price.")
        still_shopping = False
    still_shopping = input("Would you like to continue? (y/n) ")
    if(still_shopping == "Y" or still_shopping == "y"):
        still_shopping = True
    else:
        still_shopping = False
print(f"The list of the foods: {foods} their price per item is {prices} and the total price: {total}")
