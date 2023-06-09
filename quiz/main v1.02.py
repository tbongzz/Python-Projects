# Get questions and answers from a text file
import random


class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer


class Quiz:
    def __init__(self):
        self.question_pools = []
        self.score = 0

    def load_questions(self, file_path):
        """
        Load questions and answers from a text file.
        The text file should have questions and answers in the format mentioned above.
        """
        with open(file_path, 'r') as file:
            lines = file.readlines()
            current_pool = None
            current_question = None
            for line in lines:
                line = line.strip()
                if line.startswith('[Pool'):
                    if current_pool is not None:
                        self.question_pools.append(current_pool)
                    current_pool = []
                elif line.startswith('[Question'):
                    if current_question is not None:
                        current_pool.append(current_question)
                    question_text = line[1:-1]
                    current_question = Question(question_text, [], "")
                elif line.startswith('Answer:'):
                    answer = line[8:]
                    current_question.answer = answer
                elif line:
                    current_question.choices.append(line)

            # Add the last question to the question pools
            if current_pool is not None:
                self.question_pools.append(current_pool)

    def play(self):
        for pool in self.question_pools:
            question = random.choice(pool)
            print(question.text)
            for i, choice in enumerate(question.choices):
                print(f"{chr(65 + i)}. {choice}")

            user_answer = input("Enter your answer (A, B, C, D): ")
            if question.answer.lower() == user_answer.lower():
                self.score += 1
                print("Correct!\n")
            else:
                print(f"Wrong! The correct answer is {question.answer}\n")

        print(f"Your final score: {self.score}/{len(self.question_pools)}\n")


# Create a quiz instance
quiz = Quiz()

# Load questions from the text file
quiz.load_questions('quiz_questions.txt')

# Play the quiz
quiz.play()
