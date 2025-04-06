import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingGameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        self.max_attempts = 10
        self.reset_game()
        self.create_widgets()
    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="I'm thinking of a number\nbetween 1 and 100", font=("Helvetica", 14), fg="blue")
        self.title_label.pack(pady=10)

        self.attempts_label = tk.Label(self.root, text=f"Attempts left: {self.max_attempts}", font=("Helvetica", 12))
        self.attempts_label.pack()

        self.range_label = tk.Label(self.root, text=f"Guess a number between {self.low} and {self.high}")
        self.range_label.pack(pady=5)

        self.entry = tk.Entry(self.root, font=("Helvetica", 12))
        self.entry.pack(pady=5)

        self.submit_button = tk.Button(self.root, text="Submit Guess", command=self.check_guess)
        self.submit_button.pack(pady=5)

        self.feedback_label = tk.Label(self.root, text="", font=("Helvetica", 12))
        self.feedback_label.pack(pady=10)

    def reset_game(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.low = 1
        self.high = 100

    def check_guess(self):
        guess = self.entry.get()
        try:
            guess = int(guess)
            if guess < self.low or guess > self.high:
                self.feedback_label.config(text=f"Out of range! ({self.low}-{self.high})", fg="red")
                return
        except ValueError:
            self.feedback_label.config(text="Please enter a valid number!", fg="red")
            return

        self.attempts += 1
        attempts_left = self.max_attempts - self.attempts
        self.attempts_label.config(text=f"Attempts left: {attempts_left}")
        if guess < self.secret_number:
            self.low = max(self.low, guess + 1)
            self.feedback_label.config(text="Too low! Try higher.", fg="orange")
        elif guess > self.secret_number:
            self.high = min(self.high, guess - 1)
            self.feedback_label.config(text="Too high! Try lower.", fg="orange")
        else:
            messagebox.showinfo("🎉 You Win!", f"Congratulations! You guessed the number in {self.attempts} attempts.")
            self.ask_restart()
            return
        self.range_label.config(text=f"Guess a number between {self.low} and {self.high}")
        self.entry.delete(0, tk.END)
        if attempts_left == 0:
            messagebox.showerror("💀 Game Over", f"You're out of attempts! The number was {self.secret_number}.")
            self.ask_restart()

    def ask_restart(self):
        play_again = messagebox.askyesno("Play Again?", "Would you like to play again?")
        if play_again:
            self.reset_game()
            self.attempts_label.config(text=f"Attempts left: {self.max_attempts}")
            self.range_label.config(text=f"Guess a number between {self.low} and {self.high}")
            self.feedback_label.config(text="")
            self.entry.delete(0, tk.END)
        else:
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    root.iconbitmap("icon.ico")
    game = NumberGuessingGameGUI(root)
    root.mainloop()
