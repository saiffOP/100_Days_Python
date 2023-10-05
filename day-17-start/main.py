from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:
    question_text = item["text"]
    question_answer = item["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


Quiz = QuizBrain(question_bank)
while Quiz.still_has_questions():
    Quiz.next_question()

print("You have completed the Quiz")
print(f"Your Final Score is {Quiz.score}/{Quiz.question_no}")
