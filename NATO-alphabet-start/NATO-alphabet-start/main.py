student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():

    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}

alpha = pandas.read_csv("nato_phonetic_alphabet.csv")
new_dict = {row.letter:row.code for (index, row) in alpha.iterrows()}
# letter_dict = {letter:code for (letter,code) in new_dict.items()}

print(new_dict)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
in_word = input("Please write a word to be changed to the Phonetic Code\n").upper()

coded_word = [new_dict[letter] for letter in in_word]
print(coded_word)


x = {"color1": "blue", "color2": "red"}