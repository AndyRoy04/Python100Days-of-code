print("Calculating the Average")
student_height = input("\nInput list of Students : ").split()

for number in range(len(student_height)):
    student_height[number] = int(student_height[number])
# print(student_height)
total_height = 0
for a_height in student_height:
    total_height += a_height
# print(total_height)
total_students = 0
for a_height in student_height:
    total_students += 1
# average_height = total_height / len(student_height) 
average_height = total_height / total_students
print(f"Average height is {round(average_height)}\n")