import os
from os import system
system("clear")
import random

word = ["cat", "knife", "melon", "store"]
hint = ["4legs and fluffy","sharp and stabby", "round and juicy", "buy things here"]

randonum = random.choice(range(len(word)))

pickword = word[randonum]
pickhint = hint[randonum]

dashword = []

for letter in pickword:
    dashword.append("-")

print(pickhint)
print(dashword)

while list(pickword) != dashword:
    guess = input("Guess the letters! ")
    if list(pickword) != dashword:
        for i in range(len(pickword)):
            if guess == pickword[i]:
                dashword[i] = guess
                print(dashword)
    else:
        break

if list(pickword) == dashword:
    print("you got it!")

