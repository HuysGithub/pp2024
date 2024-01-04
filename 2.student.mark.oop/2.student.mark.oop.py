from Student import Student
from Course import Course

def input_student(student_list):
    id = input("ID: ")
    name = input("Name: ")
    dob = input("DoB: ")
    student = Student(id, name, dob)
    student_list.append(student)
    
def input_course(course_list):
    course_id = input("Course ID: ")
    course_name = input("Course Name: ")
    course = Course(course_id,course_name)
    course_list.append(course)
    
def display_student(student_list):
    print("\033[1;32mStudent List:\033[0m")
    for student in student_list:
        print(f"{student.get_name()} {student.get_id()} {student.get_dob()}")
        
def display_course(course_list):
    print("\033[1;32mCourse List:\033[0m")
    for course in course_list:
        print(f"{course.get_course_id()} {course.get_course_name()}")
        
def add_score(student_list, course_list):
    course_id_to_check = input("Enter Course ID: ")
    for course in course_list:
        if course_id_to_check == course.get_course_id():
            for student in student_list:
                score = float(input(f"Enter mark for {student.get_name()} {student.get_id()}: "))
                course.add_score(student.get_id(),score)
            return
    print(f"{course_id_to_check} does not exist!!!")
    
def display_score(student_list, course_list):
    tmp_course_id = input("Enter Course ID: ")
    for course in course_list:
        if tmp_course_id == course.get_course_id():
            for student in student_list:
                student_score = course.get_score(student.get_id())
                if student_score is not None:
                    print(f"{student.get_name()} {student.get_id()} {student.get_dob()} {course.get_course_id()} {student_score}")
                else: 
                    print(f"{student.get_name()} {student.get_id()} {student.get_dob()} {course.get_course_id()}  ")
            return
    print(f"{tmp_course_id} does not exist!!!")

def main():
    student_list = []
    course_list = []
    number_of_student = int(input("Enter number of student: "))
    for _ in range(number_of_student):
        input_student(student_list)
        
    number_of_course = int(input("Enter number of course: "))
    for _ in range(number_of_course):
        input_course(course_list)
        
    # display_student(student_list)
    # display_course(course_list)
    add_score(student_list,course_list)
    display_score(student_list,course_list)
    
if __name__ == "__main__":
    main()