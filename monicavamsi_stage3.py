name = input("Enter student name: ")
m1 = int(input("Enter marks for Subject 1: "))
m2 = int(input("Enter marks for Subject 2: "))
m3 = int(input("Enter marks for Subject 3: "))

print(name)
total_marks = m1 + m2 + m3
percentage = (total_marks / 300) * 100
print("Total: ", total_marks ,"/ 300")
print("Percentage:", percentage)

if percentage >= 75:
    grade = "A"
    print("Grade: ", grade)
elif percentage >= 60:
    grade = "B"
    print("Grade: ", grade)
elif percentage >= 40:
    grade = "C"
    print("Grade: ", grade)
else:
    grade = "F"
    print("Grade: ", grade)
