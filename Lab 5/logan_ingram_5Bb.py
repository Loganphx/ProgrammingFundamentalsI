import random
playAgain = 'yes'
while playAgain.lower() == 'yes':
    randomNumber = random.randint(0, 1000)
    guess = int(input('Guess the number: '))
    attempts = 1
    while guess != randomNumber:
        if 0 < randomNumber-guess < 10:
            print('Getting warm but still Low!')
            guess = int(input('Guess again: '))
            attempts+=1
        elif guess < randomNumber:
            print('Too Low')
            guess = int(input('Guess again: '))
            attempts+=1
        elif 0 < guess-randomNumber < 10:
            print('Getting warm but still High!')
            guess = int(input('Guess again: '))
            attempts+=1
        elif guess > randomNumber:
            print('Too High!')
            guess = int(input('Guess again: '))
            attempts+=1
    if guess == randomNumber:
        print('Congrats you guessed the number!')
        print('It only took ' + str(attempts) + ' tries!')
        print('')
        playAgain = str(input('Do you wish to play again?: '))
