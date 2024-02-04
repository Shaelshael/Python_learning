numbers = [value**3 for value in range(1, 11)]
frst3qubes = numbers[1:4]
print('The first three items in list are:')
print(frst3qubes)

threequbesinmiddle = numbers[4:7]
print('\nThree items from the middle of the list are:')
print(threequbesinmiddle)

lastthreequbes = numbers[-3:]
print('\nThe last three items in the list are:')
print(lastthreequbes)
