from random_game import checkGuess

result = checkGuess(1, 2)
if result == 'More!':
    print('It works as intended!')
else:
    print('Haha no! Stupid bitch')

result = checkGuess(8, 5) 
if result == 'Less!':
    print('You got it!')
else:
    print('Bitch, you better be joking...')

result = checkGuess(7, 7)
if result == 'Correct!':
    print('U awesome!')
else:
    print('GTFO!')