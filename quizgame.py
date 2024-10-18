import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, master):
        # Initialize the main window
        self.master = master
        self.master.title("Quiz Game")
        self.master.geometry("400x300")

        # Create and place the question label
        self.question_label = tk.Label(master, text="", wraplength=380)
        self.question_label.pack(pady=20)

        # Create and place the answer entry field
        self.answer_var = tk.StringVar()
        self.answer_entry = tk.Entry(master, textvariable=self.answer_var)
        self.answer_entry.pack(pady=10)

        # Create and place the submit button
        self.submit_button = tk.Button(master, text="Submit", command=self.check_answer)
        self.submit_button.pack(pady=10)

        # Define the quiz questions and answers
        self.questions = [
            {"question": "When was the first known use of the word 'quiz'?", "answer": "1781"},
            {"question": "Which built-in function can get information from the user?", "answer": "input"},
            {"question": "What does CPU stand for?","answer": "central processing unit"},
            {"question": "What does RAM stand for?","answer": "random access memory"},
            {"question": "What does GPU stand for?","answer": "graphics processing unit"},
            {"question": "What does SSD stand for?","answer": "solid state drive"}
        ]
        self.current_question = 0  # Keep track of the current question
        self.score = 0  # Initialize the user's score

        self.load_question()  # Load the first question

    def load_question(self):
        # Check if there are more questions to ask
        if self.current_question < len(self.questions):
            # Update the question label with the current question
            self.question_label.config(text=self.questions[self.current_question]["question"])
            self.answer_var.set("")  # Clear the answer entry field
        else:
            self.show_result()  # If no more questions, show the final result

    def check_answer(self):
        # Get the user's answer and the correct answer
        user_answer = self.answer_var.get().strip()
        correct_answer = self.questions[self.current_question]["answer"]

        # Check if the answer is correct (case-insensitive)
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            messagebox.showinfo("Correct!", "Your answer is correct!")
        else:
            messagebox.showerror("Incorrect", f"The correct answer is '{correct_answer}'")

        # Move to the next question
        self.current_question += 1
        self.load_question()

    def show_result(self):
        # Display the final score
        result = f"Quiz completed!\nYour score: {self.score}/{len(self.questions)}"
        messagebox.showinfo("Quiz Result", result)
        self.master.quit()  # Close the application

# Create the main window and start the quiz
root = tk.Tk()
quiz_app = QuizApp(root)
root.mainloop()