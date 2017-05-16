""" pour jouer au casino ! """
from random import randrange 
import os

testReserveArgent = 1
while testReserveArgent == 1:
    reserveArgent = input("combien avez-vous d'argent ?")
    try:
        reserveArgent = float(reserveArgent)
        assert reserveArgent >= 0
        testReserveArgent = 0
    except ValueError:
        print("vous devez entre un chiffre!")
        testReserveArgent = 1
    except AssertionError:
        print("vous devez entre un nombrePositif!")
        testReserveArgent = 1

while reserveArgent > 0:
    
    testNombreMise = 1
    while testNombreMise == 1:
        nombreMise = input("choisissez un nombre entre 0 et 49")
        try:
            nombreMise = int(nombreMise)
            assert nombreMise<50
            testNombreMise = 0
        except ValueError:
            print("vous devez entre un chiffre!")
            testNombreMise = 1
        except AssertionError:
            print("votre nombre n'est pas compris entre 0 et 49 !")
            testNombreMise = 1

    testArgentMise = 1
    while testArgentMise == 1:
        argentMise = input("quelle somme misez-vous ?")
        testArgentMise = 0
        try:
            argentMise = float(argentMise)
            assert argentMise <= reserveArgent
        except AssertionError:
            print("vous n'avez que", reserveArgent, "dans votre portefeuille !")
            testArgentMise = 1
        except ValueError:
            print("vous devez entre un chiffre!")
            testArgentMise = 1
        
    reserveArgent -= argentMise
        
    nombreGagnant = randrange(50)
    print ("le nombre gagnant est", nombreGagnant)
    
    if nombreGagnant == nombreMise:
        print("bravo !! le nombre que vous avez misé est le nombre gagnant!")
        reserveArgent += 3*argentMise

    elif nombreGagnant%2 == nombreMise%2:
        if nombreGagnant%2 == 0:
            parite = "paires"
        elif nombreGagnant%2 == 1:
            parite = "impaires"
        print("Le nombre que vous avez misé et le nombre gagnant sont tous les deux", parite)
        reserveArgent += argentMise/2
        
    else:
        print("vous avez perdu !")
    print("il vous reste", reserveArgent, "dollards")
    os.system("pause")

print("C'est fini, vous n'avez plus d'argent !!")
