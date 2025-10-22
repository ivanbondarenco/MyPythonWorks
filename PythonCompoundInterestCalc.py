#Principle
principle = 0
#Interest rate
rate = 0
#Number of years
time = 0
#Calculus
calc = 0

while principle <=0:
    principle = float(input("Enter your principle: "))
    if principle <= 0:
        print("Please enter a positive integer")
while rate <=0:
    rate = float(input("Enter your rate: "))
    if rate <= 0:
        print("Please enter a positive integer")
while time <=0:
    time = int(input("Enter your time: "))
    if time <= 0:
        print("Please enter a positive integer")

calc = principle * pow((1 + rate / 100),time)

print(f"Your calculation is: {calc}")
