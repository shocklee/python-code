import random

def randomList(size, lrange=0, urange=10):
    """Place a value in the random list.
    The size specifies the number of elements.
    The lrange specified the lower value; default is 0.
    The urange specifies the upper value; default is 10.
    """
    random.seed()
    rlist = []
    for i in range(size):
        rlist.append(random.randrange(lrange, urange))
    return rlist

def check(rlist, guess):
    black = 0 #The count of correct guesses (position and value)
    white = 0 #The count of guesses where only the value is correct
    rlistused = [0] * len(rlist) #Record the random list entries that have been used
    guessused = [0] * len(guess) #Record the guess list entries that have been used
    #This is the check to determine if there was an exact match
    for i in range(len(rlist)):
        if(rlist[i] == guess[i]):
            black += 1 #The position and value was correct
            rlistused[i] = 1
            guessused[i] = 1
    #This is the check to determine if the right number is in the wrong place
    for i in range(len(rlist)):
        for j in range(len(guess)):
            if(rlist[i] == guess[j]):
                #print "i", i, rlist[i], rlistused[i]
                #print "j", j, guess[j], guessused[j]
                if(rlistused[i] == 0 and guessused[j] == 0):
                    white += 1
                    rlistused[i] = 1
                    guessused[j] = 1
                    break
    
    #print "rlistused:", rlistused
    #print "guessused:", guessused
    return [black, white]

def get_guess(size):
    """Get the user to provide a guess of the proper length."""
    answer = ''
    guess = []
    while (len(answer) != size):
        answer = str(raw_input("Please enter your guess: "))
    #Breakdown the guess
    for char in answer:
        guess.append(int(char))
    return guess        

def play_again():
    """As the user if they want to play the game again."""
    answer = str(raw_input("Do you want to play again? "))
    char = answer[0].lower()
    if(char == 'y'):
        return True
    else:
        return False

def play():
    again = True
    guessSize = 6
    result = []
    print "Enter " + str(guessSize) + " numbers as your guess on one line."
    print "The system will respond with two numbers in brackets."
    print "The number outside of the brackets is guess number."
    print "The first number in the brackets is the number of correct guesses that are in the correct location."
    print "The second number in the brackets is the number of correct guesses that are not in the correct location."
    print "The goal of the game is to get the numbers in the correct sequence in the least number of tries."
    while again:
        rlist = randomList(guessSize)
        #print "rlist", rlist
        guessNumber = 0
        result = [0, 0]
        while result != [guessSize, 0]:
            guess = get_guess(guessSize)
            result = check(rlist, guess)
            guessNumber += 1
            print guessNumber, result
        print "You have won the game!"
        again = play_again()
    
def test():
    """Using some test conditions, check to see if the code works
    correctly."""
    rlist = [6, 5, 3, 3, 2, 1]
    guess = [1, 2, 3, 4, 5, 6]
    result = check(rlist, guess)
    print "rlist", rlist
    print "guess", guess
    print "result", result # should be [1, 4]
    guess = [3, 3, 3, 4, 5, 6]
    result = check(rlist, guess)
    print "rlist", rlist
    print "guess", guess
    print "result", result # should be [1, 3]
    guess = [6, 5, 3, 3, 2, 1]
    result = check(rlist, guess)
    print "rlist", rlist
    print "guess", guess
    print "result", result #should be [6, 0]

play()
