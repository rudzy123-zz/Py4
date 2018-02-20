#C14e6
#GradedActivity:INHERITANCE Example

class GradedActivity:
    def set_score(self,s):
        self._score = s
    def get_score(self):
        return self._score
    def get_grade(self):
        if self._score >= 90:
            grade = "A"
        elif self._score >= 80:
            grade = "B"
        elif self._score >=70:
            grade = "C"
        elif self._score >=60:
            grade = "D"
        else:
            grade = "F"
        return grade
    
class FinalExam(GradedActivity):
    def __init__(self,questions,missed,points_each):
        #set the _num_questions, _num_missed fields, num_points_each
        self._num_questions = questions
        self._num_missed = missed

        #calc for the points for each questions
        numeric_score = 100 - (missed*points_each)

        #call for the inherited set_score
        self.set_score(numeric_score)

    def get_points_each(self):
        return self._points_each
    def get_num_missed(self):
        return self._num_missed

def main():
    questions = int(input("Enter the number of questions on the exams: "))

    missed = int(input("Enter the number of questions that the student missed: "))

    points_each = 100.0/questions

    exam = FinalExam(questions,missed,points_each)

    print("Each question is on the exam counts",points_each,"points.")
    print("The exam score is: ",exam.get_score())
    print("The exam score is: ",exam.get_grade())
    
main()        
