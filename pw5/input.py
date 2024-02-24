from domains import Box

# input student function
def inputStudent(stdscr):
    stdscr.clear()
    IdBox = Box.makebox(stdscr, "ID", 1, 20, 2, 2)
    NameBox = Box.makebox(stdscr, "Name", 1, 20, 4, 2)
    DoBBox = Box.makebox(stdscr, "DoB", 1, 20, 6, 2)

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
    
    with open("pw5/students.txt", "a") as file:
        file.write(f"{IdBox.gather()},{NameBox.gather()},{DoBBox.gather()}\n")
    # Return a dict Student
    return {
        "ID": IdBox.gather(),
        "Name": NameBox.gather(),
        "DoB": DoBBox.gather()
    }

# input course function
def inputCourse(stdscr):
    stdscr.clear()
    CourseIDBox = Box.makebox(stdscr, "Course ID", 1, 20, 2, 2)
    CourseNameBox = Box.makebox(stdscr, "Course Name", 1, 20, 4, 2)
    CourseCreditBox = Box.makebox(stdscr, "Course Credit", 1, 20, 6, 2)

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
    
    with open("pw5/courses.txt", "a") as file:
        file.write(f"{CourseIDBox.gather()},{CourseNameBox.gather()},{CourseCreditBox.gather()}\n")
    # Return a dict Course
    return {
        "CourseID": CourseIDBox.gather(),
        "CourseName": CourseNameBox.gather(),
        "CourseCredit": int(CourseCreditBox.gather())
    }
    
def inputMarks(stdscr, courses, students):
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
    file = open("pw5/marks.txt", "a")
    for student in students:
        stdscr.addstr(row, 0, f"{student.getId():<15}{student.getName():<30}{student.getDob():<15}")
        # Add a box for entering score
        score_input_box = Box.makebox(stdscr, "", 1, 10, row, 35)
        stdscr.refresh()
        score_input_box.edit()
        file.write(f"{selected_course.getCourseID()},{student.getId()},{score_input_box.gather()}\n")
        student.addScore(selected_course.getCourseID(),float(score_input_box.gather()))
        row += 2
    
    file.close()
    stdscr.refresh()
    stdscr.addstr(row, 0, "Done!")
    stdscr.getch()