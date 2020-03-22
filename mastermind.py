# Getting the secret code - player 1
def isValid (code):
    if len(code) == 4 and code.isdigit():
        return True
    else:
        return False

def get4DigitCode():   # should return back a valid 4 digit code
    while True:
        code = input("Enter a 4 digit code: ")
        if isValid(code):
            return code
        else:
            print("Not a 4 digit code. Try again")

def isCorrectCode (code, guess): #does code match position of secret code
    numCorrectPlace = 0
    numIncorrectPlace = 0
    guessCopy = list(guess)
    codeCopy = list(code)
    i = 0
    while i < len(code):
        if guess[i] == code[i]:
            numCorrectPlace += 1
            codeCopy[i] = ""
        i += 1
    print(numCorrectPlace, 'matching digit and in position')
    for j in guessCopy:
        if j != "":
            if j in codeCopy:
                numIncorrectPlace +=1
                guessCopy.remove(j)
    print(numIncorrectPlace, 'matching digit not in position')



secret = get4DigitCode()  # code is stored in variable 'secret'
print(20 * "\n")

# Guessing game - player 2
# now we have a valid secret code
# player 2 now has to guess secret code made by player 1
isSuccess = False
numberOfTries = 20
while isSuccess == False and numberOfTries > 0:
    guess = get4DigitCode()   # ensure four digit code is entered
    if guess == secret:
        isSuccess = True
        print("You win!")
    else:
        numberOfTries = numberOfTries - 1
        isCorrectCode(secret, guess)
        print("You have", numberOfTries, "guesses remaining")

    if numberOfTries == 0:
        print("You failed. Goodbye")


#1.	Compare the input to the code and print out two things:
#How many digits they have matching AND in position
#	How many digits they have matching but not in position
#“1 matching digit and in position, 1 matching digit not in position”

