class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number].text
        choice = input(f"Q.{self.question_number+1}: {current_question} (True/False) ")
        while choice.lower() not in  ["true", "false"]:
            choice = input("type a valid option: (True/False)")
        choice = choice.lower()
        self.check_answer(choice)
        print(f"You current score: {self.score}/{self.question_number+1}")
        print("\n")
        self.question_number += 1

    def check_answer(self, user_answer):
        correct_answer =self.question_list[self.question_number].answer.lower()
        choice = user_answer
        if choice == correct_answer:
            print("You're correct!!!!")
            self.score += 1
        else:
            print("Sorry, you wrong!!!")

    def still_has_question(self):
            return len(self.question_list) > self.question_number




