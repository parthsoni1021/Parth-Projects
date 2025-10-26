question_data = [
    {"text": "The Earth revolves around the Sun.", "answer": "True"},
    {"text": "The chemical symbol for water is H2O2.", "answer": "False"},
    {"text": "Python is a statically typed programming language.", "answer": "False"},
    {"text": "Light travels faster than sound.", "answer": "True"},
    {"text": "The capital of Australia is Sydney.", "answer": "False"},
    {"text": "Humans have walked on the Moon.", "answer": "True"},
    {"text": "The Great Wall of China is visible from space with the naked eye.", "answer": "False"},
    {"text": "An octopus has three hearts.", "answer": "True"},
    {"text": "Electrons are larger than atoms.", "answer": "False"},
    {"text": "Mount Everest is the highest mountain above sea level.", "answer": "True"}
]

class Question:
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer

# new_q = Question('New Delhi is the capital of India', True)

# Question bank = A list of question objects each being initialized with a text and answer

question_bank = []
for questions in question_data:
    question_text = questions['text']
    question_answer = questions['answer']
    
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
    
print(question_bank)

# Bring questions and ask user to answer the questions unless he's wrong

# Create class named QuizBrain
class QuizBrain:
    def __init__(self, q_list):
        print('Welcome to the Quiz Brain Game')
        self.question_no = 0
        self.question_list = q_list 
        
    def next_question(self):
        current_question = self.question_list[self.question_no]
        self.question_no += 1
        input(f"Q{self.question_no}: {current_question.text} (True or False): ")
                
    def still_has_question(self):
        
        
        
        
quiz = QuizBrain(question_bank)
quiz.next_question()




