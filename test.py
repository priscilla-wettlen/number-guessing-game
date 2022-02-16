from random_game import checkGuess
numbers_to_test = [[2, 78, "More!"], [1, 0, "Less!"], [1, 1, "Correct!"]]

listA = numbers_to_test[0][2]
listB = numbers_to_test[1][2]
listC = numbers_to_test[2][2]
print(listA, listB, listC)



# for i in numbers_to_test:
#     print(i)
# print(type(i))



# result = checkGuess(1, 2)
# if result == 'More!':
#     print('It works as intended!')
# else:
#     print('Haha no! Stupid bitch')

# result = checkGuess(8, 5) 
# if result == 'Less!':
#     print('You got it!')
# else:
#     print('Bitch, you better be joking...')

# result = checkGuess(7, 7)
# if result == 'Correct!':
#     print('U awesome!')
# else:
#     print('GTFO!')