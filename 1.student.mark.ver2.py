# input student function
def inputStudent():
    Id = input("ID: ")
    Name = input("Name: ")
    DoB = input("DoB: ")
    # return a dict
    return {"ID": Id, "Name": Name, "DoB" : DoB, "Mark" : {}}

# input course function
def inputCourse():
    CourseID = input("Course ID: ")
    CourseName = input("Course Name: ")
    return {"Course ID": CourseID, "Course Name": CourseName}

# listing functions
def listingStudent(students):
    print("Student information:")
    for student in students:
        print(f"{student.get('ID')}\t{student.get('Name')}\t{student.get('DoB')}")
def listingCourses(courses):
    print("Course information:")
    for course in courses:
        print(f"{course.get('Course ID')}\t{course.get('Course Name')}")
    
def main():
    students = []
    courses = []
    
    numberOfStudent = 0
    numberOfCourse = 0
    
    # input student
    numberOfStudent = int(input("How many students? \n> "))
    for _ in range(numberOfStudent):
        student = inputStudent() # one student as a dict
        students.append(student)
    
    # input course
    numberOfCourse = int(input("How many courses?\n> "))
    for _ in range(numberOfCourse):
        course = inputCourse()
        courses.append(course)
        
    # select course to input mark
    courseID = input("Input Course ID or Course Name to input mark:\n> ").lower()
    addStatus = False
    for course in courses:
        if course["Course ID"].lower() == courseID or course["Course Name"].lower() == courseID:
            addStatus = True
            for student in students:
                mark = float(input(f"Input mark for {student.get('ID')} - {student.get('Name')}: "))
                student['Mark'] = {course.get('Course ID') : mark}
    if addStatus == False:
        print(f"Course {courseID} Not Found")        

    listingStudent(students)
    
    listingCourses(courses)
    
    courseID = input("Show student mark for given course:\n> ")
    checkStatus = False
    for course in courses:
        if course["Course ID"].lower() == courseID or course["Course Name"].lower() == courseID:
            checkStatus = True
            for student in students:
                print(f"{student.get('ID')}\t{student.get('Name')}\t{student.get('DoB')}\t{student['Mark'].get(courseID)}")
                
    if checkStatus == False:
        print(f"Course {courseID} Not Found") 

if __name__ == "__main__":
    main()