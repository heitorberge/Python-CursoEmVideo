import datetime
ano = int(input("Que ano quer analisar? Digite 0 para pegar o ano atual: "))
if ano == 0:
    ano = datetime.datetime.now().year
if ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0:
  print(f"O ano {ano} é bissexto.")
else:
  print(f"O ano {ano} não é bissexto.")