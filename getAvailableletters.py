def getAvailableletters(lettersGuessed):
    l = list(string.ascii_lowercase)
    availletters = ''
    for letter3 in l:
        if letter3 not in lettersGuessed:availletters+=letter3
    return availletters