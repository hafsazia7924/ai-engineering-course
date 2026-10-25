print("**STUDENT MARKS CALCULATOR**")
marks=input("Enter your  marks to check grade")
marks=int(marks)
if marks>=80:
    print("Grade A")
elif marks>=60 and marks<80:
    print("Grade B")
elif marks>=40 and marks<60:
    print("Grade c")
else:
    print("Fail")