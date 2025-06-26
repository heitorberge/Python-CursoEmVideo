from lib.interface import *
def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except Exception as e:
        print(f'Erro ao criar o arquivo: {e}')
    else:
        print(f'Arquivo {nome} criado com sucesso!')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except Exception as e:
        print(f'Erro ao ler o arquivo: {e}')
    else:
        cabecalho(f'Pessoas cadastradas')
        for linha in a:
            dado = linha.strip().split(';')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()

def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except Exception as e:
        print(f'Erro ao abrir o arquivo: {e}')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except Exception as e:
            print(f'Erro ao escrever no arquivo: {e}')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()
