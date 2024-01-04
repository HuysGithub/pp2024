# list []:     order,   changeable,       allow duplicates
# tuple():     order, unchangeable,       allow duplicates
# set  {}: unordered, unchangeable, duplicates not allowed
# dict {}:              changeable, duplicates not allowed

# student: ID, Name, DoB, Mark
# course: Course, ID, Course Name,

def inputStudentInfo():
    ID = input("\nID: ")
    Name = input("Name: ")
    DoB = input("DoB: ")
    return {"ID": ID, "Name": Name, "DoB": DoB, "Mark": {}}

def displayStudentInfo(students):
    print("\n\033[1;32mStudent Information: \033[0m")
    for student in students:
        print(f"Student Name: {student['Name']}, Student ID: {student['ID']}, Student DoB: {student['DoB']}")
        
def inputCourseInfo(students):
    courseID = input("Course ID: ")
    courseName = input("Course Name: ")
    for student in students:
        student["Mark"][courseID] = None
    return {"Course ID" : courseID, "Course Name": courseName}

def displayCourseInfo(courses):
    print("\n\033[1;32mCourse Information: \033[0m")
    for course in courses:
        print(f"Course ID: {course['Course ID']}, Course Name: {course['Course Name']}")

def loadStudentMark(students, CourseID):
    print(f"Enter Mark For Students: Course Name \033[1;32m{CourseID.get('Course Name')}\033[0m Course ID \033[1;32m{CourseID.get('Course ID')}\033[0m")
    for student in students:
        mark = input(f"Enter mark for {student.get('Name')} ")
        student['Mark'] = { CourseID.get('Course ID') : mark }
        
def checkCourseIDBeforeAddMark(students,courses):
    courseIDtoLoadMark = input("Enter the Course ID you want to add: ")
    addStatus = False
    for course in courses:
        if course['Course ID'] == courseIDtoLoadMark:
            addStatus = True
            loadStudentMark(students,course)
    if addStatus == False:
        print(f'There is no course has Course ID = "{courseIDtoLoadMark}"')
    
def displayStudentMark(students,selectedCourse):
    print(f"\n{'ID':<10}{'Name':<20}{'DOB':<15}{'Course ID':<15}{'Mark'}")
    print('-' * 65)
    for student in students:
        mark = student['Mark'][selectedCourse]
        if mark is not None:
            print(f"{student['ID']:<10}{student['Name']:<20}{student['DoB']:<15}{selectedCourse:<15}{mark}")
        else:
            print(f"{student['ID']:<10}{student['Name']:<20}{student['DoB']:<15}{selectedCourse:<15}No mark")
            
def main():
    students = []
    courses = []
    
    numberOfStudents = int(input("Enter the number of students: "))
    for _ in range(numberOfStudents):
        student_info = inputStudentInfo()
        students.append(student_info)
        
    displayStudentInfo(students)
    
    numberOfCourse = int(input("\nEnter the number of courses: "))
    for _ in range(numberOfCourse):
        course_info = inputCourseInfo(students)
        courses.append(course_info)
    
    displayCourseInfo(courses)
    checkCourseIDBeforeAddMark(students,courses)
    selectedCourse = input("Enter Course ID u want to check mark: ")
    displayStudentMark(students,selectedCourse)
    
if __name__ == "__main__":
    main()
    