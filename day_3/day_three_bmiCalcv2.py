#BMI Calculator with Interpretations
height = float(input("Enter your height in meters: ")) 
weight = float(input("Enter your weight in kg: ")) 

bmi = weight / (height ** 2)

print(bmi)

if bmi < 18.5:
    print("underweight")

elif 18.5 <= bmi < 25:
    print("normal weight")

else:
    print("overweight")