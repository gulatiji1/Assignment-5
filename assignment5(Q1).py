student_marks={
    "Rohan": 85,
    "Anil": 95,
    "Jake": 35,
    "Alice": 89,

}

name=input("Please enter the name of the student-")
marks=student_marks.get(name)
if marks is not None:
    print(f"{name}-{marks}")
else:
    print(f"{name} not found") 
