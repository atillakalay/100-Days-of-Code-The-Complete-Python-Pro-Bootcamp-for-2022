# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
smallPizza = 15
mediumPizza = 20
largePizza = 25
if size == "S":
    bill = smallPizza
    if add_pepperoni == "Y":
        bill = smallPizza + 2
if size == "M":
    bill = mediumPizza
    if add_pepperoni == "Y":
        bill = mediumPizza + 3
if size == "L":
    bill = largePizza
    if add_pepperoni == "Y":
        bill = largePizza + 3
if extra_cheese == "Y":
    bill += 1
print(f"Your final bill ${bill}")
