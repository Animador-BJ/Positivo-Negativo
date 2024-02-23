# programa paraverificar si un numero es positivo o es negativo

# imput

print("-----------------------------------")
X = int(input("digite un numero: "))

# processing

if X > 0:
    Rta = " Positivo"

elif X == 0:
    Rta = " su numero es neutro "

else:
    Rta = " Negativo"

# output

print("-----------------------------------")
print("el numero " + str(X) + " es " + Rta)
print("-----------------------------------")