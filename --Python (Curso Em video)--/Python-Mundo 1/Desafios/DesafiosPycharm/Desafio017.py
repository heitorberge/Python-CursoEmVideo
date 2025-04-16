import math

def calcular_hipotenusa(cateto_oposto, cateto_adjacente):
  hipotenusa = math.sqrt(cateto_oposto**2 + cateto_adjacente**2)
  return hipotenusa

cateto_oposto = float(input("Digite o comprimento do cateto oposto: "))
cateto_adjacente = float(input("Digite o comprimento do cateto adjacente: "))

hipotenusa = calcular_hipotenusa(cateto_oposto, cateto_adjacente)

print("O comprimento da hipotenusa é:", hipotenusa)