import random

def game():
    print("you are playing game..")
    score = random.randint(1,62)
    
    # safe opening
    with open("highscore.txt", "a+") as f:
        f.seek(0)  # cursor ko start par le aao
        highscore = f.read()
        if highscore.strip() != "":
            highscore = int(highscore)
        else:
            highscore = 0
    
    print(f"your score: {score}")
    if score > highscore:
        with open("highscore.txt", "w") as f:
            f.write(str(score))

    return score

game()
