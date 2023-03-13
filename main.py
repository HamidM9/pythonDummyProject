def word_finder():
    user_input = input("Please Enter your document: \n")
    user_input2 = input("Please enter your word: ")
    splitted = user_input.split()
    word = user_input2
    counter = 0
    for words in splitted:
        if words == word:
            print(word + " is in the document")
            break
        else:
            counter = counter + 1
    if counter == len(splitted):
        print(" No match found")


def acronym():
    user_input_ac = input("Please input your words: \n")
    user_input_ac_splited = user_input_ac.split()
    real_ac = " "
    for words in user_input_ac_splited:
        real_ac = real_ac + words[0]

    print(real_ac.upper())


def user_input():
    input_number = input(" Hey, Need something? \n"
                         "1. is there a 'word' in a 'sentence'?\n"
                         "2. Acronym Generator\n")

    return input_number


user_input = user_input()

if user_input == "1":
    word_finder()
if user_input == "2":
    acronym()
