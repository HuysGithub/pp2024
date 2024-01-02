# list []:     order,   changeable,       allow duplicates
# tuple():     order, unchangeable,       allow duplicates
# set  {}: unordered, unchangeable, duplicates not allowed
# dict {}:              changeable, duplicates not allowed

def inputStudentInfo():
    ID = input("\nID: ")
    Name = input("Name: ")
    DoB = input("DoB: ")
    return {"ID": ID, "Name": Name, "DoB": DoB}

def displayStudentInfo(students):
    print("\n\033[1;32mStudent Information: \033[0m")
    for student in students:
        print(f"Student Name: {student['Name']}, Student ID: {student['ID']}")

def main():
    students = []
    courses = []
    
    numberOfStudents = int(input("Enter the number of students: "))
    for _ in range(numberOfStudents):
        student_info = inputStudentInfo()
        students.append(student_info)
        
    displayStudentInfo(students)
    
if __name__ == "__main__":
    main()
    