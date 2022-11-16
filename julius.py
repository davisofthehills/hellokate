import string

characters = string.printable
    # originally, the string. was 4 different variations to include everything, then i found a simpler way
phrase = list(input('Original: \n').lower())

mode = input(
    'e to ENCRYPT / d to DECRYPT \n').lower()

shift = int(input('shift up to 25: \n'))
    #inputs the degree of shift that occurs
    #does not surpass 25, since that would full loop
end_program = False

while not end_program:
    #the part that actually translates
    if mode == 'e':
        for i in range(len(phrase)):
            # get the position of each character within the phrase
            if phrase[i] == ' ':
                phrase[i] = ' '
            else:
                new_letter = characters.index(phrase[i]) + shift
                phrase[i] = characters[new_letter]
        # convert the list back to a string
        print(''.join(map(str, phrase)))
        end_program = True
    elif mode == 'd':
        for i in range(len(phrase)):
            if phrase[i] == ' ':
                phrase[i] = ' '
            else:
                new_letter = characters.index(phrase[i]) - shift
                phrase[i] = characters[new_letter]
            # convert the list back to a string
        print(''.join(map(str, phrase)))
        end_program = True
    else:
        decide = input(
            'invalid entry, try again? Y / N \n').lower()
                #more for me to see where errors occur
        if decide == 'y':
            sentence = list(input('enter your text: \n').lower())
            mode = input(
                'e to ENCRYPT / d to DECRYPT \n').lower()
            shift = int(input('enter your shift number from 1 to 25: \n'))
        else: 
            end_program = True