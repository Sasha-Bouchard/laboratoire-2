#Jeu random

#Nombre entre 1 et 100 à deviner
CIBLE = 42

#Fonctions
def erreur(x):
    if x < 1 or x > 100:
        print("Ceci n'est pas un nombre valide! Veuillez réessayer :")
        x = int(input())
        erreur(x)
    return x

#Intro
essaie = int(input("Bienvenue à Jeu Random! Veuillez tenter de deviner ma cible entre 1 et 100 : "))
erreur(essaie)
tentative = 1

while essaie != CIBLE:
    if essaie < CIBLE:
        print("Votre essaie est plus petit que ma cible, veuillez réessayer")
        essaie = int(input())
        erreur(essaie)
        tentative = tentative + 1
    if essaie > CIBLE:
        print("Votre essaie est plus grand que ma cible, veuillez réessayer")
        essaie = int(input())
        erreur(essaie)
        tentative = tentative + 1
if tentative == 1:
    print("WOW! vous avez trouvé ma cible du premier coup!")
else:
    print("Bravo! Vous avez trouvé ma cible en", tentative, "essaies")
