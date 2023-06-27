import os
os.system('cls')

class Health:
    def __init__(self):
        self.height = 0
        self.weight = 0
        self.water = 0
        self.gender = ""
        self.age = 0
        self.exercise = 0
        self.sleep = 0

    def get_values(self):
        self.height = float(input("Enter your height in meter: "))
        self.weight = int(input("Enter your weight in kilograms: "))
        self.gender = input("Enter your gender (male/female): ")
        self.water = int(input("enter a glasses of water you drink per day"))
        self.age = int(input("Enter your age in years: "))
        self.exercise = int(input("Enter the number of minute you exercise per day: "))
        self.sleep = int(input("Enter the number of hours you sleep per day: "))

    def calculate_bmi(self):
        bmi = self.weight / (self.height ** 2)
        if 18 <= bmi < 26:
            return f"Your BMI is {bmi:.2f} and you are in the healthy range."
        elif 16 <= bmi < 18:
            return f"Your BMI is {bmi:.2f} and you are slightly underweight."
        elif 26 <= bmi < 31:
            return f"Your BMI is {bmi:.2f} and you are overweight."
        elif 31 <= bmi < 41:
            return f"Your BMI is {bmi:.2f} and you have excess fat."
        else:
            return f"Your BMI is {bmi:.2f}"

    def calculate_bmr(self):
        if self.gender == "male":
            bmr = int((self.age * 5) - (self.height * 10) + (self.weight * 6.25) + 5)
        else:
            bmr = int((self.age * 5) - (self.height * 10) + (self.weight * 6.25) - 161)

        if self.exercise < 16:
            bmr *= 1.3
        elif 16 <= self.exercise < 30:
            bmr *= 1.55
        else:
            bmr *= 1.9

        return f"Your BMR is {bmr:.2f} calories per day."

    def check_hydration(self):
        if self.gender == "male":
            water_needed = 3.7 * self.water
        else:
            water_needed = 3.1 * self.water

        if water_needed < 8:
            return "You need to drink more water."
        elif 8 <= water_needed <= 10:
            return "You are drinking a normal amount of water."
        else:
            return "You are drinking more water than necessary."

    def check_exercise(self):
        if 25 <= self.exercise < 59:
            return "At least twenty minutes of exercise a day is good for your health."
        elif self.exercise >= 60:
            return "You are exercising a lot. Are you an athlete?"
        else:
            return "You should try to do more exercise."

    def check_sleep(self):
        if self.age >= 18:
            if self.sleep < 6:
                return "You need to sleep more."
            elif 6 <= self.sleep <= 8:
                return "You are getting the recommended amount of sleep."
            else:
                return "You are sleeping more than necessary."
        else:
            if self.sleep < 8:
                return "You need to sleep more."
            elif 8 <= self.sleep <= 10:
                return "You are getting the recommended amount of sleep."
            else:
                return "You are sleeping more than necessary."


def run():
    human = Health()
    human.get_values()
    print(human.calculate_bmi())
    print(human.calculate_bmr())
    print(human.check_hydration())
    print(human.check_exercise())
    print(human.check_sleep())


import tkinter as tk
from tkinter import messagebox

class HealthGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Health Assessment")
        
        self.create_widgets()
    
    def create_widgets(self):
        height_label = tk.Label(self.root, text="Height (cm):")
        height_label.grid(row=0, column=0)
        self.height_entry = tk.Entry(self.root)
        self.height_entry.grid(row=0, column=1)

        weight_label = tk.Label(self.root, text="Weight (kg):")
        weight_label.grid(row=1, column=0)
        self.weight_entry = tk.Entry(self.root)
        self.weight_entry.grid(row=1, column=1)

        gender_label = tk.Label(self.root, text="Gender:")
        gender_label.grid(row=2, column=0)
        self.gender_entry = tk.Entry(self.root)
        self.gender_entry.grid(row=2, column=1)

        water_label = tk.Label(self.root, text="Water (glasses per day):")
        water_label.grid(row=3, column=0)
        self.water_entry = tk.Entry(self.root)
        self.water_entry.grid(row=3, column=1)

        age_label = tk.Label(self.root, text="Age (years):")
        age_label.grid(row=4, column=0)
        self.age_entry = tk.Entry(self.root)
        self.age_entry.grid(row=4, column=1)

        exercise_label = tk.Label(self.root, text="Exercise (minutes per day):")
        exercise_label.grid(row=5, column=0)
        self.exercise_entry = tk.Entry(self.root)
        self.exercise_entry.grid(row=5, column=1)

        sleep_label = tk.Label(self.root, text="Sleep (hours per day):")
        sleep_label.grid(row=6, column=0)
        self.sleep_entry = tk.Entry(self.root)
        self.sleep_entry.grid(row=6, column=1)

        calculate_button = tk.Button(self.root, text="Calculate", command=self.calculate)
        calculate_button.grid(row=7, column=0, columnspan=2)

    def calculate(self):
        try:
            height = float(self.height_entry.get())
            weight = float(self.weight_entry.get())
            gender = self.gender_entry.get()
            water = int(self.water_entry.get())
            age = int(self.age_entry.get())
            exercise = int(self.exercise_entry.get())
            sleep = int(self.sleep_entry.get())

            health = Health()
            health.height = height
            health.weight = weight
            health.gender = gender
            health.water = water
            health.age = age
            health.exercise = exercise
            health.sleep = sleep

            bmi_result = health.calculate_bmi()
            bmr_result = health.calculate_bmr()
            hydration_result = health.check_hydration()
            exercise_result = health.check_exercise()
            sleep_result = health.check_sleep()

            messagebox.showinfo("Results", f"{bmi_result}\n{bmr_result}\n{hydration_result}\n{exercise_result}\n{sleep_result}")
        except ValueError:
            messagebox.showerror("Error", "enter again")

root = tk.Tk()
app = HealthGUI(root)
root.mainloop()
