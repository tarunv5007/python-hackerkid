"""
Project:Get the student name and marks, find the average and use conditional to give grades.

print the result for the following marks
# 90 to 100=A grade
# 80 to 90=B grade
# 70 to 80= C grade
# 60 to 70= D grade
# below 60= E grade
"""

Name = input("Enter your name : ")
standard = int(input("Enter which grade you are studying : "))
noOfSubjects = int(input("Enter number of subjects : "))

science_mark = int(input("Enter your science mark : "))
math_mark = int(input("Enter your math mark : "))
tamil_mark = int(input("Enter your Tamil mark : "))
IT_mark = int(input("Enter your IT mark : "))
english_mark = int(input("Enter your English mark : "))

# Checks to make sure inputs are valid

if standard <= 0 or standard > 12:
    print("Invalid standard.")
    quit()

if science_mark < 0 or science_mark > 100:
    print("Invalid mark.")
    quit()
if math_mark < 0 or math_mark > 100:
    print("Invalid mark.")
    quit()
if tamil_mark < 0 or tamil_mark > 100:
    print("Invalid mark.")
    quit()
if IT_mark < 0 or IT_mark > 100:
    print("Invalid mark.")
    quit()
if english_mark < 0 or english_mark > 100:
    print("Invalid mark.")
    quit()

totalGrade = science_mark+math_mark+tamil_mark+IT_mark+english_mark
averageGrade = totalGrade/5

print("Student name : ", Name)
print("Student is studying in ", standard, " grade")
print("Total of student : ", totalGrade)
if averageGrade >= 90 and averageGrade < 101:
    print("A grade")
elif averageGrade >= 80 and averageGrade < 90:
    print("B grade")
elif averageGrade >= 70 and averageGrade < 80:
    print("C grade")
elif averageGrade >= 60 and averageGrade < 70:
    print("D grade")
else:
    print("E grade")

