# -*-coding:Latin-1 -*

import os # On importe le module os qui dispose de variables 
          # et de fonctions utiles pour dialoguer avec votre 
          # syst�me d'exploitation

# Programme testant si une ann�e, saisie par l'utilisateur, est bissextile ou non

annee = input("Saisissez une ann�e : ") # On attend que l'utilisateur fournisse l'ann�e qu'il d�sire tester
annee = int(annee) # Risque d'erreur si l'utilisateur n'a pas saisi un nombre

if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0):
    print("L'ann�e saisie est bissextile.")
else:
    print("L'ann�e saisie n'est pas bissextile.")

# On met le programme en pause pour �viter qu'il ne se referme (Windows)
os.system("pause")