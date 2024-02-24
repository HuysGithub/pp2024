from domains import Box

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
    course_input_box = Box.makebox(stdscr, "", 1, 20, 1, 31)
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