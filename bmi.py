

height = float(input('What is your height in m?\n'))
weight = float(input('What is your weight in kg?\n'))

bmi = round(weight / height ** 2, 2)

print('Your body mass index is {}'.format(bmi))