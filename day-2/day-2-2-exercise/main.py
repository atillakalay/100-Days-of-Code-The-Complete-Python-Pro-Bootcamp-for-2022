# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
floatHeight = float(height)
floatWeight = float(weight)
BMI = (floatWeight / (floatHeight**2))
result = int(BMI)
print(result)
