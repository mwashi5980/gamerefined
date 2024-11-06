import random
def textfile(guess, score = 0):
    with open("random.txt", "w") as f:
        for _ in range(15):
            f.write(str(random.randint(0,1))+"\n")
    f.close()
    with open("random.txt", "r") as f:
        lines = f.readlines()
        for x in range(_+1):
            list = int(lines[x])
            try:
                guess = int(input("Guess: "))
                if guess != list:
                    print(f"Incorrect!\tYour final score is {score}")
                    break
                else:
                    score += 1
                    print(f"Correct!\tYour current score is {score}")
            except ValueError:
                print("Not a number!")
                score = 0
                break
    print("Game Over!")
textfile(0)