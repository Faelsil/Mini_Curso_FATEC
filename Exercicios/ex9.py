kgCafe = 8.50
litroLeite = 6.50
kgBanana = 3.50


qtdProdutoCafe = int(input('Digite  Quantidade de Café: '))
qtdProdutoLeite = int(input('Digite  Quantidade de Leite: '))
qtdProdutoBanana = int(input('Digite  Quantidade da Banana: '))


cafe = (qtdProdutoCafe * kgCafe)
leite = (qtdProdutoLeite * litroLeite)
banana = (qtdProdutoBanana * kgBanana)

somaTotal = (cafe + leite + banana)

print('------------------------------------------------')
print('                                     EXTRATO                                    ')
print('------------------------------------------------')

print('[1] - Banana: ', '                                                R$: ', banana)
print('[2] - Leite: ', '                                                     R$: ',  leite )
print('[3] - Café: ', '                                                      R$: ',  cafe)

print('------------------------------------------------')
print('[4] - Total Gasto: ', '                                       R$: ', somaTotal)
print('------------------------------------------------')


