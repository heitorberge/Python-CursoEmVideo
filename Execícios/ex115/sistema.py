from lib.arquivo import *
from lib.interface import *
from time import sleep
arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)
cabecalho('Sistema de Cadastro de Pessoas')
while True:
    opcao = menu(['Ver Pessoas Cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if opcao == 1:
        lerArquivo(arq)
    elif opcao == 2:
        cabecalho('Novo Cadastro')
        nome = str(input('Nome: ')).strip()
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif opcao == 3:
        cabecalho('Saindo do Sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida.\033[m')
        sleep(2)
