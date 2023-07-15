student_scores = {
    "Neville" : 85,
    "Harry" : 79,
    "Randy" : 68,
    "Gerald" : 80,
    "Angela" : 92,
}

student_grades = {}
for student in student_scores:
    if student_scores[student] > 90:
        student_grades[student] = "Outstanding"
    elif 81<= student_scores[student]<=90:
        student_grades[student] = "Exceeds Expectation"
    elif 71<=student_scores[student]<=80:
        student_grades[student] = "Acceptable" 
    else:
        student_grades[student] = "Fail" 

print(student_grades)