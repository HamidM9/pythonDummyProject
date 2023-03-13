import datetime

import switch as switch
from playsound import playsound
import random




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
            counter = counter +1
    if counter == len(splitted):
        print(" No match found")


def acronym():
    user_input = input("Please input your words: \n")
    user_input_splitted = user_input.split()
    real_ac = " "
    for words in user_input_splitted:
        real_ac = real_ac + words[0]

    print(real_ac.upper())


def alarm_clock():
    alarm_time = "04:22:21 am"
    alarm_hour = alarm_time[0:2]
    alarm_minute = alarm_time[3:5]
    alarm_second = alarm_time[6:8]
    alarm_ampm = alarm_time[9:11].upper()

    print("Setting up alarm..")
    x = datetime.datetime.now()
    current_hour = x.strftime("%I")
    current_minute = x.strftime("%M")
    # current_second = x.strftime("%S")

    if current_hour == alarm_hour:
        if current_minute == alarm_minute:
            # if current_second == alarm_second:
            playsound('alarm.wav')


def email_slicer():
    email_adress = "hamid.mohammadi@unipd.it"
    index = email_adress.find("@")
    username = email_adress[:index]
    domain_name = email_adress[index+1:]
    format_ = (f"Your user name is '{username}' and your domain is '{domain_name}'")
    print(format_)


def story_generator():
    when = ['A few years ago', 'Yesterday', 'Last night', 'A long time ago', 'On 20th Jan']
    who = ['a rabbit', 'an elephant', 'a mouse', 'a turtle', 'a cat']
    residence = ['Turino', 'Milano', 'Padova', 'venezia']
    went = ['cinema', 'university', 'seminar', 'school', 'laundry']
    happened = ['made a lot of friends', 'Eats a burger', 'found a secret key', 'solved a mistery', 'wrote a book']
    print(random.choice(when) + ', ' + random.choice(who) + ' that lived in ' + random.choice(
        residence) + ', went to the ' + random.choice(went) + ' and ' + random.choice(happened))

def user_input():
        input_number = input(" Hello Dear, What do you need? \n"
                             "1. is there a 'word' in a 'sectence'?\n"
                             "2. Acronym Generator\n")

        return input_number
def rockPaperScissors():
    options = [r, p, s]


#user_input = user_input()
#print(user_input)

options = ["r", "s", "p"]

player1 = user_input()
player2 = random.choice(options)
if player1 == player2:
    print("draw")
elif(player1 == "p" and player2 == "r") or (player1 == "r" and player2 == "s") or (player1 == "s" and player2 == "p"):
    print("P1WINS")
else:
    print("P2WINS")


if user_input == "1":
    word_finder()
elif user_input == "2":
    acronym()
#def password_generator():
#word_finder(word)
#acronym(splited)
#alarm_clock()
#email_slicer()
#story_generator()










