expr = str(input('Digite a expressão: '))
pilha = []
for simbolo in expr:
    if simbolo == '(':
        pilha.append('(')
    elif simbolo == ')':
        pilha.append(')')
if len(pilha) % 2 == 0:
    if pilha.count('(') == pilha.count(')'):
        print('A expressão está correta!')
    else:
        print('A expressão está incorreta!')