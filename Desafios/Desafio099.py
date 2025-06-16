def maior(*nums):
    print('-=' * 30)
    print('Analisando os valores passados...')
    print(f'{nums} Foram informados {len(nums)} valores ao todo.')
    maior = nums[0]
    for n in nums:
        if n > maior:
            maior = n
        print(f'O maior valor informado foi {maior}.')
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
