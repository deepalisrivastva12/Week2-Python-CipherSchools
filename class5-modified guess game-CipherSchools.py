import random
winning_number=random.randint(1,100)
guess=1
number=int(input("enter the number: "))
game_over=False
while not game_over:
    if number==winning_number:
        print("you win ""and" " " "your guess number is:",(guess))
        game_over=True
    else:
        if number<winning_number:
            print("too low")
            guess+=1
            number=int(input("guess again: "))
        if number>winning_number:
            print("too high")
            guess+=1
            number=int(input("guess again: "))