

height = float(input('What is your height in m?\n'))
weight = float(input('What is your weight in kg?\n'))

bmi = round(weight / height ** 2, 2)

if bmi < 18.5:
    print(f'Your body mass index is {bmi} and you are underweight')
elif bmi < 25:
    print(f'Your body mass index is {bmi} and you have a normal weight')
elif bmi < 30:
    print(f'Your body mass index is {bmi} and you are overweight')
elif bmi < 35:
    print(f'Your body mass index is {bmi} and you are obese')
else:
    print(f'Your body mass index is {bmi} and you are clinically obese')
