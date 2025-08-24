import tkinter as tk

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.root = tk.Tk()
        self.root.title("Quizzler")
        self.root.config(padx=20, pady=20, bg=THEME_COLOR)

        # Load images
        self.true_img = tk.PhotoImage(file="images/true.png")
        self.false_img = tk.PhotoImage(file="images/false.png")

        # Create label and canvas
        self.score_label = tk.Label(self.root, text="Score", fg="white", bg=THEME_COLOR, font=("Arial", 12, "bold"))
        self.canvas = tk.Canvas(self.root, width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 125,  # X and Y coordinates (center of canvas)
            width=280,
            text="Your quiz starts now!",  # Replace with your desired text
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR  # Or any color you like
        )

        # Create image-only buttons
        self.true_button = tk.Button(self.root, image=self.true_img, highlightthickness=0, bd=0, command=self.true_pressed)
        self.false_button = tk.Button(self.root, image=self.false_img, highlightthickness=0, bd=0, command=self.false_pressed)

        # Place items in a 2-column grid
        self.score_label.grid(row=0, column=1)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=40)
        self.true_button.grid(row=2, column=0)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.root.mainloop()

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="#29B677")
        else:
            self.canvas.config(bg="#EE665D")

        self.root.after(1000, self.get_next_question)

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfigure(self.question_text, text=q_text)
        else:
            self.canvas.itemconfigure(self.question_text, text=f"You've completed the quiz. Your final score is: {self.quiz.score}/{len(self.quiz.question_list)}.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
