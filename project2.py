"""
Underweight:BMI less than 18.5
Normal weight:BMI between 18.5 and 24.9
Overweight:BMI between 25 and 29.9
Obesity:
Class I (Moderate obesity): BMI between 30 and 34.9
Class II (Severe obesity): BMI between 35 and 39.9
Class III (Very severe or morbid obesity): BMI of 40 and above
"""

name = input("Enter your name : ")
age = int(input("Enter your age : "))
weight = float(input("Enter your weight : "))
height = float(input("Enter your height : "))

cmOrm = input("Are you using centimeters as unit for your height or meters? (Reply with cm or m only) : ")
if cmOrm == "cm":
    BMI = (weight/(height**2))*10000
elif cmOrm == "m":
    BMI = weight/(height**2)
else:
    print("Invalid input. Valid inputs are 'cm' or 'm' only.")
    quit()

print(f"Hello {name}. You are {age} years old. Your BMI is {BMI}. Your BMI results are : ")

if BMI < 18.5:
    print("You are underweight.")
elif BMI >= 18.5 and BMI < 25:
    print("You are normal weight.")
elif BMI >= 25 and BMI < 30:
    print("You are overweight.")
else:
    if BMI >= 30 and BMI < 35:
        print("You are in Class I (Moderate obesity)")
    elif BMI >= 35 and BMI < 40:
        print("You are in CLass II (Severe obesity)")
    else:
        print("You are in Class III (Severe obesity)")