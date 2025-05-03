peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em metros: '))
# Minha altura é 1.44m
if altura <= 0:
  print('Altura inválida!')
else:
  imc = peso / (altura ** 2)
  print(f'Seu IMC é: {imc:.1f}')
  if imc < 18.5:
      print('Você está Abaixo do Peso ideal.')
  elif 18.5 <= imc < 25:
      print('Você está Com o Peso Ideal.')
  elif 25 <= imc < 30:
      print('Você está em Sobrepeso.')
  elif 30 <= imc < 40:
      print('Você está Obeso.')
  else:
      print('Você está em Obesidade Mórbida.')