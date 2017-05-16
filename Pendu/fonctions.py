def pickWord(wordList):
    from random import randrange
    niveauMot = randrange(len(wordList))
    word = wordList[niveauMot]
    return word

def chooseLetter():
    format = False
    while format == False:
        format = True
        letter = input("Entrez une lettre")
        try:
            assert len(letter)==1 and letter.isalpha()
        except AssertionError:
            print("il faut entrer une seule lettre !")
            format = False
    return letter
    
def checkLetterInWord(letter, word, wordInProgress):
    goodLetter=False
    letter = letter.lower()
    wordInProgress=list(wordInProgress)
    for p, l in enumerate(word):
        if letter == l:
            wordInProgress[p] = letter
            goodLetter=True
    if goodLetter==False:
        print("cette lettre n'était pas dans le mot!")
    else:
        print("super, cette lettre était bien dans le mot !")
    wordInProgress= "".join(wordInProgress)
    return wordInProgress

def checkWonGame(word, wordInProgress):
    if wordInProgress == word:
        return True
    else:
        return False      

def saveScore(name, score):
    import pickle
    with open("scores.txt","rb") as file:
        try:
            p =pickle.Unpickler(file)
            savedScore=p.load()
        except:
            savedScore={}
    with open("scores.txt","wb") as file:
        savedScore[name]=score
        pic=pickle.Pickler(file)
        pic.dump(savedScore)
    print(savedScore)
