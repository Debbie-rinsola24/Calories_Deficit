class Diet:
    def __init__(self, breakfast_calories, lunch_calories, dinner_calories, exercise, bmr):
        self.breakfast_calories = breakfast_calories
        self.lunch_calories = lunch_calories
        self.dinner_calories = dinner_calories
        self.exercise = exercise
        self.bmr = bmr

    def calories_deficit(self):
        deficit =  self.bmr + self.exercise - (self.breakfast_calories + self.lunch_calories + self.dinner_calories)
        return deficit

breakfast_calories = int(input("How many calories did you have for breakfast?."))
lunch_calories = int(input("How many calories did you have for lunch?. "))
dinner_calories = int(input("How many  calories did you have for dinner?. "))
exercise = int(input("How many calories did you burn exercising?. "))
bmr = int(input("What is your basic metabolic rate?. "))

fitness = Diet(breakfast_calories, lunch_calories, dinner_calories, exercise, bmr)
weekly_deficit = 7 + fitness.calories_deficit()

if weekly_deficit > 0:
    print(f"You lose {round(weekly_deficit / 3600, 2)} kg. per week")
elif weekly_deficit == 0:
    print(f"You weight will stay the same. ")
else:
    print(f"You wil gain {round(-1 * weekly_deficit / 3600, 2)} kg. per week)")