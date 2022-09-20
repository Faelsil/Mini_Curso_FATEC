'''''
O custo ao consumidor de um carro novo é a soma do custo de fábrica com a percentagem do
distribuidor e dos impostos (aplicados ao custo de fábrica) Supondo que a percentagem do
distribuidor seja de 28 e os impostos de 45 faça um programa que leia o custo de fábrica de
um carro e escreva o custo ao consumidor

'''''


carro = float(input('Digite o Valor do carro: '))

imposto = carro * 28 /100
print('O imposto do carro é: ', imposto)

custoFabrica = carro * 45 /100
print('O custo de fabrica é: ', custoFabrica)

custoTotal = imposto + custoFabrica
print("O custo total do carro: ", custoTotal)




