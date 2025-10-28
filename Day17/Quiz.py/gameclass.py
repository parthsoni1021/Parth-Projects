class QuizBrain:
    def __init__(self, q_list):
        print('Welcome to the Quiz Brain Game')
        self.question_no = 0
        self.question_list = q_list 
        self.score = 0
        
    def still_has_question(self):
        n = len(self.question_list)
        return self.question_no < n

    def next_question(self):
        current_question = self.question_list[self.question_no]
        self.question_no += 1
        user_answer = input(f"Q{self.question_no}: {current_question.text} (True or False): ")
        self.check_answer(user_answer, current_question.answer)

            
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print('Correct answer')
            self.score += 1
        else:
            print("Wrong answer")
        print(f"The correct answer is {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_no}")
        print("\n")


        
        
        