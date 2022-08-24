# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
intAge = int(age)
years_remaining = 90 - intAge
days_remaininig = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

print(
    f"You have {days_remaininig} days, {weeks_remaining}, and {months_remaining} monsths left."
)
