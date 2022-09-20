salario = float(input('Salario? '))
imposto = input('imposto em % ?')

if imposto == '':
    imposto = 27.5
    x = salario - (salario * float(imposto) / 100)
    print('Valor real = {} '.format(x))

else:
    x = salario - (salario * float(imposto) / 100)
    print('valor real = {} '.format(x))