from question_model import Question
from quiz_brain import  QuizBrain
from data import question_data

question_bank = []
for question in question_data:
    text = question["question"]
    answer = question["correct_answer"]
    question_bank.append(Question(text, answer))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"You completed the quiz, your final score is: {quiz.score}/{quiz.question_number}")

