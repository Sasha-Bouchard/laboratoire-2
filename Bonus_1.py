#Programme qui convertis des euros en une autre devise

#Devises diponible
DISPO = ("Dollards Canadien", "Dollards Américain", "Yen", "Roupie Indienne")

#Taux de convertion
CONV_CAD = 1.5
CONV_USD = 1.04
CONV_JPY = 161.64
CONV_INR = 90.11

#Programme
euro = float(input("Veillez entré un montant d'euros : "))
print("Ce programme peut présentement convertir ce montant en les devises suivante : ")
print(DISPO)
devise = input("Veuillez en choisir une : ")
if devise == "Dollards Canadien":
    résultat = round(euro * CONV_CAD, 2)
    print(euro, "euro est équivalent à", résultat, "CAD")
elif devise == "Dollards Américain":
    résultat = round(euro * CONV_USD, 2)
    print(euro, "euro est équivalent à", résultat, "USD")
elif devise == "Yen":
    résultat = round(euro * CONV_JPY, 2)
    print(euro, "euro est équivalent à", résultat, "JPY")
elif devise == "Roupie Indienne":
    résultat = round(euro * CONV_INR, 2)
    print(euro, "euro est équivalent à", résultat, "INR")
else:
    print("Cette devise n'est présentement pas disponible")