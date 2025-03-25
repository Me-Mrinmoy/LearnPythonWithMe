'''Q6.Write a program to calculate the grade of a student from his marks 
from the folloeing scheme:
    90-100 -Ex
    80-90  -A
    70-80  -B
    60-70  -C
    50-60  -D
      <50  -F
      '''


marks = int(input("Enter your marks\n"))

if marks>=90:
    grade = "Ex"
elif marks>=80:
    garde = "A"
elif marks>=70:
    grade = "B"
elif marks>=60:
    grade = "C"
elif marks>=50:
    grade = "D"
else:
    grade = "F"   

print("Your grade is" + grade)         