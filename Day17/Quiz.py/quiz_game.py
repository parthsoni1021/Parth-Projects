from gameclass import QuizBrain
from data import question_data

class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

# Question bank = A list of question objects each being initialized with a text and answer
question_bank = []
for questions in question_data:
    question_text = questions['text']
    question_answer = questions['answer']
    
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)    
print(question_bank)


quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score is {quiz.score}/{quiz.question_no}")


