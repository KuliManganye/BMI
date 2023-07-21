# program to calculate the Body Mass Index (BMI) from a user's weight and height

# the bmi is calculated by dividing a person's weight (in kg) by the square of their height (in m)

# prompt user to input their height and weight

height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

# calculation
bmi = weight / (height ** 2)
print(int(bmi))