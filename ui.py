import tkinter as tk

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Quizzler")
        self.root.config(bg=THEME_COLOR)

        # Load images
        self.true_img = tk.PhotoImage(file="images/true.png")
        self.false_img = tk.PhotoImage(file="images/false.png")

        # Create label and canvas
        self.score_label = tk.Label(self.root, text="Score", fg="white", bg=THEME_COLOR, font=("Arial", 12, "bold"))
        self.canvas = tk.Canvas(self.root, width=400, height=400, bg="white")
        self.canvas.create_text(
            200, 200,  # X and Y coordinates (center of canvas)
            text="Your quiz starts now!",  # Replace with your desired text
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR  # Or any color you like
        )

        # Create image-only buttons
        self.true_button = tk.Button(self.root, image=self.true_img, highlightthickness=0, bd=0, command=self.true_pressed)
        self.false_button = tk.Button(self.root, image=self.false_img, highlightthickness=0, bd=0, command=self.false_pressed)

        # Place items in a 2-column grid
        self.score_label.grid(row=0, column=1, padx=10, pady=10)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        self.true_button.grid(row=2, column=0, padx=10, pady=10)
        self.false_button.grid(row=2, column=1, padx=10, pady=10)

        self.root.mainloop()

    def true_pressed(self):
        print("True button pressed")

    def false_pressed(self):
        print("False button pressed")
