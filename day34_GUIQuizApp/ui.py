from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


def true_check_answer(self):
    self.quiz.check_answer(True)
    self.get_next_question()


def false_check_answer(self):
    self.quiz.check_answer(False)
    self.get_next_question()
class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz=quiz_brain
        self.window= Tk()
        self.window.title("Quizzler")
        self.window.configure(
            bg=THEME_COLOR,
            padx=20,
            pady=20,
        )
        self.canvas = Canvas(
            height=250,
            width=300,
        )
        self.canvas_text= self.canvas.create_text(
            150, 125,
            width=280,
            font=("Arial", 20, "italic"),
            text="hello",
            fill=THEME_COLOR,
        )
        self.score_label = Label(text="Score:0", bg=THEME_COLOR, fg="#ffffff")
        self.score_label.grid(row=0, column=1)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=50, pady=50)
        correct_image = PhotoImage(file="images/true.png")
        incorrect_image = PhotoImage(file="images/false.png")
        self.correct_button = Button(image= correct_image, command=self.true_check_answer, highlightthickness=0)
        self.correct_button.grid(row=2, column=0)
        self.incorrect_button = Button(image=incorrect_image, command= self.false_check_answer, highlightthickness=0)
        self.incorrect_button.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text, text= q_text)
        else:
            self.canvas.itemconfig(self.canvas_text, text="You've reached the end of the quiz!")
            self.correct_button.config(state="disabled")
            self.incorrect_button.config(state="disabled")
    def true_check_answer(self):
        is_right = self.quiz.check_answer("True")
        self.score_label.configure(text= f"Score:{self.quiz.score}")
        self.give_feedback(is_right)

    def false_check_answer(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg = "green")
        else:
            self.canvas.config(bg= "red")
        self.window.after(1000, self.get_next_question)

