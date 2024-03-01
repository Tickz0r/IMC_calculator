import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get())
        if weight <= 0 or height <= 0:
            messagebox.showerror("Error", "Please enter positive values for weight and height.")
            return
        bmi = weight / (height ** 2)
        classification = classify_bmi(bmi)
        result_label.config(text=f"Your BMI is: {bmi:.2f}\nClassification: {classification}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values.")

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    elif 30 <= bmi < 34.9:
        return "Obesity class 1"
    elif 35 <= bmi < 39.9:
        return "Obesity class 2"
    else:
        return "Obesity class 3"

# GUI configuration
root = tk.Tk()
root.title("BMI Calculator")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack(padx=20, pady=20)

label_weight = tk.Label(frame, text="Weight (kg):")
label_weight.grid(row=0, column=0, padx=10, pady=10)

entry_weight = tk.Entry(frame)
entry_weight.grid(row=0, column=1, padx=10, pady=10)

label_height = tk.Label(frame, text="Height (m):")
label_height.grid(row=1, column=0, padx=10, pady=10)

entry_height = tk.Entry(frame)
entry_height.insert(0, "E.g., 1.75")  # Height hint
entry_height.grid(row=1, column=1, padx=10, pady=10)

calculate_button = tk.Button(frame, text="Calculate BMI", command=calculate_bmi)
calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

result_label = tk.Label(frame, text="")
result_label.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()