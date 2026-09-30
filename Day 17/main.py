from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for list in range(len(question_data)):
    text = question_data[list]["text"]
    answer = question_data[list]["answer"]
    question_bank.append(Question(text, answer))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
print("You have finished the Quiz!")
print(f"You got a score of {quiz.score}/{len(question_bank)}")