import string
def isWordGuessed(secretWord, figured):
    for letter in figured:
        if figured==secretWord:
           figured = True
           break       
        elif letter in secretWord:
            figured = True
            print('Right! ',figured,'belongs to the mystery word!')
        else:
            print("Wrong!")
            figured = False
    return figured
def getGuessedWord(secretWord, lettersGuessed):
    guessedlist = list(lettersGuessed)
    guessedWord = ''
    for letter2 in secretWord:
        if lettersGuessed==secretWord:
            guessedWord = lettersGuessed
            break
        elif letter2 in guessedlist:
            guessedWord = guessedWord + letter2
        else:guessedWord = guessedWord + '_'
    return guessedWord
def getAvailableletters(lettersGuessed):
    l = list(string.ascii_lowercase)
    availletters = ''
    for letter3 in l:
        if letter3 not in lettersGuessed:availletters+=letter3
    return availletters
def Hangaroo(secretWord):
    tries = 7
    lettersGuessed = []
    availletters = string.ascii_lowercase
    guessedWord = '' 
    print("Welcome to Hangaroo!")
    while tries>0:
        casesensitive_guessed = input("Enter a letter(press 1 to quit) ") 
        guessed = casesensitive_guessed.lower()
        if guessed =='1':break    
        if guessed in lettersGuessed:
            print('That letter has already been entered')
            print(guessedWord)
            continue       
        lettersGuessed.append(guessed)       
        availletters = getAvailableletters(lettersGuessed)
        rightletter = isWordGuessed(secretWord,guessed)            
        if rightletter == False: 
            tries -= 1
            if tries ==0:
                print("You have failed to guess the mystery word. The correct answer is",secretWord)
                break
            print("You only have",tries," tries left.")          
        guessedWord = getGuessedWord(secretWord,lettersGuessed)
        print(guessedWord) 
        if guessedWord == secretWord:
            print ('Right! You have guessed the mystery word. Congratulations!') 
            break   
    return
        
    
