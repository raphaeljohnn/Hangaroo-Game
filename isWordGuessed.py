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
    
