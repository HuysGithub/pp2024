class Course:
    def __init__(self, course_id, course_name):
        self.course_id = course_id
        self.course_name = course_name
        self.scores = {}
        
    def add_score(self,student_id,score):
        self.scores[student_id] = score
    
    def get_score(self,student_id):
        if  student_id in self.scores:
            return self.scores[student_id]
        else:
            return None
        
    def get_course_id(self):
        return self.course_id
    
    def get_course_name(self):
        return self.course_name