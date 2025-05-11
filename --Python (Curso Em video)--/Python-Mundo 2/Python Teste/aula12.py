def tem_tres_consoantes_juntas(texto):
  consoantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
  contador = 0
  for letra in texto:
    if letra in consoantes:
      contador += 1
      if contador >= 3:
        return True
    else:
      contador = 0
  return False

nome = str(input('\033[34mQual é seu nome? ')).capitalize().strip()
nl = len(nome)

if nome == 'Heitor':
    print('\033[4:33mQue nome bonito!')
elif nome == 'Kátia' or nome == 'Claudemberg' or nome == 'Melissa':
    print('\033[4:36mSeu nome é igual ao de alguns parentes meus e é bem bonito.')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('\033[4:32mSeu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('\033[4:35mBelo nome feminino.')
elif tem_tres_consoantes_juntas(nome):
    print('\033[4:36mHum... Esse nome tem um som diferente com tantas consoantes juntas!')
elif nl > 10:
    print('\033[4:36mEsse nome é um pouco estranho e longo.')
elif nome == 'Mario' or nome == 'Sonic' or nome == 'Luigi':
    print('Você tem seu próprio videogame! Me dá um autógrafo!')
else:
    print('\033[4:33mSeu nome é bem normal.')

print('\033[0:31mTenha um bom dia, {}!'.format(nome))