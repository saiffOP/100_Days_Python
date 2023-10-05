# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# new_list = [name.upper() for name in names if len(name) >= 5]
# print(new_list)

import pandas

# TODO 1: Create a Dictionary in this format
# {"A" : "Alfa", "B" : "Bravo"}

nato_alphabets = pandas.read_csv("nato_phonetic_alphabet.csv")
alpha_dict = {row.letter: row.code for (index, row) in nato_alphabets.iterrows()}
print(alpha_dict)

# TODO 2: Create a list of the phonetic code words from a word that the user inputs

Word = input("Enter a word: ").upper()

phonetic_code_words = [alpha_dict[letter] for letter in Word]
print(phonetic_code_words)

