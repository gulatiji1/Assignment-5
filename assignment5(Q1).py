student_marks={
    "Rohan": 85,
    "Anil": 95,
    "Jake": 35,
    "Alice": 89,

}

name=input("Enter student's name:")
marks=student_marks.get(name)
if marks is not None:
    print(f"{name}'s marks :{marks}")
else:
    print(f"Student not found") 
