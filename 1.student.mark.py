# list []:     order,   changeable,       allow duplicates
# tuple():     order, unchangeable,       allow duplicates
# set  {}: unordered, unchangeable, duplicates not allowed
# dict {}:              changeable, duplicates not allowed

# student: ID, Name, DoB, Mark
# course: Course ID, Course Name,

def printRED(string):
    print(f"\033[1;31m{string}\033[0m")
def printGREEN(string):
    print(f"\033[1;32m{string}\033[0m")
def clear():
    print("\033c")
def exit():
    input("\nPress Enter to exit ...")
    clear()
    
def checkValidDataType(datatype,message):
    while True:
        try:
            userInput = input(message)
            variable = datatype(userInput)
            break
        except:
            print(f"\033[1;31mInvalid input. Please enter a valid {datatype.__name__}.\033[0m")
    return variable

def inputStudentInfo():
    ID = input("\nID: ")
    Name = input("Name: ")
    DoB = input("DoB: ")
    return {"ID": ID, "Name": Name, "DoB": DoB, "Mark": {}}

def displayStudentInfo(students):
    print("\n\033[1;32mStudent Information: \033[0m")
    for student in students:
        print(f"Student Name: {student['Name']}, Student ID: {student['ID']}, Student DoB: {student['DoB']}")
        
def inputCourseInfo():
    courseID = input("Course ID: ")
    courseName = input("Course Name: ")
    return {"Course ID" : courseID, "Course Name": courseName}

def displayCourseInfo(courses):
    print("\n\033[1;32mCourse Information: \033[0m")
    for course in courses:
        print(f"Course ID: {course['Course ID']}, Course Name: {course['Course Name']}")

def inputStudentMark(students, CourseID):
    print(f"Enter Mark For Students: Course Name \033[1;32m{CourseID.get('Course Name')}\033[0m Course ID \033[1;32m{CourseID.get('Course ID')}\033[0m")
    for student in students:
        mark = -1
        while mark < 0:
            mark = checkValidDataType(float,f"Enter mark for {student.get('ID')} ")
        student['Mark'] = { CourseID.get('Course ID') : mark }
    printGREEN("DONE!")
        
def addStudent(number, students):
    for _ in range(number):
        info = inputStudentInfo()
        students.append(info)

def addCourse(number, courses):
    for _ in range(number):
        info = inputCourseInfo()
        courses.append(info)
        
def checkCourseIDBeforeAddMark(students,courses):
    courseIDtoLoadMark = input("Enter the Course ID you want to add: ")
    addStatus = False
    for course in courses:
        if course['Course ID'] == courseIDtoLoadMark:
            addStatus = True
            inputStudentMark(students,course)
    if addStatus == False:
        clear()
        printRED(f'There is no course has Course ID = "{courseIDtoLoadMark}"')
    
    
def displayStudentMark(students,selectedCourse):
    print(f"\n{'ID':<10}{'Name':<20}{'DOB':<15}{'Course ID':<15}{'Mark'}")
    print('-' * 65)
    for student in students:
        mark = student['Mark'][selectedCourse]
        if mark is not None:
            print(f"{student['ID']:<10}{student['Name']:<20}{student['DoB']:<15}{selectedCourse:<15}{mark}")
        else:
            print(f"{student['ID']:<10}{student['Name']:<20}{student['DoB']:<15}{selectedCourse:<15}No mark")
def switchCase1(students, numberOfStudents):
    while(True):
        addMore = checkValidDataType(int,"How many student you want to add: ")
        if (addMore < 0):
            printRED("Number of student must be greater than 0!")
        elif(addMore == 0):
            clear()
            printRED("Exit!")
            break
        else:
            addStudent(addMore,students)
            numberOfStudents += addMore
            clear()
            printGREEN("Add Completed!")
            break
    return students, numberOfStudents
def switchCase2(students, numberOfStudents):
    removeID = 0
    if(numberOfStudents != 0):
        removeID = input("What Student ID you want to remove: ")
        found = False
        for student in students:
            if student['ID'] == removeID:
                found = True
                printRED(f"REMOVE {student['ID']}: {student['Name']}?(Y/n): ")
                confirm = input().lower()
                if confirm == "y":
                    students.remove(student)
                    clear()
                    printGREEN(f"Remove Completed!")
                else:
                    clear()
                    print("Cancelled!")
        if not found:
            printRED(f"Student with ID {removeID} not found.")
            print(f"Do you want to add {removeID} to Student list?(Y,n): ")
            confirm = input().lower()
            if confirm == "y":
                addStudent(1,students)
                clear()
                printGREEN("Add Completed!")
            else:
                clear()
                print("Cancelled!")
    else:
        clear()
        printRED("There is no student in Student list!")
    return students, numberOfStudents

