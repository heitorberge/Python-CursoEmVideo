from math import radians, sin, cos, tan
an = float(input("Digite algum ângulo em graus: "))
se = sin(radians(an))
co = cos(radians(an))
ta = tan(radians(an))
print("Seno: {:.2f}".format(se))
print("Cosseno: {:.2f}".format(co))
print("Tangente: {:.2f}".format(ta))