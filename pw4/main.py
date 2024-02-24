from domains import Student as st, Course as co
from input import *
from output import *

from curses import wrapper

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
            student = st.Student(student_info["ID"], student_info["Name"], student_info["DoB"])
            students.append(student)
            stdscr.addstr(8,2,"Student added successfully!")
            stdscr.refresh()
            stdscr.getch()

        elif choice == ord('2'):  # Add Course
            course_info = inputCourse(stdscr)
            course = co.Course(course_info["CourseID"], course_info["CourseName"], course_info["CourseCredit"])
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