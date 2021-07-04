# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
sum_of_height  = 0
total_height = 0
for height in student_heights:
    sum_of_height += height
    total_height += 1

print(round(sum_of_height/total_height))

#Write your code below this row 👇



