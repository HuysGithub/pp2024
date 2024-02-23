import math
import numpy as np
import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle

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

def makebox(stdscr, content, height, width, begin_x, begin_y):
    stdscr.addstr(begin_x, begin_y, content)
    win = curses.newwin(height, width, begin_x, begin_y + 25)
    box = Textbox(win)
    rectangle(stdscr, begin_x - 1, begin_y + 25 - 1, begin_x + height, begin_y + width + 25)
    return box
        
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
def inputStudent(stdscr):
    stdscr.clear()
    IdBox = makebox(stdscr, "ID", 1, 20, 2, 2)
    NameBox = makebox(stdscr, "Name", 1, 20, 4, 2)
    DoBBox = makebox(stdscr, "DoB", 1, 20, 6, 2)

    stdscr.refresh()
    
    # Edit each box
    IdBox.edit()
    NameBox.edit()
    DoBBox.edit()
    
    # Check which box is empty
    while True:
        if IdBox.gather() == "":
            stdscr.addstr(8,2,"Please fill in Id fields!")
            stdscr.refresh()
            IdBox.edit()
        elif NameBox.gather() == "":
            stdscr.addstr(8,2,"Please fill in Name fields!")
            stdscr.refresh()
            NameBox.edit()
        elif DoBBox.gather() == "":
            stdscr.addstr(8,2,"Please fill in DoB fields!")
            stdscr.refresh()
            DoBBox.edit()
        else:
            break
    
    # Return a dict Student
    return {
        "ID": IdBox.gather(),
        "Name": NameBox.gather(),
        "DoB": DoBBox.gather()
    }

# input course function
def inputCourse(stdscr):
    stdscr.clear()
    CourseIDBox = makebox(stdscr, "Course ID", 1, 20, 2, 2)
    CourseNameBox = makebox(stdscr, "Course Name", 1, 20, 4, 2)
    CourseCreditBox = makebox(stdscr, "Course Credit", 1, 20, 6, 2)

    stdscr.refresh()
    
    #edit each box
    CourseIDBox.edit()
    CourseNameBox.edit()
    CourseCreditBox.edit()
    
    # Check which box is empty
    while True:
        if CourseIDBox.gather() == "":
            stdscr.addstr(8,2,"Please fill in Course ID fields!")
            stdscr.refresh()
            CourseIDBox.edit()
        elif CourseNameBox.gather() == "":
            stdscr.addstr(8,2,"Please fill in Course Name fields!")
            stdscr.refresh()
            CourseNameBox.edit()
        elif CourseCreditBox.gather() == "":
            stdscr.addstr(8,2,"Please fill in Credit fields!")
            stdscr.refresh()
            CourseCreditBox.edit()
        else:
            break

    # Return a dict Course
    return {
        "CourseID": CourseIDBox.gather(),
        "CourseName": CourseNameBox.gather(),
        "CourseCredit": float(CourseCreditBox.gather())
    }

def inputMarks(stdscr, courses, students):
    stdscr.clear()
    stdscr.addstr(1, 0, "Enter Course ID or Course Name: ")
    course_input_box = makebox(stdscr, "", 1, 20, 1, 31)
    stdscr.refresh()
    course_input_box.edit()

    # Gather course information
    course_id_or_name = course_input_box.gather().strip().lower().rstrip('\n')
    stdscr.addstr(5, 0, course_id_or_name)

    selected_course = None
    for course in courses:
        course_id_lower = course.getCourseID().strip().lower()
        course_name_lower = course.getCourseName().strip().lower()
        if course_id_lower == course_id_or_name or course_name_lower == course_id_or_name:
            selected_course = course
            break

    if selected_course is None:
        stdscr.addstr(2, 0, f"Course {course_id_or_name} not found.")
        stdscr.refresh()
        stdscr.getch()
        return

    # Clear screen
    stdscr.clear()

    # Show student list
    stdscr.addstr(0, 0, f"Selected Course: {selected_course.getCourseID()} - {selected_course.getCourseName()}")
    stdscr.addstr(2, 0, f"{'ID':<15}{'Name':<30}{'DOB':<15}{'Score':<15}")
    stdscr.addstr(3, 0, "-"*75)
    stdscr.refresh()

    row = 4
    for student in students:
        stdscr.addstr(row, 0, f"{student.getId():<15}{student.getName():<30}{student.getDob():<15}")
        # Add a box for entering score
        score_input_box = makebox(stdscr, "", 1, 10, row, 35)
        stdscr.refresh()
        score_input_box.edit()
        student.addScore(selected_course.getCourseID(),float(score_input_box.gather()))
        row += 2

    stdscr.refresh()
    stdscr.addstr(row, 0, "Done!")
    stdscr.getch()

# listing functions
def listingStudent(students, stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "Student information:")
    stdscr.addstr(2, 0, f"{'ID':<15}{'Name':<30}{'DOB':<15}")
    stdscr.addstr(3, 0, "-"*60)

    row = 4
    for student in students:
        stdscr.addstr(row, 0, f"{student.getId():<15}{student.getName():<30}{student.getDob():<15}")
        row += 2

    stdscr.refresh()
    stdscr.addstr(row, 0, "Press any key to continue ...")
    stdscr.getch()
    
