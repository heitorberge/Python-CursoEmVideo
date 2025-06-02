preco = float(input("Digite o preço normal do produto: R$"))
print("""Formas de pagamento:
[ 1 ] À vista dinheiro/cheque
[ 2 ] À vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão""")
opcao = int(input("Escolha a forma de pagamento: "))

if opcao == 1:
    desconto = preco * 0.10
    total = preco - desconto
    print(f"Preço do produto: R$ {preco:.2f}")
    print(f"Desconto de 10%: R$ {desconto:.2f}")
    print(f"Valor total a pagar: R$ {total:.2f}")
elif opcao == 2:
    desconto = preco * 0.05
    total = preco - desconto
    print(f"Preço do produto: R$ {preco:.2f}")
    print(f"Desconto de 5%: R$ {desconto:.2f}")
    print(f"Valor total a pagar: R$ {total:.2f}")
elif opcao == 3:
    total = preco
    parcela = total / 2
    print(f"Preço do produto: R$ {preco:.2f}")
    print(f"Pagamento em 2x de R$ {parcela:.2f} SEM JUROS")
    print(f"Valor total a pagar: R$ {total:.2f}")
elif opcao == 4:
    num_parcelas = int(input("Digite o número de parcelas: "))
    juros = preco * 0.20
    total = preco + juros
    parcela = total / num_parcelas
    print(f"Preço do produto: R$ {preco:.2f}")
    print(f"Juros de 20%: R$ {juros:.2f}")
    print(f"Pagamento em {num_parcelas}x de R$ {parcela:.2f} COM JUROS")
    print(f"Valor total a pagar: R$ {total:.2f}")
else:
    print("Opção de pagamento inválida!")