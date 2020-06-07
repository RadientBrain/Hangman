import random

def removNestings(l,new): 
    for i in l: 
        if type(i) == list: 
            removNestings(i,new) 
        else: 
            new.append(i) 

def wordsList():
    #reading words from the file
    a_file = open("words.txt", "r")
    list_of_words = [(line.strip()).split() for line in a_file]
    a_file.close()
    processed = []
    removNestings(list_of_words,processed)
    return (random.choice(processed))

def figure(count):
    if count!=0:
        print("\n\tOops...you have only\n")
    if count == 9:
        print("\t\t\t\t9 turns left")
        print("\t\t\t\t  --------  ")
    if count == 8:
        print("\t\t\t\t8 turns left")
        print("\t\t\t\t  --------  ")
        print("\t\t\t\t     O      ")
    if count == 7:
        print("\t\t\t\t7 turns left")
        print("\t\t\t\t  --------  ")
        print("\t\t\t\t     O      ")
        print("\t\t\t\t     |      ")
    if count == 6:
        print("\t\t\t\t6 turns left")
        print("\t\t\t\t  --------  ")
        print("\t\t\t\t     O      ")
        print("\t\t\t\t     |      ")
        print("\t\t\t\t    /       ")
    if count == 5:
        print("\t\t\t\t5 turns left")
        print("\t\t\t\t  --------  ")
        print("\t\t\t\t     O      ")
        print("\t\t\t\t     |      ")
        print("\t\t\t\t    / \     ")
    if count == 4:
        print("\t\t\t\t4 turns left")
        print("\t\t\t\t  --------  ")
        print("\t\t\t\t   \ O      ")
        print("\t\t\t\t     |      ")
        print("\t\t\t\t    / \     ")
    if count == 3:
        print("\t\t\t\t3 turns left")
        print("\t\t\t\t  --------  ")
        print("\t\t\t\t   \ O /    ")
        print("\t\t\t\t     |      ")
        print("\t\t\t\t    / \     ")
    if count == 2:
        print("\t\t\t\t2 turns left")
        print("\t\t\t\t  --------  ")
        print("\t\t\t\t   \ O /|   ")
        print("\t\t\t\t     |      ")
        print("\t\t\t\t    / \     ")
    if count == 1:
        print("\t\t\t\t1 turns left")
        print("\t\t\t\tLast breaths counting, Take care!")
        print("\t\t\t\t  --------  ")
        print("\t\t\t\t   \ O_|/   ")
        print("\t\t\t\t     |      ")
        print("\t\t\t\t    / \     ")
    if count == 0:
        print("\t\t\t\tYou loose")
        print("\t\t\t\tYou let a kind man die")
        print("\t\t\t\t  --------  ")
        print("\t\t\t\t     O_|    ")
        print("\t\t\t\t    /|\      ")
        print("\t\t\t\t    / \     ")


def hangman():
    words = wordsList()
    #this is for checking the word for debugging 
    #print (words)
    
    #validating input
    validAlphabets = "abcdefghijklmnopqrstuvwxyz"
    turns=10
    userGuess = ''
    
    _z = ''
    for i in words:
        _z = _z + " __ "
    print(_z)
    flag = ''
    while len(words)>0 :
        if turns == 0:
            break

        main = ''

        enteredWord = input("Enter the letter you guessed...\t")
        if enteredWord == flag and len(flag)>0:
            print ("\n\tYou have already entered that letter...\n\t Enter some other letter...\n")
        flag = enteredWord

        if enteredWord in validAlphabets:
            userGuess = userGuess + enteredWord
            for letter in words:
                if letter in userGuess:
                    main = main + letter
                else:
                    main = main + " __ "
        else:
            print("Enter a valid alphabet...")
            enteredWord = input()

        if main == words:
            print("\tYes the word is '"+main+"'\n\t\tYOU WIN !\n")
            break
        print(main + "\n")

        if enteredWord not in words:
            turns = turns - 1
            figure(turns)
        

        
if __name__ == "__main__":
    print("Welcome to the Hangman game...\nTry to guess the words within 10 attempts...")
    hangman()