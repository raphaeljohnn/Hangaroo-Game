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
    
