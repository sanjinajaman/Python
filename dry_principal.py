#DRY->don't repeat your self
winning_number=40
number=int(input("Enter your guess number between 1 to 100:"))
guess=1
game_over=False
while not  game_over:
    if number==winning_number:
        print(f"YOU WIN!!, And you guess this number {guess} times")
        game_over=True
    else:
        if number>winning_number:
            print("Too High")
            # guess+=1
            # number=int(input("Guess Number Again:"))

        else:
            print("Too Low")
            # guess+=1
            # number = int(input("Guess Number Again:"))

        guess += 1
        number = int(input("Guess Number Again:"))
