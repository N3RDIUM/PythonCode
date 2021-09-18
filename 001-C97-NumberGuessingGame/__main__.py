import random
numbers = ['1','2','3','4','5','6','7','8','9','10']
currentchoice = random.randint(0,len(numbers)-1)

def check_answer(value):
    if value == numbers[currentchoice]:
        return True
    else:
        return False
    
print('----- Number Guessing Game -----\nI am thinking of a number between one to ten.\nYou have to guess that number.')

while True:
    try:
        num = str(input('Enter your guess > '))
        if not num in numbers:
            print('Please enter one from {}'.format(numbers)+'.')
        else:
            if check_answer(num):
                print('You guessed it!')
                break
            else:
                print('That was so close! Try again.')
                currentchoice = random.randint(0,len(numbers)-1)
    except:
        print('\nProgram exited.')
        break
