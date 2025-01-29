#Exercice 8 non corrigé avec explication
def addition(a, b):
    resultat = a + b #Cette oppération ne peut pas être faite entre un str et un int
    return resultat
x = "5" #ceci est un str
y = 3 #ceci est un int
z = addition(x, y) #Cette fonction crash dûe aux types des entrées
print("Résultat:", z)