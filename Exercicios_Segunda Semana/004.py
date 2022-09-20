'''Faça um programa em Python que leia 3 valores a,b,c e verifica se eles formam ou não um triângulo.
Supor que os valores lidos são inteiros e positivos. Caso os valores formem um triângulo, mostrar de que tipo ele é : escaleno, equilátero ou isósceles.
Se não formam um triângulo, mostrar uma mensagem: não forma um triângulo. OBS: Para ser um triângulo têm que ser verdadeiro as seguintes condições: (a<b+c) e (b<c+a) e (c<a+b) '''

valorA = int(input('Digite o Primeiro Valor: '))
valorB = int(input('Digite o Primeiro Valor: '))
valorC = int(input('Digite o Primeiro Valor: '))

if valorB + valorC < valorA or valorC + valorA < valorB or valorA + valorB < valorC:
    print('não é um triangulo')

elif valorA == valorB and valorA == valorC:
    print('Equilatero')

elif valorA == valorB or valorA == valorC or valorB == valorC:
    print('Isósceles')

else:
    print("Escaleno")
