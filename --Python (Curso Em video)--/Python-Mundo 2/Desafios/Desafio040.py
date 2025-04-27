print('-- Escola em vídeo --')
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5.0:
    print('Você foi reprovado com a média de {:.1f}'.format(media))
elif media > 5.0 and media < 6.9:
    print('Você está em recuperação com a média de {:.1f}'.format(media))
else:
    print('Você foi aprovado com a média de {:.1f}'.format(media))