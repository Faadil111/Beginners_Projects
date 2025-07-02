import tkinter as tk
import random
import sys

def roll_dice():
    """Simulates rolling dice and updates the display."""
    try:
        num_dice = int(num_dice_entry.get())
        if num_dice <= 0:
            raise ValueError("Number of dice must be positive")

        results = [random.randint(1, 6) for _ in range(num_dice)]
        result_label.config(text=f"Results: {results}")

    except ValueError as e:
        result_label.config(text=f"Error: {e}")
    except Exception as e:
      result_label.config(text=f"An unexpected error occurred: {e}")



# Create the main window
root = tk.Tk()
root.title("Dice Roller")

# Number of dice input
num_dice_label = tk.Label(root, text="Number of dice:")
num_dice_label.pack()
num_dice_entry = tk.Entry(root)
num_dice_entry.pack()


# Roll button
roll_button = tk.Button(root, text="Roll Dice", command=roll_dice)
roll_button.pack()

# Result label
result_label = tk.Label(root, text="Results will be displayed here")
result_label.pack()

root.mainloop()
