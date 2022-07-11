from tkinter import *
from PIL import ImageTk, Image
import time
def round_one(a):
    print("Who makes the AMG model")
    print(" a. BMW   b. Tesla   c. Mercedes   d. Audi ")
    answer_one = input().lower()
    if answer_one == "c":
        print("correct! +3 points")
    else:
        print("incorrect -1 life")
        a = a - 1
    return a

def round_two(a):
    print("Who makes the car company polestar?")
    print(" a. Toyota   b. Ford   c. Volkswagen   d. Volvo ")
    answer_two = input().lower()
    if answer_two == "d":
        print("correct! +3 points")
    else:
        print("incorrect -1 life")
        a = a -1
    return a

def round_three(a):
    print("Which one of these is a type of adventador?")
    print(" a. SVG   b. Lp700-4   c. M roadster   d. tourer ")
    answer_three = input().lower()
    if answer_three == "b":
        print("correct! +3 points")
    else:
        print("incorrect -1 life")
        a = a -1
    return a

def round_four(a):
    print("Which of these is part of the exhaust system on a car?")
    print(" a.catalytic converter   b. head gasket   c. fuel injectors   d. camshaft")
    answer_four = input().lower()
    if answer_four == "a":
        print("correct! +3 points")
    else:
        print("incorrect -1 life")
        a = a - 1
    return a

def round_five(a):
    print("what was the most sold car globally in 2021?")
    print(" a. Ford fiesta   b. Toyota RAV4   c. HondaCR-V   d. Nissan qashqai ")
    answer_five = input().lower()
    if answer_five == "b":
        print("correct! +3 points")
    else:
        print("incorrect -1 life")
        a = a -1
    return a
def round_six(a):
    count = 0
    print("For this question you'll need to guess the car in the image. . .")
    time.sleep(1)
    answer_six = input('What car is this? (name and model)').lower()
    answer_list = set(answer_six)
    answer = ['p', 'a', 'g', 'n', 'i', 'z', 'o', 'd']
    if len(answer_six) > 15:
        print("incorrect -1 life")
        a = a - 1
    elif len(answer_six) < 15:
        for i in answer_list:
            index_answer = answer_list[i:(1+i)]
            if index_answer in answer:
                count += 1 
            else:
                break 
    else:
        print("Inavlid response! -1 life")

def round_seven(a):
    print("Final question this is worth 6 points...")
    print("In which year was the Bugatti Veyron made?")
    print(" a. 2001   b. 2002   c. 2005   d. 2007")
    answer_seven = input().lower()
    if answer_seven == "c":
        print("amazing you really know your cars! +6 points")
    else:
        print("incorrect -1 life")
        a = a - 1
    return a

print("Welcome, how well do you know your cars :) ")
points = 0
lives = 3
answers = 0
while lives > 0:
    lives = round_one(lives)
    answers = answers + 1
    if lives == 0:
        break
    lives = round_two(lives)
    answers = answers + 1
    if lives == 0:
        break
    lives = round_three(lives)
    answers = answers + 1
    if lives == 0:
        break
    lives = round_four(lives)
    answers = answers + 1
    if lives == 0:
        break
    lives = round_five(lives)
    answers = answers + 1
    if lives == 0:
        break
    lives = round_six(lives)
    answers = answers + 2
    break
lives_lost = 3 - lives
subtract = lives_lost * 3
tot_answers = answers * 3
score = tot_answers - subtract

print("Gameover! better luck next time")
print("Game stats. . . ")
print(f"lives lost = {lives_lost}")
print(f"Score = {score}")
print(f"Points missed = {subtract}")



