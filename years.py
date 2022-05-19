current_age = int(input('What is your current age?\n'))
years = 90 - current_age
months = years * 12
weeks = years * 52
days = years * 365

time_left = f'You have {years} years, {months} months, {weeks} weeks and {days} days left before you become 90'
print(time_left)