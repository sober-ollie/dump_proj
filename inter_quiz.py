import tkinter as tk
from tkinter import messagebox
import random

# --- YOUR DATA ---
bf_random = [
    {
        "id": 1,
        "question": "What happens if you access a missing key using my_dict['key']?",
        "options": {"A": "It returns None", "B": "It returns False", "C": "It raises a KeyError", "D": "It creates the key with value 0"},
        "answer": "C"
    },
    {
        "id": 2,
        "question": "As of Python 3.7+, which statement is true about dictionaries?",
        "options": {"A": "They are unordered collections", "B": "They maintain insertion order", "C": "They allow duplicate keys", "D": "Keys must be mutable (like lists)"},
        "answer": "B"
    },
    {
        "id": 3,
        "question": "What is the result of: {'a': 1}.get('b', 3)?",
        "options": {"A": "None", "B": "KeyError", "C": "2", "D": "3"},
        "answer": "D"
    },
    {
        "id": 4,
        "question": "Which method removes a key and returns its value?",
        "options": {"A": ".remove()", "B": ".pop()", "C": ".delete()", "D": ".discard()"},
        "answer": "B"
    },
    {
        "id": 5,
        "question": "What is the output of {x: x**2 for x in [1, 2]}?",
        "options": {"A": "{1, 4}", "B": "[1: 1, 2: 4]", "C": "{1: 1, 2: 4}", "D": "(1: 1, 2: 4)"},
        "answer": "C"
    }
]

class QuizGame:
    def __init__(self, window):
        self.window = window
        self.window.title("Python Dictionary Quiz")
        self.window.geometry("500x500")
        
        # Shuffle questions once at start
        self.questions = bf_random
        random.shuffle(self.questions)
        
        # State variables
        self.score = 0
        self.current_q_index = 0
        
        # --- UI Elements ---
        self.title_label = tk.Label(window, text="Python Quiz", font=("Arial", 20, "bold"), pady=10)
        self.title_label.pack()

        self.q_num_label = tk.Label(window, text="", font=("Arial", 10))
        self.q_num_label.pack()

        self.question_text = tk.Label(window, text="", font=("Arial", 12), wraplength=400, pady=20)
        self.question_text.pack()

        # Create 4 buttons and store them in a list
        self.option_buttons = []
        for i in range(4):
            btn = tk.Button(window, text="", width=40, height=2, command=lambda idx=i: self.check_answer(idx))
            btn.pack(pady=5)
            self.option_buttons.append(btn)

        self.status_label = tk.Label(window, text="Score: 0", pady=20, font=("Arial", 10, "italic"))
        self.status_label.pack()

        # Start the first question
        self.load_question()

    def load_question(self):
        """Updates the labels and buttons with the current question data."""
        data = self.questions[self.current_q_index]
        
        # Update question text
        self.q_num_label.config(text=f"Question {self.current_q_index + 1} of {len(self.questions)}")
        self.question_text.config(text=data["question"])
        
        # Update buttons
        options = list(data["options"].items()) # List of tuples: [("A", "text"), ("B", "text")...]
        for i in range(4):
            label, text = options[i]
            self.option_buttons[i].config(text=f"{label}: {text}")

    def check_answer(self, button_index):
        """Logic to check the answer and move forward."""
        keys = ["A", "B", "C", "D"]
        user_choice = keys[button_index]
        correct_answer = self.questions[self.current_q_index]["answer"]

        if user_choice == correct_answer:
            self.score += 1
            messagebox.showinfo("Result", "Correct!")
        else:
            messagebox.showerror("Result", f"Wrong! The correct answer was {correct_answer}")

        # Update Score Display
        self.status_label.config(text=f"Score: {self.score}")

        # Move to next or end
        self.current_q_index += 1
        if self.current_q_index < len(self.questions):
            self.load_question()
        else:
            self.show_final_score()

    def show_final_score(self):
        messagebox.showinfo("Quiz Finished", f"Final Score: {self.score} / {len(self.questions)}")
        
        # Ask to play again
        play_again = messagebox.askyesno("Play Again?", "Would you like to restart the quiz?")
        if play_again:
            self.score = 0
            self.status_label.config(text=f"Score: {self.score}")
            self.current_q_index = 0

            random.shuffle(self.questions)
            self.load_question()
        else:
            self.window.destroy()

# --- RUN THE PROGRAM ---
if __name__ == "__main__":
    root = tk.Tk()
    root.attributes('-zoomed', True)
    game = QuizGame(root)
    root.mainloop()