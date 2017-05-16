import os
os.chdir("D:/Desktop/Python/Pendu")

import fonctions as f
from donnees import *


print("Bienvenue dans notre jeu du pendu !")
name = input("Quel est votre nom ?")
try:
    assert name != None
except AssertionError:
    raise Exception("vous n'avez rentré aucun nom")

word = f.pickWord(wordList)
wordInProgress= len(word)*"*"

i =0
while i <= maxChances-1:
    letter = f.chooseLetter()
    wordInProgress = f.checkLetterInWord(letter, word, wordInProgress)
    wonGame = f.checkWonGame(word, wordInProgress)
    if wonGame == True:
        print(" Vous avez gagné !!! Le mot était bien",word)
        score = maxChances - i + 1
        break
    print("vous en êtes ici:", wordInProgress)
    if i == maxChances-1 and wonGame == False:
        print("Malheureusement vous avez épuisé toutes vos chances !")
        print("le mot à trouver était", word)
        score = 0
    i+=1

f.saveScore(name, score)