def listingCourses(courses,stdscr):
    print("Course information:")
    for course in courses:
        print(f"{course.getCourseID()}\t{course.getCourseName()}")
    stdscr.clear()
    stdscr.addstr(0, 0, "Course information:")
    stdscr.addstr(2, 0, f"{'Course ID':<15}{'Course Name':<20}{'Credit':<15}")
    stdscr.addstr(3, 0, "-"*50)

    row = 4
    for course in courses:
        stdscr.addstr(row, 0, f"{course.getCourseID():<15}{course.getCourseName():<20}{course.getCredits():<15}")
        row += 2

    stdscr.refresh()
    stdscr.addstr(row, 0, "Press any key to continue ...")
    stdscr.getch()
    
def showStudentMark(stdscr, courses, students):
    stdscr.clear()
    stdscr.addstr(1, 0, "Enter Course ID or Course Name: ")
    course_input_box = makebox(stdscr, "", 1, 20, 1, 31)
    stdscr.refresh()
    course_input_box.edit()

    # Gather course information
    course_id_or_name = course_input_box.gather().strip().lower().rstrip('\n')
    stdscr.addstr(5, 0, course_id_or_name)

    selected_course = None
    for course in courses:
        course_id_lower = course.getCourseID().strip().lower()
        course_name_lower = course.getCourseName().strip().lower()
        if course_id_lower == course_id_or_name or course_name_lower == course_id_or_name:
            selected_course = course
            break

    if selected_course is None:
        stdscr.addstr(2, 0, f"Course {course_id_or_name} not found.")
        stdscr.refresh()
        stdscr.getch()
        return

    # Clear screen
    stdscr.clear()

    # Show student list
    stdscr.addstr(0, 0, f"Selected Course: {selected_course.getCourseID()} - {selected_course.getCourseName()}")
    stdscr.addstr(2, 0, f"{'ID':<15}{'Name':<30}{'DOB':<15}{'Score':<15}")
    stdscr.addstr(3, 0, "-"*75)
    stdscr.refresh()

    row = 4
    for student in students:
        stdscr.addstr(row, 0, f"{student.getId():<15}{student.getName():<30}{student.getDob():<15}{student.getScore(selected_course.getCourseID())}")
        row += 2

    stdscr.refresh()
    stdscr.addstr(row, 0, "Press any key to continue ...")
    stdscr.getch()
    
def main(stdscr):
    students = []
    courses = []
    
    while True:
        stdscr.clear()
        stdscr.addstr("Mark Management System\n")
        stdscr.addstr("------------------------\n")
        stdscr.addstr("1. Add Student\n")
        stdscr.addstr("2. Add Course\n")
        stdscr.addstr("3. Input Marks\n")
        stdscr.addstr("4. List Students\n")
        stdscr.addstr("5. List Courses\n")
        stdscr.addstr("6. Show Student Marks for a Course\n")
        stdscr.addstr("7. Sort student list by GPA descending\n")
        stdscr.addstr("8. Exit\n")
        stdscr.addstr("Enter your choice: ")
        stdscr.refresh()

        choice = stdscr.getch()  # Get user input

        if choice == ord('1'):  # Add Student
            student_info = inputStudent(stdscr)
            student = Student(student_info["ID"], student_info["Name"], student_info["DoB"])
            students.append(student)
            stdscr.addstr(8,2,"Student added successfully!")
            stdscr.refresh()
            stdscr.getch()

        elif choice == ord('2'):  # Add Course
            course_info = inputCourse(stdscr)
            course = Course(course_info["CourseID"], course_info["CourseName"], course_info["CourseCredit"])
            courses.append(course)
            stdscr.addstr(8,2,"Course added successfully!\n")
            stdscr.refresh()
            stdscr.getch()

        elif choice == ord('3'):  # Input Marks
            inputMarks(stdscr,courses,students)

        elif choice == ord('4'):  # List Students
            listingStudent(students,stdscr)
            stdscr.clear()
            stdscr.refresh()

        elif choice == ord('5'):  # List Courses
            listingCourses(courses,stdscr)
            stdscr.clear()
            stdscr.refresh()

        elif choice == ord('6'):  # Show Student Marks for a Course
            showStudentMark(stdscr,courses,students)
            stdscr.clear()
            stdscr.refresh()

        elif choice == ord('7'):
            stdscr.clear()
            sorted_students = sorted(students, key=lambda x: x.calculateGPA(courses), reverse=True)
            stdscr.addstr(0,0,"Sorted student list by GPA descending:")
            stdscr.addstr(2, 0, f"{'ID':<15}{'Name':<30}{'DOB':<15}{'Score':<15}")
            stdscr.addstr(3, 0, "-"*75)
            stdscr.refresh()

            row = 4
            for student in sorted_students:
                stdscr.addstr(row, 0, f"{student.getId():<15}{student.getName():<30}{student.getDob():<15}{student.calculateGPA(courses):.2f}")
                row += 2
            stdscr.refresh()
            stdscr.addstr(row, 0, "Press any key to continue ...")
            stdscr.getch()
            stdscr.clear()
            stdscr.refresh()
            
        elif choice == ord('8'):  # Exit
            break


if __name__ == "__main__":
    wrapper(main)