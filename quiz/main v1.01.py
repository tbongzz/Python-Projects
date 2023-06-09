# Updated the code to incorporate question pool and randomiser
import random


class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer


class Quiz:
    def __init__(self):
        self.question_pools = [
            [
                Question("Question 1: What is the capital of France?", ["London", "Paris", "Berlin", "Rome"], "Paris"),
                Question("Question 1: What is the capital of Germany?", ["Paris", "Berlin", "London", "Rome"],
                         "Berlin"),
                # Add more questions to the pool
            ],
            [
                Question("Question 2: Which planet is known as the Red Planet?",
                         ["Mars", "Venus", "Jupiter", "Mercury"], "Mars"),
                Question("Question 2: Which planet is closest to the Sun?", ["Mars", "Venus", "Mercury", "Jupiter"],
                         "Mercury"),
                # Add more difficult questions to the pool
            ],
            # Add more question pools of increasing difficulty
        ]
        self.score = 0

    def play(self):
        for pool in self.question_pools:
            question = random.choice(pool)
            print(question.text)
            for i, choice in enumerate(question.choices):
                print(f"{i + 1}. {choice}")

            user_answer = input("Enter your answer (1-4): ")
            if question.answer.lower() == question.choices[int(user_answer) - 1].lower():
                self.score += 1
                print("Correct!\n")
            else:
                print(f"Wrong! The correct answer is {question.answer}\n")

        print(f"Your final score: {self.score}/{len(self.question_pools)}\n")


# Create a quiz instance and play the game
quiz = Quiz()
quiz.play()
