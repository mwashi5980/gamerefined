import random 
def textfile():
    with open("random.txt", "w") as f:
        for _ in range(15):
            f.write(str(random.randint(0,1))+"\n")
    f.close()
def playerguess(score=0):
    print("Its your Turn Player!")
    with open("random.txt", "r") as p:
        lines = p.readlines()
        for x in range(15):
            list = int(lines[x])
            guess = int(input("Guess: "))
            if guess !=list:
                print(f"Incorrect\tYour final score is: {score}\n")
                break
            else:
                score += 1
                print(f"Correct!\tYour current score is: {score}")
        if score == 15:
            print(f"Congrats you got a perfect score of {score}\n")
    p.close()
def AIguess(scoreAI=0):
    print("Its your turn AI!")
    with open("random.txt", "r") as AI:
        lines = AI.readlines()
        for x in range(15):
            list = int(lines[x])
            guess = (random.randint(0,1))
            print(f"Guess: {guess}")
            if guess != list:
                print(f"Incorrect AI\tYour final score is: {scoreAI}\n")
                break
            else:
                scoreAI += 1
                print(f"Correct AI!\tYour current score is: {scoreAI}")
        if scoreAI == 15:
            print(f"Congrats AI you got a perfect score of {scoreAI}\n")
    AI.close()
playerguess()
AIguess()