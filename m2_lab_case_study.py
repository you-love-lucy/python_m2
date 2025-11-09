"""
Lucy Jones
m2_lab_case_study.py
Evaluate if a student has made the Dean's List or Honor Roll based off GPA.
"""

lName = input("Enter student's last name: ")

while lName != 'ZZZ':
    fName = input("Enter student's first name: ")
    gpa = float(input("Enter student's GPA: "))
    if gpa >= 3.5:
        print(f"{fName} {lName} has made the Dean's List!")
    elif gpa >= 3.25:
        print(f"{fName} {lName} has made the Honor Roll!")
    
    lName = input("Enter student's last name: ")
