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