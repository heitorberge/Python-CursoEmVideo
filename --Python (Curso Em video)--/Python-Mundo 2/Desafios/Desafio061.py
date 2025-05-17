primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
print(primeiro, end=' -> ')
atual = primeiro
cont = 0
while cont < 10:
    cont += 1
    atual = atual + razao
    print(atual, end=' -> ')
print('FIM')