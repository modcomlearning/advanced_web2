
# Write a Python Prog. to find Body Mass Index
# we need weight and height, name, age, nationality
print('======BMI Calculator=======')
weight = float(input('What is Your Weight - Kgs:'))
height = float(input('What is Your Height - meters:'))
name = str(input('What is your name:'))
age = int(input('What is your age:'))
nationality = str(input('Are you kenyan? True/False'))

print('Received Weight is', weight, 'Kgs')
print('Received Height is', height, 'meters')
print('Your Names was', name)
print('Received Age is', age, 'Years')
print('Are you Kenyan? ', nationality)

# above combination of strings and variables  - concatenation
# Formula  - Arithmetic Operators
bmi = weight/(height**2)
print('Your Final BMI is ', round(bmi, 2))
print('======Thank You=====')

# More operations   - Comparison   - if, elif, else
if bmi <= 17.5:
    print('Underweight')

elif bmi <= 22.5:
    print('Normal')

elif bmi <= 29.5:
    print('Overweight')

else:
    print('Obese')  # over 29...




