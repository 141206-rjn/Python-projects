import random 

def getRandomNumb():
    return random.randrange(1,100)


def giveHint(number,guess):
    if guess > (number+10) or guess <(number-10):
        return "Cold"
    elif number == guess :
        return "right"
    else :
        return "Hot"


def runGuess():
    secretNumber = getRandomNumb()
    while True :
        user_guess = int(input("Enter a number between 1 to 100 : \n"))
        hint = giveHint(secretNumber,user_guess)
        if hint == "right" :
            print("You guessed it right")
            break
        else :
            print(hint)
        
if __name__ == '__main__':
    runGuess()