def switchCase3(courses, numberOfCourses):
    while(True):
        addMore = checkValidDataType(int,"How many course you want to add: ")
        if (addMore < 0):
            printRED("Number of course must be greater than 0!")
        elif(addMore == 0):
            clear()
            printRED("Exit!")
            break
        else:
            addCourse(addMore,courses)
            numberOfCourses += addMore
            clear()
            printGREEN("Add Completed!")
            break
    return courses, numberOfCourses

def switchCase4(courses, numberOfCourses):
    removeID = 0
    if(numberOfCourses != 0):
        removeID = input("What Course ID you want to remove: ")
        found = False
        for course in courses:
            if course['Course ID'] == removeID:
                found = True
                printRED(f"REMOVE {course['Course ID']}: {course['Course Name']}?(Y/n): ")
                confirm = input().lower()
                if confirm == "y":
                    courses.remove(course)
                    clear()
                    printGREEN(f"Remove Completed!")
                else:
                    clear()
                    print("Cancelled!")
        if not found:
            printRED(f"Course with Course ID {removeID} not found.")
            print(f"Do you want to add {removeID} to Course list?(Y,n): ")
            confirm = input().lower()
            if confirm == "y":
                addCourse(1,courses)
                clear()
                printGREEN("Add Completed!")
            else:
                clear()
                print("Cancelled!")
    else:
        clear()
        printRED("There is no course in Course list!")
    return courses, numberOfCourses
        
def switchCase7(students, courses):
    studentID = input("Enter Student ID to view grades: ")
    
    found_student = None
    for student in students:
        if student['ID'] == studentID:
            found_student = student
            break
    
    if found_student:
        clear()
        print(f"\n\033[1;32mGrades for Student ID {studentID} - {found_student['Name']}\033[0m")
        
        header = ["Student ID", "Name"]
        for course in courses:
            header.append(course["Course Name"])
        
        header_line = "\t".join(header)
        print(header_line)
        
        info_line = f"{found_student['ID']}\t{found_student['Name']}"
        
        for course in courses:
            courseID = course["Course ID"]
            mark = found_student['Mark'].get(courseID, "No mark")
            info_line += f"\t{mark}"
        
        print(info_line)
    else:
        printRED(f"\nStudent with ID {studentID} not found.")

def main():
    students = []
    courses = []
    
    numberOfStudents = 0
    numberOfCourses = 0
    
    clear()
    
    while(True):
        printGREEN("Welcome to Student Mark Management!")
        print("1. Add Student.")
        print("2. Remove Student.")
        print("3. Add Course.")
        print("4. Remove Course.")
        print("5. Enter Grades for a Specific Course.")
        print("6. View Grades for a Specific Course.")
        print("7. View Grades for a Specific Student.")
        print("8. Display List of Courses.")
        print("9. Display List of Students.")
        print("0. Exit")
        selection = checkValidDataType(int,"Enter the number corresponding to your choice:")
        match selection:
            case 1:
                clear()
                students, numberOfStudents = switchCase1(students,numberOfStudents)
            case 2:
                clear()
                students, numberOfStudents = switchCase2(students,numberOfStudents)
            case 3: 
                clear()
                courses, numberOfCourses = switchCase3(courses,numberOfCourses)
            case 4:
                clear()
                courses, numberOfCourses = switchCase4(courses,numberOfCourses)
            case 5:
                clear()
                checkCourseIDBeforeAddMark(students,courses)
                exit()
            case 6:
                clear()
                selectedCourse = input("Enter Course ID u want to check mark: ")
                displayStudentMark(students,selectedCourse)
                exit()
            case 7:
                clear()
                switchCase7(students,courses)
                exit()
            case 8:
                clear()
                displayCourseInfo(courses)
                exit()
            case 9: 
                clear()
                displayStudentInfo(students)
                exit()
            case 0:
                clear()
                break
            case _ :
                clear()
                printRED("Invalid Value, Please Type Again!")                   

if __name__ == "__main__":
    main()
    