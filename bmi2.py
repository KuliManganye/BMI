# program to calculate the Body Mass Index (BMI) from a user's weight and height
# this program goes even deeper to tell the user where in the bmi index that they fall in.
# under 18.5 they are underweight
# Over 18.5 but below 25, they have a normal weight
# Over 25 but below 30, they are sloghly overweight
# Over 30 but below 35, they are obese
# Above 35, they are clinally obese

# prompt user to input their height and weight
height = float(input("What is your height in metres(m)? "))
weight = float(input("What is your weight in kilograms(kg)? "))

# calculate the bmi
bmi = round(weight / (height ** 2))

# now to determine where in the index the user falls after determining their bmi
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slighly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your bmi is {bmi}, you are clinally obese")