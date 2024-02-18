class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob
        self.mark = {}
    def getId(self):
        return self.id
    def getName(self):
        return self.name
    def getDob(self):
        return self.dob
    def addScore(self, courseID, mark):
        self.mark[courseID] = mark
    def getScore(self, courseID):
        if courseID in self.mark:
            return self.mark.get(courseID)
        else:
            return None
        
class Course:
    def __init__(self, courseID, courseName):
        self.courseID = courseID
        self.courseName = courseName
    def getCourseID(self):
        return self.courseID
    def getCourseName(self):
        return self.courseName
    
# input student function
def inputStudent():
    Id = input("ID: ")
    Name = input("Name: ")
    DoB = input("DoB: ")
    # return a dict
    return Student(Id, Name, DoB)

# input course function
def inputCourse():
    CourseID = input("Course ID: ")
    CourseName = input("Course Name: ")
    return Course(CourseID, CourseName)

# listing functions
def listingStudent(students):
    print("Student information:")
    for student in students:
        print(f"{student.getId()}\t{student.getName()}\t{student.getDob()}")
def listingCourses(courses):
    print("Course information:")
    for course in courses:
        print(f"{course.getCourseID()}\t{course.getCourseName()}")
    
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
        if course.getCourseID().lower() == courseID or course.getCourseName().lower() == courseID:
            addStatus = True
            for student in students:
                mark = float(input(f"Input mark for {student.getId()} - {student.getName()}: "))
                student.addScore(course.getCourseID(),mark)
    if addStatus == False:
        print(f"Course {courseID} Not Found")        

    listingStudent(students)
    
    listingCourses(courses)
    
    courseID = input("Show student mark for given course:\n> ")
    checkStatus = False
    for course in courses:
        if course.getCourseID().lower() == courseID or course.getCourseName().lower() == courseID:
            checkStatus = True
            for student in students:
                print(f"{student.getId()}\t{student.getName()}\t{student.getDob()}\t{student.getScore(courseID)}")
                
    if checkStatus == False:
        print(f"Course {courseID} Not Found")

if __name__ == "__main__":
    main()