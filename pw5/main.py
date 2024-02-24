from domains import Student as st, Course as co
from input import *
from output import *

from curses import wrapper
from pathlib import Path
import zipfile
import os

def main(stdscr):
    students = []
    courses = []
    
    file_to_compress = ['pw5/students.txt', 'pw5/courses.txt', 'pw5/marks.txt']
    
    compressed_file = 'pw5/students.dat'

    # Decompress
    if os.path.isfile(compressed_file):
        with zipfile.ZipFile(compressed_file) as zipf:
            zipf.extractall()
        
    pw5_path = Path('pw5')
    listPath = [pw5_path/'students.txt', pw5_path/'courses.txt']
    for path in listPath:
        if path.is_file():
            with open(path, "r") as file:
                for line in file:
                    parts = line.strip().split(",")  # Loại bỏ dấu xuống dòng và chia dòng thành các phần
                    if 'students' in str(path):
                        student = st.Student(parts[0], parts[1], parts[2])
                        students.append(student)
                    elif 'courses' in str(path):
                        course = co.Course(parts[0], parts[1], int(parts[2]))
                        courses.append(course)
                        
    if (pw5_path/'marks.txt').is_file():
        with open("marks.txt", "r") as file:
            for line in file:
                parts = line.strip().split(",")
                for course in courses:
                    if course.getCourseID() == parts[0]:
                        for student in students:
                            if student.getId() == parts[1]:
                                student.addScore(parts[0], float(parts[2]))
                            
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
            with zipfile.ZipFile(compressed_file, "a") as zipf:
                for file in file_to_compress:
                    if os.path.isfile(file):
                        zipf.write(file)
                        os.remove(file)
            break


if __name__ == "__main__":
    wrapper(main)