frase = input("Digite uma frase: ").strip().upper()
quantidade_a = frase.count("A")
primeira_a = frase.find("A")
ultima_a = frase.rfind("A")

print(f"A letra A aparece {quantidade_a} vezes na frase.")
print(f"A primeira letra A aparece na posição {primeira_a}.")
print(f"A última letra A aparece na posição {ultima_a}.")