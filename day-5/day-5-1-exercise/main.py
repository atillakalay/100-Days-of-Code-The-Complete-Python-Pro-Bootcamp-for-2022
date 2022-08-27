# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
height_sum = 0
height_avarage = 0
student_sum = 0
for height in student_heights:
    student_sum += 1
    height_sum += height
    height_avarage = round(height_sum / student_sum)
    print(f"Class' height avarage is {height_avarage}")
