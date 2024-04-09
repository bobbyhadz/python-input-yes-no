# Yes/No question with user input in Python

user_input = input('Do you like pizza (yes/no): ')

if user_input.lower() == 'yes':
    print('user typed yes')
elif user_input.lower() == 'no':
    print('user typed no')
else:
    print('Type yes or no')