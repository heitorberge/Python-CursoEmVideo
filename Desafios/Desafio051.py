primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
print(primeiro, end=' -> ')
atual = primeiro
for i in range(0, 9):
    atual = atual + razao
    print(atual, end=' -> ')
print('FIM')