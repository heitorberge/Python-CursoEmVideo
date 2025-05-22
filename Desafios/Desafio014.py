prd = float(input('Digite o valor de um produto:  '))
desconto = prd * 0.05
preco_final = prd - desconto  
print('Este produto com 5% de desconto fica com o preço de: R${:.2f}'.format(preco_final))