from math import floor
import sys
most_powerful_word = -sys.maxsize
the_word = ''

command = input()

while command != 'End of words':
    word = command
    word_length = len(word)
    starting_letter = word[0] # взимаме позицията
    word_ascii = 0

    for letter in word:
        letter_ascii = ord(letter)
        word_ascii += letter_ascii

    if starting_letter in ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']:
        word_ascii *= word_length
    else:
        word_ascii = floor(word_ascii / word_length)

    if word_ascii > most_powerful_word:
        most_powerful_word = word_ascii
        the_word = word

    command = input()

print(f'The most powerful word is {the_word} - {most_powerful_word}')
