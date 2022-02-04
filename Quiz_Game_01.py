#Quiz Game

from itertools import count


print("-----WELCOME TO THE QUIZ GAME-----")

points = False
count=0
Do_you_want_to_play = input("Do You Want TO Play ? \n")

if Do_you_want_to_play.lower() != "yes":
    quit()

else:
    print("Lets Continue -----> ")

answer = input("Who developed Python Programming Language? \n a) Wick van Rossum \n b) Rasmus Lerdorf \n c) Guido van Rossum  \n d) Niene Stom \n")

if answer == "Guido van Rossum":
    print("Correct Received 1 Point")
    points = True 
    count+=1
else:
    print("Incorrect")

answer = input("Which type of Programming does Python support? \n a) object-oriented programming \n b) structured programming \n c) functional programming \n d) all of the mentioned \n")

if answer == "all of the mentioned":
    print("Correct Received 1 Point")
    points = True 
    count+=1

else:
    print("Incorrect")

answer = input("Is Python case sensitive when dealing with identifiers? \n a) no \n b) yes \n c) machine dependent \n d) none of the mentioned \n")

if answer == "none of the mentioned":
    print("Correct Received 1 Point")
    points = True
    count+=1

else:
    print("Incorrect")


answer = input("Which of the following is the correct extension of the Python file? \n a) .python \n b) .pl \n c) .py \n d) .p \n")

if answer == ".py":
    print("Correct Received 1 Point")
    points = True
    count+=1
else:
    print("Incorrect")


answer = input("Is Python code compiled or interpreted? \n a) Python code is both compiled and interpreted \n b) Python code is neither compiled nor interpreted \n c) Python code is only compiled \n d) Python code is only interpreted \n")

if answer == "Python code is neither compiled nor interpreted":
    print("Correct Received 1 Point")
    points = True
    count+=1
else:
    print("Incorrect")

print(f"Total Points Secured By You Is --> {count}")
