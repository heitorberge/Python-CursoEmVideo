import math

def calcular_trigonometria(angulo):
  angulo_radianos = math.radians(angulo)
  seno = math.sin(angulo_radianos)
  cosseno = math.cos(angulo_radianos)
  tangente = math.tan(angulo_radianos)
  return seno, cosseno, tangente

angulo = float(input("Digite o ângulo em graus: "))

seno, cosseno, tangente = calcular_trigonometria(angulo)

print("Seno:", seno)
print("Cosseno:", cosseno)
print("Tangente:", tangente)