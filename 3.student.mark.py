import math
import numpy as np

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
    def calculateGPA(self, courses):
        total_marks = np.array([self.mark.get(course.getCourseID(), 0) * float(course.getCredits()) for course in courses])
        total_credits = np.array([float(course.getCredits()) for course in courses])
        if np.sum(total_credits) == 0:
            return 0
        return np.sum(total_marks) / np.sum(total_credits)


        
class Course:
    def __init__(self, courseID, courseName, credit):
        self.courseID = courseID
        self.courseName = courseName
        self.credit = credit
    def getCourseID(self):
        return self.courseID
    def getCourseName(self):
        return self.courseName
    def getCredits(self):
        return self.credit
    
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
    CourseCredit = input("Course Credit: ")
    return Course(CourseID, CourseName, CourseCredit)

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
                # round-down student score
                student.addScore(course.getCourseID(),math.floor(mark*10)/10)
    if addStatus == False:
        print(f"Course {courseID} Not Found")        

    listingStudent(students)
    
    listingCourses(courses)
    
    # Show student marks for a given course
    courseID = input("Show student mark for given course:\n> ")
    checkStatus = False
    for course in courses:
        if course.getCourseID().lower() == courseID or course.getCourseName().lower() == courseID:
            checkStatus = True
            for student in students:
                print(f"{student.getId()}\t{student.getName()}\t{student.getDob()}\t{student.getScore(courseID)}")
                
    if checkStatus == False:
        print(f"Course {courseID} Not Found")

    sorted_students = sorted(students, key=lambda x: x.calculateGPA(courses), reverse=True)
    print("\nSorted student list by GPA descending:")
    for student in sorted_students:
        print(f"{student.getId()}\t{student.getName()}\t{student.getDob()}\t{student.calculateGPA(courses):.2f}")

if __name__ == "__main__":
    main()