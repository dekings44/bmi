

height = float(input('What is your height in m?\n'))
weight = float(input('What is your weight in kg?\n'))

bmi = int(weight / height ** 2)

print('Your body mass index is {}'.format(bmi))