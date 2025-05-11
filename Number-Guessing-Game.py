import random


print("welocme to game")
start = random.randint(1,100)

while True:
    choose = int(input("guess the number :"))
    if(choose == start):
        print("tou won the game ")
        break
    elif(choose > start):
        print("choose the smaller number")
    else:
        print("choose bigger number")

print("__GAME OVER__")

