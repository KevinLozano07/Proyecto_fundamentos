#H = altura
#G = porcentaje graso
#P = peso
#ML = masa libre de grasa
#FFMI = indice libre de grasa
#GT = grasa total
#IMC = indice de masa corporal

H = float(input("ingrese su altura en metros: " ))
P = float(input("ingrese su peso en kilos: "))
G = float(input("ingrese su porcentaje graso: "))

IMC = P / (H ** 2)
GT = P * (G/100)
ML = P * (1 - G / 100)
FFMI = ML / (H ** 2)
AFFMI = FFMI + (6.3 * (1.8 - H) )
print ("tu masa libre de grasa en kilo es " + str(ML))
print ("tu grasa total en kilos es " + str(GT))
print ("tu IMC es de " + str (IMC))
print ("tu FFMI es de " + str(FFMI))
print ("tu AFFMI aproximadamente es de: " + str(AFFMI))