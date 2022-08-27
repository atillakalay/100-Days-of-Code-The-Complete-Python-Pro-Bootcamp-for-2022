# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
min_score = student_scores[0]
max_score = student_scores[0]
for score in student_scores:

    if min_score > score:
        min_score = score

    if max_score < score:
        max_score = score

print(f"The highest score is: {max_score}")
print(f"The lowest score is: {min_score}")
