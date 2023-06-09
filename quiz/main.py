class Question:
    def __init__(self, text, choices, answer):
        """
        Initialize a question with the provided text, choices, and answer.
        """
        self.text = text
        self.choices = choices
        self.answer = answer

    def check_answer(self, user_answer):
        """
        Check if the user's answer matches the correct answer.
        Ignore case sensitivity.
        """
        return user_answer.lower() == self.answer.lower()


class Quiz:
    def __init__(self):
        """
        Initialize a quiz with an empty list of questions, score set to 0,
        and the current question index set to 0.
        """
        self.questions = []
        self.score = 0
        self.current_question_index = 0

    def add_question(self, question):
        """
        Add a question to the quiz.
        """
        self.questions.append(question)

    def display_question(self):
        """
        Display the current question.
        """
        current_question = self.questions[self.current_question_index]
        print(f"Question {self.current_question_index + 1}: {current_question.text}")

        for i, choice in enumerate(current_question.choices):
            print(f"{i + 1}. {choice}")

    def get_user_answer(self):
        """
        Prompt the user to enter their answer and return it.
        """
        user_answer = input("Enter your answer (1-4): ")
        return user_answer

    def check_user_answer(self, user_answer):
        """
        Check the user's answer against the correct answer for the current question.
        If the answer is correct, increment the score. Otherwise, do nothing.
        """
        current_question = self.questions[self.current_question_index]

        if current_question.check_answer(user_answer):
            self.score += 1
            print("Correct!\n")
        else:
            print(f"Wrong! The correct answer is {current_question.answer}\n")

    def display_score(self):
        """
        Display the final score.
        """
        print(f"Your score: {self.score}/{len(self.questions)}\n")

    def play(self):
        """
        Start the quiz, display each question, get the user's answer, check it,
        and move to the next question until all questions are answered.
        Finally, display the score.
        """
        for _ in range(len(self.questions)):
            self.display_question()
            user_answer = self.get_user_answer()
            self.check_user_answer(user_answer)
            self.current_question_index += 1

        self.display_score()


# Create quiz questions
question1 = Question("What is the capital of France?", ["London", "Paris", "Berlin", "Rome"], "Paris")
question2 = Question("Which planet is known as the Red Planet?", ["Mars", "Venus", "Jupiter", "Mercury"], "Mars")
question3 = Question("What is the largest ocean in the world?",
                     ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"], "Pacific Ocean")

# Create a quiz and add questions
quiz = Quiz()
quiz.add_question(question1)
quiz.add_question(question2)
quiz.add_question(question3)

# Play the quiz
quiz.play()
