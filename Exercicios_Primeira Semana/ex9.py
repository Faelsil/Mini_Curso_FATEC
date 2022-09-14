'''''
Suponha que você foi ao supermercado e comprou:

• N quilos de café, cujo custo unitário(1 quilo) é Q
• L litros de leite, cujo custo unitário(1 litro) é P
• B quilos de banana, cujo custo unitário(1 quilo) é T

Faça um programa que mostre: nome do produto, total gasto com cada produto e o total gasto no
mercado.

'''''


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


