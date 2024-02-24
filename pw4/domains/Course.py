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