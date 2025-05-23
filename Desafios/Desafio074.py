from random import randint
tuplarandom = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('=-' * 20)
print(f'Os números sorteados foram: {tuplarandom}')
print('=-' * 20)
menor = min(tuplarandom)
maior = max(tuplarandom)
print(f'O maior número sorteado foi: {maior}')
print(f'O menor número sorteado foi: {menor}')